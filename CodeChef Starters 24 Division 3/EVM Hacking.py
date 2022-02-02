n=int(input())
i=req=x=y=z=0
while i<n:
    a,b,c,p,q,r=map(int,input().split())
    total_possible=p+q+r
    total_won=a+b+c
    x=p-a
    y=q-b
    z=r-c
    if total_possible%2==0:
        req=total_possible//2 - total_won +1
    else:
        req=(total_possible+1)//2 -total_won 
    
    if x>=req or  y>=req or  z>=req :
        print("YES")
    else:
        print("NO")
    i+=1
