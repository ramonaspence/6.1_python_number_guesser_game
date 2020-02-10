import random

theanswer = (random.randint(0, 100))

theguess = input('The game has begun and a random number between 0 and 100 has been selected.\n You have ten chances. \nGood luck.')
theguess = int(theguess)

chances = 10

while chances > 0:
    if theguess == theanswer:
        print('Oh! My! God! You guessed it!')
        break
    elif theguess >= theanswer:
        chances = str(chances)
        theguess = input('Oof! Missed it! But you have ' + chances + ' more tries! You got this friend')
        theguess = int(theguess)
        chances = int(chances)
        chances -= 1
    elif theguess <= theanswer:
        chances = str(chances)
        theguess = input('Whoops! Not quite there. You got ' + chances + ' more tries!')
        theguess = int(theguess)
        chances = int(chances)
        chances -= 1
    elif theguess > 100:
        chances = str(chances)
        theguess = input('Uhhm. Try reading the instructions first.')
        theguess = int(theguess)
        chances = int(chances)
        chances -= 1
    elif theguess < 1:
        chances = str(chances)
        theguess = input('Uhhm. There are instructions..')
        theguess = int(theguess)
        chances = int(chances)
        chances -= 1

if chances == 0:
    print('Sorry! You ran out of chances :(')
input('Do you want continue to the next chanllenge?')
