import random
import time
class player():
  def __init__(self, name, level, skin, bg) -> None:
    self.bg = bg # background design of playing field
    self.name = name # Name of the player
    self.level = level #lock will be the lock that player is on
    self.lock_pin = []
    self.guess = []
  pass

Default_player = player(str("Default"), 0, 0, 0)

level_list = [0, 1, 2, 3, 4]

def level_select():
  print("Welcome to the game")
  print("Please select a level")
  while True:
    try:
      Default_player.level = int(input("Level 1 - 5 :"))
      if 1 <= Default_player.level <= 5:
        break
      else:
        print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 5.")
  if Default_player.level == 0:
    print("You are on level 1")
  elif Default_player.level == 1:
    print("You are on level 2")
  elif Default_player.level == 2:
    print("You are on level 3")
  elif Default_player.level == 3:
    print("You are on level 4")
  elif Default_player.level == 4:
    print("You are on level 5")
  else:
    print("Error while picking level")

def level_creator():
  x = Default_player.level * 2
  if Default_player.level == 0:
      x = 1
  for i in range(x):
      Default_player.lock_pin.append(random.randint(1, 9) - 1)

def Gameplay():
  while len(Default_player.guess) != len(Default_player.lock_pin):
    for i in range(len(Default_player.lock_pin)):
      Default_player.guess.append(int(input("Guess a number between 1 and 9:")))
      if Default_player.guess[i] == Default_player.lock_pin[i]:
        print("This lock is Correct")
      elif abs(Default_player.guess[i] - Default_player.lock_pin[i]) == 1:
        print("you're one click away")
      elif abs(Default_player.guess[i] - Default_player.lock_pin[i]) == 2:
        print("you're two clicks away")
      elif abs(Default_player.guess[i] - Default_player.lock_pin[i]) == 3:
        print("you're three clicks away")
      elif abs(Default_player.guess[i] - Default_player.lock_pin[i]) > 3:
        print("You feel you're guess is further than 3 clicks away")
  if Default_player.guess == Default_player.lock_pin:
    print("You have cracked the lock")
  else:
    print("Resetting Lock...")
    time.sleep(2)
    print("Lock Reset")
    Default_player.guess.clear()
level_select()
level_creator()
print(Default_player.lock_pin)
while Default_player.guess != Default_player.lock_pin:
  Gameplay()
quit()