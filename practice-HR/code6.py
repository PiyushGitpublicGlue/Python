#The Problem: You have a list of raw transaction numbers or sensor readings. 
# You need to parse them, categorize them into odd or even groups, and count them

# list1 = [12, 45, 78, 23, 89, 100, 56, 37]
# odd_count = 0
# even_count = 0

# for i in list1:
#     if i%2==0:
#         odd_count+=1
#     else:
#         even_count+=1

# print("odd reading is ",odd_count)
# print("even reading is ",even_count)

def remove1(list2):
    unique_ids = []
    for i in list2:
        if i not in unique_ids:
            unique_ids.append(i)
    return unique_ids

def remove2(list2):
    for i in range(len(list2)):
        for j in range(len(list2)-1,i,-1):
            if list2[i] == list2[j]:
                del(list2[j])
    return list2


list2 = ["ID_402", "ID_105", "ID_402", "ID_311", "ID_105", "ID_999"]
print(remove2(list2))