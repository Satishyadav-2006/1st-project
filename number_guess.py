import random
n = random.randint(1,10)
guess = 0
while guess != n:
  guess = int(input("Guess a number between 1 to 10"))
  if n < guess:
    print("your guess is too high...")
  elif n > guess:
    print("your guess is too low...")
  else:
    print("PERFECT GUESS!")
