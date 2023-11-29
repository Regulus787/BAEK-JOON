a=int(input())
b=[int(x) for x in input().split()]
max_num=max(b)
for i in range(len(b)):
    b[i]=(b[i]/max_num)*100
new_mean=sum(b)/a
print(new_mean)
