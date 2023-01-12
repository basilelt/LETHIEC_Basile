def clean(txt):
    str.lower(txt)
    alphachain = ""
    
    for i in txt:
        if i.isalpha() == True:
            alphachain = alphachain + i
    
    
    alphachain.replace("é", "e")
    alphachain.replace("è", "e")
    alphachain.replace("ê", "e")
    alphachain.replace("ë", "e")

    alphachain.replace("à", "a")
    alphachain.replace("ä", "a")
    
    éèêë 
    return alphachain

chain = clean(input("Entrez une chaine de caractères : "))



