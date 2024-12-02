print('''                     ___,
                    o___.-' /
                    |      _\_
                    |___.-'   `
                    |
                    |
            _   _   j   _   _
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
  _   _   _  [_j__j__j__j__]  _   _   _   _
_[_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
  _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
     j  j  j [  j  j  j  j ] j  j  j  j    
	   ''')

print("Hello Brave Traveler, Wellcome to the tower.")
print("Your mission is to save the queen.")

entry = input("You need to enter the tower. Choose your entery way. \n Type \"window\" or \"door\":  ")
if entry == "window":
  print("You sliped and fell. GAME OVER!")  
elif entry == "door":
  print("You've entered a big hallway, there is a stairs to the left.")
  movment = input(" Type \"Stairs\" or \"Hallway\":")
  if movment == "Hallway":
    print("As you step in to the hallway you realize, its dark and has many twists and turns. You got lost. GAME OVER!")
  elif movment == "Stairs":
    print("You have reached the highest point of the tower. You see a huge dragon sleeping infront of you, there are doors behind it.")
    method = input("Type \"kill dragon\" or \"snick away\": ")
    if method == "snick away":
      print("You woke the dragon up and got eaten. GAME OVER!")
    elif method == "kill dragon":
      print("You have fought bravely and slayen the dragon with your mighty sword. You are now faced with three doors arround the room. figure out where the queen is.")
      choice = input("Type \"red door\", \"blue door\" or \"yellow door\": ")
      if choice == "yellow door":
        print("CONGRATS YOU WON!!! YOU ARE THE MAIGHTY TRAVELER WHO SAVED OUR QUEEN!")        
      elif choice == "red door":
        print("A room of fire engulfed you. GAME OVER!")
      elif choice == "blue door":
        print("a room of water drowned you. GAME OVER!")
else:
  print("GAME OVER!")  








