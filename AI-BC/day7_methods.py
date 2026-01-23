def myfirstfunction ():
    print("This is my first function in python")

#myfirstfunction()

#funtciton without return

def calculate(a,b):
    print(a+b)

#print(calculate(4,4))

#function with return type

def returningFunction(a:int,b:int)->int:
    return a+b

output = returningFunction("Piyush","Saxena")
# output = returningFunction(True,False)
print(output,type(output))