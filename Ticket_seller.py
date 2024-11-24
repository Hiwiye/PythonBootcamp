print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12

    Wants_Photo = input("Do you want to take a photo? Type y for yes or n for no")

    if Wants_Photo == "y":
        bill += 3

    print(f"your final bill is {bill}")        

else:

    print("Sorry you have to grow taller before you can ride.")
