import sys, pygame, block

class GameMap(object):
	def __init__(self, filename):
		self.filename = filename
		self.blocks = []
		file = open(filename, "r")
		for line in file:
			splitstring = [x.strip() for x in line.split(',')]
			self.blocks.append(block.Block(int(splitstring[0]), int(splitstring[1]), int(splitstring[2]), int(splitstring[3]), splitstring[4]))

	def render(self, screen):
		for block in self.blocks:
			block.render(screen)

	def update(self):
		for block in self.blocks:
			block.update()

	def getBlocks(self):
		return self.blocks