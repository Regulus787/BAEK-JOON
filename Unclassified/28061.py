x=int(input())
num_list=list(int(x) for x in input().split())
for i in range(len(num_list)):
    num_list[len(num_list)-1-i]=num_list[len(num_list)-1-i]-(i+1)

print(max(num_list))
