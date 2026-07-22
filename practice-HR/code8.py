# write a program

def count_characters():
    dic = {}
    name1 = input("Enter your name : ")
    for i in name1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    print(dic)
    print(type(dic))

#count_characters()

# write a program to verify two string is anagram or not ?

def verifyAnagram():
    str1 = input(" Enter first string : ")
    str2 = input(" Enter second string : ")
    str1="".join(sorted(str1.replace(" ","").lower()))
    str2="".join(sorted(str2.replace(" ","").lower()))
    if str1 == str2:
        return True
    else:
        return False
    
print(verifyAnagram())

