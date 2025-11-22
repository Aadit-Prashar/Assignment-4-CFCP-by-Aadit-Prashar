print("Hello, user!")
#Enter the numbers:
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

#Choices for arithematic calculations
print("Select 1 for addition")
print("Select 2 for subtraction")
print("Select 3 for multiplicaion")
print("Select 4 for division")
choices=int(input("Enter your selected choice:"))
#conditions
if choices=='1' :
    sum=num1+num2
    print("On adding numbers we get:",sum)

elif(choices=='2'):
    diff=num1-num2
    print("On subtracting numbers we get:",diff)

elif(choices=='3'):
    product=num1*num2
    print("On multiplying numbers we get:",product)

elif(choices=='4'):
    quotient=num1//num2
    print("On dividing numbers we get:",quotient)

else:
    print("INVALID CHOICE!! Please select from above choices")