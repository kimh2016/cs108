""" CS 108 Project 

This game allows the user to move the black ball using the arrow keys.
The goal of this game is to avoid the falling meteors that are random
in size. Once the user touches the meteor, the game ends. The user is
able to choose the level of the game. In level one, the meteors fall
down at a slow speed. In level two, the meteors fall down at medium
speed. 


@author: Hansol Kim (hk94)
@date: Spring 2021 
"""


from guizero import App, Text, Drawing, PushButton, Box, TextBox
from random import randint
from ground_object import GroundObject 
from falling_object import FallingObject
from timer import Timer, TimerApp


class GameSimulation:
    """ This is the main game simulator that will call other methods from different modules."""
    
    def __init__(self, app):
        """Instantiate the simulator and construct basic format of the canvas."""
        
        # Set the default size of the canvas.
        app.title = 'Avoid Falling Meteor' 
        app.width = 500
        app.height = 500
        box = Box(app, layout = 'grid', width= 500, height= 500) # The canvas will be used in grid. 
        
        # Make a space for PushButtons and the running time. 
        self.drawing = Drawing(box, width= 500, height= 450, grid=[0, 0, 6, 1]) 
        self.fo_list = [] # Make an empty list for falling meteors
        self.app = app
        
        # This will provide control keys for the user. 
        app.when_key_pressed = self.key_event_handler 
        
        # Build a cover background color  
        self.drawing.rectangle(0, 0, self.drawing.width, self.drawing.height,
                               color = 'pink')
        
        # Quit Button
        self.quit_game = PushButton(box, command = app.destroy, text = 'QUIT', grid = [0,1]) 
        
        # Level 1 Button
        self.level_one = PushButton(box, text = 'Level 1', grid= [1,1], command = self.level_one)
        
        # Level 2 Button
        self.leve_two = PushButton(box, text = 'Level 2', grid = [2,1], command = self.level_two)
        
        # The time the user has taken in the game will be the user's final score. 
        self.score = Text(box, text = 'Time: ', grid = [3,1])
    
        # Call the Timer class for later use. 
        self.time = Timer()
        
        #picture = Picture(app, image = 'images/space.png', grid =[10, 10])
        
        # Set booleans for level 1 and 2 so that the user can
        # go back to PushButton to replay the game when game ends. 
        self.level_1 = False 
        self.level_2 = False
        self.running = False
        app.repeat(50, self.draw_frame)  
        
    def level_one(self):
        """ Level one is easy mode where the meteors fall at a slower speed. """
        
        # Use the boolean to run the level one when the user clicks on level one.
        app.cancel(self.make_new_object)
        app.cancel(self.game_ends)
        self.level_1 = True
        if self.level_1 == True: 
           # self.level_1 = True
            self.drawing.rectangle(0, 0, 500, 450, color='pink') # Drawing the same canvas as the cover.
            self.person = GroundObject(200, 450, 1, 5, 7, 'black') # Initial position of the black ball. 
            self.person.draw(self.drawing)
            app.repeat(800, self.make_new_object) # New balls with different sizes are created. 
            self.time.reset()
            app.repeat(50, self.game_ends)# reset the time when the user dies in the game. 
        self.level_2 = False 
        self.running = True # This boolean is used in the game termination method. 
        
        
    def level_two(self):
        """ Level two is hard mode where the meteors fall at a faster speed. """
        
        # Use the boolean to run the level one when the user clicks on level one.
        app.cancel(self.make_new_object)
        app.cancel(self.game_ends)
        self.level_2 = True
        if self.level_2 == True:
            #self.level_2 = True
            self.drawing.rectangle(0, 0, 500, 450, color='pink')
            self.person = GroundObject(200, 450, 1, 5, 15, 'black')
            self.person.draw(self.drawing)
            app.repeat(200, self.make_new_object)
            self.time.reset()
            app.repeat(50, self.game_ends)
        self.level_1 = False
        self.running = True # This boolean is used in the game termination method. 
        
           
    def key_event_handler(self, event):
        """ Allows the user to use the key arrows to move the black ball."""
        
        # Prints the name of the key in the shell. 
        print('Name of the key: ', event.tk_event.keysym)
        if event.tk_event.keysym == 'Right': # If the key is 'Right', the black ball moves 20 units to  the right. 
            self.person.move(20, 0)
        elif event.tk_event.keysym == 'Left': # If the key is 'Left', the black ball moves 20 units to  the left.
            self.person.move(-20, 0)
        elif event.tk_event.keysym == 'Up': # If the key is 'Up', the black ball moves 20 units up.
            self.person.move(-20, 1)
        elif event.tk_event.keysym == 'Down': # If the key is 'Down', the black ball moves 20 units down.
            self.person.move(20, 1)
        
    
    def draw_frame(self):
        """ Creates frames  """
        if self.running:
            self.drawing.clear() # Clears the previous canvas. 
            self.drawing.rectangle(0, 0, 500, 450, color='pink')
            self.person.draw(self.drawing) # Draws the black ball.
            
            # Every meteor that is created will be able to fall from the top of the canvas. 
            for falling_object in self.fo_list:
                falling_object.move(self.drawing)
                falling_object.draw(self.drawing)
                
            # Time is recorded once the user presses the PushButton to start the game. 
            self.score.value = 'Time: {:.02f}'.format(self.time.get_time())
            
            # Meteors continue to fall to avoid accumulation. 
        else:
            for falling_object in self.fo_list: 
                falling_object.move(self.drawing)
        
        
    def make_new_object(self):
        """ Every meteor that is created is added in to the empty list. """
        
        # Although the canvas ranges from 0 to 500 in width, meteor fall
        # from a wider range for more variety.
        newball = FallingObject(randint(1, 1000), 1, 3, randint(10, 50), 'red') 
        self.fo_list.append(newball)
        
        
    def distance(self, x1, y1, x2, y2):
        """ The distance of the objects are measured."""
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        
    def game_ends(self):
        """ The games ends when the circumferance of the black ball
            hits or touches the meteor's circumferance.
            """
        # Using the for loop, when the radius of meteor in the list and the 
        # radius of the black ball goes over a certain distance, it means
        # they are in touch with one another, thus the game ends.
        
        for i in self.fo_list:
            if self.person.radius + i.radius >= \
               self.distance(self.person.x, self.person.y, i.x, i.y): 
                current_time = self.time.get_time() # Receives the current time. 
                self.score.value = 'Time: {:.02f}'.format(current_time) # Shows the current time on the canvas. 
                self.running = False # Stops the game.
                self.fo_list = [] # Empties the list when the game stops. 
                self.time.reset() # Reset the time.
                app.cancel(self.make_new_object) # Cancels makings new objects. 
                app.cancel(self.game_ends) # Cancels the game and now the user is able to go back and play again. 
                return 
                
                    
app = App()
GameSimulation(app)
app.display()
