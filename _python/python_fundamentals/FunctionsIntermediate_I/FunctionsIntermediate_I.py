

import random

def randInt(min='', max=''):
    if min != '' and max != '':
        return round((random.random() * (max - min)) + min)
    elif min != '':
        return round((random.random() * (100 - min)) + min)
    elif max != '':
        return round(random.random() * max)
    else:
        return round(random.random() * 100)

#test_cases
print(randInt())
print(randInt(9,10))
print(randInt(min=7))
print(randInt(max=9))
