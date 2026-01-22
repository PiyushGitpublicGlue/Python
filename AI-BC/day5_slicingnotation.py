employees = {"name":"Piyush",
             "age":30,
             "dob":89}
guest_list = ["Piyush","Saxena","Shilpa","Haris","Natha"]
guest_tuple = ("Piyush","Saxena","Shilpa","Haris","Natha")
guestlist_set = {"Piyush","Saxena","Shilpa","Haris","Natha"}
name = "Piyush Saxena"

print(name[2])
print(name[2:5:1]) #slicing notation
print(guest_list[1:2:1])
print(guest_tuple[1:2:1])
print(guest_list[2])
print(guest_tuple[2])
#print(guestlist_set[2]) nor allowed
#print(employees[1])

namepod = "Podtest"
print(namepod[6::-1])

print(guest_list[1:len(guest_list):2])

#start:stop:step
print(list(employees.items())[1::1])