## a
L1 = [0] * 3

print(f"La liste {L1} a pour id {id(L1)} et comme type {type(L1)}\n")

## b
for i in range(len(L1)):
    print(f"L'élément {i + 1} a comme type {type(L1[i])} et comme id {id(L1[i])}")

print("\nOn remarque que les ids sont identiques si les variables sont égales (type et valeur)\n")

##c
L1[1] += 1

print(f"La liste {L1} a pour id {id(L1)} et comme type {type(L1)}")

print("On remarque que ni le type ni l'id de la list n'a changé\n")

##d
for i in range(len(L1)):
    print(f"L'élément {i + 1} a comme type {type(L1[i])} et comme id {id(L1[i])}")

print("\nOn remarque que l'id du 2ème élément de la liste a changé\n",
    "Nous pouvons en conclure qu'il s'agit d'un nouvel élément,",
    "on peut donc en conclure que les éléments de cette liste sont non mutables")