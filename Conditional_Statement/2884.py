a, b = map(int, input().split())

b -= 45
a = (a - 1 + 24) % 24 if b < 0 else a
b = (b + 60) % 60

print(a, b)
