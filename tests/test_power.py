from src.power import power

def test_power():
    assert power(2,3) == 8
    assert power(5,2) == 25
    assert power(10,0) == 1