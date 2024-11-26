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
        res = Dual(self.real + other.real, self.dual + other.dual)
        return res
    
    def __radd__(self, other):
        return self.__add__(other)
    
    # Overload the '-' operator 
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        res = Dual(self.real - other.real, self.dual - other.dual)
        return res
    
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
        res = Dual(a * c, a * d + b * c)
        return res
    
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
            res = Dual(a / c, (b * c - a * d) / c**2)
            return res
        except ZeroDivisionError:
            print("Divison invalid: c is (too close to) zero")
    
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    # Overload the '**' operator (for zero dual part only)   
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            other = Dual(other,0)
        a=self.real
        b=self.dual
        n=other.real
        if other.dual==0:
            res = Dual(a ** n, n * b * a ** (n-1))
            return res
        else:
            raise ValueError("Invalid exponentiation: dual part must be zero")
    

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
        if c > 1e-9:
            self = Dual(a / c, (b * c - a * d) / c**2)
            return self
        else:
            raise ValueError("Divison invalid: c is (too close to) zero")
        

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
        if a > 1e-9:
            res = Dual(1 / a, - b / a**2)
            return res
        else:
            raise ValueError("Inversion invalid: a is (too close to) zero")
        
    def __neg__(self):
        res = Dual(-self.real, -self.dual)
        return res
    
    def __pos__(self):
        return self

    # Other essential functions:

    # sine
    def sin(self):
        a=self.real
        b=self.dual
        res=Dual(np.sin(a), b * np.cos(a))
        return res

    # cosine
    def cos(self):
        a=self.real
        b=self.dual
        res=Dual(np.cos(a), - b * np.sin(a))
        return res
    
    # tangent (maybe add condition near poles)
    def tan(self):
        a=self.real
        b=self.dual
        res=Dual(np.tan(a), b / (np.cos(a) ** 2))
        return res
    
    # natural logarithm
    def log(self):
        a=self.real
        b=self.dual
        if a > 1e-9:
            res=Dual(np.log(a), b / a)
            return res
        else:
            raise ValueError("Inversion invalid: a is (too close to) zero")   
    
    # exp
    def exp(self):
        a=self.real
        b=self.dual
        res=Dual(np.exp(a), b * np.exp(a))
        return res

        
    

    
    

    