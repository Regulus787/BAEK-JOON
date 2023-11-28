a, b = map(int, input().split())
c=int(input())
b+=c

if b>=60:
    a=a+(b/60)
    b=b-60*(b//60)
else:
    b

if a>=24:
    a=a%24
else:
    a

print(int(a),int(b))
