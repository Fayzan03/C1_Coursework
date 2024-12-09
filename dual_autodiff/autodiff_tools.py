import numpy as np
from .dual import Dual

def sin(self):
    """
    Applies the trigonometric function 'sine' to a dual number.
    
    Returns:
        - Dual: A new dual number which is the sine of the dual number.

    Example:
        >>> x = Dual(2, 1)
        >>> x.sin()
        Dual(real=0.9092974268256817, dual=-0.4161468365471424)
    """
    a=self.real
    b=self.dual
    return Dual(np.sin(a), b * np.cos(a))

def cos(self):
    """
    Applies the trigonometric function 'cosine' to a dual number.
    
    Returns:
        - Dual: A new dual number which is the cosine of the dual number.
    
    Example:
        >>> x = Dual(2, 1)
        >>> x.cos()
        Dual(real=-0.4161468365471424, dual=-0.9092974268256817)
    """
    a=self.real
    b=self.dual
    return Dual(np.cos(a), - b * np.sin(a))

def tan(self):
    """
    Applies the trigonometric function 'tangent (tan)' to a dual number.
    
    Returns:
        - Dual: A new dual number which is the tangent of the dual number.
    
    Example:
        >>> x = Dual(2, 1)
        >>> x.tan()
        Dual(real=-2.185039863261519, dual=5.774399204041917)
    """
    a=self.real
    b=self.dual
    return Dual(np.tan(a), b / (np.cos(a) ** 2))

def log(self):
    """
    Applies the natural logarithm to a dual number.

    Returns:
        - Dual: A new dual number which is the natural logarithm of the dual number.
    
    Example:
        >>> x = Dual(2, 1)
        >>> x.log()
        Dual(real=0.6931471805599453, dual=0.5)
    """
    a=self.real
    b=self.dual
    try:
        return Dual(np.log(a), b / a)
    except ZeroDivisionError:
        print("Logarithm invalid: real part of dual number is zero")   

def exp(self):
    """
    Applies the exponential function to a dual number.

    Returns:
        - Dual: A new dual number which is the exponential of the dual number.

    Example:
        >>> x = Dual(2, 1)
        >>> x.exp()
        Dual(real=7.38905609893065, dual=7.38905609893065)
    """
    a=self.real
    b=self.dual
    return Dual(np.exp(a), b * np.exp(a))