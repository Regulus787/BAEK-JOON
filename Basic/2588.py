ori_a=int(input(""))
ori_b=int(input(""))

bbb=int(ori_b/100)
bb=int(ori_b/10)-bbb*10
b=int(ori_b)-(bbb*100+bb*10)

print(ori_a*b)
print(ori_a*bb)
print(ori_a*bbb)
print(ori_a*ori_b)
