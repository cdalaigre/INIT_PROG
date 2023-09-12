def qualification(sexe,record,nbvictoire,champion):
    """_summary_

    Args:
        sexe (caractère): sexe de la personne
        record (float): record personnel
        nbvictoire (int): nombre de victoire dans l'année
        champion (boolean): champion ou non
    Returns:
        res (boolean): qualifié ou non
    """

    if sexe=='M':
        if (record < 12 and nbvictoire >=3 ) or champion==True:
            res = True
        else:
            res = False

    
    if sexe=='F':
        if (record < 15 and nbvictoire >=3 ) or champion==True:
            res = True
        else:
            res = False

    return res

def test_qualification():
    assert qualification('M',13.2,1,False)==False
    assert qualification('M',15.4,0,True)==True
    assert qualification('M',13.7,4,False)==False
    assert qualification('M',13.7,8,True)==True
    assert qualification('M',9.7,1,False)==False
    assert qualification('M',9.9,0,True)==True
    assert qualification('M',11.2,4,False)==True
    assert qualification('M',10.6,8,True)==True
    assert qualification('F',16.2,1,False)==False
    assert qualification('F',17.4,0,True)==True
    assert qualification('F',16.7,4,False)==False
    assert qualification('F',16.7,8,True)==True
    assert qualification('F',12.7,1,False)==False
    assert qualification('F',12.9,0,True)==True
    assert qualification('F',14.2,4,False)==True
    assert qualification('F',13.6,8,True)==True