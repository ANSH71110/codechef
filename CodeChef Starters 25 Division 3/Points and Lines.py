t=int(input())
i=0
while i<t:
    n=int(input())
    x=[]
    y=[]
    xs=set()
    ys=set()
    j=0
    while j<n:
        x1,y1=map(int,input().split(' '))
        x.append(x1)
        y.append(y1)
        xs.add(x1)
        ys.add(y1)
        j+=1
    xn=len(x)
    yn=len(y)
    xi=len(xs)
    yi=len(ys)
    total=(2*xn)-(xn-xi)-(yn-yi)
    print(total)
    i+=1
