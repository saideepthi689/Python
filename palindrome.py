#check whether the string is palindrome or not 
s=input()
reverse=" "
rev=s[::-1]#using slicing
if(s==rev):
    print('Palindrome')
else:
    print('Not a palindrome')
#without slicing
s1=" "
for i in range(len(s)-1,-1-1):
    s1+=s[i]
if(s1==s):
    print('Palindrome')
else:
    print('Not palindrome')

