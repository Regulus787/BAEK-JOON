a = input()
ascii_values = []
i = 0

while i < len(a):
    value = ord(a[i])

    if value == ord('c'):
        if i + 1 < len(a) and (ord(a[i + 1]) == ord('=') or ord(a[i + 1]) == ord('-')):
            value = 222
            i = i + 1

    elif value == ord('d'):
        if i + 1 < len(a) and ord(a[i + 1]) == ord('z'):
            if i + 2 < len(a) and ord(a[i + 2]) == ord("="):
                value = 223
                i = i + 2
        elif i + 1 < len(a) and ord(a[i + 1]) == ord('-'):
            value = 224
            i = i + 1

    elif value == ord("l"):
        if i + 1 < len(a) and a[i + 1] == "j":
            value = 225
            i = i + 1

    elif value == ord("n"):
        if i + 1 < len(a) and a[i + 1] == "j":
            value = 226
            i = i + 1

    elif value == ord("s"):
        if i + 1 < len(a) and a[i + 1] == "=":
            value = 227
            i = i + 1

    elif value == ord("z"):
        if i + 1 < len(a) and a[i + 1] == "=":
            value = 228
            i = i + 1

    i = i + 1
    ascii_values.append(value)

print(len(ascii_values))
