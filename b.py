import random


theanswer = input('Okay, okay. This time you pick a number\n and I\'ll guess it! Of course I get ten chances too!\n It\'s got to be between 0 and 100, so no messin\' around!')
theanswer = int(theanswer)
theguess = random.randint(0, 100)
chances = 10

while chances > 0:
    if theguess == theanswer:
        theresult = input('Did I guess it? It\s a yes or no question.')
        if theresult == 'no' or 'No':
