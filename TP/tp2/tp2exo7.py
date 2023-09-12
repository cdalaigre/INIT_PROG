def contravention(agglo, exces, recidive):
    """_summary_

    Args:
        agglo (boolean): en ville ou pas 
        exces (int): depassement de vitesse 
        recidive (boolean): récidive ou pas

    Returns:
        int: triplet d'entier (montant amende, nb point, nb mois suspension)
    """
    pv=[0,0,0]
    
    if exces < 20:
        if agglo == True:
            pv=[90,1,0]
        else:
            pv=[45,1,0]
    if exces >= 20 and exces < 30:
        pv = [90,2,0]
    if exces >= 30 and exces < 40:
        pv = [90,3,3]
    if exces >= 40 and exces < 50:
        pv = [90,4,3]
    if exces > 50:
        if recidive == True:
            pv = [3750,6,3]
        else:
            pv = [1500,6,3]
        
    return pv

def test_contravention():
    assert contravention(True, 15, False)==[90,1,0]
    assert contravention(False, 15, False)==[45,1,0]
    assert contravention(False, 25, False)==[90,2,0]
    assert contravention(False, 35, False)==[90,3,3]
    assert contravention(False, 45, False)==[90,4,3]
    assert contravention(False, 55, False)==[1500,6,3]
    assert contravention(False, 55, True)==[3750,6,3]