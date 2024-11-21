print("Wellcome to the tip calculator")
Bill = float(input("What was the total bill? $"))
Tip = int(input("What percentage tip would you like to give? 10 12 15 ?"))
People = int(input("How many people will split the bill?"))
money = float((Bill * Tip/100)+150)/5
print("Each person should pay", money)