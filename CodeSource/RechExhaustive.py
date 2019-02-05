import math

def RechercheE(k,V,s):
    """
        k(int): longeur du systéme de capacité
        V(int[]): liste des volumes des bocaux du systéme de capacité
        s(int): la quantitée de la confiture
        Implémentation de l'algorithme de recherche exhaustive.
        Retourne le nombre minimum de bocaux nécessaire pour conserver la quantitée s de confiture
    """
    if s<0:
        return math.inf
    else:
        if s==0:
            return 0
        else:
            NbCont=s
            for i in range(0,k):
                x=RechercheE(k,V,s-V[i])
                if x+1<NbCont:
                    NbCont=x+1
            return NbCont
