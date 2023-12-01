""" tests pour les API matrices
    Remarques : tous les tests de ce fichier doivent passer
    quelle que soit l'API utilisée
"""
import API_matrice1 as API
import utilitaires_matrice as utils

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

def test_matrice():
    assert API.matrice(2,6,0)==(2,6,[0,0,0,0,0,0,0,0,0,0,0,0])
    assert API.matrice(2,4,0)==(2,4,[0,0,0,0,0,0,0,0])
    assert API.matrice(2,2,10)==(2,2,[10,10,10,10])

def test_get_ligne():
    """ tests pour get_ligne """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert utils.get_ligne(matr1,0)==[10,11,12,13]
    assert utils.get_ligne(matr2,1)==['D','E','F']
    assert utils.get_ligne(matr3,2)==[4,3,8]
    assert utils.get_ligne(matr1,3)==None

def test_get_colonne():
    """ tests pour get_colonne """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert utils.get_colonne(matr1,0)==[10,14,18]
    assert utils.get_colonne(matr2,1)==['B','E']
    assert utils.get_colonne(matr3,2)==[6,1,8]
    
def test_get_diagonale_principale():
    """ tests pour get_colonne """
    matr3 = matrice3()
    assert utils.get_diagonale_principale(matr3)==[2,5,8]

def test_get_diagonale_secondaire():
    """ tests pour get_colonne """
    matr3 = matrice3()
    assert utils.get_diagonale_secondaire(matr3)==[4,5,6]   
    
def test_transpose():
    """ tests pour transpose """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert utils.transpose(matr1)==(4,3,[10,14,18,11,15,19,12,16,20,13,17,21]) 
    assert utils.transpose(matr2)==(3,2,['A','D','B','E','C','F'])  
    assert utils.transpose(matr3)==(3,3,[2,9,4,7,5,3,6,1,8])  

def test_is_triangulaire_inf():
    """ tests pour is_triangulaire_inf """
    assert utils.is_triangulaire_inf((2,2,[1,0,2,3]))==True
    assert utils.is_triangulaire_inf((3,3,[1,0,0,2,2,0,3,2,1]))==True
    assert utils.is_triangulaire_inf((4,4,[1,0,0,0,2,1,0,0,3,2,1,0,4,3,2,1]))==True
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert utils.is_triangulaire_inf(matr1)==False
    assert utils.is_triangulaire_inf(matr2)==False
    assert utils.is_triangulaire_inf(matr3)==False

def test_bloc():
    """ tests pour bloc """
    matr1 = matrice1()
    matr2 = matrice2()
    matr3 = matrice3()
    assert utils.bloc(matr1,0,0,2,3)==(2,3,[10,11,12,14,15,16])
    assert utils.bloc(matr1,1,2,2,2)==(2,2,[16,17,20,21])
    assert utils.bloc(matr2,1,0,1,3)==(1,3,['D','E','F'])
    assert utils.bloc(matr3,0,1,2,2)==(2,2,[7,6,5,1])
