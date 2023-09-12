def Population(lv,pop):
    """recherche la ville la plus peuplée parmi une liste
    Args:
        lv (str[]): un tableau de chaines de caractères représentant les villes
        pop (int[]): un tableau d'entier représentant les populations des villes

    Returns:
        str,int: la ville et son nombre d'habitants
    """
    max = 0
    ville = ''
    for i in range (0,len(pop)):
        if (pop[i]>=max):
            max = pop[i]
            ville = lv[i]
    if max >0:
        return ville, max
    else:
        return None,None


# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
def test_Population():
    liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
    population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,25725]

    assert Population(liste_villes,population)==('Tours',136463)
    assert Population([],[])==(None, None)
    