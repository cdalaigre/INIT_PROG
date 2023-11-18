"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    mes_familles=set()
    for tuple in pokedex:
        mes_familles.add(tuple[1])
    
    return mes_familles

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nombre = 0
    for tuple in pokedex:
        if tuple[1] == famille:
            nombre += 1
    
    return nombre

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    frequence=dict()
    for tuple in pokedex:
        frequence[tuple[1]]=nombre_pokemons(pokedex,tuple[1])
        
    return frequence


def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_famille = dict()
    
    for nom,famille in pokedex:
        if famille in dico_famille.keys():
            dico_famille[famille].add(nom) 
        else:
            dico_famille[famille]=set()
            dico_famille[famille].add(nom)
                   
    
    return dico_famille


def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    nb=0
    famille_max=None

    for nom,famille in pokedex:
        nombre = nombre_pokemons(pokedex,famille)
        if nombre > nb:
            nb = nombre
            famille_max = famille
            
    return famille_max

# ==========================
# Petites bêtes (la suite)
# ==========================


def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    mes_familles=set()
    for lesFamilles in pokedex.values():
        for famille in lesFamilles:
            if famille not in mes_familles:
                mes_familles.add(famille)
    
    return mes_familles

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nombre = 0
    for lesFamilles in pokedex.values():
        for uneFamille in lesFamilles:
            if uneFamille == famille:
                nombre += 1
    
    return nombre


def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    frequence=dict()
    for lesFamilles in pokedex.values():
        for uneFamille in lesFamilles:
            frequence[uneFamille]=nombre_pokemons_v2(pokedex,uneFamille)
        
    return frequence

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_famille = dict()
    
    for nom,lesFamilles in pokedex.items():
        for uneFamille in lesFamilles:
            if uneFamille in dico_famille.keys():
                dico_famille[uneFamille].add(nom) 
            else:
                dico_famille[uneFamille]=set()
                dico_famille[uneFamille].add(nom)
                   
    return dico_famille

def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    nb=0
    famille_max=None

    for lesFamilles in pokedex.values():
        for uneFamille in lesFamilles:
            nombre = nombre_pokemons_v2(pokedex,uneFamille)
            if nombre > nb:
                nb = nombre
                famille_max = uneFamille
            
    return famille_max
