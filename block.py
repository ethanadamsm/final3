import sys, pygame

class Block(object):
	def __init__(self, x, y, w, h, image):
		self.x = x 
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0
		self.vy = 0
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (self.w, self.h))

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self):
		self.x += self.vx
		self.y += self.vy

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getW(self):
		return self.w

	def getH(self):
		return self.h