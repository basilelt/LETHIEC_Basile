nom = []
prenom = []
i = 1

while True:
    nom.append(str.lower((input(f"Entrez le {i}è nom  (0 pour sortir) : "))))
    if nom[i - 1] == "0":
        break
    prenom.append(str.lower(input(f"Entrez le {i}è prénom : ")))
    i = i + 1

for k in range(len(prenom) - 1):
    for l in range(k + 1 , len(prenom)):
        if nom[l] == nom[k]:
            if prenom[l] < prenom[k]:
                prenom[k], prenom[l] = prenom[l], prenom[k]
                nom[k], nom[l] = nom[l], nom[k]
        elif nom[l] < nom[k]:
            prenom[k], prenom[l] = prenom[l], prenom[k]
            nom[k], nom[l] = nom[l], nom[k]

for j in range(len(prenom)):
    print(f"{str.capitalize(prenom[j])} {str.upper(nom[j])}")