def getCoupleAmourReciproque(amoureux):
    liste_couple_amoureux_reciproque=dict()

    for amoureux1,amoureux2 in amoureux.items():
        if amoureux2 in amoureux.keys() and amoureux[amoureux2]==amoureux1 and amoureux2 not in liste_couple_amoureux_reciproque.keys():
            liste_couple_amoureux_reciproque[amoureux1]=amoureux2
    
    return liste_couple_amoureux_reciproque

def getSoupirants(amoureux, personne):
    soupirants = set()

    for soupirant, crush in amoureux.items():
        if crush == personne: 
            soupirants.add(soupirant)
    
    return soupirants


