import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numswap=0
for i in range(n):
    for j in range(n-1):
        if (a[j]>a[j+1]):
            numswap+=1
            a[j], a[j+1]=a[j+1] ,a[j]
        
    if numswap==0:
        break
print('Array is sorted in '+str(numswap) +' swaps.')
print("First Element: "+str(a[0]))
print('Last Element: ' + str(a[n-1]))
