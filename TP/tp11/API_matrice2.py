""" Matrices : API n 2 """
""" Modélisation de matrice numéro 2 """
""" [ [liste] [liste] ] """

def matrice(nb_lignes, nb_colonnes, valeur_par_defaut=0):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    matrice = [[valeur_par_defaut for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
    
    return matrice

def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    la_matrice[ligne][colonne]=nouvelle_valeur


def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return len(la_matrice)


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return (len(la_matrice[0]))
    
def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    return la_matrice[ligne][colonne]

# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    
   
    liste_valeurs=[]

    with open(nom_fichier, 'r') as file:
        lignes = file.readlines()
    
        for ligne in lignes:
            l_champs = ligne.split(",")
            del(l_champs[-1])
            liste_valeurs.append(l_champs)
                    
    return (liste_valeurs)

#print(charge_matrice_str('matrice.csv'))


def sauve_matrice(la_matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    nbl = get_nb_lignes(la_matrice)
    nbc = get_nb_colonnes(la_matrice)
    
    with open(nom_fichier, "w") as file:

        for ligne in range(nbl):
            for col in range(nbc):
                coef = la_matrice[ligne][col]
                file.write(f"{coef},")
            file.write(f"\n")

#sauve_matrice([[0,2],[4,6],[1,5]],"test.csv")    


""" Fonctions utilitaires pour manipuler les matrices """

def get_ligne(matrice, num_ligne):
    nbl = get_nb_lignes(matrice)
  
    if num_ligne < nbl:
        return matrice[num_ligne]    
    else: return None

def get_colonne(matrice, num_colonne):
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    colonne=[]

    if num_colonne < nbc:
        for ligne in range (nbl):
            coef = matrice[ligne][num_colonne]
            colonne.append(coef)
        return colonne
    
    else: return None

def get_diagonale_principale(matrice):
    nbl = get_nb_lignes(matrice)
    main_diag=[]

    for ligne in range (nbl):
        coef = matrice[ligne][ligne]
        main_diag.append(coef)
    return main_diag

def get_diagonale_secondaire(matrice):
    nbl = get_nb_lignes(matrice)
    second_diag=[]

    for ligne in range (nbl):
        coef = matrice[nbl-1-ligne][ligne]
        print(coef)
        second_diag.append(coef)
    return second_diag

def transpose (matrice):
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    transpose_val = [[0 for _ in range(nbl)] for _ in range(nbc)]

    for colonne in range(nbc):
        ma_colonne=get_colonne(matrice,colonne)
        for j in range(nbl):
            transpose_val[colonne][j]=ma_colonne[j]

    return(transpose_val)

def is_triangulaire_inf(matrice):
    
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)

    if nbl != nbc: return False

    #vérification si les valeurs au dela de la diagonale sont nulles
    for ligne in range(nbl):
        for colonne in range(ligne+1,nbc):
            if get_val(matrice,ligne,colonne) != 0:
                return False
    
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    bloc = [[0 for _ in range(largeur)] for _ in range(hauteur)]

    if ligne>nbl or colonne>nbc or (ligne+hauteur)>nbl or (colonne+largeur)>nbc:
        return None
       
    #extractiob du bloc
    for i in range(ligne, ligne+hauteur):
        for j in range(colonne, colonne+largeur):
             bloc[i-ligne][j-colonne]=get_val(matrice,i,j)
    
    return bloc

def somme_matrice(la_matrice_1, la_matrice_2):
   
    nbl = get_nb_lignes(la_matrice_1)
    nbc = get_nb_colonnes(la_matrice_1)
    nbl_ = get_nb_lignes(la_matrice_2)
    nbc_ = get_nb_colonnes(la_matrice_2)

    if nbl==nbl_ and nbc==nbc_ :
        matrice = [[0 for _ in range(nbc)] for _ in range(nbl)]

        for ligne in range(nbl):
            for col in range(nbc):
                matrice[ligne][col] = la_matrice_1[ligne][col]+la_matrice_2[ligne][col]

        return matrice
    
    else: return None

def produit_matrice(la_matrice_1, la_matrice_2):
   
    nbligne1 = get_nb_lignes(la_matrice_1)
    nbcol1 = get_nb_colonnes(la_matrice_1)
    nbligne2 = get_nb_lignes(la_matrice_2)
    nbcol2 = get_nb_colonnes(la_matrice_2)

    if  nbcol1 == nbligne2:
        matrice = [[0 for _ in range(nbcol2)] for _ in range(nbligne1)]
        for ligne in range(nbligne1): 
            for col in range(nbcol2):
                for elt in range(len(la_matrice_2)):
                    matrice[ligne][col] += la_matrice_1[ligne][elt] * la_matrice_2[elt][col]
        return matrice
    else:
        return None

def colle_sous_matrice(matrice, sousmatr, l, c):
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    hauteur = get_nb_lignes(sousmatr)
    largeur = get_nb_colonnes(sousmatr)

    if l>nbl or c>nbc or (l+hauteur)>nbl or (c+largeur)>nbc:
        return None

    for ligne in range (l, l+get_nb_lignes(sousmatr)):
        for col in range (c, c+get_nb_colonnes(sousmatr)):
            set_val(matrice, ligne, col, sousmatr[ligne-l][col-c])
    
    return matrice

