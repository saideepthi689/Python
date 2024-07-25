#numbers divisible by 4 and 6
arr=list(map(int,input().split()))
def divby4and6(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]%4==0 and arr[i]%6==0:
            print(arr[i],end=" ")
            count+=1
    return count
print("the count is",divby4and6(arr))


    