import numpy as np

class Dual:
    def __init__(self, real, dual):
        self.real=real # Real part of dual number
        self.dual=dual # Dual part of dual number

    # Return real part of dual number
    def re(self):
        return self.real
    
    # Return dual part of a dual number
    def du(self):
        return self.dual
         
    # Overrides output so we get a dual number displayed in a nice format
    def __repr__(self):
        return f"Dual(real={self.real}, dual={self.dual})" 
    

    # Arithmetic Operators

    # Overload the '+' operator 
    def __add__(self, other):
        # Allow addition of real numbers on RHS
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return Dual(self.real + other.real, self.dual + other.dual)
    
    # Include addition of reals on the LHS
    def __radd__(self, other):
        return self.__add__(other)
    
    # Overload the '-' operator 
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return Dual(self.real - other.real, self.dual - other.dual)
    
    def __rsub__(self, other):
        return Dual(other-self.real, -self.dual)
    
    # Overload the '*' operator 
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        return Dual(a * c, a * d + b * c)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    # Overload the '/' operator 
    def __truediv__(self, other):
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
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        return other.__truediv__(self)
    
    # Overload the '**' operator (for zero dual part only)   
    def __pow__(self, other):
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

    # Overload the '+=' operator
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        self = Dual(self.real + other.real, self.dual + other.dual)
        return self
    
    # Overload the '-=' operator 
    def __isub__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        self = Dual(self.real - other.real, self.dual - other.dual)
        return self

    # Overload the '*=' operator 
    def __imul__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        self = Dual(a * c, a * d + b * c)
        return self
    
    # Overload the '/=' operator 
    def __idiv__(self, other):
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

    # Overload the '==' operator
    def __eq__(self, other):
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
    
    # Overload the '!=' operator
    def __ne__(self, other):
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
        a=self.real
        b=self.dual
        try:
            return Dual(1 / a, - b / a**2)
        except ZeroDivisionError:
            print("Inversion invalid: real part of dual number is zero")
        
    def __neg__(self):
        return Dual(-self.real, -self.dual)
        
    def __pos__(self):
        return self

    # Other essential functions:

    # sine
    def sin(self):
        a=self.real
        b=self.dual
        return Dual(np.sin(a), b * np.cos(a))

    # cosine
    def cos(self):
        a=self.real
        b=self.dual
        return Dual(np.cos(a), - b * np.sin(a))
    
    # tangent (maybe add condition near poles)
    def tan(self):
        a=self.real
        b=self.dual
        return Dual(np.tan(a), b / (np.cos(a) ** 2))
    
    # natural logarithm
    def log(self):
        a=self.real
        b=self.dual
        try:
            return Dual(np.log(a), b / a)
        except ZeroDivisionError:
            print("Logarithm invalid: real part of dual number is zero")   
    
    # exp
    def exp(self):
        a=self.real
        b=self.dual
        return Dual(np.exp(a), b * np.exp(a))

        
    

    
    

    