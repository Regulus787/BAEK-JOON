grade=input()
score=0
grades={'F':0.0,'D':1.0,'C':2.0,'B':3.0,'A':4.0}

if grade[0] in grades:
    score=grades[grade[0]]
if len(grade)>1:
  if grade[1]=='+':
    score=score+0.3
  elif grade[1]=='-':
    score=score-0.3

print(score)
