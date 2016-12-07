import sys, pygame, lazer, healthbar, character

class Enemy(character.Character):
	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))
		self.healthbar.render(screen)

	def update(self, blocks, player, lazers):
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

		if self.x > player.getX():
			self.vx = -.1
		if self.x + self.w < player.getX():
			self.vx = .1
		if self.y > player.getY():
			self.vy = -.1
		if self.y + self.h < player.getY():
			self.vy = .1

		for laser in lazers:
			if self.x < laser.getX() + 5 and self.x + self.w > laser.getX() and self.y < laser.getY() + 5 and self.y + self.h > laser.getY():
				self.healthbar.setHealth(self.healthbar.getHealth() - 10.0)
				self.removeLazer = laser

		if self.healthbar.getHealth() < 2:
			self.alive = False

	def getRemoveLazer(self):
		return self.removeLazer

	def getAlive(self):
		return self.alive

