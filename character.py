import sys, pygame, lazer, healthbar

class Character(object):
	def __init__(self, x, y, w, h, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0.0
		self.vy = 0.0
		self.image = image
		self.lazers = []
		self.healthbar = healthbar.Healthbar(self.x - 10, self.y - 20, 100)

	def render(self, screen):
		for lazer in self.lazers:
			lazer.render(screen)
		screen.blit(self.image, (self.x, self.y))
		self.healthbar.render(screen)

	def update(self, blocks):
		for lazer in self.lazers:
			lazer.update(blocks)
			if not lazer.getAlive():
				self.lazers.remove(lazer) 
		if self.x < 0:
			self.x = 0 + 1
		if self.x + 30 > 640:
			self.x = 610 - 1
		if self.y < 0:
			self.y = 0 + 1
		if self.y + 30 > 480:
			self.y = 450 - 1
		self.healthbar.update()
		self.clamp(self.healthbar)
		collision = False
		prevx = self.x 
		self.x += self.vx
		prevy = self.y
		self.y += self.vy
		for block in blocks:
			if self.x < block.getX() + block.getW() and self.x + 30 > block.getX() and self.y + self.vy < block.getY() + block.getH() and self.y + 30 + self.vy > block.getY():
				collision = True
		if collision: 
			self.x = prevx 
		collision = False
		for block in blocks:
			if self.x < block.getX() + block.getW() and self.x + 30 > block.getX() and self.y + self.vy < block.getY() + block.getH() and self.y + 30 + self.vy > block.getY():
				collision = True
		if collision:
			self.y = prevy
		#if self.x < 0:
			#self.x = 0

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def addLazer(self):
		if len(self.lazers) < 6:
			self.lazers.append(lazer.Lazer(self.x + 15, self.y + 15))

	def clamp(self, objects):
		objects.setX(self.x - 10)
		objects.setY(self.y - 20)