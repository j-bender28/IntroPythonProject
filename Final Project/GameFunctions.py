import sys
import pygame

def checkEvents(settings, screen, person):
	"""Respond to keypresses and mouse events."""
	#Watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			checkKeydownEvents(event, settings, screen, person)
		elif event.type == pygame.KEYUP:
			checkKeyupEvents(event, person)

def checkKeydownEvents(event, settings, screen, person):
	if event.key == pygame.K_LEFT:
		#move the person to the right
		person.movingLeft = True
	elif event.key == pygame.K_RIGHT:
		#move the person to the right
		person.movingRight = True
	elif event.key == pygame.K_UP:
		#move the person to the right
		person.movingUp = True
	elif event.key == pygame.K_DOWN:
		#move the person to the right
		person.movingDown = True
	elif event.key == pygame.K_q:
		sys.exit()

def checkKeyupEvents(event, person):
	if event.key == pygame.K_LEFT:
		#move the person to the right
		person.movingLeft = False
	elif event.key == pygame.K_RIGHT:
		#move the person to the right
		person.movingRight = False
	elif event.key == pygame.K_UP:
		#move the person to the right
		person.movingUp = False
	elif event.key == pygame.K_DOWN:
		#move the person to the right
		person.movingDown = False
				
def updateScreen(settings, screen, person):
	"""Update images on the screen and flip to the new screen."""
	#Redraw the game each pass
	screen.fill(settings.bgColor)	
	person.draw()
			
	#Make the most recently drawn screen visible
	pygame.display.flip()