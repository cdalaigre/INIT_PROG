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
