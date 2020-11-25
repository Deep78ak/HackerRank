class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        lenelement=len(a)
        maximum=0
        for i in range(len(a)):
            for j in range(len(a)):
                diff=abs(a[i]-a[j])
                if maximum<diff:
                    maximum=diff
        self.maximumDifference=maximum

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)