def BooleanListInitialize(N):
    res=[]
    for i in range (0,N+1):
        if i==0 or i==1:
            res.append(False)
        else:
            res.append(True)
    
    return res

def test_BooleanListInitialize():
    assert BooleanListInitialize(5)==[False,False,True,True,True,True]
    assert BooleanListInitialize(6)==[False,False,True,True,True,True,True]

def SetToFalseInListMutlipleOfX(liste, x):
    for i in range (2,len(liste)):
        if (i != x) and (i % x == 0):
            liste[i]= False

    return liste

def test_SetToFalseInListMutlipleOfX():
    assert SetToFalseInListMutlipleOfX(BooleanListInitialize(5),2)==[False,False,True,True,False,True]
    assert SetToFalseInListMutlipleOfX(BooleanListInitialize(6),2)==[False,False,True,True,False,True,False]

def Crible(N):
    liste = BooleanListInitialize(N)
    res=[]
    for i in range(2, len(liste)):
        if liste[i] == True:
            res.append(i)
            liste = SetToFalseInListMutlipleOfX(liste,i)

    return res

def test_Crible():
    assert Crible(6)==[2,3,5]
    assert Crible(25)==[2,3,5,7,11,13,17,19,23]
    assert Crible(100)==[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]