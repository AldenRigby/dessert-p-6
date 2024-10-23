from potato import (
    add,
    sub,
    mul,
    div
)

def test_add():
    assert add(2, 10) == 12
    assert add(5, 0) == 5
    assert add(100, 21) == 121

def test_sub():
    assert sub(10, 0) == 10
    assert sub(5, 0) == 5
    assert sub(100, 21) == 79

def test_mul():
    assert mul(2, 10) == 20
    assert mul(5, 0) == 0
    assert mul(100, 21) == 2100

def test_div():
    assert div(2, 10) == 0.2
    assert div(5, 0) == None
    assert div(100, 10) == 10