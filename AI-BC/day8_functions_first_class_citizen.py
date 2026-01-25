def findSqaure(a):
    return a**2
#assign a function to a variable
res = findSqaure
print(findSqaure(2))
print(res(2))

#you can pass func to another func as argument
#it is called call back function->it is mercy on another function, when a parent function
#wants to call back

# def f1(variable1, variable2):
#     print("Start")
#     variable1(variable2) #calling a function
#     print("Stop")

# #f1("Piyush")

# def f2(msg):
#     print(msg,"i'am method2")

# def f3(msg):
#     print(f"Learning {msg},i'am method3")

# f1(f2,"method2-args")
# f1(f3,"method3-args")

#you can return a function from another function
def f1(msg):
    print(f"f1 called me as {msg}")
    def f2():
        print(f"Hello f2 called me as {msg}")
    return f2

#f2() #not allowed

res = f1("Piyush")
res()
#print(res())
#res("Piyush Saxena")
