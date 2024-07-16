def cal(grade):
    if grade == "A+":
        gpa=4.5
    elif grade == "A0":
        gpa=4.0
    elif grade == "B+":
        gpa=3.5
    elif grade == "B0":
        gpa=3.0
    elif grade == "C+":
        gpa=2.5
    elif grade == "C0":
        gpa=2.0
    elif grade == "D+":
        gpa=1.5
    elif grade == "D0":
        gpa=1.0
    elif grade == "P":
        gpa="aa"
    else:
        gpa=0

    return gpa
a=0
grade_list=[]
credit_list=[]
for i in range(20):
    subject, credit, grade=map(str,input().split())
    credit=float(credit)
    if type(cal(grade))==str:
        a=a+1
    else:
        grade_list.append(cal(grade)*credit)
        credit_list.append(credit)
print(sum(grade_list)/sum(credit_list))
