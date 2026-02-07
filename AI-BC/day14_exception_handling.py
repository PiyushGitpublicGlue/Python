def findDivision(num1):
    try:
        res = 100/num1
    except FileNotFoundError as e:
        print(f"File not found error : {e}")

    except ArithmeticError as e1: # Arthmetaic error OR ZeroDivisionError
        print("Zero division error handle block")
        print(f"Error infor : {e1}")
        num1 = 10
        res = 100/num1
        return res
        # you can use multiple except blocks
    else:
        print("i am at else block")
    finally:
        print("Now we are in finally block, this runs everytime")
    return res

def findOutput(num1):
    return findDivision(num1)

print(findOutput(20))
print("Hello to everyOne!!")