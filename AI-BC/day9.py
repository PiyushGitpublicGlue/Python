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
        #all your instance variable should be initialize in constructor only
        self.cardid = cardid
        self.fname = fname
        print(f"{self.fname} with card is {self.cardid} Constructor created in pyhton")

    # instance method

    def getPunchInTime(self, startTime,endTime):
        #name = "Piyush Saxena" #local variable
        diff = endTime-startTime
        return f'{self.cardid} User spent time as : {diff}'
    
    # class method
    @classmethod # decorator
    def updateName(cls,companyname):
        cls.employeeName = companyname

# object creation
e1 = Employee(45,"Piyush Saxena")
e2 = Employee(50,"Python BI")
res = e2.getPunchInTime(80,100)
#print(res)
e1.updateName("infosys")
#Employee.employeeName="Infosys"
print(e1.employeeName)
print(e2.employeeName)

