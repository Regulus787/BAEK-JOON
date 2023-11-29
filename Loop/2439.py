import sys
iteration=int(sys.stdin.readline())

for i in range(iteration):
    print((iteration-i-1)*" "+(i+1)*"*")
