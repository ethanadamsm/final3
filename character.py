import sys, pygame

class Character(object):
	def __init__(self, x, y, w, h, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0.0
		self.vy = 0.0
		self.image = image

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self, blocks):
		self.x += self.vx
		self.y += self.vy
		prevx = self.x
		prevy = self.y
		if self.x < 0 or self.x + 30 > 640:
			self.x = prevx
		if self.y < 0 or self.y + 30 > 480:
			self.y = prevy

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def getX(self):
		return self.x

	def getY(self):
		return self.y