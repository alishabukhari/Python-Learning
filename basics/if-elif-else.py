#if = do some code IF some condition is True
#     Else do something Else

age = int(input("Enter you age: "))

if 18 < age < 75:
    print("You can drive.")
elif age == 18:
     print("You must get a driver's liscence before you are eligible to drive.")
elif age < 0:
     print("You are not born yet!")
elif age >= 100:
     print("You are too old!")
else:
     print("You are not eligible to drive")
