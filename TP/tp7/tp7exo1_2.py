import csv

############################################################################
def DisplayMenu(t,lopt):
    print("+-------------------------+")
    print("|", t, "|")
    print("+-------------------------+")
    for i in range (len(lopt)):
        print (i+1, "->" , lopt[i])

def AskAnswer(m,borne_max):
    print (m)
    answer=int(input())
    if 1<=answer<=borne_max:
        return answer
    else:
        return None

def GestionMenu(t, lopt):
    DisplayMenu(t,lopt)
    return AskAnswer("Faites votre choix parmi ces options : ", len(lopt))

###########################################################################
def charger_fichier_population(f):
    ldepcomptot=[]
    with open(f, newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=';')
        entete=False
        for row in reader:
            if entete==False:
                entete=True
            else:
                ldepcomptot.append((row[0],row[1],int(row[4])))
                    
    return ldepcomptot

###########################################################################
def GetPopulationByCity(ldepcomptot,c):
    people = None
    for elem in ldepcomptot:
        if elem[1]==c:
            people = elem[2]
    
    return people   

def test_GetPopulationByCity():
    liste_communes=charger_fichier_population("population2017.csv")
    assert GetPopulationByCity(liste_communes,"Amilly")==13577
    assert GetPopulationByCity(liste_communes,"Montargis")==15212
    assert GetPopulationByCity(liste_communes,"")==None

###########################################################################
def GetCitiesBySearch(ldepcomptot,request):
    lc = []
    for elem in ldepcomptot:
        if elem[1].startswith(request):
            lc.append(elem[1])
    
    return lc
    
def test_GetCitiesBySearch():
    liste_communes=charger_fichier_population("population2017.csv")
    assert GetCitiesBySearch(liste_communes,"Orlé")==['Orléans', 'Orléat']
    assert GetCitiesBySearch(liste_communes,"Yvo")==['Yvoy-le-Marron','Yvoire']
    assert GetCitiesBySearch(liste_communes," ")==[]

###########################################################################
def GetBiggestCityByDpt(ldepcomptot,dpt):
    maxpop=0
    maxtown=None
    for elem in ldepcomptot:
        if elem[0].startswith(dpt):
            if elem[2]>=maxpop:
                maxpop=elem[2]
                maxtown=elem[1]
    
    return maxtown

def test_GetBiggestCityByDpt():
    liste_communes=charger_fichier_population("population2017.csv")
    assert GetBiggestCityByDpt(liste_communes,"45")=='Orléans'
    assert GetBiggestCityByDpt(liste_communes,"37")=='Tours'
    assert GetBiggestCityByDpt(liste_communes,"41")=='Blois'

###########################################################################
def GetCitiesBetweenRange(ldepcomptot,inf,sup):
    nbr = 0
    for elem in ldepcomptot:
        if inf<=elem[2]<=sup:
            nbr = nbr + 1
    
    return nbr

def test_GetCitiesBetweenRange():
    liste_communes=charger_fichier_population("population2017.csv")
    assert GetCitiesBetweenRange(liste_communes,400000,500000)==1
    assert GetCitiesBetweenRange(liste_communes,300000,400000)==2
    assert GetCitiesBetweenRange(liste_communes,200000,300000)==6
    assert GetCitiesBetweenRange(liste_communes,200000,500000)==9

###########################################################################
def place_top(commune, liste_pop):
    for ind in range(len(liste_pop)):
        if liste_pop[ind][2]<commune[2]:
            return ind
    return len(liste_pop)

def ajouter_trier(commune,liste_pop,taille_max):
    place=place_top(commune,liste_pop)
    if place<taille_max:
        liste_pop.insert(place,commune)
        if len(liste_pop)>taille_max:
            liste_pop.pop()
    
def top_n_population(liste_pop,nb):
    res=[]
    for commune in liste_pop:
        ajouter_trier(commune,res,nb)
    return res

###########################################################################
def GetPopTotaleByDpt(ldepcomptot):
    stats=1000*[0]
    for elem in ldepcomptot:
        if elem[0][:2] == '2A' or elem[0][:2] == '2B':
            indice=20
        elif elem[0][:2]=='97':
            indice=int(elem[0][:3])
        else:
            indice=int(elem[0][:2])
        stats[indice]=stats[indice]+elem[2]
    
    return stats

def sauve_population_dpt(f,lpd):
    with open(f, 'w', newline='') as csvfile:
        fieldnames = ['NUMDPT', 'POPDPT']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
                   
        for i in range (1,len(lpd)):
            if lpd[i] != 0:
                writer.writerow({'NUMDPT': str(i), 'POPDPT': str(lpd[i])})
        


###########################################################################
def main():
    liste_options=["Charger un fichier",
                   "Rechercher la population d'une commune",
                   "Recherche avancée d'une commune",
                   "Trouver la commune  la plus peuplée d'un département",
                   "Déterminer le nombre de communes dans une tranche de population",
                   "Communes les plus peuplées",
                   "Afficher la population d'un département",
                   "Quitter"]
    liste_communes=[]
    while True:
        rep=GestionMenu("Menu de mon application",liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep==1:
            nom_fic=input("Entrer le nom du fichier à charger : ")
            liste_communes=charger_fichier_population(nom_fic)
            print("Le fichier",nom_fic,"contient",len(liste_communes),"communes")
        elif rep==2:
            commune=input("Entrer le nom de la commune : ")
            population = GetPopulationByCity(liste_communes,commune)
            print("La commune",commune,"contient",population,"habitants")
        elif rep==3:
            search=input("Entrer les premieres lettres du nom de la commune : ")
            liste_recherche = GetCitiesBySearch(liste_communes,search)
            print("Liste des communes : ")
            for nom in liste_recherche:
                print(nom)
            print(len(liste_recherche),"communes trouvées")
        elif rep==4:
            departement=input("Entrer le département : ")
            topcity = GetBiggestCityByDpt(liste_communes,departement)
            print("La commune la plus peuplée du", departement, "est la commune : ", topcity)
        elif rep==5:
            inferieur=int(input("Borne inférieure : "))
            superieur=int(input("Borne supérieure : "))
            quantite = GetCitiesBetweenRange(liste_communes,inferieur,superieur)
            print("Il y a ", quantite, " communes entre", inferieur, "et" ,superieur, "habitants.")
        elif rep==6:
            taille_res=int(input("Entrez le nombre de communes de votre top :"))
            top=top_n_population(liste_communes,taille_res)
            print("voici le top")
            for i in range(len(top)):
                print(i+1,top[i])  
        elif rep==7:
            nom_fic = input("Entrez le nom du fichier pour la sauvegarde : ")
            poptot = GetPopTotaleByDpt(liste_communes)
            sauve_population_dpt(nom_fic,poptot)
        else:
            break
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")
    
# programme principal
main()