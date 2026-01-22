#unpacking

#List

guestlist = ["Piyush","Saxena","Shilpa","Haris","Natha"]

a, b, c, d, e = guestlist
print(a,b,c,d,e)

#tuple

guestlist = ("Piyush","Saxena","Shilpa","Haris","Natha")

a, b, c, d, e = guestlist
print(a,b,c,d,e)

#Set

guestlist = {"Piyush","Saxena","Shilpa","Haris","Natha"}

a, b, c, d, e = guestlist
print(a,b,c,d,e)

#dict

employees = {"name":"Piyush",
             "age":30}

#a,b = employees.keys()
#a,b = employees.values()
a,b = employees.items()
print(a,b)