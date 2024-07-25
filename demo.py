n=int(input())
s,prod=0,0
t=n
while(n>0):
    s+=n%10
    n=n//10
s2=s
rev=0
while s>0:
    rev=rev*10+s%10
    s=s//10
prod=s2*rev
if(prod==t):
    print('Magical Number')
else:
    print('Not magical number')
    