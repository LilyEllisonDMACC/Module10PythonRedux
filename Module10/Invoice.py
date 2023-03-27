"""
Program: Invoice.py
Author: Lily Ellison
Last date modified: 03/27/2023

The purpose of this program is to create a class with data members that is used to print out an invoice.

"""


class Invoice:
    """Invoice class"""

    def __init__(self, iid, cid, lname, fname, pnum, addr, item="", price=0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_characters = set("1234567890-()")

        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not phone_characters.issuperset(pnum):
            raise ValueError

        self.invoice_id = iid
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnum
        self.address = addr
        if item != "":
            self.items_with_price = dict([(item, price)])
        else:
            self.items_with_price = {}

    def __str__(self):
        return "Invoice ID: " + str(self.invoice_id) + "\nFor Customer ID: " + str(self.customer_id) + "\nName: " + \
            self.first_name + " " + self.last_name + "\nPhone: " + str(
            self.phone_number) + "\nAddress: " + self.address

    def __repr__(self):
        return 'Invoice({},{},{},{},{},{})'.format(self.invoice_id, self.customer_id, self.last_name, self.first_name,
                                                   self.phone_number, self.address)

    def add_item(self, to_add):
        self.items_with_price.update(to_add)

    def create_invoice(self):
        TAX = 0.06
        print(self.__str__() + "\n")
        total_items = len(self.items_with_price)
        i = 0
        subtotal = 0
        while i < total_items:
            item = list(self.items_with_price)[i]
            price = self.items_with_price[item]
            subtotal += price
            print(item + "........$" + "{:,.2f}".format(price))
            i += 1
        tax_amt = subtotal * TAX
        total_due = subtotal + tax_amt
        print("Tax..........${:,.2f}".format(tax_amt) + "\nTotal........${:,.2f}".format(total_due))


# Driver code
invoice = Invoice(1, 123, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

"""
Testing:
 
Invoice ID: 1
For Customer ID: 123
Name: Minnie Mouse
Phone: 555-867-5309
Address: 1313 Disneyland Dr, Anaheim, CA 92802

iPad........$799.99
Surface........$999.99
Tax..........$108.00
Total........$1,907.98

Process finished with exit code 0

"""
