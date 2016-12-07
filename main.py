import sys, pygame, character, gamemap, socket, enemy, random
pygame.init()
pygame.display.set_caption('AP Game')
black = 0, 0, 0
size = width, height, = 640, 480
screen = pygame.display.set_mode(size)
playerblock = pygame.image.load("player.png")
player = character.Character(50, 215, 30, 30, playerblock)
enemy1 = pygame.image.load("enemy1.png")
background = pygame.image.load("background.png")
frame = 300
frames = 0
frames2 = 0
maps = gamemap.GameMap("map.txt", "spots.txt")
player2x = -50
player2y = -50
enemies = []

IP = sys.argv[1]
PORT = 9000
BUFFER_SIZE = 1024
TIME = 600

if len(sys.argv) > 3:
	player.setX(int(sys.argv[2]))
	player.setY(int(sys.argv[3]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def render():
    screen.fill(black)
    screen.blit(background, (0, 0))
    player.render(screen)
    for enemy in enemies:
    	enemy.render(screen)
    maps.render(screen)
    screen.blit(playerblock, (player2x, player2y))
    pygame.display.flip()

def update():
    global lazers
    global frame
    global frames2
    player.update(maps.getBlocks())
    removeLazers = []
    for enemys in enemies:
    	enemys.update(maps.getBlocks(), player, player.getLazers())
    	if enemys.getRemoveLazer() != "":
    		removeLazers.append(enemys.getRemoveLazer())
    if pygame.mouse.get_pressed()[0]:
    	if frame % 300 == 0:
    		player.addLazer()
    	frame += 1
    if frame > 300 and not pygame.mouse.get_pressed()[0]:
    	frame = 300
    maps.update()
    if frames % TIME == 0:
    	spots = maps.getSpawns()
    	spot = random.randint(0, len(spots) - 1)
    	spot = spots[spot]
    	enemies.append(enemy.Enemy(spot[0], spot[1], 30, 30, enemy1))
    frames2 += 1
    for enemys in enemies:
	    for lazer in player.getLazers():
	    	if lazer == enemys.getRemoveLazer():
	    		player.removeLazer(lazer)
	    if enemys.getAlive() == False:
	    	enemies.remove(enemys)
    # for lazer in removeLazers:
    # 	if lazer != "":
			#player.getLazers().remove(lazer)

while(True):
	# global s 
	# global player
	# global IP
	update()
	if frames >= 300:
		#while True:
		s.sendall(str(player.getX()) + ", " + str(player.getY()) + ", " + str(socket.gethostbyname(socket.gethostname())))
		data = s.recv(1024)
		print data
		mylist = data.replace(' ', '').split(',')
		if len(mylist) > 2:
			#print mylist[0] + " " + mylist[1] + " " + mylist[2]
			if str(socket.gethostbyname(socket.gethostname())) != mylist[2]:
				if mylist[0].count('.') == 1:
					player2x = float(mylist[0])
					player2y = float(mylist[1])
				else:
					player2x = int(mylist[0])
					player2y = int(mylist[1])

		if not data: break	
		#s.close()

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
	frames += 1