# take input and output

print("use to print on the screen")
age = input("Age:") #take input from user
print("Enterd age is:",age) 

 # sample problem
boy_name = input("Enter a boy name:")  #krishna
boy_age = int(input("enter boy age:"))#30 # it convets in to int  

girl_name = input("Enter a girl name:") #radha
girl_age = int(input("Enter a gir age:"))#50

# using abs because sometimes boys might be yonger 
age_diff = abs(boy_age - girl_age)#20

# it called concatenation
print( boy_name + " loves " +  girl_name + ".age diifference is " + str( age_diff) ) #krishna loves radha .age difference is 10
#or we can use formated method(for simple)
print(f"{boy_name} loves {girl_name} - age difference is {age_diff}") # same output