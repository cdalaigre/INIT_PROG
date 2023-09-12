def algo1(a,b,c,d):
    """Trouve le plus petit des 4 nombres entier passés en entrée
    Args
    a (int)
    b (int)
    c (int)
    d (int)
    Returns:
    res (int) : retourne le resultat
    """   
    if a < b:
        res = a
    else:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d

    return res

def test_algo1():
    assert algo1(1,2,3,4)==1
    assert algo1(4,2,3,1)==1
    assert algo1(4,1,3,2)==1
    assert algo1(4,3,1,2)==1

def algo2(m):
    """Détermine s'il y a plus de voyelles que de consonnes dans le mot m
    Args:
    m (texte): le mot
    Returns:
    res (boolean) : vrai s'il y a plus de voyelle
    """
    res = 0

    for i in range(0, len(m)):
            if m[0]=='a' or m[0]=='e' or m[0]=='i' or m[0]=='o' or m[0]=='u' or m[0]== 'y':
                 res = res + 1
            else:
                 res = res - 1
    return res>0

def test_algo2():
    assert algo2("bonjour")==False
    assert algo2("amical")==True
    assert algo2("aujourdhui")==True