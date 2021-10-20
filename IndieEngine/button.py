from .font import FONT
from .colour import COLOUR
import pygame
from .text import TEXT
from .panel import PANEL
from . import app  as e
import IndieEngine

class BUTTON(TEXT, PANEL):
    """
    Create a interactable button a Surface\n
    """
    padding = 0.2
    ispressed = False
    ishovered = False
    def __init__(self, text: str, font: FONT, colour: COLOUR, background_colour: COLOUR):
        self.isselected = False
        super().__init__(text, font, colour, background_colour)

    def blit(self) -> None:
        """
        Draw the Button on the Screen\n
        """
        width = self.font.get_width()
        height = self.font.get_height()
        b_rect = (self.position[0]-self.padding*width/2, self.position[1]-self.padding*height/2,
                  width+self.padding*width, height+self.padding*height)
        self.rect = pygame.Rect((b_rect))
        self.size = [b_rect[2],b_rect[3]]
        pygame.draw.rect(e.screen, self.colour, 
            self.rect, self.thick)
        e.screen.blit(self.font, self.position)
        


    def control(self,event,mouse)->None:
        """
        Handle Events of a Button\n
        Parameters:\n
        :event(event.pygame.get()): The event to handle\n
        :mouse(x,y): Position of mouse\n
        """
        self.ispressed = False
         
        try:
            if self.rect.collidepoint((mouse)):
                self.ishovered = True
            else:
                self.ishovered = False

            if event.type == IndieEngine.inputs.EVENT.mouse_button_down and self.rect.collidepoint((mouse)):
                self.ispressed = True
                self.isselected = True
            elif event.type == IndieEngine.inputs.EVENT.mouse_button_down and not self.rect.collidepoint((mouse)):
                self.isselected = False
        except AttributeError as e:
            pass
