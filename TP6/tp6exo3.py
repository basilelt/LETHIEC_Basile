def ajouter_elt(lst = [0, 1, 2], elt = 3):
    lst.append(elt)
    return lst

print(f"Le résultat de 'print(ajouter_elt())' serait : [0, 1, 2, 3], nous pouvons le vérifier : {ajouter_elt()},",
    "en effet la fonction se lance avec ses valeurs par défaut n'ayant pas d'autre input\n")

print(f"Si nous rappelons la fonction, nous trouverons le même résultat suivi de 3 à nouveau",
    f"(réutilisation des mêmes valeurs par défaut et même id donc maj de lst) : {ajouter_elt()}\n")


def ajouter_carac(ch = "abc", elt = "d"):
    return ch + elt

print(f"\nLe résultat de 'print(ajouter_carac())' serait : 'abcd', nous pouvons le vérifier : {ajouter_carac()},",
    "en effet la fonction se lance avec ses valeurs par défaut n'ayant pas d'autre input\n")

print(f"Si nous rappelons la fonction, nous trouverons le même résultat",
    f"(réutilisation des mêmes valeurs par défaut, l'id change car il s'agit d'un string (non mutables)) : {ajouter_carac()}")
