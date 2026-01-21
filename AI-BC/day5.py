subStudents = [3,True]
students = ["Piyush","Akhil",subStudents]
name = "Saxena"

#indexing
print(students[0])

#insertion
students.append("Hari")
print(students)

students.insert(1,"new entry")
print(students)

students.extend(name)
print(students)

#Remove
#students.clear()
print(students)

students.pop(1) #index position
print(students)

students.remove('Akhil') #remove
print(students)

#count
print(students.count("Piyush"))

#index
print(students.index("Piyush"))

students.append("Piyush")

print(students.index("Piyush",3,10))

#sort
names = ["Akhil","Piyush","Zishan","Priya","Natrajan"]
print(names)
names.sort() #acending order
print(names)
names.sort(reverse=True) #decending order
print(names)
#Reverse
#names.reverse() #decending order
#print(names)

print("copy method")
secondList = names.copy()
print(names)
print(secondList)
names.append("new entry")
print(names)
print(secondList)
names[5]="updated"
print(names)