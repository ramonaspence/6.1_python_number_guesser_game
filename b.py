import random


theanswer = input('Okay, okay. This time you pick a number\n and I\'ll guess it! Of course I get ten chances too!\n It\'s got to be between 0 and 100, so no messin\' around!')
theanswer = int(theanswer)

chances = 10

while chances > 0:
    theguess = random.randint(0, 100)
    print(theguess)
    if theguess == theanswer:
        theresult = input('Did I guess it? It\s a yes or no question.')
        if theresult == 'no' or 'No':
            chances -= 1
            chances = str(chances)
            print('Alright, I\'ve got ' + chances + ' more chances then!')
            chances = int(chances)
            continue
        elif theresult == 'yes' or 'Yes':
            print('Aha! I knew I would get it right!')
            break
    elif theguess <= theanswer:
        theresult = input('Tell me I got it right! ...yes/no?')
        if input == 'no' or 'No':
            chances -= 1
            chances = str(chances)
            print('Oh cmon! I got ' + chances + ' chances left!')
            chances = int(chances)
            continue
        elif input == 'yes' or 'Yes':
            print('Ooooo yeaaa!')
            input('next level?')
    elif theguess >= theanswer:
        theresult = input('Alright! Did I get it right? yes/no?')
        if input == 'no' or 'No':
            chances -= 1
            chances = str(chances)
            print('Fine! I still have ' + chances + 'tries left.')
            chances = int(chances)
            continue
        elif input == 'yes' or 'Yes':
                print('Aha! Now that\'s a gotcha!')
                input('Lets go one more round?')

if chances == 0:
    print("Yeah yeah, ham, spam and eggs. Out of chances once again")
