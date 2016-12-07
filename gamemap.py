import sys, pygame, block

class GameMap(object):
	def __init__(self, filename, spotfile):
		self.filename = filename
		self.spotfile = spotfile
		self.blocks = []
		self.spawnlocals = []
		file = open(filename, "r")
		file2 = open(spotfile, "r")
		for line in file:
			splitstring = [x.strip() for x in line.split(',')]
			self.blocks.append(block.Block(int(splitstring[0]), int(splitstring[1]), int(splitstring[2]), int(splitstring[3]), splitstring[4]))
		for line in file2:
			splitstring = [x.strip() for x in line.split(',')]
			self.spawnlocals.append([float(splitstring[0]), float(splitstring[1])])

	def render(self, screen):
		for block in self.blocks:
			block.render(screen)

	def update(self):
		for block in self.blocks:
			block.update()

	def getBlocks(self):
		return self.blocks

	def getSpawns(self):
		return self.spawnlocals