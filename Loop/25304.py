total=int(input())
kinds=int(input())
total_price=0

for i in range(kinds):
    items, quantity=map(int,input().split())
    total_price=total_price+(items*quantity)

if total_price==total:
    print("Yes")

else:
    print("No")
