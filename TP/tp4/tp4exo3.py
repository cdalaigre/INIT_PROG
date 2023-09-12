def Conversion(s):
    """Conversion d'une chaine de caractère en nombre 

    Args:
        s (str): chaine de caractère 

    Returns:
        int: nombre entier correspondant 
    """    
    nb=0
    for i in range (len(s)):
        match s[i]:
            case '0' : nb = nb*10 + 0
            case '1' : nb = nb*10 + 1
            case '2' : nb = nb*10 + 2
            case '3' : nb = nb*10 + 3
            case '4' : nb = nb*10 + 4
            case '5' : nb = nb*10 + 5
            case '6' : nb = nb*10 + 6
            case '7' : nb = nb*10 + 7
            case '8' : nb = nb*10 + 8
            case '9' : nb = nb*10 + 9
            case _ : return None

    return nb

def test_Conversion():
    assert Conversion("1234")==1234
    assert Conversion("001234")==1234
    assert Conversion("00120304")==120304
    assert Conversion(" ")==None
    assert Conversion("")==0
    assert Conversion("1O8")==None