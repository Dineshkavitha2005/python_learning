mark1=int(input("Enter mark1:"))
mark2=int(input("Enter mark2:"))
mark3=int(input("Enter mark3:"))
mark4=int(input("Enter mark4:"))
mark5=int(input("Enter mark5:"))
average=(mark1+mark2+mark3+mark4+mark5)/5
if(average<35):
    print("Additional class is required")
else:
    print("You are good to do")
