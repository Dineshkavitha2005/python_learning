a=[]
print("Enter 10 numbers:")
for i in range(10):
    num=int(input("Enter num "+ str(i+1)+ ":"))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print("sum:",sum)

average=0
for i in a:
    average=sum/10
print("average:",average)
# PRINTS SUM AND AVERAGE OF AN NUMBER
