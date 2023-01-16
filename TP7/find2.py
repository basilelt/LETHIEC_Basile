import sys
import os

def aide_arg():
    print("Veuillez donner au moins un argument\n", 'Ex : py find.py "arg1" "arg2" ...')

def aide_exist(repertoire):
    print(f"Le chemin {repertoire} n'existe pas")

def recherche(repertoire, x = ""):
    repertoire = os.path.join(repertoire, x)
    list = os.listdir(repertoire)
    
    for i in list:
        chemin = os.path.join(repertoire, i)
        
        if os.path.isfile(chemin):
            listeFichiers.append(os.path.join(x, i))
        
        elif os.path.isdir(chemin):
            listeRepertoires.append(os.path.join(x, i))      

listeFichiers = []
listeRepertoires = []

print(f"Le chemin actuel est : {os.path.normpath(__file__.replace('find2.py', ''))}\n")

if len(sys.argv) < 2:
    aide_arg()

else:
    for elt in sys.argv:
        if elt != sys.argv[0]:
            path = os.path.normpath(elt)
        
            if os.path.exists(path):
                recherche(path)
                
                if __name__ == '__main__':
                    for l in listeRepertoires:
                        recherche(path, l)
                
                print("Les fichiers sont :")
                for j in listeFichiers:
                    print(j)

                print("\nLes dossiers sont :")
                for k in listeRepertoires:
                    print(k)

            else:
                aide_exist(path)
