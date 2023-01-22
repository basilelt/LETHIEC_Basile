# Nom : LE THIEC
# Prénom : Basile
# Groupe TP : RT112

n = int(input("Merci de préciser le nombre de lignes : "))
star = "* "

for i in range(n):
    print(star)
    star += "* "

print()

star = n * "* "
for i in range(n):
    print(star)
    star = " " + star[0:len(star) - 2]
    