import syracuse

def test_Syracuse():
    assert syracuse.Syracuse(1) == [1]
    assert syracuse.Syracuse(2) == [2,1]
    assert syracuse.Syracuse(3) == [3,10,5,16,8,4,2,1]
    assert syracuse.Syracuse(5) == [5,16,8,4,2,1]
    assert syracuse.Syracuse(20) == [20, 10, 5, 16, 8, 4, 2, 1]
    assert syracuse.Syracuse(10) == [10, 5, 16, 8, 4, 2, 1]
    #assert syracuse.Syracuse(27) == [27, 82, 41, 124, 62, 31, ...]
    #assert syracuse.Syracuse(124) == [124, 62, 31,... 47, 142, ...]

def test_FlyTime():
    assert syracuse.FlyTime(27) == 111
    assert syracuse.FlyTime(3) == 7
    assert syracuse.FlyTime(5) == 5
    assert syracuse.FlyTime(10) == 6
    assert syracuse.FlyTime(124) == 108
    assert syracuse.FlyTime(20) == 7

def test_Champion():
    assert syracuse.Champion(27) == 25
    assert syracuse.Champion(5) == 3

def test_temps_de_vol_avec_precalcul():
    assert syracuse.temps_de_vol_avec_precalcul(27, {10: 6, 124: 108}) == 111
    assert syracuse.temps_de_vol_avec_precalcul(20, {10: 6, 124: 108}) == 7

def test_Champion_avec_precalcul():
    assert syracuse.Champion_avec_precalcul(27,{10: 6, 124: 108}) == 25
    assert syracuse.Champion_avec_precalcul(20,{10: 6, 124: 108}) == 18
  