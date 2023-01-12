h = float(input("Combien d'heures avez-vous travaillées ? : "))
s = float(input("Quel est votre salaire horaire ? : "))

if h > 200:
    money = 160 * s + 40 * s * 1.25 + (h - 200) * s * 1.5

elif h > 160:
    money = 160 * s + (h - 160) * s * 1.25

else:
    money = h * s

print(f"\nVotre salaire est de {money}eur")