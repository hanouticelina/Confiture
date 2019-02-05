from Outils import *
from AlgoGlouton import *
from AlgoDynamique import *
from RechExhaustive import *
import time
import sys
import os

def varSysCapAlgo1(sk,s,k,d,t,sym=""):
    """
        sk(int): si sk==0 la fonction fait varier s 
                 si sk==1 la fonction fait varier k
        s(int): valeur initiale de s (le premier volume de confiture) 
        k(int): valeur initiale de k (la taille du permier systéme de capacité utilisé)
        d(int): valeur de d, vaut 2,3 ou 4, permet de créer le systéme de capacité Expo
        t(int): taux d'augmentation de s ou de k (en fonction de sk) à chaque itération
        sym(string): un ou plusieurs charcatéres permettent de différencier les fichier de données qui seront créer pour les mêmes valeurs des autres paramétres
        fait varier s ou k (en fonction de sk) de t jusqu'a ce que le temps d'éxectution dépasse une minute, et écris à chaque tour de boucle le temps d'éxecution de l'agorithme de Recherche éxhaustive dans un fichier nommé "RE_sk_s_k_d_t.txt"
    """  
    os.makedirs("RE"+str(sk), exist_ok=True)
    filename="RE"+str(sk)+"/RE"+str(sym)+"_"+str(sk)+"_"+str(s)+"_"+str(k)+"_"+str(d)+"_"+str(t)+".txt"
    f=open(filename,'w')   
    tps1=0
    sys.setrecursionlimit(50000)
    if(sk==0):
        strk=str(k)+(20-len(str(k)))*" "
        strd=str(d)+(20-len(str(d)))*" "
        while(tps1<=60):
            V=genSysExpo(d,k)        
            tps0=time.perf_counter()
            RechercheE(k,V,s)
            tps1=time.perf_counter()-tps0   
            print(tps1)
            if(tps1>=30):
                t=1
            strS=str(s)+(20-len(str(s)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            s+=t
    if(sk==1):
        strS=str(s)+(20-len(str(s)))*" "
        strd=str(d)+(20-len(str(d)))*" "    
        while(tps1<=60):
            V=genSysExpo(d,k)
            tps0=time.perf_counter()
            RechercheE(k,V,s)
            tps1=time.perf_counter()-tps0
            print(tps1) 
            if(tps1>=30):
                t=1
            strk=str(k)+(20-len(str(k)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            k+=t
    f.close()
    return filename

def varSysCapAlgo2(sk,s,k,d,it,t,sym=""):
    """
        sk(int): si sk==0 la fonction fait varier s 
                 si sk==1 la fonction fait varier k
        s(int): valeur initiale de s (le premier volume de confiture) 
        k(int): valeur initiale de k (la taille du permier systéme de capacité utilisé)
        d(int): valeur de d, vaut 2,3 ou 4, permet de créer le systéme de capacité Expo
        it(int): nombre d'itérations
        t(int): taux d'augmentation de s ou de k (en fonction de sk) à chaque itération
        sym(string): un ou plusieurs charcatéres permettent de différencier les fichier de données qui seront créer pour les mêmes valeurs des autres paramétres
        fait varier s ou k (en fonction de sk) de t pour it fois et écris le temps d'éxecution de l'agorithme Dynamique dans un fichier nommé "AD_sk_s_k_d_it_t.txt"
    """  
    os.makedirs("AD"+str(sk), exist_ok=True) 
    filename="AD"+str(sk)+"/AD"+str(sym)+"_"+str(sk)+"_"+str(s)+"_"+str(k)+"_"+str(d)+"_"+str(it)+"_"+str(t)+".txt"
    f=open(filename,'w')   
    
    if(sk==0):
        strk=str(k)+(20-len(str(k)))*" "
        strd=str(d)+(20-len(str(k)))*" "
        
        for i in range(0,it):
            V=genSysExpo(d,k)
            tps0=time.perf_counter()
            AlgoDynamique(k,V,s)
            tps1=time.perf_counter()-tps0
            print(tps1) 
            strS=str(s)+(20-len(str(s)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            s+=t
    if(sk==1):
        strS=str(s)+(20-len(str(s)))*" "
        strd=str(d)+(20-len(str(d)))*" "     
        for i in range(0,it):
            V=genSysExpo(d,k)
            tps0=time.perf_counter()
            AlgoDynamique(k,V,s)
            tps1=time.perf_counter()-tps0
            print(tps1)
            strk=str(k)+(20-len(str(k)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            k+=t
    f.close()
    return filename

def varSysCapAlgo3(sk,s,k,d,it,t,sym=""):
    """varSysCapAlgo2(int: sk,int: s,int: k,int: d,int: it,int: t)
        sk(int): si sk==0 la fonction fait varier s 
                 si sk==1 la fonction fait varier k
        s(int): valeur initiale de s (le premier volume de confiture) 
        k(int): valeur initiale de k (la taille du permier systéme de capacité utilisé)
        d(int): valeur de d, vaut 2,3 ou 4, permet de créer le systéme de capacité Expo
        it(int): nombre d'itérations
        t(int): taux d'augmentation de s ou de k (en fonction de sk) à chaque itération
        sym(string): un ou plusieurs charcatéres permettent de différencier les fichier de données qui seront créer pour les mêmes valeurs des autres paramétres
        fait varier s ou k (en fonction de sk) de t pour it fois et écris le temps d'éxecution de l'agorithme Glouton dans un fichier nommé "AG_sk_s_k_d_it_t.txt"
    """  
    os.makedirs("AG"+str(sk), exist_ok=True)
    filename="AG"+str(sk)+"/AG"+str(sym)+"_"+str(sk)+"_"+str(s)+"_"+str(k)+"_"+str(d)+"_"+str(it)+"_"+str(t)+".txt"
    f=open(filename,'w') 
      
    if(sk==0):
        strk=str(k)+(20-len(str(k)))*" "
        strd=str(d)+(20-len(str(d)))*" "     
        for i in range(0,it):
            V=genSysExpo(d,k)
            tps0=time.perf_counter()
            AlgoGlouton(k,V,s)
            tps1=time.perf_counter()-tps0
            print(tps1) 
            strS=str(s)+(20-len(str(s)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            s+=t
    if(sk==1):
        strS=str(s)+(20-len(str(s)))*" "
        strd=str(d)+(20-len(str(d)))*" "     
        for i in range(0,it):
            V=genSysExpo(d,k)
            tps0=time.perf_counter()
            AlgoGlouton(k,V,s)
            tps1=time.perf_counter()-tps0
            print(tps1) 
            strk=str(k)+(20-len(str(k)))*" "
            strtps=str(tps1)+(20-len(str(tps1)))*" "
            f.write(strS+strk+strd+strtps+"\n")
            k+=t
    f.close()
    return filename

def calculTpsMoy(filenames,d):
    """
        filenames(string[]): liste des noms de fichiers a lire, ils doivent etre du meme format, de la meme tailles, 
        et etre fait pour les memes valeurs de s,k et d
        d(int):la valeur de d afin de différencier les fichiers de données
        cette fonction prend une liste de fichiers en paramétres, les fichiers sont de même format et de même taille et elle les lits et calcul la moyenne des temps d'executions marqués sur le fichier pour chaque valeur de k,d et s, puis les réecris sur un fichier nommé "resTpsMoy(d).txt"
    """
    nbfiles=len(filenames)
    f=[None]*nbfiles
    fout=open("resTpsMoy"+str(d)+".txt",'w')
    for i in range (nbfiles):
        f[i]=open(filenames[i],'r')
    nblines = sum(1 for line in f[0]) 
    f[0]=open(filenames[0],'r')
    moy=0.0
    for i in range (nblines):
        for j in range (nbfiles):
            (s,k,d,t)=f[j].readline().split()
            moy=float(moy)+float(t)
        moy=moy/nbfiles
        s=s+(20-len(s))*" "
        k=k+(20-len(k))*" "
        d=d+(20-len(d))*" "
        moy=str(moy)+(20-len(str(moy)))*" "
        fout.write(s+k+d+moy+"\n")
    for i in range (nbfiles):
        f[i].close()
    fout.close()
   
        
    
        
    

