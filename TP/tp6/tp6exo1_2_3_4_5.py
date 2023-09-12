# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(lobs):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    oiseau_max = None
    nb_max=0
    for i in range(len(lobs)):
        nom, nb = lobs[i]
        if nb > nb_max:
            nb_max = nb
            oiseau_max = nom
    return oiseau_max

def test_oiseau_le_plus_observe():
    assert oiseau_le_plus_observe(observations1)=="Moineau"
    assert oiseau_le_plus_observe(observations2)=="Tourterelle"
    assert oiseau_le_plus_observe(observations3)=="Mésange"
    assert oiseau_le_plus_observe([])==None

def recherche_oiseau(lo,n):
    """fonction qui permet de retrouver les caractéristiques (nom,famille) d'un oiseau dans
une liste d'oiseaux à partir de son nom

    Args:
        lo (list): liste d'oiseaux
        n (str): nom d'un oiseau

    Returns:
        str,str: tuple représentant les caractéristiques de l'oiseau (nom, famille)
    """
    caracteristique=(None,None)
    for i in range(len(lo)):
        nom, famille = lo[i]
        if nom == n:
            caracteristique=(nom,famille)

    return caracteristique

def test_recherche_oiseau():
    assert recherche_oiseau(oiseaux,"Pie")==("Pie", "Corvidé")
    assert recherche_oiseau(oiseaux,"Pigeon")==(None, None)
    assert recherche_oiseau(oiseaux,"")==(None, None)

def recherche_par_famille(lo,f):
    """fonction qui permet de retrouver tous les oiseaux d'une même famille dans une liste
d'oiseaux

    Args:
        lo (list): liste d'oiseaux
        f (str): famille d'un oiseau

    Returns:
        list: liste d'oiseaux faisant parti de la famille passée en paramètre.
    """    
    lb=[]
    for i in range(len(lo)):
        nom, famille = lo[i]
        if famille == f:
            lb.append(nom)

    return lb

def test_recherche_par_famille():
    assert recherche_par_famille(oiseaux,'Passereau')==['Moineau','Mésange','Pinson','Rouge-gorge']
    assert recherche_par_famille(oiseaux,'Pigeon')==[]
    assert recherche_par_famille(oiseaux,'Corvidé')==['Pie']
    assert recherche_par_famille(oiseaux,'Picidae')==['Pic vert']

def est_liste_observations(lobs):
    """fonction qui vérifie qu'une liste est bien une liste d'observations suivant les critères
donnés : ordre alphabétique des noms d'oiseau et qui ne contient aucune observation avec 0 spécimens vus.

    Args:
        lo (list): liste d'observation composée de tuples (nom oiseau, nb observé)

    Returns:
        boolean: vrai si la liste d'observation respecte les critères.
    """    
    
    for i in range(1,len(lobs)):
        if lobs[i][1]==0:             #le nombre d'oiseaux observé est à la position 1 dans le tuple
            return False
        if lobs[i-1][0]>lobs[i][0]:     #comparaison des noms en position 0 du tuple pour l'ordre alpha 
            return False

    return True

def test_est_liste_observations():
    assert est_liste_observations(observations1)==True
    assert est_liste_observations(observations2)==False
    assert est_liste_observations(observations3)==True
 
def frequence_le_plus_observe(lobs):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: frequence la plus elevée 
    """
    oiseau_max = None
    nb_max=0
    for i in range(len(lobs)):
        nom, nb = lobs[i]
        if nb > nb_max:
            nb_max = nb
            oiseau_max = nom
    return nb_max

def test_frequence_le_plus_observe():
    assert frequence_le_plus_observe(observations1)==5
    assert frequence_le_plus_observe(observations2)==5
    assert frequence_le_plus_observe(observations3)==4
    assert frequence_le_plus_observe([])==0

def moyenne_oiseaux_observes(lobs):
    """fonction qui calcule le nombre moyen de spécimens observés dans une liste d'observations.

    Args:
        lo (list): liste d'observations

    Returns:
        float: nombre moyen de specimens observés
    """    
    res=0
    for i in range(len(lobs)):
        nom, nb = lobs[i]
        res = res + nb
    res = res / len(lobs)

    return res

def test_moyenne_oiseaux_observes():
    assert moyenne_oiseaux_observes(observations1)==18/6
    assert moyenne_oiseaux_observes(observations2)==15/6
    assert moyenne_oiseaux_observes(observations3)==16/6
    
def total_famille(lo,lobs,f):
    """fonction qui calcule le nombre total de spécimens observés pour une famille d'oiseaux
à partir d'une liste d'oiseaux et d'une liste d'observations.

    Args:
        lo (list): liste d'oiseaux
        lobs (list): liste d'observations
        f (str): famille d'oiseaux

    Returns:
        int: nombre total de spécimens observés pour la famille considérée
    """
    somme=0

    especes=recherche_par_famille(lo,f)
    for i in range(len(lobs)):
        nom, nb = lobs[i]
        if nom in especes:
            somme = somme + nb

    return somme

def test_total_famille():
    assert total_famille(oiseaux,observations1,'Passereau')==8
    assert total_famille(oiseaux,observations2,'Passereau')==8
    assert total_famille(oiseaux,observations3,'Passereau')==7
    assert total_famille(oiseaux,observations1,'Pigeon')==0


def construire_liste_observations(lo,cpt):
    """une fonction qui à partir d'une liste d'oiseaux et d'une liste de comptage crée une liste
d'observations

    Args:
        lo (list): liste d'oiseaux
        cpt (list): comptage

    Returns:
        list: liste d'observation générée
    """   
    lobs=[]

    for i in range(len(lo)):
        nom, famille = lo[i]
        if cpt[i] > 0:
            lobs.append((nom,cpt[i]))

    return lobs

def test_construire_liste_observations():
    assert construire_liste_observations(oiseaux,[2,0,0,0,0,0,0,9])==[('Merle',2),('Tourterelle',9)]
    assert construire_liste_observations(oiseaux,[0,0,0,0,0,0,0,0])==[]
    assert construire_liste_observations(oiseaux,[0,0,0,1,1,0,0,0])==[('Pic vert',1),('Pie',1)]

def saisie_observations(lo):
    """fonction qui prend en paramètre une liste d'oiseaux et demande à l'utilisateur le
nombre de spécimens de chaque oiseau qu'il a observés. La fonction doit retourner une liste
d'observations.

    Args:
        lo (list): liste d'oiseaux

    Returns:
        list: liste d'observations
    """
    lobs=[]
    reponse=[]

    for oiseau in lo:
        print("Combien de", oiseau[0], "de la famille des", oiseau[1], "avez-vous observé ?")
        rep=int(input())
        reponse.append(rep)
    
    lobs = construire_liste_observations(lo,reponse)

    return lobs

def afficher_observations(lo,lobs):
    for obs in lobs:
        for oiseau in lo:
            if oiseau[0]==obs[0]:
                print ("Nom:", oiseau[0].ljust(15," "), "Famille:", oiseau[1].ljust(15," "), "Nb observés:", obs[1])

def creer_ligne_sup(lobs, seuil):
    """crée une ligne contenant des ** pour les oiseaux dont le nombre de spécimens observés et supérieur au seuil 
            et '    ' pour les autres

    Args:
        lobs (list): une liste d'observations
        seuil (int): le seuil pour avoir des étoiles

    Returns:
        str: la chaîne de caractères décrite ci-dessus
    """  
    res=''
    for obs in lobs:
        if obs[1]>=seuil:
            res+="**  "
        else:
            res+="    "
    return res      

def test_creer_ligne_sup():
    assert creer_ligne_sup(observations1,0)=="**  **  **  **  **  **  "
    assert creer_ligne_sup(observations2,0)=="**  **  **  **  **  **  "
    assert creer_ligne_sup(observations3,0)=="**  **  **  **  **  **  "

def creer_ligne_noms_oiseau(lobs):
    """crée une ligne contenant les 3 premières lettre du nom de chacun des oiseaux observés suivies d'une espace

    Args:
        lobs (list): une liste d'observations

    Returns:
        str: la chaîne de caractères décrite ci-dessus
    """    
    res=''
    for obs in lobs:
        res+=obs[0][:3]+' '
    return res

def test_creer_ligne_noms_oiseau():
    assert creer_ligne_noms_oiseau(observations1)=="Mer Moi Pic Pie Rou Tou "
    assert creer_ligne_noms_oiseau(observations2)=="Mer Més Moi Pin Tou Rou "
    assert creer_ligne_noms_oiseau(observations3)=="Més Pic Pie Pin Rou Tou "

def afficher_graphique_observation(lobs):
    """affiche le graphique correspondant à une liste d'observations

    Args:
        liste_observations (list): une liste d'observations
    """    
    
    nb_oiseaux=len(lobs)
    for seuil in range(frequence_le_plus_observe(lobs),0,-1):
        print(creer_ligne_sup(lobs,seuil))

    print(creer_ligne_noms_oiseau(lobs))

#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------
# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# print(saisie_observations(oiseaux))
# afficher_graphique_observation(observes)
#afficher_observations(oiseaux, observations1)
#afficher_observations(oiseaux, observations2)
#afficher_observations(oiseaux, observations3)
#afficher_graphique_observation(observations1)
#afficher_graphique_observation(observations2)
#afficher_graphique_observation(observations3)