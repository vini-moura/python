from random import randint

print('welcome to the Guessing Game')
print("I'm thinking in a number between 1 and 100\n")

def guessing_game():
  a = randint(0,100)
  win = False
  level = input('type "e" for easy level and "h" for hard level: ')
  attempts = 0
  if level == 'e':
    attempts = 10
  elif level == 'h':
    attempts = 5
  else:
    print('invalid answer')
  while attempts != 0:
    print(f'You have {attempts} attemps remaining')
    b = int(input('\nMake a guess: '))
    if b > a:
      attempts -= 1
      print('Too high')
    elif b < a:
      attempts -= 1
      print('Too low')
    elif b == a:
      attempts = 0
      win = True
      print("That's right!")
    if win == False and attempts == 0:
      print('you lose!')
      print(f'The answer was {a}')
    elif win == True and attempts > 0:
      print("you win!")
      break
      
guessing_game()




#################teacher's solution


from random import randint

EASY = 10
HARD = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print('too high')
    return turns - 1
  elif guess < answer:
    print('Too low')
    return turns - 1
  else:
    print("That's It!")
  
def set_dificulty():
  level = input("Choose a dificulty, 'e' or 'h'")
  if level =='e':
    return EASY
  else:
    return HARD

def game():
  print("Welcome to the guessing game")
  print("I'm guessing a number between 1 and 100")
  answer = randint(1,100)

  turns = set_difficulty()
  guess = 0
  while guess != answer
  

guess = int(input("make a guess: "))
turns = 0






