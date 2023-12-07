
def getNbParticipant(weekend):
    """Détermine le nombre de participant

    Args:
        weekend (dict): dictionnaire dont la clé est le participant et la valeur la liste des achats

    Returns:
        int: nombre de participants (clés)
    """    
    return len(weekend)

def getTotalByPerson(weekend):
    """Détermine le total de dépenses par personne

    Args:
        weekend (dict): dictionnaire dont la clé est le participant et la valeur la liste des achats

    Returns:
        dict: dictionnaire dont la clé est le participant et la valeur le total de ses achats
    """    
    TotalByPerson = dict()
    for Participant, listeDépenses in weekend.items():
        total = 0
        for uneDépense in listeDépenses:
            total += uneDépense
        TotalByPerson[Participant]=total
    
    return TotalByPerson

def getTotalDepenses(total_by_person):
    """Détermine le total de la facture

    Args:
        total_by_person (dict): dictionnaire dont la clé est le participant et la valeur le total de ses achats

    Returns:
        int: total de la facture
    """    
    facture = 0
    for Dépense in total_by_person.values(): 
        facture += Dépense
    
    return facture

def getCalculRépartition(NbParticipant, DepensesParParticipant, Facture):
    """Détermine le montant qu'une personne doit payer ou recevoir

    Args:
        NbParticipant (int): nombre de participants
        DepensesParParticipant (dict): dictionnaire dont la clé est le participant et la valeur le total de ses achats
        Facture (int): total de la facture

    Returns:
        dict: dictionnaire dont la clé est le participant et la valeur est un tuple (action, montant)
    """    
    CalculRépartition = dict()
    
    BilanParParticipant = Facture / NbParticipant

    for Participant, TotalPayé in DepensesParParticipant.items():
        if (TotalPayé >= BilanParParticipant): PayerOuRecevoir = ('recevoir', TotalPayé-BilanParParticipant)
        if (TotalPayé <= BilanParParticipant): PayerOuRecevoir = ('verser', BilanParParticipant-TotalPayé)
        CalculRépartition[Participant]=PayerOuRecevoir
    
    return CalculRépartition

def affiche_bilan_financier(weekend):
    """Affiche le bilan financier

    Args:
        weekend (dict): dictionnaire dont la clé est le participant et la valeur la liste des achats
    """    

    NbParticipant = getNbParticipant(weekend)
    DepensesParParticipant = getTotalByPerson(weekend)
    Facture = getTotalDepenses(DepensesParParticipant)
    calcul = getCalculRépartition(NbParticipant, DepensesParParticipant, Facture)
    for Participant, bilan in calcul.items():
        print (Participant + " doit " + bilan[0] + " " + str(bilan[1])+ " euros.")



