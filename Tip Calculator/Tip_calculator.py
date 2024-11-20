print("Wellcome to the tip calculator")
Bill = float(input("What was the total bill?"))
Tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people will split the bill?"))
money = float((Bill * Tip/100)+ 150)/5
formatted_money = "{:.2f}".format(money)
print("Each person should pay", formatted_money)