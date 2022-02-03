"""CS 108 - Lab 8.1

This module implements a Fraction class for simple fraction calculations.

@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

import math # math gadget is need for gcd calculation. 

class Fraction:
    """ Constructs a class name Fraction """
    
    def __init__(self, numerator, denominator):
        """ Constructs a method with the given attributes"""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    def __str__(self):
        """ Constructs a method that would return attributes into a string"""
        return ("{}/{}".format(self.numerator, self.denominator)) # the turns the fraction into a string

    def is_valid (self):
        """Constructs a method so that attribute denominator returns false when it is equal to 0 """
        if self.denominator == 0: # if- else statement defines False if the denominator is 0
                                  # becaues 0 as a denominator is not definied in math.
            return False
        else:
            return True
    def simplify(self):
        """Constructs a method that simplifies the fraction whenever possible"""
        gcd = math.gcd(self.numerator, self.denominator) # Attributes shown below are set to turn into the simplest form 
        if gcd != 0 :                                    # e.g. 2/4 would turn into 1/2
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        if self.denominator < 0: #negative numerator and denominator would turn into positive by multiplying -1.
            self.numerator = self.numerator* -1
            self.denominator = self.denominator* -1
            
    def __mul__(self, other): 
        """Constructs a method that two different fractions are multiplied"""
        return Fraction(self.numerator * other.numerator, 
                        self.denominator * other.denominator)        




