def clean(txt):
    alphachain = ""
    
    for i in txt:
        if i.isalpha():
            alphachain = alphachain + i
    
    alphachain = str.lower(alphachain)
    
    return alphachain
    
def special(specialchain):
    specialchain = specialchain.replace("é", "e")
    specialchain = specialchain.replace("è", "e")
    specialchain = specialchain.replace("ê", "e")
    specialchain = specialchain.replace("ë", "e")

    specialchain = specialchain.replace("à", "a")
    specialchain = specialchain.replace("ä", "a")
    specialchain = specialchain.replace("â", "a")

    specialchain = specialchain.replace("ö", "o")
    specialchain = specialchain.replace("ò", "o")
    specialchain = specialchain.replace("ô", "o")
    
    specialchain = specialchain.replace("ï", "i")
    specialchain = specialchain.replace("î", "i")
    specialchain = specialchain.replace("ì", "i")

    specialchain = specialchain.replace("û", "u")
    specialchain = specialchain.replace("ü", "u")
    specialchain = specialchain.replace("ù", "u")

    specialchain = specialchain.replace("ç", "c")

    specialchain = specialchain.replace("ÿ", "y")

    specialchain = specialchain.replace("ñ", "n")
    
    return specialchain


alpha_chain = clean(input("Entrez une chaine de caractères : "))
print(alpha_chain)

chain = special(alpha_chain)
print(chain)

death = 0
len_chain = len(chain)

for j in range(int(len_chain / 2)):
    if chain[j] != chain[len_chain - 1 - j]:
        print("Ce n'est pas un palindrome !")
        death = 1
        break

if death == 0:
    print("C'est un palindrome !")
