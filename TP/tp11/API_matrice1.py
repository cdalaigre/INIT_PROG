""" Matrices : API n 1 """
""" Modélisation de matrice numéro 1 """
""" (nb_lignes, nb_colonnes, liste_valeur) """

def matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    liste_valeur=[]
    for i in range (nb_lignes*nb_colonnes):
        liste_valeur.append(valeur_par_defaut)
    
    return (nb_lignes, nb_colonnes, liste_valeur)

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
    la_matrice[2][ligne*get_nb_colonnes(la_matrice)+colonne]=nouvelle_valeur


def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return la_matrice[0]


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return la_matrice[1]


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
    return la_matrice[2][ligne*get_nb_colonnes(la_matrice)+colonne]

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
    
    nblignes = 0
    nbcolonnes = 0
    liste_valeurs=[]

    with open(nom_fichier, 'r') as file:
        lignes = file.readlines()
    
        for ligne in lignes:
            l_champs = ligne.split(",")
            nblignes += 1
            nbcolonnes = len(l_champs)-1
            for colonne in range (nbcolonnes):
                liste_valeurs.append(l_champs[colonne])
                    
    return (nblignes, nbcolonnes, liste_valeurs)

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
    lst_vl = la_matrice[2]

    with open(nom_fichier, "w") as file:

        for ligne in range(nbl):
            for colonne in range(nbc):
                file.write(f"{lst_vl[ligne*nbc + colonne]},")
            file.write(f"\n")

#sauve_matrice((3,2,[0,2,4,6,1,5]),"test.csv")    

""" Fonctions utilitaires pour manipuler les matrices """

def get_ligne(matrice, num_ligne):
    lst_val=matrice[2]
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    ligne=[]

    if num_ligne < nbl:
        for position in range (num_ligne*nbc, num_ligne*nbc+nbc):
            coef = lst_val[position]
            ligne.append(coef)
        return ligne
    
    else: return None

def get_colonne(matrice, num_colonne):
    lst_val=matrice[2]
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    colonne=[]

    if num_colonne < nbc:
        for ligne in range (nbl):
            coef = lst_val[ligne*nbc+num_colonne]
            colonne.append(coef)
        return colonne
    
    else: return None

def get_diagonale_principale(matrice):
    lst_val=matrice[2]
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    main_diag=[]

    for ligne in range (nbl):
        coef = lst_val[ligne*nbc+ligne]
        main_diag.append(coef)
    return main_diag

def get_diagonale_secondaire(matrice):
    lst_val=matrice[2]
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    second_diag=[]

    for ligne in range (nbl):
        coef = lst_val[(2-ligne)*nbc+ligne]
        second_diag.append(coef)
    return second_diag

def transpose (matrice):
    nbl = get_nb_lignes(matrice)
    nbc = get_nb_colonnes(matrice)
    transpose_val = []

    for colonne in range(nbc):
        ma_colonne=get_colonne(matrice,colonne)
        for coef in ma_colonne:
            transpose_val.append(coef)

    return(nbc,nbl,transpose_val)

def is_triangulaire_inf(matrice):
    lst_val=matrice[2]
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
    lst_bloc=[]

    if ligne>nbl or colonne>nbc or (ligne+hauteur)>nbl or (colonne+largeur)>nbc:
        return None
       
    #extractiob du bloc
    for i in range(ligne, ligne+hauteur):
        for j in range(colonne, colonne+largeur):
             lst_bloc.append(get_val(matrice,i,j))
    
    return (hauteur,largeur,lst_bloc)

def somme_matrice(la_matrice_1, la_matrice_2):
   
    nbl = get_nb_lignes(la_matrice_1)
    nbc = get_nb_colonnes(la_matrice_1)
    nbl_ = get_nb_lignes(la_matrice_2)
    nbc_ = get_nb_colonnes(la_matrice_2)

    if nbl==nbl_ and nbc==nbc_ :
        matrice = []

        for ligne in range(nbl):
            for col in range(nbc):
                matrice.append( get_val(la_matrice_1,ligne,col) + get_val(la_matrice_2,ligne,col) )

        return (nbl, nbc, matrice)
    
    else: return None

def produit_matrice(la_matrice_1, la_matrice_2):
   
    nbligne1 = get_nb_lignes(la_matrice_1)
    nbcol1 = get_nb_colonnes(la_matrice_1)
    nbligne2 = get_nb_lignes(la_matrice_2)
    nbcol2 = get_nb_colonnes(la_matrice_2)

    if  nbcol1 == nbligne2:
        matrice = []
        for ligne in range(nbligne1): 
            for col in range(nbcol2):
                total=0
                for elt in range(len(la_matrice_2)):
                    total += get_val(la_matrice_1,ligne,elt) * get_val(la_matrice_2,elt,col)
                matrice.append(total)
                
        return (nbligne1, nbcol2, matrice)
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
            set_val(matrice, ligne, col, get_val(sousmatr,ligne-l,col-c))
    
    return matrice