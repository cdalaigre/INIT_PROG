scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']

def TopScore(ls, lj, nom):
    """Fonction qui retourne le meilleur score d'un joueur dont le nom sera donné en
paramètre. Si le joueur n'est pas dans la liste, on retournera None.

    Args:
        ls (list): liste de scores
        lj (list): liste de joueurs
        nom (str): nom d'un joueur

    Returns:
        int: meilleur du score du joueur passé en paramètre parmi les listes
    """    
    best=None

    for i in range(len(lj)):
        if lj[i]==nom:
            best = ls[i]
            return best 

def test_TopScore():
    assert TopScore(scores,joueurs,'Joker')==220199
    assert TopScore(scores,joueurs,'Robin')==325410
    assert TopScore(scores,joueurs,'TiTof')==None
    assert TopScore(scores,joueurs,'Batman')==352100

def IsDsc(ls):
    """Fonction qui vérifie le tri décroissant d'une liste d'entiers

    Args:
        liste (list): liste d'entiers naturels positifs

    Returns:
        boolean: vrai si la liste est triée dans l'ordre décroissant, faux sinon.
    """    
    for i in range (1,len(ls)):
        if ls[i-1]<ls[i]:
            return False
        
    return True

def test_IsDsc():
    assert IsDsc(scores)==True

def HowManyTimes(lj,nom):
    """Fonction qui détermine combien de fois un joueur dont le nom est passé en paramètre apparait.

    Args:
        lj (list): liste des joueurs
        nom (str): nom d'un joueur

    Returns:
        int: nombre de fois que le joueur apparait dans la liste
    """    
    cpt = 0
    for i in range(len(lj)):
        if lj[i]==nom:
            cpt = cpt + 1
    return cpt

def test_HowManyTimes():
    assert HowManyTimes(joueurs,'Batman')==3
    assert HowManyTimes(joueurs,'Titof')==0
    assert HowManyTimes(joueurs,'Joker')==1
    assert HowManyTimes(joueurs,'Robin')==1

def TopClassement(lj,nom):
    """Fonction qui détermine le meilleur classement d'un joueur passé en paramètre

    Args:
        lj (list): liste de joueurs
        nom (str): nom d'un joueur

    Returns:
        int: position dans le classement
    """
    pos=None

    for i in range(len(lj)):
        if lj[i]==nom:
            pos = i+1
            return pos 
        
    return pos

def test_TopClassement():
    assert TopClassement(joueurs,'Batman')==1
    assert TopClassement(joueurs,'Titof')==None
    assert TopClassement(joueurs,'Joker')==4
    assert TopClassement(joueurs,'Robin')==2

def InsertScore(ls, s):
    """Fonction qui indique à quelle position insérer le nouveau score passé en paramètre

    Args:
        ls (list): liste des scores triés dans l'ordre décroissant
        s (int): score à insérer

    Returns:
        int: position à laquelle il faut insérer le nouveau score
    """
    pos = 0

    for i in range(len(ls)):
        if s > ls[i]:
            pos = i
            return pos        
    if pos==0:
        pos = len(ls)
        return pos

def test_InsertScore():
    assert InsertScore(scores,410000)==0
    assert InsertScore(scores,41000)==5
    assert InsertScore(scores,281004)==3
    assert InsertScore(scores,130377)==4

def InsertPlayerWithScore(ls,lj,s,n):
    """Procédure qui insert le score et le joueur à la bonne place dans les listes

    Args:
        ls (list): liste des scores
        lj (list): liste des joueurs
        s (int): score à insérer
        n (str): nom du joueur à insérer
    """
    position = InsertScore(ls,s)

    if position==len(ls):
        ls.append(s)
        lj.append(n)
    else:
        ls.insert(position,s)
        lj.insert(position,n)

def test_InsertPlayerWithScore():
    InsertPlayerWithScore(scores,joueurs,281004,'CatWoman')
    assert scores==[352100, 325410, 312785, 281004, 220199, 127853]
    assert joueurs==['Batman', 'Robin', 'Batman', 'CatWoman', 'Joker', 'Batman']
    InsertPlayerWithScore(scores,joueurs,41000,'Pingouin')
    assert scores==[352100, 325410, 312785, 281004, 220199, 127853, 41000]
    assert joueurs==['Batman', 'Robin', 'Batman', 'CatWoman', 'Joker', 'Batman', 'Pingouin']
    InsertPlayerWithScore(scores,joueurs,130377,'Alfred')
    assert scores==[352100, 325410, 312785, 281004, 220199, 130377, 127853, 41000]
    assert joueurs==['Batman', 'Robin', 'Batman', 'CatWoman', 'Joker', 'Alfred', 'Batman', 'Pingouin']