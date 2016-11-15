import sys, pygame, character, lazer
pygame.init()
pygame.display.set_caption('AP Game')
black = 0, 0, 0
size = width, height, = 640, 480
screen = pygame.display.set_mode(size)
playerblock = pygame.image.load("player.png")
player = character.Character(20, 215, 30, 30, playerblock)
background = pygame.image.load("background.png")
blocks = []
lazers = []

def render():
    screen.fill(black)
    screen.blit(background, (0, 0))
    player.render(screen)
    for lazer in lazers:
    	lazer.render(screen)
    pygame.display.flip()

def update():
    global lazers
    player.update(blocks)
    if pygame.mouse.get_pressed()[0]:
    	lazers.append(lazer.Lazer(player.getX() + 15, player.getY() + 15))
    for lazerz in lazers:
    	lazerz.update()

while(True):
	update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.setVelX(-1)
			if event.key == pygame.K_d:
				player.setVelX(1)
			if event.key == pygame.K_s:
				player.setVelY(1)
			if event.key == pygame.K_w:
				player.setVelY(-1)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				player.setVelX(0)
			if event.key == pygame.K_s or event.key == pygame.K_w:
				player.setVelY(0)
	render()