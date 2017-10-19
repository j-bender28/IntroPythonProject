import pygame

class Person():

	def __init__(self, settings, screen):
		"""Initialize the person and set its starting postion"""
		self.screen = screen
	
		#Load the person image and get its rect
		self.imageFront = pygame.image.load('personFront.bmp')
		self.imageSide = pygame.image.load('personSide.bmp')
		self.image = self.imageFront
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.settings = settings
	
		#Start at the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
		
		#Movement flags
		self.movingLeft = False
		self.movingRight = False
		self.movingUp = False
		self.movingDown = False

	def update(self):
		"""Draw the person at its current location"""
		if self.movingLeft and self.rect.left > 0:
			self.centerX -= self.settings.personSpeedFactor
			self.image = self.imageSide
		if self.movingRight and self.rect.right < self.screen_rect.right:
			self.centerX += self.settings.personSpeedFactor
			self.image = self.imageSide
			
		#Update rect object with self.centerx
		self.rect.centerx = self.centerX
		
		if self.movingUp and self.rect.top > 0:
			self.centerY -= self.settings.personSpeedFactor
			self.image = self.imageFront
		if self.movingDown and self.rect.bottom < self.screen_rect.bottom:
			self.centerY += self.settings.personSpeedFactor
			self.image = self.imageFront
			
		#Update rect object with self.centery
		self.rect.centery = self.centerY
		
	def draw(self):
		"""Draw the person at its current location"""
		self.screen.blit(self.image, self.rect)