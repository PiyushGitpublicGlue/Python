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

print(dir(name))
print(help(str))
print(help(str.lower))