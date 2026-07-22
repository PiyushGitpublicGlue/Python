class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_items(self,item_name):
        self.items.append(item_name)
    
    def remove_items(self,item_name):
        if item_name in self.items:
            self.items.remove(item_name)
        else:
            print("Item not found")

    def show_items(self):
        print("Your items list is :",self.items)


cart = ShoppingCart()
cart.add_items("Piyush")
cart.show_items()
cart.add_items("Sakshi")
cart.show_items()
cart.add_items("Noodles")
cart.show_items()
cart.remove_items("Noodles")
cart.show_items()
cart.remove_items("Noodles")