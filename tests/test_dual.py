# tests/test_dual.py

import pytest
from dual_autodiff.dual import Dual

def test_init():
    x=Dual(real=-1/3, dual=1)
    assert x.real == -1/3
    assert x.dual == 1

def test_real():
    x=Dual(2,1)
    assert x.re() == 2

def test_dual():
    x=Dual(2,1)
    assert x.du() == 1

# Might need to change this
def test_str(capsys):
    x=Dual(2,1)
    print(x)
    captured=capsys.readouterr()
    assert captured.out == "Dual(real=2, dual=1)\n"

def test_add():
    assert Dual(2,1.3)+Dual(-3.5,4.8) == Dual(-1.5, 6.1)
    assert Dual(2,1) + Dual(0,0) == Dual(2, 1)
    assert Dual(2,1) + Dual(2,-1) == Dual(4,0)
    assert Dual(2,1) + 2 == Dual(4,1)
    assert 2 + Dual(2,1) == Dual(4,1)
    assert 2 + 2 == Dual(4,0)

def test_sub():
    assert Dual(2,1.3) -Dual(-3.5,4.8) == Dual(5.5, -3.5)
    assert Dual(2,1) - Dual(0,0) == Dual(2, 1)
    assert Dual(2,1) - Dual(2,-1) == Dual(0,2)
    assert Dual(2,1) - 4 == Dual(-2,1)
    assert 4 - Dual(2,1) == Dual(2,-1)
    assert 2 - 2 == Dual(0,0)

def test_mul(capsys):
    x=Dual(2,1.3)
    y=Dual(-3.5,4.8)
    print(x-y)
    captured=capsys.readouterr()
    assert captured.out == "Dual(real=5.5, dual=-3.5)\n"
