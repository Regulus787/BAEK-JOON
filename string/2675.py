iteration=int(input())
for i in range(iteration):
    a, word=map(str,input().split())
    a=int(a)
    for i in range(len(word)):
        value=word[i]*a
        print(value,end="")
    print()
