n=int(input())
def sumofDig(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    if sum<10:
        print(sum)
    else:
        check(sum)
def check(sum):
    if sum<10:
        print(sum)
    else:
        sumofDig(sum)
sumofDig(n)
    