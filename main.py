"""
PowerOfTen
"""
# Provide your solution here
while True:
    number = int(input("Enter a max three-digit number: "))

    if number < 0:
        print("number cannot be negative")
        continue

    if number >= 1000:
        print("number has more than 3 digits")
        continue

    if number >= 0 and number < 1000:
        result_integer = number // 10; number%10
        print(f"(integer): {result_integer}")
        break


"""
Cash Box
"""
# Provide your solution here

while True:
    n1 = int(input("To pay: "))
    n2 = int(input("Received: "))
    change = n2 - n1

    if n1 < 0:
        print("Negative payment is invalid.")
        continue

    if n2 < 0:
        print("Negative received amount is invalid.")#
        continue

    if n1 > n2:
        print("You did not pay enough.")
        continue

    if n2 > n1:
        print(f"Your change is: {change}")
        break


