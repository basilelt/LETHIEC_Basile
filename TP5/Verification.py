import os
import datetime

path1 = input("Entrer le nom du 1er fichier : ")
path2 = input("Entrer le nom du 2eme fichier : ")

path = os.path.join(__file__.replace("Verification.py", ""), "tp5exo7")
print(path)

full1 = os.path.join(path, path1)
full2 = os.path.join(path, path2)

test1 = os.path.isfile(full1)

if test1:
    print(f"Le fichier {path1} existe, sa taille est de {os.path.getsize(full1)}")
    time1 = os.path.getmtime(full1)

if os.path.isfile(full2):
    print(f"Le fichier {path2} existe, sa taille est de {os.path.getsize(full2)}")
    time2 = os.path.getmtime(full2)

    if test1:
        if time1 > time2:
            time1 = datetime.datetime.fromtimestamp(time1)
            print(f"\nLe fichier le plus récent est {path1}, sa date de modification est le {time1}")
        
        else:
            time2 = datetime.datetime.fromtimestamp(time2)
            print(f"\nLe fichier le plus récent est {path2}, sa date de modification est le {time2}")

