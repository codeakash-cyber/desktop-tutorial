num1=int(input("Enter A number: "))
num2=int(input("Enter A number: "))

ops=input("Use the operator: (+,-,*,/)= ")
if(ops=='+'):
    print("Sum= ",num1+num2)
elif(ops=='-'):
    print("Substraction= ",num1-num2)
elif(ops=='*'):
    print("Product= ",num1*num2)
elif(ops=='/'):
    if num2 != 0:
        print("Division= ",num1/num2) 
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")      