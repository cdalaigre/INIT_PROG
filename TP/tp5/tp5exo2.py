
def RecherchePremierChiffre(phrase):
    """Fonction qui recherche le premier chiffre dans une chaine de caractère

    Args:
        phrase (str): chaine de caractères

    Returns:
        int: position du chiffre dans la chaine
    """
    for i in range(len(phrase)):
        if phrase[i] in '0123456789':
            return i
        
def test_RecherchePremierChiffre():
    assert RecherchePremierChiffre("Nous sommes le 04/08/2023")==15
    assert RecherchePremierChiffre("Demain nous serons le 05/08/2023")==22

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,  25725]

def TrouvePopulationVille(lv,pop,v):
    """Fonction qui trouve le nombre d'habitants de la ville passée en paramètre

    Args:
        lv (list): liste de villes
        pop (list): populations des villes
        v (str): nom d'une ville

    Returns:
        int: nombre d'habitants
    """
    res=None
    
    for i in range(len(lv)):
        if lv[i]==v:
            res=pop[i]

    return res

def test_TrouvePopulationVille():
    assert TrouvePopulationVille(liste_villes,population,'Blois')==45871
    assert TrouvePopulationVille(liste_villes,population,'Olivet')==22168
    assert TrouvePopulationVille(liste_villes,population,'La Ferté-Saint-Cyr')==None
