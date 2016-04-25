import random
number = random.randint(1, 1000)
guess_taken = 0

print('Hello! What is your name?')
player = input()

number = random.randint(1, 1000)
print('Well, ' + player + ', I am thinking of a number between 1 and 1000.')

while guess_taken < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guess_taken = guess_taken + 1

    if guess < number:
        print('Your guess is too low.') 
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guess_taken = str(guess_taken)
    print('Good job, ' + player + '! You guessed my number in ' + guess_taken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
