"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 'w'
EST = 's'

import matrice as MAT 

def init(nom_fichier="./labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    plateau = MAT.charge_matrice(nom_fichier,'int')
    MAT.set_val(plateau,0,0,2)
    MAT.set_val(plateau, MAT.get_nb_lignes(plateau)-1,MAT.get_nb_colonnes(plateau)-1,3)

    return plateau



def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    return True if (0<=position[0]<MAT.get_nb_lignes(le_plateau) and 0<=position[1]<MAT.get_nb_colonnes(le_plateau)) else False


def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    return MAT.get_val(le_plateau,position[0],position[1]) if est_sur_le_plateau(le_plateau,position) else None


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    return True if get(le_plateau,position)==MUR else False


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    return True if get(le_plateau,position)==FANTOME else False

def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """
    return True if ( position[0]==(MAT.get_nb_lignes(le_plateau)-1) and position[1]==(MAT.get_nb_colonnes(le_plateau)-1) ) else False


def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    old = personnage
    
    match direction:
        case 'w': 
            new = (personnage[0]+1, personnage[1])
        case 'z':
            new = (personnage[0]-1, personnage[1])
        case 's':
            new = (personnage[0], personnage[1]+1)
        case 'q':
            new = (personnage[0], personnage[1]-1)  

    if ( not est_un_mur(le_plateau, new) and est_sur_le_plateau(le_plateau, new) ) :
        MAT.set_val(le_plateau, old[0], old[1], 0)
        MAT.set_val(le_plateau, new[0], new[1], 2)
        return new
    else :
        return old
        
def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    lesPositionsValides = set()

    for ligne in range ( position[0]-1, position[0]+2, 1):
        valide = (ligne,position[1])
        if est_sur_le_plateau(le_plateau, valide) and not est_un_mur(le_plateau, valide) and valide != position :
            lesPositionsValides.add(valide)

    for colonne in range ( position[1]-1, position[1]+2, 1):
        valide = (position[0],colonne)
        if est_sur_le_plateau(le_plateau, valide) and not est_un_mur(le_plateau, valide) and valide != position :
            lesPositionsValides.add(valide)
    
    return lesPositionsValides


def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """

    #création du calque
    nb_lignes = MAT.get_nb_lignes(le_plateau)
    nb_colonnes = MAT.get_nb_colonnes(le_plateau)
    calque = MAT.new_matrice(nb_lignes, nb_colonnes , None )
    MAT.set_val(calque,position_depart[0],position_depart[1],0)
    
    i=0                                 #nombre de tour de boucle, mais représente aussi la valeur à mettre dans une case pour le tour considéré
    fin=(nb_lignes-1,nb_colonnes-1)     #position de la case d'arrivée
    changed=True

    while ( get(calque,fin) is None or changed==True):      
    # tant que la case d'arrivée n'est pas atteinte (donc None) ou tant qu'il y a des changements
            
        for ligne in range (nb_lignes):
            for colonne in range (nb_colonnes):
                #parcours du calque et sauvegarde de la position actuelle
                position = (ligne,colonne)

                #détermination des 4 voisins du calque
                lesVoisinsSurCalque = { (position[0]-1,position[1]), (position[0]+1,position[1]), (position[0],position[1]-1), (position[0],position[1]+1) }
                
                #pour chaque voisin
                for leVoisinSurCalque in lesVoisinsSurCalque:

                    # si le voisin est marqué d'une valeur (i) et que la position courante est None sur le calque et valide sur le plateau
                    if get(calque,leVoisinSurCalque)==i and get(calque,position) == None and not est_un_mur(le_plateau,position):

                        #modification de la valeur de la case à la position courante (i+1)
                        MAT.set_val(calque,position[0],position[1], i+1)
                        changed = True

                    else :
                        #sinon pas de changement
                        changed = False
        
        # GO pour le tour suivant
        i=i+1

    return calque

def fabrique_chemin(le_plateau, position_depart, position_arrivee):
    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
   
    calque = fabrique_le_calque(le_plateau,position_depart)
    top = get(calque,position_arrivee)
    chemin=[]
    chemin.append(position_arrivee)
    actuelle = position_arrivee

    for decroissant in range(top-1,0,-1):
        
        #détermination des 4 voisins de la position actuelle
        lesVoisins = { (actuelle[0]-1,actuelle[1]), (actuelle[0]+1,actuelle[1]), (actuelle[0],actuelle[1]-1), (actuelle[0],actuelle[1]+1) }

        #parmi les voisins, si un voisin contient la valeur du compteur decroissant, on le stocke dans le chemin, et la position actuelle devient celle stockée.
        for leVoisin in lesVoisins:
            if get(calque,leVoisin)==decroissant :
                chemin.append(leVoisin)
                actuelle = leVoisin

    return chemin


def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    if (fantome[0]>personnage[0] and fantome[1]>personnage[1]):
        chemin = fabrique_chemin(le_plateau, personnage, fantome)
        print(chemin)
        old = chemin[0]
        new = chemin[1]
        print(new)
        print(old)
        MAT.set_val(le_plateau,old[0],old[1],0)
        MAT.set_val(le_plateau,new[0],new[1],3)
    elif (fantome[0]<personnage[0] and fantome[1]<personnage[1]):
        chemin = fabrique_chemin(le_plateau, fantome,personnage)
        print(chemin)
        new = chemin[-1]
        print(new)
        print(fantome)
        MAT.set_val(le_plateau,new[0],new[1],3)
        MAT.set_val(le_plateau,fantome[0],fantome[1],0)
    else:
        new=fantome

    return new

