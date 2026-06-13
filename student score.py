score=int(input("Enter the score:"))
if(score<35):
    print("poor student")
if(score>35 and score<70):
    print("average student")
if(score>70):
    print("good student")
# ELSE IS NOT NECESSARY FOR IF ELSE STATEMENT WHEN MORE THAN 1 IF OCCURS

score=int(input("Enter the score:"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
else:
    print("good student")
# TO OVERCOME MULTIPLE IS CONDITION , ELIF CAN BE USED
# WHEN USE OF ELIF ATLAST ELSE STATEMENT IS PRESENT
# AFTER ELSE STATEMENT NOTHING CAN BE EXECUTED


score=int(input("Enter the score:"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
elif(score>70 and score<100):
    print("good student")
else:
    print("invalid score")
