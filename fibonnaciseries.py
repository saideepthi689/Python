def fib(num):
    first=0
    second=1
    print(first,second,end=' ')
    num-=2
    while(num>0):
        third=first+second
        print(third,end=" ")
        first=second
        second=third
        num-=1
num=int(input())
if num==1:
    print("0")
elif num>1:
    fib(num)
else:
    print()



    