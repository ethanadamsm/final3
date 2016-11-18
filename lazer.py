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

	def update(self, blocks):
		self.x += self.vx
		self.y += self.vy
		for block in blocks:
			if self.x < block.getX() + block.getW() and self.x + 5 > block.getX() and self.y < block.getY() + block.getH() and self.y + 5 > block.getY():
				if self.x + 5 > block.getX() or self.x < block.getX() + block.getW():
					self.vx = -self.vx
				elif self.y + 5 > block.getY() or self.y < block.getY() + block.getH():
					self.vy = -self.vy 
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
