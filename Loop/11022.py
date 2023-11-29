import sys
iteration=int(sys.stdin.readline())
i=0

for i in range(iteration):
    a,b=map(int,sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" % (i+1,a,b,a+b))
