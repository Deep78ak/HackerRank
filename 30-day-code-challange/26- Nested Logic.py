from datetime import date

actual=list(map(int,input().split()))
ex=list(map(int,input().split()))
actual=date(day=actual[0], month=actual[1], year=actual[2])
ex= date(day=ex[0], month=ex[1], year=ex[2])

fine=0

if actual>ex:
    if actual.year==ex.year:
        if actual.month==ex.month:
            fine=15*(actual.day-ex.day)
        else:
            fine=500*(actual.month-ex.month)
    else:
        fine=10000

print(fine)



