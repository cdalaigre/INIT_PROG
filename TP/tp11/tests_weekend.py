import weekend

weekend_mai={ 'Pierre': [12,70,10], 'Paul':[100], 'Marie': [15], 'Anna': [0] }
weekend_juin={ 'Pierre':[15,12,8,3], 'Marie':[20,34], 'Anna' : [52], 'Beatrice': [8], 'Sasha':[0]}

def test_getNbParticipant():
    assert weekend.getNbParticipant(weekend_mai)==4
    assert weekend.getNbParticipant(weekend_juin)==5

def test_getTotalByPerson():
    assert weekend.getTotalByPerson(weekend_mai)== { 'Pierre': 92, 'Paul':100, 'Marie': 15, 'Anna': 0 }
    assert weekend.getTotalByPerson(weekend_juin)== { 'Pierre': 38, 'Marie':54, 'Beatrice': 8, 'Anna': 52, 'Sasha':0 }

def test_getTotalDepenses():
    assert weekend.getTotalDepenses(weekend.getTotalByPerson(weekend_mai))==207
    assert weekend.getTotalDepenses(weekend.getTotalByPerson(weekend_juin))== 152

def test_getCalculRépartition():
    assert weekend.getCalculRépartition(weekend_mai)=={ 'Pierre': ('recevoir',40.25), 'Paul':('recevoir',48.25), 'Marie': ('verser', 36.75), 'Anna': ('verser',51.75) }

weekend.affiche_bilan_financier(weekend_mai)
weekend.affiche_bilan_financier(weekend_juin)