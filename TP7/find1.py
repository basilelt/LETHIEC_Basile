import sys
import os

def aide_arg():
    print("Veuillez donner au moins un argument\n", 'Ex : py find.py "arg1" "arg2" ...')

def aide_exist(repertoire):
    print(f"Le chemin {repertoire} n'existe pas")

def affiche(repertoire):
    list = os.listdir(repertoire)
    for i in list:
        print(i)


print(f"Le chemin actuel est : {os.path.normpath(__file__.replace('find1.py', ''))}\n")

if len(sys.argv) < 2:
    aide_arg()

else:
    for elt in sys.argv:
        if elt != sys.argv[0]:
            path = os.path.normpath(elt)
        
            if os.path.exists(path):
                affiche(path)
            
            else:
                aide_exist(path)
