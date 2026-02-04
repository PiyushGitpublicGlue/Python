class A:
    def m1(self,a):
        pass

    def m2(self, a):
        print(f"method has a value {a}")

a = A() # this should not allowed to create obj of abstract class
# abstract class should only be allowed to inherited, nothing else
a.m1(7)