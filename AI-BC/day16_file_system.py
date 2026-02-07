# file = open("dummy.txt","r+", encoding="utf-16")
# file.write("Hi")
# #file.write("Hi") #this will overwright everything in file
# # content = file.readline()
# # content1 = file.readline()
# file.seek(0) # reset cursor to 1st line
# content = file.read()
# print(content)
# file.close()

# content1 = file.read()
# print(content)
# print(f'remeaning {content1}')

# with open("dummy.txt","a+", encoding="utf-16") as file:
#     file.write("Hi")
#     #file.write("Hi") #this will overwright everything in file
#     # content = file.readline()
#     # content1 = file.readline()
#     file.seek(0) # reset cursor to 1st line
#     content = file.read()
#     print(content)
#     #file.close()

import os
print(os.getcwd())
print(__file__)
print(os.path.dirname(__file__))
print(os.path.exists(__file__))
print(os.path.basename(__file__))
print(os.getcwd(),)