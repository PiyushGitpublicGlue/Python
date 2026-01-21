#lists []
#tuples ()
#dic {}

grade = ["a1","a2"]
students = ["Akhil","Piyush","Zishan","Priya","Natrajan"]
lastName = "Saxena"

firstTuple = ("Piyush","Saxena",True,89)
print(firstTuple)

#tuple are immutable
firstTuple = ("Akhil",90) #allowed reassigning new value to tuple
print(firstTuple)

firstTuple[0]="update"