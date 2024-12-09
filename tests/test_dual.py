# tests/test_dual.py

import pytest
from dual_autodiff.dual import Dual
import numpy as np

def test_init():
    x=Dual(real=-1/3, dual=1)
    assert x.real == -1/3
    assert x.dual == 1

class TestComponents:
    def test_real(self):
        x=Dual(2,1)
        assert x.re() == 2

    def test_dual(self):
        x=Dual(2,1)
        assert x.du() == 1

def test_repr(capsys):
    x=Dual(2,1)
    print(x)
    captured=capsys.readouterr()
    assert captured.out == "Dual(real=2, dual=1)\n"

class TestBasicArithmetic:
    def test_add(self):
        # Check floats, negative numbers
        assert Dual(2,1.3)+Dual(-3.5,4.8) == Dual(-1.5,6.1)
        # Check adding nothing works
        assert Dual(2,1) + Dual(0,0) == Dual(2, 1)
        # Check adding 'conjugates' works
        assert Dual(2,1) + Dual(2,-1) == Dual(4,0)
        # Dual + Real
        assert Dual(2,1) + 2 == Dual(4,1)
        # Real + Dual
        assert 2 + Dual(2,1) == Dual(4,1)
        # Real + Real == Dual with no dual part
        assert 2 + 3 == Dual(5,0)

    def test_sub(self):
        assert Dual(2,1.3) -Dual(-3.5,4.8) == Dual(5.5,-3.5)
        assert Dual(2,1) - Dual(0,0) == Dual(2, 1)
        assert Dual(2,1) - Dual(2,-1) == Dual(0,2)
        assert Dual(2,1) - 4 == Dual(-2,1)
        assert 4 - Dual(2,1) == Dual(2,-1)
        assert 2 - 3 == Dual(-1,0)

    def test_mul(self):
        assert Dual(2,1.3) * Dual(-3.5,4.8) == Dual(-7.0,5.05)
        assert Dual(2,1) * Dual(0,0) == Dual(0,0)
        assert Dual(2,1) * Dual(2,-1) == Dual(4,0)
        assert Dual(2,1) * 4 == Dual(8,4)
        assert 4 * Dual(2,1) == Dual(8,4)
        assert 2 * 3 == Dual(6,0)

    def test_div(self, capsys):
        # Some rounding error from division so we have to approximate the result here
        assert Dual(2,1.3) / Dual(-3.5,4.8) == Dual(-4/7, pytest.approx(-283/245, rel=1e-9))
        assert Dual(2,1) / Dual(2,-1) == Dual(1,1)
        assert Dual(2,1) / 4 == Dual(0.5,0.25)
        assert 4 / Dual(2,1) == Dual(2,-1)
        assert 2 / 3 == Dual(2/3,0)
        # Check division by zero
        Dual(2,1) / Dual(0,0)
        captured = capsys.readouterr()
        assert "Divison invalid: real part of divisor is zero" in captured.out
        
    def test_pow(self, capsys):
        assert Dual(2,1) ** 10 == Dual(1024,5120)
        assert Dual(2,1) ** 0 == Dual(1,0)
        assert Dual(2,1) ** 1 == Dual(2,1)
        assert Dual(2,1) ** Dual(2,0) == Dual(4,4)
        with pytest.raises(ValueError):
            Dual(2,1) ** Dual(2,1)
            captured = capsys.readouterr()
            assert "Power invalid: dual part of exponent must be zero" in captured.out

class TestAssignmentOperators:
    def test_iadd(self):
        x = Dual(2,1)
        x += Dual(2,1)
        assert x == Dual(4,2)
        x += 2
        assert x == Dual(6,2)

    def test_isub(self):
        x = Dual(2,1)
        x -= Dual(2,1)
        assert x == Dual(0,0)
        x -= 2
        assert x == Dual(-2,0)

    def test_imul(self):
        x = Dual(2,1)
        x *= Dual(3,4)
        assert x == Dual(6,11)
        x *= 2
        assert x == Dual(12,22)

    def test_idiv(self, capsys):
        x = Dual(2,1)
        x /= Dual(3,4)
        assert x == Dual(pytest.approx(2/3, rel=1e-9), pytest.approx(-5/9, rel=1e-9))
        x /= 2
        assert x == Dual(1/3, -5/18)
        x /= Dual(0,0)
        captured = capsys.readouterr()
        assert "Divison invalid: real part of divisor is zero" in captured.out
    
class TestComparisonOperators:
    def test_eq(self):
        assert Dual(2,1) == Dual(2,1)
        assert 2 == Dual(2,0)
        assert Dual(2,0) == 2

    def test_ne(self):
        assert Dual(2,1) != Dual(2,0)
        assert 3 != Dual(2,0)
        assert Dual(2,0) != 3

class TestUnaryOperators:
    def test_invert(self, capsys):
        assert ~Dual(2,1) == Dual(0.5,-0.25)
        ~Dual(0,1)
        captured=capsys.readouterr()
        assert "Inversion invalid: real part of dual number is zero" in captured.out

    def test_neg(self):
        assert -Dual(2,1) == Dual(-2,-1)
        assert -Dual(2,-1) == Dual(-2,1)
        assert -Dual(2,0) == Dual(-2,0)

    def test_pos(self):
        assert +Dual(2,-1) == Dual(2,-1)
        assert +Dual(2,0) == Dual(2,0)
