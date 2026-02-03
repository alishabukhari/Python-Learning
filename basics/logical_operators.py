# logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condtion must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = 35
is_raining = False

#if temp > 32 or temp <0 or is_raining:
#    print("The outdoor event is cancelled")
#else:
#    print("The outdoor event is still scheduled")

is_sunny = True
if temp >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is moderate outside 🙂")
else:
    print("It is good weather outside 😃")