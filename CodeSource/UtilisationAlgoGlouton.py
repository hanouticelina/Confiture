from Outils import *
from AlgoGlouton import *
from AlgoDynamique import *
from RechExhaustive import *
import random
import sys


def testVal(p,kmax,nbSys,ff):
    """
        p(int): volume maximale d'un bocal des systémes de capacité
        kmax(int): longeur maximale des systémes de capacité
        nbSys(int): nombre de systémes de capacité a créer
        ff(int): f le quotient qui permet de donner l'intervalle des valeurs de s sur lesquelles les tests seront fait
        Cette fonction crée nbSys de systémes de capacités de longeur variante entre 3 et kmax de façon aléatoire, et ayant des bocaux de volumes variant entre 2 et p de façon aléatoire également, si le systéme de capacités créé est glouton compatible, la fonction écrit cela dans un fichier nommé "GloutonCompatible_p_nbSys_ff.txt", sinon execute l'algorithme glouton et l'algorithme dynamique sur ce systéme de capacité avec un volume s qui va de p à p*ff puis écrit l'écart moyen et l'écart maximum entre les deux solutions danc le même fichier
        
    """
    f=open('GloutonCompatible'+'_'+str(p)+'_'+str(nbSys)+'_'+str(ff)+'.txt','w')
    f.write("GC"+"\t\t"+"EMAX"+"\t\t"+"EMOY"+"\t\t"+"SC"+"\n")
    compatible=0
    noncompatible=0
    for nb in range(nbSys):
        k=random.randint(3,kmax+1)
        V=[0]*k
        V[0]=1
        for i in range(1,k):
            b=True
            while(b):
                V[i]=random.randint(2,p+1)
                b=False
                for j in range (1,i): 
                    if V[i]==V[j]:
                        b=True
        V=sorted(V)
        if(TestGloutonCompatible(k,V)):
            f.write("oui"+"\t\t\t\t\t\t\t")
            compatible+=1
        else:
            noncompatible+=1
            f.write("non"+"\t\t")
            maxi=0
            sumi=0
            for s in range(p,p*ff):
                 (s1,L1)=(AlgoGlouton(k,V,s))
                 (s2,L2)=(AlgoDynamique(k,V,s))
                 print(s1,L1)
                 print(s2,L2)
                 ecart=s1-s2
                 sumi+=ecart
                 if(ecart>maxi):
                     maxi=ecart
            moy=round(sumi/((p*ff-p)+1),3)
            f.write(str(maxi)+"\t\t")
            f.write(str(moy)+"\t\t")
        f.write("[")
        for i in range(0,k):
            f.write(str(V[i])+" ")
        f.write("]")
        f.write("\n")
    f.write("Proportion des systeme Glouton Compatible "+str(compatible)+"/"+str(nbSys)+"\n")
    f.write("Proportion des systeme Glouton Non Compatible "+str(noncompatible)+"/"+str(nbSys)+"\n")
    f.close()
    
