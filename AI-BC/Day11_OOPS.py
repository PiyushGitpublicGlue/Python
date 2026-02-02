class Human:

    def __init__(self,name1,age1,city1):
        self._name = name1 #protected #instance variables
        self.age = age1 #public
        self.__city=city1 #private there is a concept name mangling applies, 
        # what is name mangling
        # for outside world, don't access it as a __city
        # use it as : _Human__city

    #def _printInfo(self):
    #    print(f'{self._name} has age as {self.age} and lives in city {self.__city}')

    def _printInfo(self, *args):
        if len(args)>0: print(f'{self._name} has age as {self.age} and lives in city {self.__city} with {args[0]}')
        else : print(f'{self._name} has age as {self.age} and lives in city {self.__city}')

h1 = Human("Piyush",25,"Delhi")
#h1.printInfo()
#print(h1._name) #accessing protected variable, outside the class
#print(h1.age) #public
#print(h1.__city) #accessing private variable, outside the class  #not working
#print(h1._Human__city) #accessing private variable, outside the class #working with prefix as _classname
#print(h1.__dict__) # dunder methods
h1._printInfo("extra1","extra2")
h1._printInfo()