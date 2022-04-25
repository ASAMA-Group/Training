import operation

def test_add():
    assert operation.add(2,3) == 5
    assert operation.add(-2,-3) == -5
    assert operation.add(0,-3) == -3



def test_sub():
    assert operation.sub(2,3) == -1
    assert operation.sub(-2,-3) == 1
    assert operation.sub(0,-3) == 3



def test_div():
    assert operation.div(6,3) == 2
    assert operation.div(-6,-3) == 2
    assert operation.div(0,-3) == 0