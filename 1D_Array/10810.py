a,b=map(int,input().split())
list=[0]*a

for i in range(b):
    c,d,e=map(int,input().split())
    for j in range(d-c+1):
        list[c+j-1]=e

print(*list)
