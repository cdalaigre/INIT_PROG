""" Fonctions utilitaires pour manipuler les matrices """

import API_matrice1 as matrice_util

def get_ligne(matrice, num_ligne):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    ligne=[]

    if num_ligne < nbl:
        for position in range (num_ligne*nbc, num_ligne*nbc+nbc):
            coef = lst_val[position]
            ligne.append(coef)
        return ligne
    
    else: return None

def get_colonne(matrice, num_colonne):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    colonne=[]

    if num_colonne < nbc:
        for ligne in range (nbl):
            coef = lst_val[ligne*nbc+num_colonne]
            colonne.append(coef)
        return colonne
    
    else: return None

def get_diagonale_principale(matrice):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    main_diag=[]

    for ligne in range (nbl):
        coef = lst_val[ligne*nbc+ligne]
        main_diag.append(coef)
    return main_diag

def get_diagonale_secondaire(matrice):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    second_diag=[]

    for ligne in range (nbl):
        coef = lst_val[(2-ligne)*nbc+ligne]
        second_diag.append(coef)
    return second_diag

def transpose (matrice):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    matrix=[[0 for _ in range(nbc)] for _ in range(nbl)]    
    trans=[[0 for _ in range(nbl)] for _ in range(nbc)]
    transpose_val = []

    # récupération des valeurs de la liste dans un tableau à 2 dimensions
    for i in range(nbl):
        for j in range(nbc):
            matrix[i][j]=lst_val[i*nbc+j]
    
    # transposition
    for i in range(nbl):
        for j in range(nbc):
            trans[j][i]=matrix[i][j]
    
    # coenstruction de la nouvelle liste de valeur
    for ligne in trans:
        for elem in ligne:
            transpose_val.append(elem)
        
    return (nbc, nbl, transpose_val)

def is_trinagulaire_inf(matrice):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    matrix=[[0 for _ in range(nbc)] for _ in range(nbl)]  

    if nbl != nbc: return False

    # récupération des valeurs de la liste dans un tableau à 2 dimensions
    for i in range(nbl):
        for j in range(nbc):
            matrix[i][j]=lst_val[i*nbc+j]

    #vérification si les valeurs au dela de la diagonale sont nulles
    for i in range(nbl):
        for j in range(i+1,nbc):
            if matrix[i][j]!=0:
                return False
    
    return True

