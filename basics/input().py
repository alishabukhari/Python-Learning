#intput() = a function that prompts the user to enter data 
#           Retruns the enerted data as string

name = input("What is you name?: ")
age = int(input("How old are you? "))

#age = int(age) or age = int(input("how old are you?"))
age = age + 1


print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old.")