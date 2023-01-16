import sys

arg = sys.argv
nb_arg = len(arg)
    
print(f"Le nombre d'argument est : {nb_arg}")

if nb_arg == 1:
    print(f"Pas assez d'arguments pour le script {arg[0]}")

elif (__name__ == '__main__') & (nb_arg > 1):
    for i in range(nb_arg):
        print(arg[i])
        
    for elt in arg:
        print(elt)