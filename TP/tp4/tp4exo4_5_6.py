def Recherche(lm,lettre):
    """Recherche de mot commencant par une lettre précise dans une liste 

    Args:
        lm (liste): liste de mots
        lettre (str): caractère 

    Returns:
        liste: liste de mots de la liste initiale commencant par le caractère spécifié
    """    

    res=[]

    for mot in lm:
        if mot != "" and mot[0]==lettre:
            res.append(mot)
    return res

def test_Recherche():
    assert Recherche(["salut","hello","hallo","ciao","hola"],'h')==["hello", "hallo", "hola"]
    assert Recherche(["salut","hello","hallo","ciao","hola"],'a')==[]
    assert Recherche(["salut"," hello","hallo","ciao","hola"],'h')==["hallo", "hola"]
    assert Recherche([],'h')==[]

def Decoupage(phrase):
    """Decoupage d'une phrase en mots

    Args:
        phrase (str): texte à découper

    Returns:
        liste: liste des mots composant le texte
    """
    res=[]
    mot_courant = ""
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            mot_courant += phrase[i]
        else:
            if mot_courant != "":
                res.append(mot_courant)
                mot_courant = ""
    if mot_courant != "":
        res.append(mot_courant) 
    return res

def test_Decoupage():
    assert Decoupage("Cela fait déjà 28 jours! 28 jours à l'IUT'O! Cool!!")==["Cela", "fait", "déjà", "jours", "jours", "à", "l", "IUT", "O", "Cool"]
    assert Decoupage("(3*2)+1")==[]
    assert Decoupage("")==[]
    assert Decoupage("   essai    avec    plein d'espaces  ")==["essai","avec","plein","d","espaces"]

def Mixte(phrase,lettre):
 
    return Recherche(Decoupage(phrase),lettre)
    

def test_Mixte():
    assert Mixte("Cela fait déjà 28 jours! 28 jours à l'IUT'O! Cool!!","C")==["Cela","Cool"]