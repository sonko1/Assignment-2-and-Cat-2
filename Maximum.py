#Write a Python program to find the max number among the three numbers 
def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list) 
# Driven code of X,Y and Z 
x = int(input("Enter First number="))
y = int(input("Enter Second number="))
z = int(input("Enter Third number="))
print("Maximum Number is ::",maximum(x, y, z)) 