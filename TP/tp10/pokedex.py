"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    res = False
    for tuple in pokedex:
        if tuple[0]==pokemon: res=True
    return res   


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    res = set()
    for tuple in pokedex:
        if tuple[0]==pokemon: 
            res.add(tuple[1])
    return res   


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt=0
    for tuple in pokedex:
        if tuple[1]==attaque: 
            cpt+=1
    return cpt 


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    max=0
    attaque=""
    for tuple in pokedex:
        nb = nombre_de_v1(tuple[1],pokedex)
        if  nb > max:
            max = nb
            attaque=tuple[1]
    return attaque


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    return pokemon in pokedex


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt=0
    for values in pokedex.values():
        if attaque in values:
            cpt+=1
    return cpt

def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    max=0
    attaque=""
    for lesAttaques in pokedex.values():
        for uneAttaque in lesAttaques:
            nb = nombre_de_v2(uneAttaque,pokedex)
            if  nb > max:
                max = nb
                attaque=uneAttaque
    return attaque

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    ...


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    ...


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    ...


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    ...

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    ...


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    ...

