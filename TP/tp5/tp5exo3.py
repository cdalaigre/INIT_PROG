def IsAsc(liste):
    """Fonction qui vérifie le tri croissant d'une liste d'entiers

    Args:
        liste (list): liste d'entiers naturels positifs

    Returns:
        boolean: vrai si la liste est triée dans l'ordre croissant, faux sinon.
    """    
    for i in range (1,len(liste)):
        if liste[i-1]>liste[i]:
            return False
        
    return True

def test_IsAsc():
    assert IsAsc([2,4,6,8,10])==True
    assert IsAsc([9,7,5,3,1])==False
    assert IsAsc([2,4,6,8,7])==False
    assert IsAsc([2,4,1,8,10])==False

def IsOver (liste, seuil):
    """Fonction qui vérifie que la somme des nombres entiers dans la liste dépasse un seuil

    Args:
        liste (list): liste de nombres entiers positifs
        seuil (int): valeur de seuil

    Returns:
        booleans: vrai si le cheksum dépasse le seuil
    """
    somme=0
    for elem in liste:
        somme = somme + elem

    if somme > seuil:
        return True
    else:
        return False
    
def test_IsOver():
    assert IsOver([1, 4, 1, 2, 3, 4],6)==True
    assert IsOver([1, 4, 1, 2, 3, 4],50)==False
    assert IsOver([],50)==False

def IsAnEmail(courriel):
    """Fonction qui vérifie que la chaine de caractère est un courriel

    Args:
        courriel (str): chaine de caractère à tester

    Returns:
        boolean: vrai si la chaine de caractère répond aux spécifications
    """
    arobase = False
    point = False
    
    for i in range(len(courriel)):
        if courriel[i] == " ":
            return False
        if courriel[i] == "@":
            if arobase==True: return False
            arobase=True 
        if courriel[i]=="." and arobase==True:
            point = True

    if courriel[0]=="@" or courriel[len(courriel)-1]==".":
            return False    
        
    return arobase and point

def test_IsAnEmail():
    assert IsAnEmail("@gmail.com.")==False
    assert IsAnEmail("cda@gmail.com.")==False
    assert IsAnEmail("cdal@gmail.com")==True
    assert IsAnEmail("cd@l@gmail.com")==False
    assert IsAnEmail("c.d@gmail.com")==True
    assert IsAnEmail(" ")==False