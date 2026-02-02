class P:

    def __init__(self,name,age,city):
        self.city = city # public variable
        self._name = name # protected variables
        self.__age = age #private variable

    def m1(self):
        print("Parent way of running things!")

class C(P):
    def m1(self):
        print(self.city)
        print(self._name)
        #print(self.__age) #name mangling, need to add _Classname__Variable
        print(self._P__age) #name mangling, need to add _Classname__Variable
        super().m1()
        print("Child way of running things!")


c1 = C("Piyush",30,"Delhi")
c1.m1()

#p1 = P("Piyush",30,"Delhi")
# print(p1.city)
# print(p1._name)
# print(p1._P__age) #name mangling, need to add _Classname__Variable

