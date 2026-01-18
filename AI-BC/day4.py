firstname = "Piyush"
lastname = "Saxena"
age = 30
havePassport = True

#concatination
fullname = firstname+lastname
print(fullname)
intro = "Hi my name is "+firstname+" "+lastname+" , My age is "+str(age)+" I have Passport ?: "+str(havePassport)
print(intro)

new_intro = f'Hi my name is {firstname} {lastname}, My age is {age} I have Passport ?: {havePassport}'
print(new_intro)

#new_intro[2]='O'
print(new_intro[1])


#funtion vs method
print(len(new_intro))



#equality
if firstname == lastname: print("equal")
else: print("not equal")

if firstname == lastname:
    print("equal")
else:
    print("not equal")

#euality is

if firstname is lastname: print("equal")
else: print("not equal")

#covert to string
print(33)
print(type(33))
print(str(30))
print(type(str(30)))

myIntro = "Piyush learning Python, we are learning together"
print(myIntro.capitalize())
print(myIntro.upper())
print(myIntro.lower())
print(myIntro.islower())

#indexing
print(myIntro.count("learning",20))
print(myIntro.find("Learning"))
print(myIntro.index("learning"))

#ends with
print(myIntro.replace("Python","AI"))
print(myIntro)

print(myIntro.upper().startswith("PIYUSH"))

print(myIntro.split())

print(myIntro.split(","))