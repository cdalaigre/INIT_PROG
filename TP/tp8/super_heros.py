def intelligence_moyenne(super_heros):
    """ Calcule la valeur moyenne de l'intelligence de tous les personnages

    Args:
        super_heors (dict): un dictionnaire modélisant les supers heros

    Returns:
        float: la valeur moyenne de l'intelligence dans le dictionnaire
    """
    total=0

    if super_heros == {}: return None
    for tuple in super_heros.values():
        total+=tuple[1]

    return total/len(super_heros)

def kikelplusfort(super_heros):
    """ Recherche le nom du personnage le plus fort

    Args:
        super_heors (dict): un dictionnaire modélisant les supers heros

    Returns:
        str: le nom du personnage le plus fort
    """
    le_plus_fort=""
    force = 0

    for nom,tuple in super_heros.items():
        if tuple[0]>force:
            force=tuple[0]
            le_plus_fort= nom

    return le_plus_fort

def combiendecretins(super_heros):
    """ Calcule le nombre de personnages dont l'intelligence est strictement inférieure à la moyenne.

    Args:
        super_heors (dict): un dictionnaire modélisant les supers heros

    Returns:
        int: le nombre de personnages dont l'intelligence est strictement inférieure à la moyenne.
    """
    nombre_de_cretins=0
    seuil_imbecilite = intelligence_moyenne(super_heros)

    for tuple in super_heros.values():
        if tuple[1]<seuil_imbecilite:
            nombre_de_cretins+=1

    return nombre_de_cretins