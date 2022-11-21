import datetime

age = int(input("Donnez votre âge : "))

annee = int(datetime.date.today().year - age)

print(f"Votre année de naissance est  : {annee}")