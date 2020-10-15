# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#     def add_product(self, new_product):
#         self.products.append(new_product)
#         print(self.products)
#     def sell_product(self, id):
#         self.products.pop(id)
#         print(self.products)
#     def inflation(self, percent_increase):
        

# class Products:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category
#     def update_price(self, percent_change, is_increased):
#         if is_increased == True:
#             self.price += self.price*(percent_change/100)
#         else:
#             self.price -= self.price*(percent_change/100)
#     def print_info(self):
#         print(self.name, self.category, self.price)

# target = Store("Target")

# paperclips = Products("Paperclips", 4.99, "Toiletries")
# avocados = Products("Avocado", .99, "Food")

# target.add_product(new_product=paperclips.name)
# target.add_product(new_product=avocados.name)
# # print(target.products)
# avocados.print_info()
# paperclips.print_info()
# paperclips.update_price(20,False)
# paperclips.print_info()
# target.sell_product(1)