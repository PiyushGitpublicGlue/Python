class InvalidLoginException (Exception):
    pass

class OutOfStockException (Exception):
    pass

class User:

    def __init__(self, username:str, password:str):
        self.username = username
        self.__password = password
        self.isLoggedIn = False

    def login(self, password:str):
        if self.isLoggedIn == True:
            raise InvalidLoginException(" User Already Logged In !!")
        if self.__password != password:
            raise InvalidLoginException(" Wrong password !!")
        self.isLoggedIn=True
        print(" User is logged in !!")

    def logout(self):
        if self.isLoggedIn==False:
            raise InvalidLoginException(" No user logged in !! ")
        

class Product:
    def __init__(self, product_id:int, name:str, price:float, quantity:int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_hashmap = {}
        self.my_hashmap[self.product_id] = self.name


    def add_stocks(self,qty:int):
        self.quantity+=qty        

    def sell(self,qty:int):
        if self.quantity<qty:
            raise OutOfStockException (" Out of Stock Limit !!")
        self.quantity-=qty

user = User("Piyush","Sakshi")
try:
    user.login("Sakshii")
except InvalidLoginException as e:
    print(f"⚠️ Login System Caught Error: {e}")
log = []
#user.login("Piyush")
product = Product(101,"Dress",100.0,10)
product.add_stocks(10)
log.append(f"{user.username} add {product.quantity} ({product.name})")
#print(log)
try:
    product.sell(22)
except OutOfStockException as e:
    print(f"⚠️ Out of Stock Caught Error: {e}")
log.append(f"{user.username} sold {product.quantity} ({product.name})")
print(log)
print(product.quantity)

