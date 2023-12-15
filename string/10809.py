word = input()
lst = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(alphabet)):
    found = False
    for j in range(len(word)):
        if alphabet[i] == word[j]:
            lst.append(j)
            found = True
            break
    if found == False:
        lst.append(-1)

print(*lst)
