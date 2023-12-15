a, b = map(str, input().split())

if a[2] > b[2]:
    anw = a
elif a[2] < b[2]:
    anw = b
elif a[2] == b[2]:
    if a[1] > b[1]:
        anw = a
    elif a[1] < b[1]:
        anw = b
    elif a[1] == b[1]:
        if a[0] > b[0]:
            anw = a
        elif a[0] < b[0]:
            anw = b

anw_list = list(anw)
anw_list[0], anw_list[2] = anw_list[2], anw_list[0]
anw = ''.join(anw_list)

print(anw)
