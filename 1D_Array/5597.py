selected_list=[0]*30

for i in range(28):
    a=int(input())
    selected_list[a-1]=a
for j in range(30):
    if selected_list[j] == 0:
        answer=j+1
        print(answer)
