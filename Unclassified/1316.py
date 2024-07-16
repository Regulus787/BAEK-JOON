x = int(input())
count = 0

for i in range(x):
    charset = set()
    result = True
    a = input()

    for j in range(len(a)):
        if a[j] in charset:
            if a[j-1] != a[j]:
                result = False
                break
        else:
            charset.add(a[j])

    if result:
        count += 1

print(count)
