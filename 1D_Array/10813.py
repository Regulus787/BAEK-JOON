a,b=map(int,input().split())
list=[0]*a
for i in range(a):
    list[i]=i+1

for j in range(b):
    c,d=map(int,input().split())
    value=list[c-1]
    list[c-1]=list[d-1]
    list[d-1]=value

print(*list)
