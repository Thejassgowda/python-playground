#print 1 to 20 numbers
'''i=1
while  i<=20:
 print(i)
 i+=1'''
 
 #print even numbers 1to 50
i=1
while i<=50:
   if i%2==0: 
     print(i)
   i+=1 

#sum from 1to n given by user
n=int(input("enter the number till sum:"))
total=0
i=1
while i<=n:
    total+=i
    i+=1
print("sum of 1 to", n ,"is",total ) 

###  Multiplication Table
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
 
 # 19. Guess the Secret Number
secret = 7  # hardcoded for now
guess = int(input("Guess the number: "))

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess the number: "))

print("Correct! You guessed it.")
