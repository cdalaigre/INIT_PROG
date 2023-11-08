import super_heros

avengers = {
'Spiderman': (5 , 5 , ' araignée a quatre pattes ') ,
'Hulk': (7 , 4 , " Grand homme vert " ) ,
'Agent 13': (2 , 3 , ' agent 13 ') ,
'M Melin': (2 , 6, ' expert en archi '),
'Drax': (5,2,'Benet tatoué'),
'Gamora' : (3,4,'moutarde verte')
}

# dictionnaires bidons pour faire des tests :
exemple2 = { 'a':(1 , 1, 'a') , 'b':(3 , 9, 'b') , 'c':(7 , 2, 'c')}
exemple3 = { 'a':(1 , 1, 'a') , 'b':(3 , 9, 'b') , 'd':(4 , 4, 'd')}
no_hero = dict()

def test_intelligence_moyenne():
    assert super_heros.intelligence_moyenne (exemple2) == 4
    assert super_heros.intelligence_moyenne (exemple3) == 14/3 
    assert super_heros.intelligence_moyenne (avengers) == 4
    assert super_heros.intelligence_moyenne (no_hero) == None

def test_kikelplusfort():
    assert super_heros.kikelplusfort (exemple2) == 'c'
    assert super_heros.kikelplusfort (exemple3) == 'd' 
    assert super_heros.kikelplusfort (avengers) == 'Hulk'
    assert super_heros.kikelplusfort (no_hero) == ""

def test_combiendecretins():
    assert super_heros.combiendecretins (exemple2) == 2
    assert super_heros.combiendecretins (exemple3) == 2
    assert super_heros.combiendecretins (avengers) == 2
    assert super_heros.combiendecretins (no_hero) == 0