""" is_name = "Piyush"
if is_name:
    print("Correct!")
else:
    print("Wrong!")

age = 18

if age<18:
    print("User is Child")
elif age>=18 and age<=60:
    print("User is Adult")
else: print("User is Elder")

guest_list = []
if guest_list:
    print("in true block")
else: print("in false block")



while age>10:
    age-=1
    print("age is 18")
    
print("ending while loop!")
 

guestlist = ["Piyush","Saxena","Shilpa","Haris","Natha"]

for name in "Piyush":
    print(f'name is {name}')

 """

# for i in range(10): #only int is allowed
#     print("repeated tasks!!")

# guestlist = ["Piyush","Saxena","Shilpa","Haris","Natha"]

# for index,value in enumerate(guestlist): #index, value
#     print(f'{index} : my guest {guestlist[index]}')

# for i in range(0,10,2):
#     print(i)

# for i in range(10,-1,-1):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# guestlist = ["Piyush","Saxena","Shilpa","Haris","Natha"]
# print(guestlist[2:1:-1])

# l1 = ["a",12,"b"]

# l2 = ["a",12,"b"]

# l3 = l1

# if l1 == l2: # == comparing content not memory, but is is comparing memory not content
#     print("object matches!")
# else:
#     print("object doesn't match!")

l1 = ["a",12,"b"]
#if l1.count("a")==1:
if "c" in l1:
    print("exist in list")
else: print("doesn't exists")