"""@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Hansol Kim (hk94)
@date: Spring, 2021
"""

import random

class FallingObject :
    
    def __init__(self, x=50, y=50, vel_y=5, radius=40, color="red"):
        """Instantiate a falling object."""
        self.x = x
        self.y = y
        self.vel_y = vel_y
        self.radius = radius
        self.color = color
        self.on_screen = True
        
        
    def draw(self,drawing):
        """Draw the falling meteors. """
        drawing.oval(self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             color=self.color
             )
        
    def move(self,drawing):
        """Allows the falling meteors to stay on the canvas screen. """
        if self.y + self.radius > drawing.height :
            self.on_screen = False 
            
        self.y += self.vel_y

       
       
       
       
       
       
       
       
        