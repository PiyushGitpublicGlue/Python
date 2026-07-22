class Product:
    total_items_in_warehouse  = 0

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        Product.total_items_in_warehouse +=self.quantity

# Before creating anything, total is 0
print(Product.total_items_in_warehouse)  # Should print 0

p1 = Product("Laptops", 10)
p2 = Product("Monitors", 5)

# Both products have been added to the overall warehouse count
print(Product.total_items_in_warehouse)  # Should print 15
print(p2.quantity)                       # Should print 10 (individual quantity)