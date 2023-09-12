def SommeDesPairs(entree):
    """Fonction qui somme les nombres pairs
    Args:
        entree ([tableau entier]): [liste de nombres pair ou impair]
    Returns:
        [entier]: [Sommes des nombres pairs]
    """
    somme = 0
    # au début de chaque tour de boucle
    #  on regarde si le nombre courant est pair 
    for nb in entree:
        if nb % 2 == 0:
            somme = somme + nb   
    return somme

def test_SommeDesPairs():
    assert SommeDesPairs([12,13,6,5,7]) == 18
    assert SommeDesPairs([12,13,-6,5,7]) == 6
    assert SommeDesPairs([11,13,3,5,7]) == 0
    assert SommeDesPairs([]) == 0

def DerniereVoyelle(phrase):
    """Fonction qui retourne la derniere voyelle d'une phrase
    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)
    Returns:
        str: la derniere voyelle de la phrase
    """    
    resultat = None
    carac = ' '
    # au début de chaque tour de boucle
    # caracr vaut
    # resultat vaut
    for carac in phrase:
        if carac =='a' or carac =='e' or carac =='i' or carac =='u' or carac =='o' or carac =='y':
            resultat = carac
    return resultat

def test_DerniereVoyelle():
    assert DerniereVoyelle("bonjour") == 'u'
    assert DerniereVoyelle("buongiorno") == 'o'
    assert DerniereVoyelle("hey !") == 'y'
    assert DerniereVoyelle("zrtp") is None

def ProportionNegatifs(entree):
    """Fonction qui somme les nombres pairs
    Args:
        entree ([tableau entier]): [liste de nombres pair ou impair]
    Returns:
        [float]: [pourcentage des nombres négatifs]
    """
    somme = 0
    total = len(entree)
    if total == 0:
        return None
    # au début de chaque tour de boucle
    #  on regarde si le nombre courant est pair 
    for nb in entree:
        if nb < 0:
            somme = somme + 1   
    return somme / total

def test_ProportionNegatifs():
    assert ProportionNegatifs([4,-2,8,2,-2,-7]) == 0.5
    assert ProportionNegatifs([12,13,-6,5,7]) == 0.2
    assert ProportionNegatifs([12,13,6,5,7]) == 0
    assert ProportionNegatifs([-4,-2,-8,2,-7]) == 0.8
    assert ProportionNegatifs([]) is None