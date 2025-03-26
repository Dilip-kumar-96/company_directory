# # creating a class called cart
#
# class cart:
#     def __init__(self):
#         self.items = {}
#         self.item_prices = {"pendrive": 500, "laptop": 80000}
#
#     def add_item(self, item_name, item_quantity):
#         self.items[item_name] = item_quantity
#
#     def update_item(self, item_name, item_quantity):
#         self.items[item_name] = item_quantity
#
#     def delete_item(self, item_name):
#         del self.items[item_name]
#
#     def total_price(self):
#         total_price = 0
#         for item_name, item_quantity in self.items.items():
#             print(item_name, item_quantity)
#             total_price += item_quantity * self.item_prices[item_name]
#             print("total price of {} = {}".format(item_name, total_price))
#         return total_price
#
#
# cart_obj1 = cart()
#
# cart_obj1.add_item("laptop", 3)
# cart_obj1.add_item("pendrive", 3)
# print(cart_obj1.items)
#
# cart_obj1.update_item("laptop", 10)
# print(cart_obj1.items)
#
# cart_obj1.delete_item("laptop")
# print(cart_obj1.items)
# print(f"total price = {cart_obj1.total_price()}")
#
#
# class Car:
#     def __init__(self, color, max_speed, acceleration, tyre_friction):
#         self.color = color
#         self.max_speed = max_speed
#         self.acceleration = acceleration
#         self.tyre_friction = tyre_friction
#         self.current_speed = 0
#         self.is_engine_started = False
#
#     def start_engine(self):
#         self.is_engine_started = True
#
#     def stop_engine(self):
#         self.is_engine_started = False
#
#     def accelerate(self):
#         if self.is_engine_started == False:
#             print("Car has not started yet")
#         elif self.current_speed < self.max_speed:
#             self.current_speed += self.acceleration
#
#     def apply_brakes(self):
#         self.current_speed -= self.tyre_friction
#         if self.current_speed < 0:
#             self.current_speed = 0
#
#     def sound_horn(self):
#         if self.is_engine_started == True:
#             print("Beep")
#         else:
#             print("Car has not started yet")
#
#     def apply_brakes(self):
#         if self.current_speed < self.tyre_friction:
#             self.current_speed = 0
#         else:
#             self.current_speed -= self.tyre_friction
#
#
# car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
# car.sound_horn()
# car.start_engine()
# car.sound_horn()
# car.accelerate()
# print(car.current_speed)
# car.apply_brakes()
# print(car.current_speed)
# print(car.color)
#
# #Types of attributes (Instance attributes, class attributes)
# #types of methods (Instance methods(self), class methods (cls), static methods() )

# class cart:
#     discount = 50  #class attribute
#     def __init__(self):
#         self.items = {}  #instance attribute
#         self.item_prices = {"pendrive": 500, "laptop": 80000} #instance attribute
#
#     def add_item(self, item_name, item_quantity):
#         self.items[item_name] = item_quantity
#
#     def update_item(self, item_name, item_quantity):
#         self.items[item_name] = item_quantity
#
#     def delete_item(self, item_name):
#         del self.items[item_name]
#
#     def total_price(self):
#         total_price = 0
#         for item_name, item_quantity in self.items.items():
#             print(item_name, item_quantity)
#             total_price += item_quantity * self.item_prices[item_name]
#             print("total price of {} = {}".format(item_name, total_price))
#         print(f"discount = {cart.discount}")
#         return total_price
#
#     @classmethod
#     def discounted_total_price(cls, total_price):
#         return total_price - cart.discount
#
#
#
# cart_obj1 = cart()
#
# cart_obj1.add_item("laptop", 3)
# cart_obj1.add_item("pendrive", 3)
# print(cart_obj1.items)
#
# cart_obj1.update_item("laptop", 10)
# print(cart_obj1.items)
#
# cart_obj1.delete_item("laptop")
# print(cart_obj1.items)
# print(f"Total price after discount = {cart.discounted_total_price(cart_obj1.total_price())}")

class Product:  # parent class
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"You Saved: {self.you_save}")
        print(f"Ratings: {self.ratings}")


class ElectronicItem(Product):  # child class
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months

    def display_electronic_product_details(self):
        self.display_product_details()
        print(f"Warranty {self.warranty_in_months} months")


e = ElectronicItem("AC", 30000, 25000, 5.0)
e.set_warranty(12)
print(e.get_warranty())
e.display_electronic_product_details()
