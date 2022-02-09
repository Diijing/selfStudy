import random
def getRanNum():
    while True:
        ranNum = random.randint(1,100)
        if ranNum % 2 != 0:
            break
    return ranNum
print(getRanNum())