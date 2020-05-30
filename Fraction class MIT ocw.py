# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:52:16 2020

@author: Oluseyi Oshin
"""

class Fraction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__ (self, other):      # Adds the fractio to another fraction.
        denominator = self.y * other.y
        numerator = int(((denominator/other.y) * other.x) + ((denominator/self.y) * self.x))
        return Fraction(numerator , denominator)
    
    def __sub__ (self, other):      # subtracts the fraction from another fraction
        denominator = self.y * other.y
        numerator = int(((denominator/self.y) * self.x) - ((denominator/other.y) * other.x))
        return Fraction(numerator , denominator)
    
    def __str__ (self):             #Prints the fraction.
        return str(self.x) + "/" + str(self.y)
    
    def Flt(self):                  # Converts the fraction to floats
        return self.x / self.y
    
    def invt(self):
        def __init__(self, y, x):
           self.x = y
           self.y = x
        return 
m = Fraction(1,3)   
l = Fraction(2, 3)
print(l.x)
print(l.y)


print(l + m)
print(l - m)
print(m)
print(l)

print(m.Flt())        