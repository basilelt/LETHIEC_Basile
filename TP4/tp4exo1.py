x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

mult = [[0 for col in range(2)] for row in range(10)]

for i in range(10):
    mult[i][0] = i
    mult[i][1] = round(x * mult[i][0], 1)

for i in range(10):     ##possible de mettre cette boucle direct dans celle du dessus
    print(f"{x} * {mult[i][0]} = {mult[i][1]}")
