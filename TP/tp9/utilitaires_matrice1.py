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
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    transpose_val = []

    for colonne in range(nbc):
        ma_colonne=get_colonne(matrice,colonne)
        for coef in ma_colonne:
            transpose_val.append(coef)

    return(nbc,nbl,transpose_val)

def is_triangulaire_inf(matrice):
    lst_val=matrice[2]
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)

    if nbl != nbc: return False

    #vérification si les valeurs au dela de la diagonale sont nulles
    for ligne in range(nbl):
        for colonne in range(ligne+1,nbc):
            if matrice_util.get_val(matrice,ligne,colonne) != 0:
                return False
    
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    nbl = matrice_util.get_nb_lignes(matrice)
    nbc = matrice_util.get_nb_colonnes(matrice)
    lst_bloc=[]

    if ligne>nbl or colonne>nbc or (ligne+hauteur)>nbl or (colonne+largeur)>nbc:
        return None
       
    #extractiob du bloc
    for i in range(ligne, ligne+hauteur):
        for j in range(colonne, colonne+largeur):
             lst_bloc.append(matrice_util.get_val(matrice,i,j))
    
    return (hauteur,largeur,lst_bloc)