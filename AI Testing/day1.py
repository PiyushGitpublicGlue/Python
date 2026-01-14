from datetime import datetime
message = 'Hello World World'
print(message)

multi_line_message = """Hi world!!
how are you!!"""

print(multi_line_message)
print(len(multi_line_message))
print(len(message))

print(message[1:6])
print(message.upper())
print(message.count("l"))
print(message.find("Sakshi"))

print(message.replace("World","Sakshi",2))

greeting = "Hi"
name = "Piyush"

print(greeting+" "+name+ " How are you ?")
print(f"{greeting.upper()} {name.upper()} How are you ?")
print('{} {} How are You ?'.format(greeting,name))

#dir function

#print(dir(name))
#print(help(str))
#print(help(str.lower))

person = {'name':'Piyush','age':32}
sentence = 'My name is {} and I\'am {} years old!'.format(person['name'],person['age'])
sentence_f = f"My name is {person['name']} and I'am {person['age']} years old!"

print(sentence)
print(sentence_f)

calculation_in_f_str = f"4 time 11 is wuqal to {4*11}"
print(calculation_in_f_str)

#for loop with f string

for n in range(1,11):
    sentence = f"The value is {n:02}"
    print(sentence)

pi = 3.14159265
sentence = f"Pi is equal to {pi:.4f}"
print(sentence)



birthday = datetime(1900,1,1)
sentence = f"Piyush has a birthday on {birthday:%B %d, %Y}"

print(sentence)