import random
name = input('What is your name?')
print('Welcome to my quiz',name)
guess = 0
tries = 0
answer = 5
score = 0
while guess != answer and tries < 2:
    guess = int(input("10/2 is..."))
    if guess == answer:
       print ("Correct")
       score = score + 1
    else:
       print ("Incorrect")
       score = score + 0
    tries = tries + 1
guess = 0
tries = 0
answer = 25
while guess != answer and tries <2:
    guess = int(input("5*5 is..."))
    if guess == answer:
      print("Correct")
      score = score + 1
    else:
      print("Incorrect")
      score = score + 0
    tries = tries + 1
print("Thank you for playing",name,". You scored",score,"points")
