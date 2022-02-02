n=int(input())
i=0
while i<n:
    num=int(input())
    if num%2==0:
        print(num//2 +1)
    else:
        print((num+1)//2)
    i+=1
