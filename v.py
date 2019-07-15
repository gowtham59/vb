a1=str(input())
sum2=0
for i in a1:
    if a1.count(i)>sum2:
        sum2=a1.count(i)
        max=i
print(max)
