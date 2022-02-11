t=int(input())
i=0
while i<t:
    n,x=map(int,input().split(' '))
    if x>n:
        x%=(n+1)
    print(x)
    i+=1
