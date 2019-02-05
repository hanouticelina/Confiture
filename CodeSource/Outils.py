import random
from AlgoGlouton import *

def genSysExpo(d,k):
    """
        d(int): d du systéme de capacité Expo
        k(int): longeur du systéme de capacité Expo
        Retourne la liste de bocaux du systéme de capacité Expo
    """
    L=[1]*k
    for i in range (1,k):
        L[i]=L[i-1]*d
    return L
    
def TestGloutonCompatible(k,V):
    """
        k(int): longeur du systéme de capacité Expo
        V(int[]): liste des volumes des bocaux du systéme de capacité
        Retourne Vrai si le systéme de capacité est glouton compatible, et retourne faux sinon
    """
    S=0
    j=0
    if(k>=3):
        for S in range (V[2]+2,V[k-2]+V[k-1]-1):
            for j in range(0,k):
                if(V[j]<S)and(AlgoGlouton(k,V,S)[0]>1+AlgoGlouton(k,V,S-V[j])[0]):
                    return False
    return True

def total(L,V,k):
    """
        L(int[]): liste de bocaux utilisés par une solution
        V(int[]): liste des volumes des bocaux du systéme de capacité 
        k(int): longeur du systéme de capacité
        Retourne le total des volumes des bocaux utilisés par la solution, permet de vérifier que la solution est bien valide
    """
    som=0
    for i in range(0,k):
        som+=L[i]*V[i]
    return som

def testFiles(s,k):
    """
        s(int): la quantitée de la confiture
        k(int): la longeur du systéme de capacité
        Cette fonction crée trois fichiers de données qu'on peut lire avec la fonction readFile, les fichiers contiennet le volume s, la longeur k du systéme de capacité, et la liste des volumes des bocaux du systéme de capacité Expo, les trois fichiers s'appellent "data1", "data2" et "data3", contenant dans cette ordre le systéme de capacité Expo avec d=2, d=3 puis d=4
    """
    createFileExpo(s,k,2,'data1')
    createFileExpo(s,k,3,'data2')
    createFileExpo(s,k,4,'data3')
    
def createRandomFile(filename):
    """
        filename(string): le nom du fichier a créer
        créer un fichier de données qu'on peut lire avec la fonction readFile, le fichier s'appelle filename, et continuer un systéme de capacité crée aléatoirement, de longeur k aléatoire en 1 et 50, et de quantitée s de confiture choisie aléatoirement entre 1 et 10000, et les bocaux sont de V[i], le volume V[i] choisie entre 10 et 1000.
    """
    f=open(filename,'w')
    s=random.randint(1,10001)
    k=random.randint(1,51)
    f.write(str(s)+"\n")
    f.write(str(k)+"\n")
    V=[0]*k
    V[0]=1
    for i in range(1,k):
        V[i]=i*random.randint(10,1001)
    V=sorted(V)
    for i in range(0,k):
        f.write(str(V[i])+"\n")
    f.close()
    return filename
        
def createFileExpo(s,k,d,filename):
    """int: s, int: k, int: d, filename: string
    Cree un fichier de donnees, contenant a la premiere ligne le volume de confiture s, a la deuxieme ligne la taille k du systeme de capacite, et le reste des lignes representes les valeurs des volumes des bocaux du systeme de capacite en ordre croissant
    """
    f=open(filename,'w')
    f.write(str(s)+"\n")
    f.write(str(k)+"\n")
    val=1
    for i in range(0,k):
        f.write(str(val)+"\n")
        val*=d
    f.close()

def readFile(filename):
    """filename: string
    lit un fichier de donnees, et retourne le nuplet s,k,V, avec s le volume de confiture, k le nombre de bocaux du systeme de capacite et V la liste des volumes des bocaux du systeme de capacite
    """
    f=open(filename,'r')
    s=int(f.readline())
    k=int(f.readline())
    V=[0]*k
    for i in range(0,k):
        V[i]=int(f.readline())
    f.close()
    return s,k,V
    
