import sys, pygame, character, gamemap, socket
pygame.init()
pygame.display.set_caption('AP Game')
black = 0, 0, 0
size = width, height, = 640, 480
screen = pygame.display.set_mode(size)
playerblock = pygame.image.load("player.png")
player = character.Character(50, 215, 30, 30, playerblock)
background = pygame.image.load("background.png")
frame = 300
maps = gamemap.GameMap("map.txt")

IP = sys.argv[1]
PORT = 9000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def render():
    screen.fill(black)
    screen.blit(background, (0, 0))
    player.render(screen)
    maps.render(screen)
    pygame.display.flip()

def update():
    global lazers
    global frame
    player.update(maps.getBlocks())
    if pygame.mouse.get_pressed()[0]:
    	if frame % 300 == 0:
    		player.addLazer()
    	frame += 1
    if frame > 300 and not pygame.mouse.get_pressed()[0]:
    	frame = 300
    maps.update()

while(True):
	global s 
	global player
	update()
	s.send(str(player.getX()) + ", " + str(player.getY()))
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