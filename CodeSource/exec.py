from Outils import *
from AnalyseComp import *
from RechExhaustive import *
from AlgoGlouton import *
from AlgoDynamique import *
from UtilisationAlgoGlouton import *
import sys
import ctypes
import os
import time




"""
Ce fichier est un fichier de test, et contient les différents scripts utiliser pour génerer les fichiers de données, et les graphes.
"""

"""
Fonctions:

varSysCapAlgo1(sk,s,k,d,t)
varSysCapAlgo2(sk,s,k,d,it,t)
varSysCapAlgo3(sk,s,k,d,it,t)
tiragesTestGloutonComp(pmax,kmax) pmax: le volume max, kmax, la valeur max de k
genRandomSysCapList(kmax,pmax)
ExpGComp(f,pmax,kmax)
testVal(p,kmax,nbSys,ff)
"""



"""
k=30
s=30
d=2
V=genSysExpo(d,k)
print(s,k,V)
tps0=time.perf_counter()
print(RechercheE(k,V,s))
tps1=time.perf_counter()-tps0
print(tps1)
"""




"""
#code de création des fichiers de données du graphe AD1

nbfiles=5
filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo2(1,1000000,1,2,500,1,i)
calculTpsMoy(filenames,2)


filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo2(1,1000000,1,3,500,1,i)
calculTpsMoy(filenames,3)


filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo2(1,1000000,1,4,500,1,i)
calculTpsMoy(filenames,4)
"""



"""
#Code de création des fichiers de données du graphe AD0

nbfiles=5
filenames=[None]*nbfiles
for i in range (nbfiles):
    filenames[i]="./"+varSysCapAlgo1(0,500,1,2,100,500,i)
calculTpsMoy(filenames,2)

filenames=[None]*nbfiles
for i in range (nbfiles):
    filenames[i]="./"+varSysCapAlgo1(0,500,1,3,100,500,i)
calculTpsMoy(filenames,3)

filenames=[None]*nbfiles
for i in range (nbfiles):
    filenames[i]="./"+varSysCapAlgo1(0,500,1,4,100,500,i)
calculTpsMoy(filenames,4)
"""





"""
#code de création des fichiers de données du graphe AG1
nbfiles=5
filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(1,1000000,1,2,500,1,i)
calculTpsMoy(filenames,2)

filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(1,1000000,1,3,500,1,i)
calculTpsMoy(filenames,3)

filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(1,1000000,1,4,500,1,i)
calculTpsMoy(filenames,4)
"""

"""
#code de création des fichiers de données du graphe AG0
nbfiles=5
filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(0,500,1,2,100,500,i)
calculTpsMoy(filenames,2)


filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(0,500,1,3,100,500,i)
calculTpsMoy(filenames,3)


filenames=[None]*nbfiles
for i in range (len(filenames)):
    filenames[i]="./"+varSysCapAlgo3(0,500,1,4,100,500,i)
calculTpsMoy(filenames,4)
"""



"""
***Instructions gnuplot***
gnuplot

plot "" u 2:4 title "d=" with lines
plot "" u 1:4 title "d=" with lines

replot "" u 2:4 title "d=" with lines
replot "" u 1:4 title "d=" with lines

set title ""
set xlabel ""
set ylabel ""
set key left top

q
"""



                    
