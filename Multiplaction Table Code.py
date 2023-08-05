#Welcome Message
print("Welcome to the Multiplication Table Generator!")

#Name
name = input("Please enter your name: ")

def checkNum():
    user_input = input(":")
    while user_input.isdigit() == False:
        user_input = input("Not valid please try again: ")
    return user_input
    
#Accept input Multiplicand from user  
print("Give me a starting multiplicand")
multiplicand = int(checkNum())
print("You gave me", multiplicand)

#Accept input Multiplier from user
print("Now please give me a multiplier")
multiplier = int(checkNum())
print("You gave me", multiplier)

#Accept input Range from user
print("Now give me a ending range")
times = int(checkNum())
print("You gave me", times)

for i in range (multiplicand, times+1):
   math = i * multiplier
   print(i, "x", multiplier, "=", math)

while multiplicand >= times:
   product = multiplicand * multiplier
   print(multiplicand, "x", multiplier, "=", product)
   multiplicand = multiplicand + 1
