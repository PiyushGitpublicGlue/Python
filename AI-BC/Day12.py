#inheritence

class parent:

    # def __init__(self):
    #     print(f"Parent is called")

    def __init__(self,name):
        self.name=name
        print(f"{name} Child is called")

    def m1(self):
        print(f"{self.name} m1 method from parent class")

class child(parent):


    def __init__(self,age,name):
       self.age = age
       #self.name = name
       #parent.__init__(parent,name)
       print(f"{name} Child is called")
       super().__init__(name)

    # def __init__(self):
    #     print(f"Child is called")

    def m2(self):
        print(f"{self.age} m2 method from child class")

#p1 = parent()
#p1.m1()

c1 = child(30,"Piyush") #constructor gets called
c1.m1()
#c1.m2()
#c1.m1()