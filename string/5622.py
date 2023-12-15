def counttime(charstring):
    if charstring == "A" or charstring == "B" or charstring == "C":
        count = 3
    elif charstring == "D" or charstring == "E" or charstring == "F":
        count = 4
    elif charstring == "G" or charstring == "H" or charstring == "I":
        count = 5
    elif charstring == "J" or charstring == "K" or charstring == "L":
        count = 6
    elif charstring == "M" or charstring == "N" or charstring == "O":
        count = 7
    elif charstring == "P" or charstring == "Q" or charstring == "R" or charstring == "S":
        count = 8
    elif charstring == "T" or charstring == "U" or charstring == "V":
        count = 9
    elif charstring == "W" or charstring == "X" or charstring == "Y" or charstring == "Z":
        count = 10
    return int(count)

charstring = input()
count = 0
for i in range(len(charstring)):
    count = count + counttime(charstring[i])
print(count)
