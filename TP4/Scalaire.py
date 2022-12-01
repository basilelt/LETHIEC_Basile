nMax = 10
scalar = 0.0

while True:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
    if 1 <= n <= nMax:
        break

v1 = [0] * n
v2 = [0] * n

print("Saisie du premier vecteur :")
for i in range(n):
    v1[i] = float(input(f"v1[{i}] = "))

print("Saisie du second vecteur :")
for i in range(n):
    v2[i] = float(input(f"v2[{i}] = "))

for i in range(n):
    scalar = scalar + v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {scalar}")