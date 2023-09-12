def SommeDesEntiers(n):
    """Fonction qui somme les n premiers entiers
    Args:
        n ([entier]): [un nombre entier]
    Returns:
        [entier]: [Sommes des entiers jusqu' à n]
    """
    somme = 0
    
    for i in range(n+1):
        somme = somme + i   
    return somme

def test_SommeDesEntiers():
    assert SommeDesEntiers(4)==10
    assert SommeDesEntiers(6)==21
    assert SommeDesEntiers(1)==1
    assert SommeDesEntiers(0)==0


def Syracuse(initial, n):
    """Fonction qui calcule la suite de syracuse
    Args:
        n ([entier]): n termes de la suite
        initial ([entier]): valeur de Uo
    Returns:
        [entier]: resultat de la suite de syracuse
    """
    syracuse = initial
    
    for i in range(n):
        if syracuse % 2 == 0:
            syracuse = syracuse//2
        else:
            syracuse = 3 * syracuse + 1
           
    return syracuse

def test_Syracuse():
    assert Syracuse(6,3) == 5
    assert Syracuse(15, 9) == 40
    assert Syracuse(14, 17) == 1
    assert Syracuse(4520, 0) == 4520
    