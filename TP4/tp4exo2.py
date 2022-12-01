# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
sum = 0.0

# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = [0] * nombreEtudiants

for i in range(nombreEtudiants):
    notes[i] = float(input(f"Note étudiant {i} : "))
    sum = sum + notes[i]

mean = sum / nombreEtudiants
print(f"Moyenne de la classe : {mean}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    gap = notes[i] - mean
    print(f"{i} | {notes[i]} | {gap}")
