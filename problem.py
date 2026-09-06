name=input("enter your name:")
age=int(input("enter your age:"))
print('Hi',name , "next year youll be " , age+1)


n1=float(input("enter a 1st number:"))
n2=float(input("enter a 2st number:"))
sum=n1+n2
diff=abs(n1-n2)
pro=n1*n2
quo=n1/n2
print("sum is :",sum , 
      "diff is:" ,diff ,
      "pro is :" ,pro ,
      "qou is :",quo)
      
fullname=input("enter full name:")
parts=fullname.split()
print("first name",parts[0])
print("last name",parts[-1])

  
sent = input("enter a word: ")
vowels ="aeiouAEIOU"
count = 0
for ch in sent :
    if ch in vowels:
        count=count+1
        print(count)
        
num=input("enter a number:")
if num==num[::-1]:
    print('palandrom',num)
    