import random
def randInt(min=0, max=100):
# def randInt(min=0, max=None):
    # if max == None:
    #     num = random.random() * (100-min) + min
    # else:
    num = random.random() * (max-min) + min
    return int(num)
x = randInt(min=50, max=100)
print(x)
#print(randInt()) 