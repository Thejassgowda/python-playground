#string is collection of sequence of charecter and is immutabel(unchangeadle)
fruit="Banana"
letter=fruit[0]
print(letter) # B

letters=fruit[0:4]#  String slicing [start:stop;step]
print(letters) # Bana

leter=fruit[0:7:2]#  String slicing [start:stop;step]
print(leter)#bnn

#manuplation
fruit="A apple is to costly  "
length=len(fruit)
print(length)#7

print(fruit.lower()) #a aplle
print(fruit.upper()) #A APPLE

message = "his is warning! "
print(message*10)     # multi times display
print(message.strip()*2)   # use  to remove the spacce b/w words 

print(message.replace("warning","error"))  # to replace the word
print(message.title())         # convert first letter to upper



