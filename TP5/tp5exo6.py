import numpy
import string

vowels = ["a", "e", "i", "o", "u", "y"]
t = []
txt = ""

test = bool(int(input("Voulez-vous rentrer vous même une chaine de caractères ? (0 : non, 1 : oui) : ")))
if test:
    txt = input("Entrez votre chaine de caractères : ")
    for j in txt:
        t.append(j)

else:
    alphabet = list(string.ascii_lowercase)
    rng = numpy.random.default_rng()
    t = rng.choice(alphabet, size = numpy.random.randint(100), replace = True).tolist()

    for o in t:
        txt += o

    print(f"La liste générée aléatoirement est : {txt}, elle contient {len(t)} caractères\n")

t.append(None)

v = 0
occurence = False
k = 0
m = 0

i = 0
l = t[i]

while l != None:

    if l in vowels:
        v += 1
    
    if l == "w":
        if t[i + 1] == "a":
            if t[i + 2] == "g":
                if t[i + 3] == "o":
                    if t[i + 4] == "n":
                        if occurence == False:
                            k = i + 1
                        occurence = True
                        m += 1

    i += 1
    l = t[i]

print("\nA l'aide de notre algorithme, nous trouvons :\n",
    f"Taille de la chaine de caractères : {i}\n",
    f"Pourcentage de voyelles : {v / i}\n")

if k != 0:
    print(f"La chaine 'wagon' existe dans notre chaine de caractères, celle-ci commence au caractère n°{k}\n",
        f"Le nombre d'occurence de la chaine 'wagon' dans notre chaine de caractères est de {m}")
        