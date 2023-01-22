# Nom : LE THIEC
# Prénom : Basile
# Groupe TP : RT112

import datetime

# Donner le code de la fonctions assurance. À ne pas modifier ni l'ordre ni le nom des arguments de la fonction ! 

def assurance(age, annee, nbr_accident, anciennete):
    annee_courante = datetime.date.today().year
    permis = annee_courante - annee
    annee_dif = annee_courante - anciennete
    
    if nbr_accident < 0 or anciennete < 0 or age < 16 or annee > annee_courante or annee_dif < annee:
        return "Anomalie"

    if age < 25 and permis < 2:
        if nbr_accident == 0:
            if anciennete > 1:
                return "Orange"
            else:
                return "Rouge"
        else:
            return "Refus"
    
    if (age < 25 and permis > 1) or (age > 24 and permis < 2):
        if nbr_accident == 0:
            if anciennete > 1:
                return "Vert"
            else:
                return "Orange"
        elif nbr_accident == 1:
            if anciennete > 1:
                return "Orange"
            else:
                return "Rouge"
        else:
            return "Refus"
    
    if age > 24 and permis > 1:
        if nbr_accident == 0:
            if anciennete > 1:
                return "Bleu"
            else:
                return "Vert"
        elif nbr_accident == 1:
            if anciennete > 1:
                return "Vert"
            else:
                return "Orange"
        elif nbr_accident == 2:
            if anciennete > 1:
                return "Orange"
            else:
                return "Rouge"
        else:
            return "Refus"

    return 


print(assurance(23, 2022, 0, 0))

age = int(input("Entrez votre âge : "))
annee = int(input("Entrez l'année d'obtention de votre permis : "))
nbr_accident = int(input("Combien d'accident avez-vous provoqué : "))
anciennete = int(input("Quelle est votre ancienneté avec cette assurance : "))

print(assurance(age, annee, nbr_accident, anciennete))
