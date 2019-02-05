import math

def AlgoDynamique(k,V,s):
    """
        k(int): Le nombre de types de bocaux du systéme de capacité
        V(int[k]): La liste des volumes des bocaux du systéme de capacité
        s(int): La quantité de confiture 
        Implementation de l'algorithme de programmation dynamique.
        Cette fonction prend k, V et s en paramétres, et retourne une solution de la forme (nombre_de_bocaux_utilisés,liste_des_bocaux_utilisés).
    """
    M = init(s+1, k+1)
    for i in range(s+1):
        for j in range(k+1):
            M[i][j] = getMatrix(V, M, i, j)
    return AlgoBackward(k,V,s,M)

def getMatrix(V, M, s, k):
    """
        V(int[k]): La liste des volumes des bocaux du systéme de capacité
        M(int[s+1][k+1]): une liste contenant a chaque case i la liste de bocaux utilisés pour la quantité i de confiture
        s(int): La quantité de confiture 
        k(int): Le nombre de types de bocaux du systéme de capacité
        Crée et retourne une matrice qui dans chaque colonne M[s] le nombre minimum de bocaux nécessaire pour conserver cette quantitée s de confiture  
        
    """
    if s == 0:
        return 0
    elif s < 0:
        return math.inf
    elif k == 0:
        return math.inf
    elif M[s][k] != 0:
        return M[s][k]
    else:
        return min(getMatrix(V,M,s,k-1), getMatrix(V,M,s-V[k-1],k)+1)

def AlgoBackward(k, V, s, M):
    """
        k(int): Le nombre de types de bocaux du systéme de capacité
        V(int[k]): La liste des volumes des bocaux du systéme de capacité
        s(int): La quantité de confiture 
        M(int[k+1][s+1]): une liste contenant a chaque case i la liste de bocaux utilisés pour la quantité i de confiture
        Crée la liste A des bocaux utilisés par la solution et retourne le couple sum(A),A ou sum(A) représente le nombre de bocaux utilisés par la solution
    """
    A = [0]*k
    q = s
    i = k
    while q != 0:
        if (i > 0) and (M[q][i] == M[q][i-1]):
            i = i - 1
        else:
            A[i-1] = A[i-1] + 1
            q = q - V[i-1]
    return sum(A),A
    
def init(r, c):
    """
        r(int): nombre de lignes
        c(int): nombre de colonnes
        Retourne une matrice M[r][c] initialisée à 0
    """
    M = []
    for i in range(r):
        M.append([0]*c)
    return M
