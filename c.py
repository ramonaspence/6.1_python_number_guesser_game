import random

theanswer = input('Okay, okay. This time you pick a number\n and I\'ll guess it! Of course I get ten chances too!\n It\'s got to be between 0 and 100, so no messin\' around!')
theanswer = int(theanswer)
theguess = random.randint(0, 100)
chances = 10

while chances > 0:
    print(theguess)
    if theguess == theanswer:
        theresult = input('Did I guess it? It\s a yes or no question.')
        if theresult.lower() == 'no':
            chances -= 1
            print('Alright, I\'ve got ' + str(chances) + ' more chances then!')
            continue
        else:
            print('Aha! I knew I would get it right!')
            break
    elif theguess < theanswer:
        print('the guess is too low')
        theresult = input('Tell me I got it right! ...yes/no?')
        if theresult.lower() == 'no':
            chances -= 1
            print('Oh cmon! I got ' + str(chances) + ' chances left!')
            theguess = random.randint(theanswer, 100)
            continue
        elif theresult == 'yes':
            print('Ooooo yeaaa!')
            break
    elif theguess > theanswer:
        print('the guess is too high')
        theresult = input('Alright! Did I get it right? yes/no?')
        if theresult.lower() == 'no':
            chances -= 1
            print('Fine! I still have ' + str(chances) + 'tries left.')
            theguess = random.randint(0, theanswer)
            continue
        elif theresult == 'yes' or 'Yes':
                print('Aha! Now that\'s a gotcha!')
                input('Lets go one more round?')
                break
if chances == 0:
    print("Yeah yeah, ham, spam and eggs. Out of chances once again")
