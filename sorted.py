arr=list(map(int,input().split()))
even=sorted([x for x in arr if x%2==0])
odd=sorted([x for x in arr if x%2!=0])
print(even+odd)


