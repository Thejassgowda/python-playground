#to find even number useing if
a=int(input("Enter the number:"))
if a%2==0:
    print("Enterd number is is even")
    
#to find even  and odd number 
a=int(input("Enter the number:"))
if a%2==0:
    print("Enterd number is is even")   
else:
     print("Enterd number is is odd")  
         

#to check single condition
num1=int(input("Enter the first num:"))
num2=int(input("Enter the second num:"))
if num1<num2: #if condition
    print("second number is greter")
else:
    print('first number is greter')    
    
    #to check multiple condition(elif)
num1=int(input("Enter the first num:"))
num2=int(input("Enter the second num:"))
if num1>num2: #if condition
    print("first number is greter")
elif num1<num2:
    print('second number is greter')  
elif num1==num2:   
    print('Both number are equal') 
    
    #Grading the marks
marks = float(input("Enter the obtain marks : "))
if marks>=90:
    Grade = "A"
elif marks>=75:
    Grade = "B"
elif marks>=50:
    Grade = "C"
else:
    Grade ="F"
print("Your Grade is :", Grade)