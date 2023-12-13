import amoureux

ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida',
'Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri',
'Gaston':'Beatrice','Henri':'Firmin'}

def test_getCoupleAmourReciproque():
    assert amoureux.getCoupleAmourReciproque(ATM)== {'Cesar':'Dalida', 'Firmin':'Henri'} 


def test_getSoupirants():
    assert amoureux.getSoupirants(ATM,'Beatrice')=={'Armand', 'Etienne', 'Gaston' }
    assert amoureux.getSoupirants(ATM,'Cesar')=={'Beatrice', 'Dalida'}
    assert amoureux.getSoupirants(ATM,'Dalida')=={'Cesar'}
    assert amoureux.getSoupirants(ATM,'Henri')=={'Firmin'}
    assert amoureux.getSoupirants(ATM,'Firmin')=={'Henri'}