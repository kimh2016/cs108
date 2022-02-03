"""@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Hansol Kim (hk94)
@date: Spring, 2021
"""
class GroundObject :
    def __init__(self, x=50, y=50, vel_x=1, vel_y=1, radius=40, color="red"):
        """Instantiate a ground object."""
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.color = color
        
    def draw(self,drawing):
        """ Draws the ground object which is in a sphere shape."""
        drawing.oval(self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             color=self.color
             )
        
    def move(self, move, change):
        """ Allows the ground object to move. """ 
        if change == 0:
            self.x += move
        else:
            self.y += move
        
    
    
    
    
    
    
    