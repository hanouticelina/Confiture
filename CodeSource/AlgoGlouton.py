def AlgoGlouton(k,V,s):
    """ 
        s(int): valeur initiale de s (le premier volume de confiture) 
        k(int): valeur initiale de k (la taille du permier systéme de capacité utilisé)
        V(int[k]): La liste des volumes des bocaux du systéme de capacité
    Implementation de l'algorithme Glouton. 
    Retourne un couple (cpt,L) avec cpt le nombre total de bocaux utilises et L la liste des bocaux utilises
    """
    L=[0]*k
    st=s
    while(st>0):
        i=0
        imax=0
        while((i<k)and(V[i]<=st)):
            if(V[i]>V[imax]):
                imax=i
            i+=1
        st-=V[imax]
        L[imax]+=1
    return sum(L),L
