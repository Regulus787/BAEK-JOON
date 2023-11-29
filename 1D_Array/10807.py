a=int(input())
b=list(input().split())
num=0

if len(b)==a:
    c=input()
    for i in range(a):
        if b[i]==c:
            num=num+1
        else:
            num=num
print(num)
