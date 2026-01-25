def f1():
    print("Hellow World!")

def f2():
    print("My name is Piyush Saxena")

def f3(val1):
    print(f'$$$$$$')
    val1()
    print('******')
    val1()

# passing f to an arg
def f4(val1):
    def f5():
# inner f rem the variable provided from parent scope (closure)
        print(f'$$$$$$')
        val1()
        print('******')
        val1()
# return a f from a f
    return f5

#f3(f1)
#f3(f2)

f1 = f4(f2)
f1()