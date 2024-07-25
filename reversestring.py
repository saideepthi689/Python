s=input()
#using slicing
#method1
print(s[::-1])
#using functions
#method2
def rev_str(s):
    rev=""
    for i in s:
        rev=i+rev #i starts from first letter
    return rev
print(rev_str(s))
#method 3
def rev_str1(s):
    rev=""
    s=s.split()
    rev=list(reversed(s))#s became reverse list
    print(rev)
    for i in rev:
        rev=i[::-1]
        print(rev,end=" ")
rev_str1(s)
