# Nom : LE THIEC
# Prénom : Basile
# Groupe TP : RT112

# Donner le code de la fonctions produit_scalair()

def produit_scalair():
    chain1 = input("Merci de saisir les composantes du vecteur V1 : ")
    lst1 = chain1.split(",")

    chain2 = input("Merci de saisir les composantes du vecteur V2 : ")
    lst2 = chain2.split(",")

    len1 = len(lst1)
    len2 = len(lst2)

    if len1 == 1 or len2 == 1:
        print("Un des deux vecteurs est composé d'un seul élément ou bien un autre séparateur a été utilisé")
        return -1

    if len1 != len2:
        print("Les deux vecteurs ne sont pas de même taille")
        return -2
    
    scal = 0
    for i in range(len1):
        lst1[i] = int(lst1[i])
        lst2[i] = int(lst2[i])

        scal += lst1[i] * lst2[i]
    
    return scal


pscal = produit_scalair()

while pscal == -1 or pscal == -2:
    pscal = produit_scalair()

print(f"Le produit scalaire de v1 par v2 vaut {pscal}")
