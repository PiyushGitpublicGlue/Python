word = "x7K9pM4wB2vR8sY*12Df"
countupper=0
countlower=0
countnumber=0
for char in word:
    if char.isupper():
        countupper=countupper+1
    elif char.islower():
        countlower=countlower+1
    elif char.isnumeric():
        countnumber=countnumber+1
    elif char=="*":
        break
print("Upper : ",countupper)
print("Lower :",countlower)
print("Number :",countnumber)
