num = -1

# elif
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# nested if
if num > 0:
    print("Positive number")
else:
    if num == 0:
        print("Zero")
    else:
        print("Negative number")