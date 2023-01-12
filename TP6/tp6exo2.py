def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

## a
lst1 =  [0, 1, 2]

## b
lst2 = ajouter_elt(lst1, len(lst1))

##c
print(f"La liste 1 : {lst1} a pour id {id(lst1)} et comme type {type(lst1)}")
print(f"La liste 2 : {lst2} a pour id {id(lst2)} et comme type {type(lst2)}\n")

print("Nous remarquons que lst1 est devenu égale à lst2 qui s'est vu rajouté la longueur de lst1 à lst1\n",
    "Nous pouvons en conclure que des listes ayant les même valeur pointent vers la même mémoire (id)",
    "et si on modifie une valeur d'une de ces listes, cette valeur sera modifiée pour toutes ces listes")
