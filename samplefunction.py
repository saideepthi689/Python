def evenorodd(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
n=int(input())
print(evenorodd(n))
#without using modulo of 2
def check(n):
    if 1&n==0:
        return "even"
    else:
        return "odd"
print(check(n))
# 1 36 24 9 2 12