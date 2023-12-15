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
        tps = FlyTime(i)
        if tps>temps_de_vol:
            temps_de_vol = tps
            champion = i
    
    return champion

def temps_de_vol_avec_precalcul(n, temps_connus):
    temps_de_vol=0
    suite = Syracuse(n)

    for element in suite:
        if element in temps_connus.keys():
            temps_de_vol= temps_connus[element]+suite.index(element)

    return temps_de_vol

def temps_de_vol_avec_precalculv2(n, temps_connus):
    temps_de_vol=0
    suite=n
    i=0
    while suite !=1: 
        if suite % 2 == 0:
            suite = suite//2
        else:
            suite = 3 * suite + 1
        i+=1

        if suite in temps_connus.keys():
            temps_de_vol= temps_connus[suite]+i
            return temps_de_vol
    
    return i

def Champion_avec_precalcul(n,temps_connus):
    temps_de_vol=0
    champion = None
    for i in range (1,n):
        tps = temps_de_vol_avec_precalculv2(i, temps_connus)
        if tps>temps_de_vol:
            temps_de_vol = tps
            champion = i
    
    return champion

