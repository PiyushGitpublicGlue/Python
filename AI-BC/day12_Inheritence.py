class A:
    def m1(self):
        print("M1 - I am from class A")

class B:
    def m1(self):
        print("M2 - I am from class B")

class C(B,A):
    def m3(self):
        print("M3 - I am from class C")


c1 = C()
c1.m1()
#c1.m2()
c1.m3()

#mro method resolution order
# if same method same with two class which is inherited by parent class
print(C.mro())
