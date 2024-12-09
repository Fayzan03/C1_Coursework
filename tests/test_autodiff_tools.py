# tests/test_dual.py

import pytest
from src/dual_autodiff_x.dual import Dual
import numpy as np

class TestEssentialFunctions:
    def test_sin(self):
        x=Dual(np.pi/2,np.pi)
        assert x.sin() == Dual(pytest.approx(1, rel=1e-9), pytest.approx(0, rel=1e-9))

    def test_cos(self):
        x=Dual(np.pi/2,np.pi)
        assert x.cos() == Dual(pytest.approx(0, rel=1e-9), pytest.approx(-np.pi, rel=1e-9))

    def test_tan(self):
        x=Dual(np.pi/4,np.pi)
        assert x.tan() == Dual(pytest.approx(1, rel=1e-9), pytest.approx(2*np.pi, rel=1e-9))
        y=Dual(np.pi/2,1)
        assert y.tan() == Dual(pytest.approx(np.tan(np.pi/2), rel=1e-9), pytest.approx(1/np.cos(np.pi/2)**2, rel=1e-9))
    
    def test_log(self, capsys):
        x=Dual(2,1)
        assert x.log() == Dual(pytest.approx(np.log(2), rel=1e-9), 0.5)
        y=Dual(0,1)
        with pytest.warns(RuntimeWarning):
            y.log()
        captured = capsys.readouterr()
        assert "Logarithm invalid: real part of dual number is zero" in captured.out
        with pytest.warns(RuntimeWarning):
            Dual(-1,1).log()

    def test_exp(self):
        x=Dual(0,1)
        assert x.exp() == Dual(1,1)