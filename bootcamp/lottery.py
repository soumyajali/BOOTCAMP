num = int(input("Enter a 6-digit number: "))

if num < 100000 or num > 999999:
    print("Invalid Number")
else:
    # Split into 3 parts
    part1 = num // 10000
    part2 = (num // 100) % 100
    part3 = num % 100

    # Get the last digit of each part
    last1 = part1 % 10
    last2 = part2 % 10
    last3 = part3 % 10

    # Check if they are consecutive
    if last2 == last1 + 1 and last3 == last2 + 1:
        print("Winning Number")
    else:
        print("Not a Winning Number")