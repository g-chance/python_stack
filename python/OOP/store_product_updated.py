class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        
    def sell_product(self, id):
        self.products.pop(id)
        for val in self.products:
            print(val.name)
    def inflation(self, percent_increase):
        for val in self.products:
            val.price += val.price * percent_increase/100
    def set_clearance(self, category, percent_discount):
        for val in self.products:
            if val.category == category:
                val.price -= val.price * percent_discount/100
    

class Product:
    
    static = 0

    def __init__(self,name,price,cat,store):
        self.name = name
        self.price = price
        self.category = cat
        self.id = Product.static
        Product.static += 1
        store.products.append(self)
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    def print_info(self):
        print(self.name, self.category, self.price, "ID=", self.id)

productid = 0

kohls = Store("Kohl's")
target = Store("Target")
tp = Product("TP", 4.99, "Toiletries", target)
zelda = Product("Zelda", 4.99, "Video Games", target)
akjfdhjk = Product("dsajhg", 6, "dfsjhg", target)
tp.print_info
print("*****")
# target.sell_product(0)
# zelda.print_info()
target.inflation(20)
for val in target.products:
    print(val.name)
print("***********")
tp.print_info()
zelda.print_info()
target.set_clearance("Video Games", 20)
zelda.print_info()
tp.print_info()
print(kohls.products)
akjfdhjk.print_info()
# tp.print_info()
# target.inflation(20)
# tp.print_info()