n=int(input())
i=0
while i<n:
    a,b=(map(int, input().split(' ')))
    a1=a//2
    b1=b
    if a1<b1:
        print(a1)
    else:
        print(b1)
    i+=1
