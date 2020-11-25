import math

def prime_number(num):
    if num==1:
        return "Not prime"
    sq=int(math.sqrt(num))
    for i in range(2, sq+1):
        if num%i ==0:
            return "Not prime"
    return "Prime"

t= int(input())
for i in range(t):
    number=int(input())
    print(prime_number(number))