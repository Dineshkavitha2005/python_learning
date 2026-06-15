salary=int(input("Enter the salary:"))
age=int(input("Enter your age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Enter loan amount:"))
    if(loan>50000):
        print("Maximum loan amount is 50000")
    else:
        print("you are eligible for loan")
        
else:
    print("you are not eligible for loan")
