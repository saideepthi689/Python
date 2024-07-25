s=input()
sum=0
countofDig=0
for i in range(0,len(s)):
    if s[i].isdigit():
        sum+=int(s[i])
        countofDig+=1
print(sum)
print(countofDig)
#sum of digits in a string
#a1b2c3
#output 6
#isdigit() checks whether it is digit or not