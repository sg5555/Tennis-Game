import pygame

from window import Window

class Player:
    def __init__(self,name,country,ranking,rankingPoints,power,accuracy,speed,fitness,x,y,xChange,yChange,width,height,difficulty,skillPoints):
        self.name = str(name)
        self.country = country
        self.ranking = ranking
        self.rankingPoints = rankingPoints
        self.power = power
        self.accuracy = accuracy
        self.speed = speed
        self.fitness = fitness
        self.x = x
        self.y = y
        self.xChange = xChange
        self.yChange = yChange
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.skillPoints = skillPoints

    def playerControls(self):
        ballBounceChance = random.randint(1,100)
        ballBounceTime = 100000
        for event in pygame.event.get(): #if user clicks on x on start screen
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pauseMenu.pause() #pause
                elif event.key == pygame.K_LEFT:
                    player.xChange = - player.speed / 2.6
                elif event.key == pygame.K_RIGHT:
                    player.xChange = player.speed / 2.6
                elif event.key == pygame.K_UP:
                    player.yChange = - player.speed / 2.
                elif event.key == pygame.K_DOWN:
                    player.yChange = player.speed / 2.6
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.fitness = player.fitness - 0.03125
                    if player.fitness <= 100:
                        player.speed = player.speed - 0.03125
                    if player.fitness <= 80:
                        player.speed = player.speed - 0.03125
                    if player.fitness <= 60:
                        player.speed = player.speed - 0.0625
                    if player.fitness <= 40:
                        player.speed = player.speed - 0.125
                    if player.fitness <= 20:
                        player.speed = player.speed - 0.25
                    elif player.fitness == 0:
                        player.speed = player.speed - 1
                print('fitness',player.fitness)
                print('speed:',player.speed)
                if event.key == pygame.K_SPACE and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                elif event.key == pygame.K_SPACE and event.key == pygame.K_LEFT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player.x + player1.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    ball.ballXChange = 0
                elif event.key == pygame.K_SPACE  and event.key == pygame.K_RIGHT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player1.x + player1.width: #player and ball collision
                    ball.ballYChange = + ball.ballSpeed
                elif event.key == pygame.K_LCTRL and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height - 70 and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    ball.ballXChange = - int(player.power / 5.8)
                elif event.key == pygame.K_LALT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height - 70 and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    ball.ballXChange = - int(-player.power / 5.8)
                elif ballBounceChance > 50:
                    if ballBounceTime > 0:
                        ballBounce = pygame.draw.circle(window.gameDisplay,window.colors["grey"],[ball.ballX+3,ball.ballY+3],ball.ballRadius)
                        ballBounceTime = ballBounceTime - 1
            if event.type == pygame.KEYUP:
                player.xChange = 0
                player.yChange = 0

                
    def playerBoundaries(self):
        if player.x <= 0: 
            player.x = 0
            player.xChange = 0
        if player.x > display_width - player.width:
            player.x = display_width - player.width
            player.xChange = 0
        if player.y <= display_height / 4:
            player.y = display_height / 4
            player.yChange = 0
        if player.y > display_height - player.height:
            player.y = display_height - player.height
            player.yChange = 0

    def playerAnimations(self):
        pass

class Opponent(Player):
    def __init__(self,name,country,ranking,rankingPoints,power,accuracy,speed,fitness,x,y,xChange,yChange,width,height,difficulty,skillPoints):
        super().__init__(name,country,ranking,rankingPoints,power,accuracy,speed,fitness,x,y,xChange,yChange,width,height,difficulty,skillPoints) #calls Player class

    def opponentBoundaries(self):
        if opponent.x >= display_width-opponent.width:
            opponent.x = display_width-opponent.width
            opponent.xChange = 0
        if opponent.x <= 0:
            opponent.x = 0
            opponent.xChange = 0
        if opponent.y >= display_height / 10000:
            opponent.y = display_height / 10000 
            opponent.yChange = 0
        if opponent.y <= 0:
            opponent.y = 0
            opponent.yChange = 0

    def opponentMovement(self): #opponent AI
        netChance = random.randint(1,100)
        if opponent.x < ball.ballX:
            opponent.xChange = opponent.speed / 5 #1 to teleport
        if opponent.x > ball.ballX:
            opponent.xChange = - opponent.speed / 5
        if opponent.y < ball.ballY:
            opponent.yChange = opponent.speed / 5
        if opponent.y > ball.ballY:
            opponent.yChange = - opponent.speed / 5
        if ball.ballY >= opponent.y and ball.ballX >= opponent.x and ball.ballY <= opponent.y + opponent.height - 85 and ball.ballX <= opponent.x + opponent.width:#opponent ball collision
            if opponent.x > 300 and opponent.x < 700: #a shot that can go anywhere
                ball.ballYChange = int(opponent.power / 5.5) + 10
                ball.ballXChange = random.randint(0,20)
            elif opponent.x > 600: #shot to the right
                ball.ballYChange = int(opponent.power / 5.5) + 10
                ball.ballXChange = - random.randint(5,25)
                opponent.xChange = - opponent.speed / 5
            elif opponent.x < 400: #shot to the left
                ball.ballYChange = int(opponent.power / 5.5) + 10
                ball.ballXChange = random.randint(5,25)
        #if netChance < 10:
            #opponent.xChange = opponent.speed / 5
        #if netChance > 80:
            #opponent.yChange = - opponent.speed / 5
            #opponent.xChange = - opponent.speed / 5

    def opponentAnimations(self):
        pass
    
    def randomOpponent(self, randomName):
        self.randomName = random.choice(opponentNames)
        if self.randomName == "Djokovic":
            opponent = Opponent('Novak Djokovic','Serbia',1,10200,85,89,95,90,100,100,0,0,60,180,'')
        elif self.randomName == "Federer":
            opponent = Opponent('Roger Federer','Switzerland',2,9000,87,92,100,89,100,100,0,0,60,180,'')
        elif self.randomName == "Nadal":
            opponent = Opponent('Rafael Nadal','Spain',3,8900,94,80,94,90,100,100,0,0,60,180,'')
        elif self.randomName == "Medvedev":
            opponent = Opponent('Daniil Medvedev','Russia',4,9200,82,87,96,90,100,100,0,0,60,180,'')
        elif self.randomName == "Zverev":
            opponent = Opponent('Alexander Zverev','Germany',5,8400,95,81,90,85,100,100,0,0,60,180,'')
        elif self.randomName == "Togami":
            opponent = Opponent('Light Togami','Japan',6,8300,85,80,98,89,100,100,0,0,60,180,'')
        elif self.randomName == "de Minaur":
            opponen = Opponent('Alex De Minaur','Australia',7,7000,83,85,100,87,100,100,0,0,60,180,'')
        elif self.randomName == "Kyrgios":
            opponent = Opponent('Nick Kyrgios','Australia',8,6500,96,84,82,85,100,100,0,0,60,180,'')
        elif self.randomName == "Tsitsipas":
            opponent = Opponent('Stefanos Tsitsipas','Greece',9,6200,86,82,84,84,100,100,0,0,60,180,'')
        elif self.randomName == "Karlovic":
            opponent = Opponent('Ivo Karlovic','Croatia',10,4900,90,80,10,79,100,100,0,0,60,180,'')
        elif self.randomName == "Koaykul":
            opponent = Opponent('Krittin Koaykul','Thialand',11,2100,25,30,24,24,100,100,0,0,60,180,'')
        elif self.randomName == "Bahmet":
            opponent = Opponent('Artem Bahmet','Ukraine',12,1200,15,5,25,15,100,100,0,0,60,180,'')
        
player = Player('Sam Gibb','United Kingdom',13,1000,40,80,80,80,0,0,(display_width * 0.45),(display_height * 0.8),60,180,'Amateur',99)#an instance of the Player class


