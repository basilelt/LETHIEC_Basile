x = 0
sum = 0
i = 0

while x < 2:
    x = int(input("Entrez un nombre X, entier supérieur à 1 : "))

while sum <= x:
    sum = sum + i
    i = i + 1

n = i - 2

print(f"Le plus grand nombre N tel que (∑i) de 0 à N ≤ X est {n}")
