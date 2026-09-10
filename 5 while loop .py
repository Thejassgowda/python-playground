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