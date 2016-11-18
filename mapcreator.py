import sys, pygame, block
pygame.init()
pygame.display.set_caption("Map Creator")
black = 0, 0, 0
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
background = pygame.image.load("background.png")
current = 0
blocks = []
frame = 300

def render():
	#screen.fill(black)
	screen.blit(background, (0, 0))
	for block in blocks:
		block.render(screen)
	pygame.display.flip()

def update():
	global blocks
	global frame
	if pygame.mouse.get_pressed()[0]:
		if frame % 300 == 0:
			if current == 0:
				blocks.append(block.Block(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20, "block1.png"))
			elif current == 1:
				blocks.append(block.Block(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20, "block2.png"))
			frame += 1
	if frame > 300 and not pygame.mouse.get_pressed()[0]:
		frame = 300

while(True):
	global current
	global blocks
	update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				string = ""
				for block in blocks:
					string += str(block.getX()) + ", " + str(block.getY()) + ", " + str(block.getW()) + ", " + str(block.getH()) + ", " + str(block.getImage()) + "\n"
				file = open("map.txt", 'w')
				file.write(string)
			if event.key == pygame.K_1:
				current = 0
			if event.key == pygame.K_2:
				current = 1
			if event.key == pygame.K_3:
				current = 2
	render()
