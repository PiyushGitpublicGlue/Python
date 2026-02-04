from abc import ABC,abstractmethod

class A(ABC):
    def m1(self,a):
        print(f"var is {a}")

    @abstractmethod
    def m2(self,a):
        pass


class B(A):

    def m2(self,a):
        print(f"var is {a}")

b1 = B()
b1.m2(8)