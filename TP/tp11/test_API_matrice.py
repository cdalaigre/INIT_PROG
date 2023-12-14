""" tests pour les API matrices
    Remarques : tous les tests de ce fichier doivent passer
    quelle que soit l'API utilisée
"""
# import API_matrice1 as API
# import utilitaires_matrice1 as utils

import API_matrice1 as API


def matrice1():
    """ définition d'une matrice pour les tests """
    mat1 = API.matrice(3, 4, None)
    API.set_val(mat1, 0, 0, 10)
    API.set_val(mat1, 0, 1, 11)
    API.set_val(mat1, 0, 2, 12)
    API.set_val(mat1, 0, 3, 13)
    API.set_val(mat1, 1, 0, 14)
    API.set_val(mat1, 1, 1, 15)
    API.set_val(mat1, 1, 2, 16)
    API.set_val(mat1, 1, 3, 17)
    API.set_val(mat1, 2, 0, 18)
    API.set_val(mat1, 2, 1, 19)
    API.set_val(mat1, 2, 2, 20)
    API.set_val(mat1, 2, 3, 21)
    return mat1

def matrice2():
    """ définition d'une matrice pour les tests """
    mat2 = API.matrice(2, 3, None)
    API.set_val(mat2, 0, 0, 'A')
    API.set_val(mat2, 0, 1, 'B')
    API.set_val(mat2, 0, 2, 'C')
    API.set_val(mat2, 1, 0, 'D')
    API.set_val(mat2, 1, 1, 'E')
    API.set_val(mat2, 1, 2, 'F')
    return mat2

def matrice3():
    """ définition d'une matrice pour les tests """
    mat3 = API.matrice(3, 3, None)
    API.set_val(mat3, 0, 0, 2)
    API.set_val(mat3, 0, 1, 7)
    API.set_val(mat3, 0, 2, 6)
    API.set_val(mat3, 1, 0, 9)
    API.set_val(mat3, 1, 1, 5)
    API.set_val(mat3, 1, 2, 1)
    API.set_val(mat3, 2, 0, 4)
    API.set_val(mat3, 2, 1, 3)
    API.set_val(mat3, 2, 2, 8)
    return mat3

def matrice4():
    """ définition d'une matrice pour les tests """
    mat4 = API.matrice(3, 3, None)
    API.set_val(mat4, 0, 0, 2)
    API.set_val(mat4, 0, 1, 0)
    API.set_val(mat4, 0, 2, 0)
    API.set_val(mat4, 1, 0, 9)
    API.set_val(mat4, 1, 1, 5)
    API.set_val(mat4, 1, 2, 0)
    API.set_val(mat4, 2, 0, 4)
    API.set_val(mat4, 2, 1, 3)
    API.set_val(mat4, 2, 2, 8)
    return mat4

def test_get_nb_lignes():
    """ tests get_nb_lignes """
    matrice_1 = matrice1()
    matrice_2 = matrice2()
    matrice_3 = matrice3()
    assert API.get_nb_lignes(matrice_1) == 3
    assert API.get_nb_lignes(matrice_2) == 2
    assert API.get_nb_lignes(matrice_3) == 3

def test_get_nb_colonnes():
    """ tests pour get_nb_colonnes """
    mat_1 = matrice1()
    mat_2 = matrice2()
    mat_3 = matrice3()
    assert API.get_nb_colonnes(mat_1) == 4
    assert API.get_nb_colonnes(mat_2) == 3
    assert API.get_nb_colonnes(mat_3) == 3

def test_get_val():
    """ tests pour get_val """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert API.get_val(matr1, 0, 1) == 11
    assert API.get_val(matr1, 2, 1) == 19
    assert API.get_val(matr2, 1, 1) == 'E'
    assert API.get_val(matr2, 0, 2) == 'C'
    assert API.get_val(matr3, 2, 0) == 4
    assert API.get_val(matr3, 1, 0) == 9

def test_sauve_charge_matrice():
    """tests pour sauvegarde et restauration"""
    la_matrice = matrice2()
    API.sauve_matrice(la_matrice, "matrice.csv")
    matrice_bis = API.charge_matrice_str("matrice.csv")
    assert la_matrice == matrice_bis


def test_get_ligne():
    """ tests pour get_ligne """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert API.get_ligne(matr1,0)==[10,11,12,13]
    assert API.get_ligne(matr2,1)==['D','E','F']
    assert API.get_ligne(matr3,2)==[4,3,8]
    assert API.get_ligne(matr1,3)==None

def test_get_colonne():
    """ tests pour get_colonne """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert API.get_colonne(matr1,0)==[10,14,18]
    assert API.get_colonne(matr2,1)==['B','E']
    assert API.get_colonne(matr3,2)==[6,1,8]
    
def test_get_diagonale_principale():
    """ tests pour get_colonne """
    matr3 = matrice3()
    assert API.get_diagonale_principale(matr3)==[2,5,8]

def test_get_diagonale_secondaire():
    """ tests pour get_colonne """
    matr3 = matrice3()
    assert API.get_diagonale_secondaire(matr3)==[4,5,6]   

def test_is_triangulaire_inf():
    """ tests pour is_triangulaire_inf """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    matr4 = matrice4()
    assert API.is_triangulaire_inf(matr1)==False
    assert API.is_triangulaire_inf(matr2)==False
    assert API.is_triangulaire_inf(matr3)==False
    assert API.is_triangulaire_inf(matr4)==True

    
def test_transpose():
    """ tests pour transpose """
    matr1 = matrice1()  # matrice 3 x 4
    assert API.get_ligne(matr1,0)==[10,11,12,13]
    assert API.get_colonne(matr1,0)==[10,14,18]
    transpose1 =  API.transpose(matr1) # transpose 4 x 3
    assert API.get_nb_colonnes(transpose1)==3
    assert API.get_nb_lignes(transpose1)==4
    assert API.get_colonne(transpose1,0)==[10,11,12,13]
    assert API.get_ligne(transpose1,0)==[10,14,18]

    matr2 = matrice2()  # matrice 2 x 3
    assert API.get_ligne(matr2,0)==['A', 'B', 'C']
    assert API.get_colonne(matr2,0)==['A', 'D']
    transpose2 =  API.transpose(matr2) # transpose 3 x 2
    assert API.get_nb_colonnes(transpose2)==2
    assert API.get_nb_lignes(transpose2)==3
    assert API.get_colonne(transpose2,0)==['A','B','C']
    assert API.get_ligne(transpose2,0)==['A','D']

def test_bloc():
    """ tests pour bloc """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()

    bloc1 = API.bloc(matr1,0,0,2,3)     
    assert API.get_nb_lignes(bloc1)==2
    assert API.get_nb_colonnes(bloc1)==3
    assert API.get_ligne(bloc1,0)==[10,11,12]
    assert API.get_ligne(bloc1,1)==[14,15,16]

    bloc1 = API.bloc(matr1,1,2,2,2)
    assert API.get_nb_lignes(bloc1)==2
    assert API.get_nb_colonnes(bloc1)==2
    assert API.get_ligne(bloc1,0)==[16,17]
    assert API.get_ligne(bloc1,1)==[20,21]

    bloc2 = API.bloc(matr2,1,0,1,3)
    assert API.get_nb_lignes(bloc2)==1
    assert API.get_nb_colonnes(bloc2)==3
    assert API.get_ligne(bloc2,0)==['D','E','F']
   
    bloc3 = API.bloc(matr3,0,1,2,2)
    assert API.get_nb_lignes(bloc3)==2
    assert API.get_nb_colonnes(bloc3)==2
    assert API.get_ligne(bloc3,0)==[7,6]
    assert API.get_ligne(bloc3,1)==[5,1]

                                    
def test_somme_matrice():
    """ tests pour somme matrice """
    matr1 = matrice1()
    matr3 = matrice3()
    
    sum1 = API.somme_matrice(matr1,matr1)
    assert API.get_ligne(sum1,0)==[20, 22, 24, 26]
    assert API.get_ligne(sum1,1)==[28, 30, 32, 34]
    assert API.get_ligne(sum1,2)==[36, 38, 40, 42]

    sum3 = API.somme_matrice(matr3,matr3)
    assert API.get_ligne(sum3,0)==[4, 14, 12]
    assert API.get_ligne(sum3,1)==[18, 10, 2]
    assert API.get_ligne(sum3,2)==[8, 6, 16]

    assert API.somme_matrice(matr3,matr1)==None  
    
 
def test_produit_matrice():
    """ tests pour somme matrice """
    matr1 = matrice1()
    matr3 = matrice3()
    matr4 = matrice4()
    assert API.produit_matrice(matr1,matr1)==None
    assert API.produit_matrice(matr1,matr3)==None
    assert API.produit_matrice(matr1,matr4)==None

    multi4 = API.produit_matrice(matr4,matr4)
    assert API.get_ligne(multi4,0)==[4, 0, 0]
    assert API.get_ligne(multi4,1)==[63, 25, 0]
    assert API.get_ligne(multi4,2)==[67, 39, 64]

    multi3_4 = API.produit_matrice(matr3,matr4)
    assert API.get_ligne(multi3_4,0)==[91, 53, 48]
    assert API.get_ligne(multi3_4,1)==[67, 28, 8]
    assert API.get_ligne(multi3_4,2)==[67, 39, 64]

    multi3_1 = API.produit_matrice(matr3,matr1)
    assert API.get_ligne(multi3_1,0)==[226, 241, 256, 271]
    assert API.get_ligne(multi3_1,1)==[178, 193, 208, 223]
    assert API.get_ligne(multi3_1,2)==[226, 241, 256, 271]

    multi4_1 = API.produit_matrice(matr4,matr1)
    assert API.get_ligne(multi4_1,0)==[20, 22, 24, 26]
    assert API.get_ligne(multi4_1,1)==[160, 174, 188, 202]
    assert API.get_ligne(multi4_1,2)==[226, 241, 256, 271]

    multi4_3 = API.produit_matrice(matr4,matr3)
    assert API.get_ligne(multi4_3,0)==[4, 14, 12]
    assert API.get_ligne(multi4_3,1)==[63, 88, 59]
    assert API.get_ligne(multi4_3,2)==[67, 67, 91]

    multi3_3 = API.produit_matrice(matr3,matr3)
    assert API.get_ligne(multi3_3,0)==[91, 67, 67]
    assert API.get_ligne(multi3_3,1)==[67, 91, 67]
    assert API.get_ligne(multi3_3,2)==[67, 67, 91]






