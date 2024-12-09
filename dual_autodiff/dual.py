import numpy as np

class Dual:
    """
    A class to implement basic operations and common functions on dual numbers.

    Attributes:
        - real (int, float): The real part of a dual number.
        - dual (int, float): The dual part of a dual number.
    """

    def __init__(self, real, dual):
        """
        Initialises an instance of the dual class with a dual number consisting of a real part and dual part.

        Parameters:
            - real (int, float): real part.
            - dual (int, float): dual part.
        """
        self.real=real
        self.dual=dual

    
    def re(self):
        """
        Returns the real part of dual number.

        Returns:
            - int, float: The real part of a dual number.
        """
        return self.real
    
    def du(self):
        """
        Returns the dual part of dual number.

        Returns:
            - int, float: The dual part of a dual number.
        """
        return self.dual
         
    def __repr__(self):
        """
        Defines the string representation of a dual number so that it is displayed in a nice format.

        Returns:
            - str: A string of the form 'Dual(real= , dual= )'.
        """
        return f"Dual(real={self.real}, dual={self.dual})" 
    

    # Arithmetic Operators
    
    def __add__(self, other):
        """
        Overloads the '+' operator so that we can add dual numbers. 
        Also allows the addition of real numbers (i.e. int, float) to dual numbers on RHS.

        Returns:
            - Dual: A new dual number which is the sum of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return Dual(self.real + other.real, self.dual + other.dual)
    
    def __radd__(self, other):
        """
        Allows the addition of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the sum of the two dual numbers.
        """
        return self.__add__(other)
    
    def __sub__(self, other):
        """
        Overloads the '-' operator so that we can subtract dual numbers. 
        Also allows the subtraction of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the difference of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return Dual(self.real - other.real, self.dual - other.dual)
    
    def __rsub__(self, other):
        """
        Allows the subtraction of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the difference of the two dual numbers.
        """
        return Dual(other-self.real, -self.dual)
    
    def __mul__(self, other):
        """
        Overloads the '*' operator so that we can multiply dual numbers. 
        Also allows the multiplication of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the product of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        return Dual(a * c, a * d + b * c)
    
    def __rmul__(self, other):
        """
        Allows the mutipliation of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the product of the two dual numbers.
        """
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """
        Overloads the '/' operator so that we can divide dual numbers. 
        Also allows the division of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the ratio of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        try:
            return Dual(a / c, (b * c - a * d) / (c * c))
        except ZeroDivisionError:
            print("Divison invalid: real part of divisor is zero")
    
    def __rtruediv__(self, other):
        """
        Allows the division of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the ratio of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return other.__truediv__(self)
    
    def __pow__(self, other):
        """
        Overloads the '**' operator so that we can raise dual numbers to a (int, float, Dual) exponent. 
        Note that if the exponent is an instance of the Dual class, the dual part of the exponent must be zero, otherwise an error is raised.
        
        Returns:
            - Dual: A new dual number which is the difference of the two dual numbers.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        n=other.real
        if other.dual==0:
            return Dual(a ** n, n * b * a ** (n-1))
        else:
            print("Power invalid: dual part of exponent must be zero")
            raise ValueError()
            
    

    # Operate-and-Assign Operators

    def __iadd__(self, other):
        """
        Overloads the '+=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been added to it.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        self = Dual(self.real + other.real, self.dual + other.dual)
        return self
    
    def __isub__(self, other):
        """
        Overloads the '-=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been subtracted from it.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        self = Dual(self.real - other.real, self.dual - other.dual)
        return self

    def __imul__(self, other):
        """
        Overloads the '*=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been multiplied to it.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        self = Dual(a * c, a * d + b * c)
        return self
    
    def __idiv__(self, other):
        """
        Overloads the '/=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after it has been divided by another number (int, float or Dual).
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        try:
            self = Dual(a / c, (b * c - a * d) / (c * c))
            return self
        except ZeroDivisionError:
            print("Divison invalid: real part of divisor is zero")
        

    # Comparison Operators

    def __eq__(self, other):
        """
        Overloads the '==' operator so that it also works with dual numbers.

        Returns:
            - bool: True if the two dual numbers are equal (i.e. if both the real and dual parts are equal), otherwise returns False.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        if (a==c) & (b==d):
            return True
        else:
            return False
    
    def __ne__(self, other):
        """
        Overloads the '!=' operator so that it also works with dual numbers.

        Returns:
            - bool: True if the two dual numbers are not equal (i.e. if either the real or dual parts are not equal), otherwise returns False.
        """
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        if (a!=c) or (b!=d):
            return True
        else:
            return False    
        

    # Unary operators 

    def __invert__(self):
        """
        Overloads the '~' (inversion) operator so that it also works with dual numbers.

        Returns:
            - Dual: The inverse of the dual number.
        """
        a=self.real
        b=self.dual
        try:
            return Dual(1 / a, - b / a**2)
        except ZeroDivisionError:
            print("Inversion invalid: real part of dual number is zero")
        
    def __neg__(self):
        """ Returns the negative of a dual number. """
        return Dual(-self.real, -self.dual)
        
    def __pos__(self):
        """ Returns the positive of a dual number. """
        return self

# Other essential functions:

from .autodiff_tools import sin, cos, tan, log, exp

Dual.sin = sin
Dual.cos = cos
Dual.tan = tan
Dual.log = log
Dual.exp = exp




        
    

    
    

    