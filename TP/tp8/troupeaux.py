# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    total=0
    for nombre in troupeau.values():
        total+=nombre
    
    return total

def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    ensemble_animaux=set()

    for animal in troupeau.keys():
        ensemble_animaux.add(animal)
    
    return ensemble_animaux


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    plus_de_trente=False
    
    for nombre in troupeau.values():
        if nombre >= 30:
            plus_de_trente = True
    
    return plus_de_trente



def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    animal = None
    max=0
    for (espece, quantite) in troupeau.items():
        if quantite > max :
            max=quantite
            animal = espece
    
    return animal

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    suffisant = True

    for (espece, quantite) in troupeau.items():
        if quantite < 5 :
            suffisant = False
    
    return suffisant        

def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    if troupeau1=={}: return troupeau2
    elif troupeau2=={}: return troupeau1
    else:
        troupeau_reuni = dict()

        for (espece,quantite) in troupeau2.items():
            troupeau_reuni[espece]=quantite

        for (animal, nombre) in troupeau1.items():
            if animal in troupeau_reuni.keys():
                troupeau_reuni[animal]=nombre+troupeau_reuni[animal]
            else:
                troupeau_reuni[animal]=nombre
    
        return troupeau_reuni           