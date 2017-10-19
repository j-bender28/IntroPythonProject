import sys
import pygame
import GameFunctions as gf
from Settings import Settings
from Person import Person

def runGame():
	#Initialize pygame, settings, and screen object.
	pygame.init
	settings = Settings()
	screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
	pygame.display.set_caption("Name of the Game")
	
	#Make a person
	person = Person(settings, screen)
	
	#Start the main loop for tha game
	while True:
		gf.checkEvents(settings, screen, person)
		person.update()
		gf.updateScreen(settings, screen, person)

runGame()