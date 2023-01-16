import sys
import os

def aide_arg():
    print("Veuillez donner au moins deux arguments\n", 'Ex : py find.py "arg1" "arg2" ...')

def aide_exist(repertoire):
    print(f"Le chemin {repertoire} n'existe pas")

def recherche(repertoire, fichier):
    list = os.listdir(repertoire)
    
    for i in list:
        chemin = os.path.join(repertoire, i)
        
        if os.path.isfile(chemin) & (i == fichier):
            listeFichiers.append(chemin)
        
        elif os.path.isdir(chemin):
            listeRepertoires.append(chemin)    

listeFichiers = []
listeRepertoires = []

print(f"Le chemin actuel est : {os.path.normpath(__file__.replace('find.py', ''))}\n")

if len(sys.argv) < 3:
    aide_arg()

else:
    path = os.path.normpath(sys.argv[1])
        
    if os.path.exists(path):
        recherche(path, sys.argv[2])
                
        if __name__ == '__main__':
            for l in listeRepertoires:
                recherche(l, sys.argv[2])
                
        print("Les fichiers sont :")
        for j in listeFichiers:
            print(j)

    else:
        aide_exist(path)
