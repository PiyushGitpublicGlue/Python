def division():

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter Second number : "))
    
    try:
        result = num1/num2
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    

#print("Result is : ",division())

def load_cap():
    list_of_boxes = [10, 20, 35, 15, 40]
    target = int(input("Enter target : "))
    for i in range(len(list_of_boxes)-1):
        #for j in range(1,len(list_of_boxes),1):
        if list_of_boxes[i]+list_of_boxes[i+1]==target:
            print(list_of_boxes[i],list_of_boxes[i+1])

load_cap()