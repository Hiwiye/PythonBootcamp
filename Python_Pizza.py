print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

pepperoni_size = input("for small or large? if small say s for large say l")
if pepperoni == "Y":
    if pepperoni_size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is{bill}")
else:
    print(f"Your final bill is{bill}")





