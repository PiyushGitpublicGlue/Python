if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    largest = float('-inf')
    slargest = float('-inf')

    for i in range(0, len(arr)):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
            
        elif arr[i]>slargest and arr[i]<largest:
            slargest=arr[i]

    #print(largest)
    print(slargest)