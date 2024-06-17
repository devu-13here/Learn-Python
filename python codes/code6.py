#Ques 6. WAP to create a list of 100 random numbers between 100 and 900. Count and 
#print the:
#I. All odd numbers
#II. All even numbers
#III.All prime numbers


print("THe number chosen randomly here is:")
import random
l=[random.randint(100,900) for _ in range(100)]

print(l)
odd=[]
even=[]

prime1=[]
flag=1
if (int(l%2)==0):
   print("EVEN NUMBER")
else:
     print("ODD NUMBER")
    
