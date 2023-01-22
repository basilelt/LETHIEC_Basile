# Nom : LE THIEC
# Prénom : Basile
# Groupe TP : RT112

def test_int(to_int):
    while True:
        try:
            to_int = int(to_int)
            return to_int
        except ValueError:
            to_int = input("Désolé la valeur saisie n'est pas un nombre entier, réessayez : ")

n = test_int(input("Merci de préciser le nombre souhaité : "))

for i in range(1, n + 2):
    for j in range(1, i):
        print(j, end = " ")
    print()

print()

for i in range(0, n + 1):
    for j in range(n - i, 0, -1):
        print(j, end = " ")
    print()
    