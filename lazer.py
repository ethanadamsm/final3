import sys, pygame, math

class Lazer(object):
	def __init__(self, px, py):
		self.x = px
		self.y = py
		self.bounces = 0
		self.alive = True
		self.image = pygame.image.load("lazer.png")
		cx = pygame.mouse.get_pos()[0] - px
		cy = pygame.mouse.get_pos()[1] - py
		div = math.sqrt((cx * cx) + (cy * cy))
		self.vx = ((cx / div) * 2)
		self.vy = ((cy / div) * 2)

	def render(self, screen):
		if self.alive:
			screen.blit(self.image, (self.x, self.y))

	def update(self):
		self.x += self.vx
		self.y += self.vy
		if self.x <= 0 or self.x >= 640:
			self.vx = -self.vx
			self.bounces += 1
		if self.y <= 0 or self.y >= 480:
			self.vy = -self.vy
			self.bounces += 1
		if self.bounces >= 4:
			self.alive = False

	def getAlive(self):
		return self.alive
