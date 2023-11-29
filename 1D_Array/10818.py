a=int(input())
b = [int(x) for x in input().split()]

if len(b)==a:
    print(min(b))
    print(max(b))
