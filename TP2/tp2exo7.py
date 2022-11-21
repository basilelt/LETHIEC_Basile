import random

rand = random.randrange(0, 100, 1)
# 0-49 = 50 ; 50-99 = 50

if rand < (200/3):
    print("Pile !")
else:
    print("Face !")