# Nom : LE THIEC
# Prénom : Basile
# Groupe TP : RT112

def test_int(to_int):
    while True:
        try:
            to_int = int(to_int)
            return to_int
        except ValueError:
            try:
                to_int = float(to_int)
                return to_int
            except ValueError:
                to_int = input("Désolé la valeur saisie n'est pas un nombre entier ni réel, réessayez : ")

# Donner le code des deux fonctions :

def tabl_multi():
    x = test_int(input("Vous cherchez la table de multiplication de quel nombre ? "))
    L = []
    for i in range(1, 11):
        L.append(i * x)

    return L

def affich_table(L):
    x = L[0]
    print(f"Voici la table de multiplication de {x}\n")

    if type(x) == float:
        for i in range(len(L)):
            print(f"{i + 1} * {x} = ","{:.1f}".format(round(L[i], 1)))
    else:
        for i in range(len(L)):
            print(f"{i + 1} * {x} = {L[i]}")

affich_table(tabl_multi())