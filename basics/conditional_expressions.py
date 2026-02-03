# conditional expression = a one-line shortcut for if-else statement (ternary operator)
# print or assign one of two values based on a condition
# x if condition eelse y

num = 5
a = 6
b = 7

# print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b

#print(max_num)
#print(min_num)

temperature = 20
weather = "HOT" if temperature > 20 else "COLD"
#print(weather)

user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
