
def getNbParticipant(weekend):
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

def getCalculRépartition(NbParticipant, DepensesParParticipant, Facture):

    CalculRépartition = dict()
    
    BilanParParticipant = Facture / NbParticipant

    for Participant, TotalPayé in DepensesParParticipant.items():
        if (TotalPayé >= BilanParParticipant): PayerOuRecevoir = ('recevoir', TotalPayé-BilanParParticipant)
        if (TotalPayé <= BilanParParticipant): PayerOuRecevoir = ('verser', BilanParParticipant-TotalPayé)
        CalculRépartition[Participant]=PayerOuRecevoir
    
    return CalculRépartition

def affiche_bilan_financier(weekend):

    NbParticipant = getNbParticipant(weekend)
    DepensesParParticipant = getTotalByPerson(weekend)
    Facture = getTotalDepenses(DepensesParParticipant)
    calcul = getCalculRépartition(NbParticipant, DepensesParParticipant, Facture)
    for Participant, bilan in calcul.items():
        print (Participant + " doit " + bilan[0] + " " + str(bilan[1])+ " euros.")



