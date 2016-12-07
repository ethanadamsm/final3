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
			w = 0.5 * (5 + block.getW())
			h = 0.5 * (5 + block.getH())
			dx = (self.x + (5 / 2.0)) - (block.getX() + (block.getW() / 2))
			dy = (self.y + (5 / 2.0)) - (block.getY() + (block.getH() / 2))

			if(abs(dx) <= w and abs(dy) <= h):
				wy = w * dy
				hx = h * dx
				if (wy > hx):
					if(wy > -hx):
						self.vy = -self.vy
						self.bounces += 1
					else:
						self.vx = -self.vx
						self.bounces += 1
				else:
					if(wy > -hx):
						self.vx = -self.vx
						self.bounces += 1
					else:
						self.vy = -self.vy
						self.bounces += 1
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

	def getX(self):
		return self.x

	def getY(self):
		return self.y
