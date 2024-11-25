import numpy as np

class Dual:
    def __init__(self, real, dual):
        self.real=real # Real part of dual number
        self.dual=dual # Dual part of dual number

    # Return real part of dual number
    def real(self):
        return self.real
    
    # Return dual part of a dual number
    def dual(self):
        return self.dual
        
    # Overrides print statements so we get a dual number printed in a nice format
    def __str__(self):
        return "Dual(real={0}, dual={1})".format(self.real, self.dual)
    

    # Arithmetic Operators

    # Overload the '+' operator 
    def __add__(self, other):
        res = Dual(self.real + other.real, self.dual + other.dual)
        return res
    
    # Overload the '-' operator 
    def __sub__(self, other):
        res = Dual(self.real - other.real, self.dual - other.dual)
        return res
    
    # Overload the '*' operator 
    def __mul__(self, other):
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        res = Dual(a * c, a * d + b * c)
        return res
    
    # Overload the '/' operator 
    def __truediv__(self, other):
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        if c > 1e-9:
            res = Dual(a / c, (b * c - a * d) / c**2)
            return res
        else:
            raise ValueError("Divison invalid: c is (too close to) zero")
        
    # Overload the '**' operator (for zero dual part only)   
    def __pow__(self, other):
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
        self = Dual(self.real + other.real, self.dual + other.dual)
        return self
    
    # Overload the '-=' operator 
    def __isub__(self, other):
        self = Dual(self.real - other.real, self.dual - other.dual)
        return self

    # Overload the '*=' operator 
    def __imul__(self, other):
        a=self.real
        b=self.dual
        c=other.real
        d=other.dual
        self = Dual(a * c, a * d + b * c)
        return self
    
    # Overload the '/' operator 
    def __idiv__(self, other):
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
        res=Dual(np.sin(self.real), np.sin(self.dual))
        return res

    # cosine
    def cos(self):
        res=Dual(np.cos(self.real), np.cos(self.dual))
        return res
    
    # tangent
    def tan(self):
        res=Dual(np.tan(self.real), np.tan(self.dual))
        return res
    
    # natural logarithm
    def log(self):
        res=Dual(np.log(self.real), np.log(self.dual))
        return res
    
    # exp
    def exp(self):
        res=Dual(np.exp(self.real), np.exp(self.dual))
        return res

        
    

    
    

    