# def add(a,b):
#     return a+b

# output = add(4,5)
# print(output)
# print(type(add))

class Employee:

    #not a instance variable
    #class variable
    #these are shred resources #1 copy shared with others
    

    #cardid: int#
    # class variable it is same as in java [static veriable]
    employeeName: str

    #constructor

    def __init__(self, cardid, fname):
        # all your instance variable should be initialize in constructor only
        # instance variable
        self.cardid = cardid
        self.fname = fname
        print(f"{self.fname} with card is {self.cardid} Constructor created in pyhton")


    # instance method
    
    def accessVariables(self):
        print("I'am from instance 'accessVariables' method")
        #print(self.cardid)
        print(Employee.employeeName)

    # instance method

    def getPunchInTime(self, startTime,endTime):
        #name = "Piyush Saxena" #local variable
        #accessVariables()
        Employee.accessVariables()
        diff = endTime-startTime
        return f'{self.cardid} User spent time as : {diff}'
    

    # class method
    @classmethod # decorator
    def updateName(cls,companyname):
        cls.employeeName = companyname

    @classmethod
    def accessVariableInsideClassMethods(cls):
        print("I'am from class method")
        cls.accessVariables()
        #print(self.fname)
        #print(fname)
        #print(cls.fname)
        #print(cls.fname)
    
    @staticmethod
    def m4():
        print("Here i'am")
        print(Employee.employeeName)

# object creation
e1 = Employee(45,"Piyush Saxena")
Employee.employeeName="Piyush"
e1.m4()
#e1.accessVariables()
#e1.accessVariableInsideClassMethods()
#Employee.accessVariableInsideClassMethods()
#Employee.accessVariables()
#print(e1.fname)
#e1.getPunchInTime(66,88)