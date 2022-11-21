x = int(input("Entrez x: "))
y = int(input("Entrez y: "))
print(f"Avant permutation:\nx : {x}\ny : {y}")

temp = x
x = y
y = temp
print(f"Après permutation:\nx : {x}\ny : {y}")