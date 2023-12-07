
def getNbParticipant(weekend):
    """_summary_

    Args:
        weekend (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return len(weekend)

def getTotalByPerson(weekend):
    TotalByPerson = dict()
    for Participant, listeDépenses in weekend.items():
        total = 0
        for uneDépense in listeDépenses:
            total += uneDépense
        TotalByPerson[Participant]=total
    
    return TotalByPerson

def getTotalDepenses(total_by_person):
    facture = 0
    for Dépense in total_by_person.values(): 
        facture += Dépense
    
    return facture

def getCalculRépartition(weekend):

    CalculRépartition = dict()
    NbParticpant = getNbParticipant(weekend)
    DepensesParParticipant = getTotalByPerson(weekend)
    Facture = getTotalDepenses(DepensesParParticipant)

    BilanParParticipant = Facture / NbParticpant

    for Participant, TotalPayé in DepensesParParticipant.items():
        if (TotalPayé >= BilanParParticipant): PayerOuRecevoir = ('recevoir', TotalPayé-BilanParParticipant)
        if (TotalPayé <= BilanParParticipant): PayerOuRecevoir = ('verser', BilanParParticipant-TotalPayé)
        CalculRépartition[Participant]=PayerOuRecevoir
    
    return CalculRépartition

def affiche_bilan_financier(weekend):

    calcul = getCalculRépartition(weekend)
    for Participant, bilan in calcul.items():
        print (Participant + " doit " + bilan[0] + " " + str(bilan[1])+ " euros.")



