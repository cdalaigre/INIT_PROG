import time


def Syracuse(n):
    """Fonction qui calcule la suite de syracuse
    Args:
        initial ([entier]): valeur de Uo
    Returns:
        [entier]: resultat de la suite de syracuse
    """
    syracuse=[]
    syracuse.append(n)
    suite=n
    
    while suite !=1: 
        if suite % 2 == 0:
            suite = suite//2
        else:
            suite = 3 * suite + 1
        
        syracuse.append(suite)
           
    return syracuse

def FlyTime(n):
    return len(Syracuse(n))-1

def Champion(n):
    temps_de_vol=0
    champion = None
    for i in range (1,n):
        if FlyTime(i)>temps_de_vol:
            temps_de_vol = FlyTime(i)
            champion = i
    
    return champion

def temps_de_vol_avec_precalcul(n, temps_connus):
    temps_de_vol=0
    suite = Syracuse(n)

    for element in suite:
        if element in temps_connus.keys():
            temps_de_vol= temps_connus[element]+suite.index(element)

    return temps_de_vol

def Champion_avec_precalcul(n,temps_connus):
    temps_de_vol=0
    champion = None
    for i in range (1,n):
        if temps_de_vol_avec_precalcul(i, temps_connus)>temps_de_vol:
            temps_de_vol = temps_de_vol_avec_precalcul(i, temps_connus)
            champion = i
    
    return champion