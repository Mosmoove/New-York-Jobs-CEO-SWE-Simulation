from datetime import datetime

"""
1. An invoice tracks the name, address, and email of both its sender and recipient. ✅
2. An invoice tracks the date it was created, as well as items to charge for.
3. An item may be added to an existing invoice.
4. Each item has an associated name, price, and percent tax. ✅
5. The total price of an invoice is the sum of all its constituent items.
6. A percent discount may be applied to the entire invoice.
7. A discount must be applied before tax is determined.
8. An invoice must calculate its total price based on all contained items.

"""
class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""
    def __init__(self, sender_name,recipient_name, sender_address, recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.comments = []

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            discounted_price = price - (price * discount)
            total += discounted_price + (discounted_price * tax)
        return total
    
    """*Implenting a new comment feature*"""
    def add_comment(self, comment):
        self.comments.append(comment)
    def get_comments(self):
        result = ""
        for comm in self.comments:
            result += f"\n{comm}"
        
        return result #returns the comment
        
if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice.add_comment("This is a comment for an invoice") #sets a comment 
    invoice.add_comment("We noticed one of the windows on the East side of the 12th floor has a hairline fracture")
    invoice.add_comment("The job took 7 hours and 45 minutes to complete")
    invoice_total = invoice.calculate_total(.20) # Initally it was just 20 since the discount is passed as 20%, it is written as .20
    print(f"Total is ${invoice_total}.")
    print(invoice.get_comments())

