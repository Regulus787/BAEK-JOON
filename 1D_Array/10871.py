a, b=map(int,input().split())
c = [int(x) for x in input().split()]

list=[]
if len(c)==a:
    for i in range(a):
        if c[i]<b:
            list.append(c[i])
print(*list)
