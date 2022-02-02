n=int(input())
i=0
while i<n:
    t,y=map(int,input().split(" "))
    if t==y:
        print(y*2 -1)
    elif y==0:
        print(t)
    else:
        x=t-y
        print(x+ (2*y))
    i+=1
