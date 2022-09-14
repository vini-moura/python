rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
list = [rock,paper,scissors]
pc_choice = random.randint(0,2)
player_choice = int(input("Type 0 for rock, 1 for paper and 2 for scissors  "))

print(list[player_choice])
print("\ncomputer's choise:\n")
print(list[pc_choice])

if player_choice == 0:
  if pc_choice == 2:
    print("You win!")
  elif pc_choice == 0:
    print("Deal")
  else:
    print("You lose!")
elif player_choice == 1:
  if pc_choice ==0:
    print("You win!")
  elif pc_choice == 2:
    print("You lose!")
  else:
    print("Deal")
elif player_choice == 2:
  if pc_choice == 0:
    print("You lose!")
  elif pc_choice == 1:
    print("You win!")
  else:
    print("deal") 
