# reverse a number
num = 123
sum=""
while num!=0:
    n=num%10
    sum=sum+str(n)
    num=num//10

print(sum)

#countdown till 0.
count = 18
for i in range(count, -1, -1):
    print(i)

