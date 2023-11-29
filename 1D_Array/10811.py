list=[]
a,b=map(int,input().split())
for num in range(a):
    list.append(num+1)

for i in range(b):
    c,d=map(int,input().split())
    for j in range(d-c+1):
        if c+j<=d-j:
            list[c+j-1],list[d-j-1] = list[d-j-1], list[c+j-1]
        else:
            break
print(*list)
