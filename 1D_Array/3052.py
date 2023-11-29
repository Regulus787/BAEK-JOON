list=[]
for i in range(10):
    a=int(input())
    n=0
    value=a%42
    for j in range(len(list)):
        if list[j]!=value:
            n=n+1
    
    if n-len(list) == 0:
        list.append(value)
    else:
        n=0
print(len(list))
