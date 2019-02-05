from Outils import *
from AlgoGlouton import *
from AlgoDynamique import *
from RechExhaustive import *
import random
import sys

"""
Programme de test, prend un nom de fichier en entrée, le lit si il existe ou créer un fichier de façon aléatoire portant le même nom si il n'existe pas, le programme permet de vérifier que les algorithmes glouton et de programmation dynamique retournent bien des solutions valide, et permet de préciser pour le systéme de capacité testé l'algorithme qui fournit une solution optimale.

"""
if __name__=="__main__":
    #vérifie si on a bien passé un fichier en entrée
    try:
        [filename]=sys.argv[1:]
    except:
        print("Erreur format: python exec.py <filename>")
    #vérifie si le fichier existe sinon en crée un de façon aléatoire avec le même nom
    try:
        f = open(filename, 'r')
        f.close()
    except FileNotFoundError:
        print("le fichier "+filename+" n'existe pas!\ncréation d'un nouveau fichier de façon aléatoire portant le même nom\n")
        createRandomFile(filename)
        
    (s,k,V)=readFile(filename)
    print("s = ",s,"\nk = ",k,"\nV = ",V)
    
    (s1,L1)=(AlgoGlouton(k,V,s))
    (s2,L2)=(AlgoDynamique(k,V,s))
    
    print("\nS1: ",s1,L1,"\ntotal = ",total(L1,V,k))
    
    if(total(L1,V,k)==s):
        print("\nLa Solution S1 est valide!")
    else:
        print("\nSolution S1 n'est pas valide!")
        
    print("\nS2: ",s2,L2,"\ntotal = ",total(L2,V,k))
        
    if(total(L2,V,k)==s):
        print("\nLa Solution S2 est valide!")
    else:
        print("\nSolution S2 n'est pas valide!")
        
    if(TestGloutonCompatible(k,V)):
        print("\nLa solution optimale est: S1\n")
    else:
        print("\nLa solution optimale est: S2\n")
