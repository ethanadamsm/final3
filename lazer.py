import sys, pygame, math

class Lazer(object):
	def __init__(self, px, py):
		self.x = px
		self.y = py
		bounces = 0
		self.image = pygame.image.load("lazer.png")
		cx = pygame.mouse.get_pos()[0] - px
		cy = pygame.mouse.get_pos()[1] - py
		div = math.sqrt((cx * cx) + (cy * cy))
		self.vx = ((cx / div) * 2)
		self.vy = ((cy / div) * 2)

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self):
		self.x += self.vx
		self.y += self.vy