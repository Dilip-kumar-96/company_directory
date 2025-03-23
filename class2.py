# CONCEPT OF COMPOSITION, INHERITANCE, MULTIPLE INHERITANCE, METHOD OVERRIDING
# classes product, electronic_item, grocery_item, order


class product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price

    def display_items(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"You Saved: {self.you_saved}")
        print(f"Ratings: {self.ratings}")


class electrinic_item(product):
    def set_warranty(self, warranty):
        self.warranty = warranty

    def get_warranty(self):
        return self.warranty

    def display_items(self):
        super().display_items()  #METHODOVERRIDING
        print(f"warranty: {self.get_warranty()}")

class grocery_item(product):
    def set_expiry(self, expiry):
        self.expiry = expiry
    def get_expiry(self):
        return self.expiry
    def display_items(self):
        super().display_items()  #METHODOVERRIDING
        print(f"expiry: {self.get_expiry()}")


class multi_inherit(grocery_item):

    def print_grand_parent(self):
        print("##############################################")
        print("This is multiple inheritance example")
        print(f"expiry: {self.display_items()}")

class order:
    def __init__(self, delivery_type, address):
        self.cart_items = []
        self.delivery_type = delivery_type
        self.address = address

    def add_item(self, product, quantity):
        self.cart_items.append((product, quantity))

    def cart_total(self):
        total_bill = 0
        for product, quantity in self.cart_items:
            product.display_items()
            total_price = product.deal_price * quantity
            total_bill += total_price
        print(f"Deliver_type: {self.delivery_type}")
        print(f"Address: {self.address}")
        print(f"Total bill: {total_bill}")


laptop = electrinic_item("laptop", 30000, 25000, 4.5)
laptop.set_warranty(24)

milk = grocery_item("milk", 50, 45, 5.0)
milk.set_expiry("25-03-2025")

curd = grocery_item("curd", 100, 90, 5.0)
curd.set_expiry("30-03-2025")

order = order("fast_delivery", "hyderabad")
order.add_item(milk, 2)  # sending object(instance) of grocery_item class
order.add_item(laptop, 2)
order.add_item(curd, 3)
order.cart_total()

get_details = multi_inherit("milk", 50, 45, 5.0)
get_details.set_expiry("25-03-2025")
get_details.print_grand_parent()
