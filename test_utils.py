import utils

def test_fact():
    assert utils.fact(-1) == False
    assert utils.fact(1) == 1
    assert utils.fact(4) == 24
    assert utils.fact(10) == 3628800
    assert utils.fact(0) == 1

def test_roots():
	assert utils.roots(1, 1, 1) == ()
	assert utils.roots(1, 2, 1) == (-1)
	assert utils.roots(1, -6, 2) == (5.646, 0.354)

def test_integrate():
	assert utils.integrate("1", 0, 1) == 1 
	assert utils.integrate("cos(x)", 0, 1) == 0.8414709848078966
	assert utils.integrate("x**2+4*x+6", 0, 1) == 8.333333333333334
	