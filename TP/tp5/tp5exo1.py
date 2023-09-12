def mystere(liste, valeur):
    """Renvoie la position à laquelle se trouve la quatrième valeur correspondante sinon rien

    Args:
        liste ([int]): tableau d'entier
        valeur ([int]): valeur recherché dans la liste

    Returns:
        [int]: position de la quatrieme valeur correspondante
    """
    nbfoistrouve = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            nbfoistrouve += 1
            if nbfoistrouve > 3:
                return i
    return None

def test_mystere():
    assert mystere([12, 5, 5, 48, 12, 418, 5, 17, 5, 87], 5)==8
    assert mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)==None
    assert mystere([], 41)==None


