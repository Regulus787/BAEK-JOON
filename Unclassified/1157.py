a=input()
max_num=0
askii=[]
num=[]
for i in range(len(a)):
    value=ord(a[i])
    if value>=97 and value<=127:
        value=value-32
    askii.append(value)
for j in range(65,91):
    num=askii.count(j)
    if num>max_num:
        max_num=num
        result=j
    elif num==max_num:
        result=False

if result == False:
    print("?")
else:
    print(chr(result))
