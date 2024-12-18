import numpy as np

cdef class Dual:
    """
    A class to implement basic operations and common functions on dual numbers.

    Attributes:
        - real (int, float): The real part of a dual number.
        - dual (int, float): The dual part of a dual number.
    """
    cdef public double real
    cdef public double dual

    def __init__(self, double real, double dual):
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
    
    def __add__(self, Dual other):
        """
        Overloads the '+' operator so that we can add dual numbers. 
        Also allows the addition of real numbers (i.e. int, float) to dual numbers on RHS.

        Returns:
            - Dual: A new dual number which is the sum of the two dual numbers.
        """
        
        return Dual(self.real + other.real, self.dual + other.dual)
    
    def __radd__(self, Dual other):
        """
        Allows the addition of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the sum of the two dual numbers.
        """
        return self.__add__(other)
    
    def __sub__(self, Dual other):
        """
        Overloads the '-' operator so that we can subtract dual numbers. 
        Also allows the subtraction of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the difference of the two dual numbers.
        """
        
        return Dual(self.real - other.real, self.dual - other.dual)
    
    def __rsub__(self, Dual other):
        """
        Allows the subtraction of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the difference of the two dual numbers.
        """
        return Dual(other-self.real, -self.dual)
    
    def __mul__(self, Dual other):
        """
        Overloads the '*' operator so that we can multiply dual numbers. 
        Also allows the multiplication of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the product of the two dual numbers.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
        return Dual(a * c, a * d + b * c)
    
    def __rmul__(self, Dual other):
        """
        Allows the mutipliation of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the product of the two dual numbers.
        """
        return self.__mul__(other)
    
    def __truediv__(self, Dual other):
        """
        Overloads the '/' operator so that we can divide dual numbers. 
        Also allows the division of real numbers (i.e. int, float) on RHS.

        Returns:
            - Dual: A new dual number which is the ratio of the two dual numbers.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
        try:
            return Dual(a / c, (b * c - a * d) / (c * c))
        except ZeroDivisionError:
            print("Divison invalid: real part of divisor is zero")
    
    def __rtruediv__(self, Dual other):
        """
        Allows the division of real numbers (i.e. int, float) to dual numbers on LHS.

        Returns:
            - Dual: A new dual number which is the ratio of the two dual numbers.
        """
        
        return other.__truediv__(self)
    
    def __pow__(self, Dual other):
        """
        Overloads the '**' operator so that we can raise dual numbers to a (int, float, Dual) exponent. 
        Note that if the exponent is an instance of the Dual class, the dual part of the exponent must be zero, otherwise an error is raised.
        
        Returns:
            - Dual: A dual number raised to an exponent.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double n=other.real
        if other.dual==0:
            return Dual(a ** n, n * b * a ** (n-1))
        else:
            print("Power invalid: dual part of exponent must be zero")
            raise ValueError()
            
    

    # Operate-and-Assign Operators

    def __iadd__(self, Dual other):
        """
        Overloads the '+=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been added to it.
        """
        
        self = Dual(self.real + other.real, self.dual + other.dual)
        return self
    
    def __isub__(self, Dual other):
        """
        Overloads the '-=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been subtracted from it.
        """
        
        self = Dual(self.real - other.real, self.dual - other.dual)
        return self

    def __imul__(self, Dual other):
        """
        Overloads the '*=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after another number (int, float or Dual) has been multiplied to it.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
        self = Dual(a * c, a * d + b * c)
        return self
    
    def __idiv__(self, Dual other):
        """
        Overloads the '/=' operator so that it also works with dual numbers.

        Returns:
            - Dual: The updated dual number after it has been divided by another number (int, float or Dual).
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
        try:
            self = Dual(a / c, (b * c - a * d) / (c * c))
            return self
        except ZeroDivisionError:
            print("Divison invalid: real part of divisor is zero")
        

    # Comparison Operators

    def __eq__(self, Dual other):
        """
        Overloads the '==' operator so that it also works with dual numbers.

        Returns:
            - bool: True if the two dual numbers are equal (i.e. if both the real and dual parts are equal), otherwise returns False.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
        if (a==c) & (b==d):
            return True
        else:
            return False
    
    def __ne__(self, Dual other):
        """
        Overloads the '!=' operator so that it also works with dual numbers.

        Returns:
            - bool: True if the two dual numbers are not equal (i.e. if either the real or dual parts are not equal), otherwise returns False.
        """
        
        cdef double a=self.real
        cdef double b=self.dual
        cdef double c=other.real
        cdef double d=other.dual
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
        cdef double a=self.real
        cdef double b=self.dual
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
        cdef double a=self.real
        cdef double b=self.dual
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
        cdef double a=self.real
        cdef double b=self.dual
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
        cdef double a=self.real
        cdef double b=self.dual
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
        cdef double a=self.real
        cdef double b=self.dual
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
        cdef double a=self.real
        cdef double b=self.dual
        return Dual(np.exp(a), b * np.exp(a))




        
    

    
    

    