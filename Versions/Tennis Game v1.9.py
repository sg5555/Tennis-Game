import pygame, random, sys, datetime, os, time, re
#print(pygame.font.get_fonts())
pygame.mixer.pre_init(48100,16,2,4096) #music
pygame.init()
display_width = 1200
display_height = 920
opponentNames = ["Novak Djokovic","Roger Federer","Rafael Nadal","Daniil Medvedev","Stefanos Tsitsipas","Dominic Thiem","Alexander Zverev","Matteo Berrettini","David Goffin",
                         "Gael Monfils","Stan Wawrinka","Fabio Fognini","Benoit Paire","Denis Shapovalov","Marin Cilic","Grigor Dimitrov",
                         "Light Togami","Alex de Minaur","Nick Kyrgios","Milos Raonic","Dan Evans","Ivo Karlovic","Ernests Gulbis","Dustin Brown","Bernard Tomic","Andy Murray",
                 "Krittin Koaykul","Artem Bahmet","Jimmy Connors","John Mcenroe","Brad Gilbert","Andre Agassi","Bjorn Borg","Stefan Edberg","Marcus Willis"]
opponentImageChance = random.randint(1,100)
blah = ''
blah2 = ''

def scrollX(screenSurf, offsetX):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (offsetX, 0))
    if offsetX < 0:
        screenSurf.blit(copySurf, (width + offsetX, 0), (0, 0, -offsetX, height))
    else:
        screenSurf.blit(copySurf, (0, 0), (width - offsetX, 0, offsetX, height))

def scrollY(screenSurf, offsetY):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (0, offsetY))
    if offsetY < 0:
        screenSurf.blit(copySurf, (0, height + offsetY), (0, 0, width, -offsetY))
    else:
        screenSurf.blit(copySurf, (0, 0), (0, height - offsetY, width, offsetY))

def main():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        scrollY(window.gameDisplay, 2)
    elif pressed[pygame.K_DOWN]:
        scrollY(window.gameDisplay, -2)
    elif pressed[pygame.K_LEFT]:
        scrollX(window.gameDisplay, 2)
    elif pressed[pygame.K_RIGHT]:
        scrollX(window.gameDisplay, -2)

class Window:

    def __init__(self): #holds all of the constants
        self.gameDisplay = pygame.display.set_mode((display_width,display_height))
        self.rect = self.gameDisplay.get_rect()
        self.time = pygame.time.get_ticks()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.tinyFont = pygame.font.SysFont('comicsansms', 16)
        self.smallFont = pygame.font.SysFont('comicsansms', 25)
        self.smallMedFont = pygame.font.SysFont('comicsansms', 32)
        self.medFont = pygame.font.SysFont('comicsansms', 40)
        self.largeFont = pygame.font.SysFont('comicsansms', 80)
        self.gameExit = True
        self.levelUp = False
        self.newNewGame = False
        self.colors = {"red": (255,0,0),
                       "green": (0,150,0),
                       "blue": (48,138,255),
                       "darkBlue": (48,108,205),
                       "white": (255,255,255),
                       "black": (0,0,0),
                       "grey": (80,80,80),
                       "lightRed": (255,0,0),
                       "yellow": (230,218,0),
                       "lightYellow": (200,200,0),
                       "lightGreen": (0,200,0),
                       "lightBlue": (26,156,255),
                       "purple": (51, 51, 255),
                       "lightPurple": (110, 110, 255)}

    def setupPlayMatch(self):
        if opponent.name == 'Novak Djokovic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/player1front.png')
        elif opponent.name == 'Roger Federer':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/federer.png')
        elif opponent.name == 'Rafael Nadal':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/nadal.png')
        elif opponent.name == 'Daniil Medvedev':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/medvedev.png')
        elif opponent.name == 'Matteo Berrettini':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/berrettini.png')
        elif opponent.name == 'Dominic Thiem':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/thiem.png')
        elif opponent.name == 'Stefanos Tsitsipas':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/tsitsipas.png')
        elif opponent.name == 'Alexander Zverev':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/zverev.png')
        elif opponentImageChance > 95:
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1ultimate.png')
            opponent.ultimate = True
        else:
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
        self.playMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/powerbaseliner.png')
        if player.hand == 'Right':
            self.playerImage = pygame.image.load('C:/NEA Tennis Game/Player/player1upright.png')
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontright.png')
            self.playerImageRight = pygame.image.load('C:/NEA Tennis Game/Player/player1right.png')
        else:
            self.playerImage = pygame.image.load('C:/NEA Tennis Game/Player/player1upleft.png')
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontleft.png')
            self.playerImageLeft = pygame.image.load('C:/NEA Tennis Game/Player/player1left.png')
        player.x += player.xChange
        player.y += player.yChange
        opponent.x += opponent.xChange
        opponent.y += opponent.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        self.outText = self.medFont.render(str("Out!"),True,self.colors["black"])
        self.energyText = self.tinyFont.render(str("Energy"),True,self.colors["black"])
        window.gameDisplay.blit(self.energyText,(display_width-55,display_height-25))
        window.gameDisplay.blit(window.playerImage, [player.x,player.y])
        window.gameDisplay.blit(self.opponentImage, [opponent.x,opponent.y])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        energyBar0 = pygame.draw.rect(window.gameDisplay,(self.colors["green"]),(display_width-46,display_height-150,40,120))
        #energyBar1 = pygame.draw.rect(window.gameDisplay,(self.colors["green"]),(display_width-50,display_height-150,50-(5*(10-player.fitness)),120))
        pygame.display.set_caption("Play Match")
        pygame.display.set_icon(self.playerImage)

    def setupPlayerWin(self):
        if player.hand == 'Right':
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontright.png')
        else:
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontleft.png')
        if player.level == 2 or player.level == 3 or player.level == 5 or player.level == 10 or player.level == 15 or player.level == 20 or player.level == 30 or player.level == 40 or player.level == 50 or player.level == 60 or player.level == 65 or player.level == 68 or player.level == 75 or player.level == 80 or player.level == 90 or player.level == 95 or player.level == 100:
            self.levelUp = True
        self.bgIntro = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.winText = self.medFont.render(str("You won against"+" "+str(opponent.name+"!")),True,self.colors["black"])
        self.youGotText = self.smallMedFont.render(str("You got a skill point and 100 ranking points!"),True,self.colors["black"])
        self.youAdvancedToText = self.smallMedFont.render(str("You advanced to the "+str(player.currentRound+" in the "+str(player.currentTournament+"!"))),True,self.colors["black"])
        self.youWonText = self.smallMedFont.render(str("You won the "+str(player.currentTournament)+"!"),True,self.colors["black"])
        self.largePlayerName = self.medFont.render(str(player.name),True,window.colors["black"])
        self.largeOpponentName = self.medFont.render(str(opponent.name),True,window.colors["black"])
        self.largeScoreGames = self.medFont.render(str(scoring.playerGames),True,window.colors["black"])
        self.largeOpponentScoreGames = self.medFont.render(str(scoring.opponentGames),True,window.colors["black"])
        self.largeScoreSets = self.medFont.render(str(scoring.playerSets),True,window.colors["black"])
        self.largeOpponentScoreSets = self.medFont.render(str(scoring.opponentSets),True,window.colors["black"])
        self.gameDisplay.blit(self.bgIntro,[0,0])
        window.gameDisplay.blit(self.winText,[330,135]),
        window.gameDisplay.blit(self.largePlayerName,[330,250]),window.gameDisplay.blit(self.largeOpponentName,[630,250])
        window.gameDisplay.blit(self.largeScoreGames,[330,350]),window.gameDisplay.blit(self.largeOpponentScoreGames,[630,350])
        window.gameDisplay.blit(self.largeScoreSets,[330,400]),window.gameDisplay.blit(self.largeOpponentScoreSets,[630,400])
        window.gameDisplay.blit(self.youGotText,[290,480])
        if player.currentTournamentMatchWins == 7:
            window.gameDisplay.blit(self.youWonText,[175,530])
        else:
            window.gameDisplay.blit(self.youAdvancedToText,[70,530])
        pygame.display.set_caption("You Won!")
        pygame.display.set_icon(self.playerImageFront)

    def setupOpponentWin(self):
        self.opponentGotText = self.medFont.render(str(opponent.name+" has gained 100 ranking points."),True,self.colors["black"])
        self.loseText = self.medFont.render(str("You lost against:"+" "+str(opponent.name)+"!"),True,self.colors["black"])
        self.largePlayerName = self.medFont.render(str(player.name),True,window.colors["black"])
        self.largeOpponentName = self.medFont.render(str(opponent.name),True,window.colors["black"])
        self.largeScoreGames = self.medFont.render(str(scoring.playerGames),True,window.colors["black"])
        self.largeOpponentScoreGames = self.medFont.render(str(scoring.opponentGames),True,window.colors["black"])
        self.largeScoreSets = self.medFont.render(str(scoring.playerSets),True,window.colors["black"])
        self.largeOpponentScoreSets = self.medFont.render(str(scoring.opponentSets),True,window.colors["black"])
        self.gameDisplay.blit(self.bgIntro,[0,0])
        window.gameDisplay.blit(self.loseText,[330,135]),
        window.gameDisplay.blit(self.largePlayerName,[330,250]),window.gameDisplay.blit(self.largeOpponentName,[630,250])
        window.gameDisplay.blit(self.largeScoreGames,[330,350]),window.gameDisplay.blit(self.largeOpponentScoreGames,[630,350])
        window.gameDisplay.blit(self.largeScoreSets,[330,400]),window.gameDisplay.blit(self.largeOpponentScoreSets,[630,400])
        window.gameDisplay.blit(self.opponentGotText,[330,480])
        pygame.display.set_caption("You Lost!")
        pygame.display.set_icon(self.opponentImage)

    def setupNextPoint(self):
        player.x += player.xChange
        player.y += player.yChange
        opponent.x += opponent.xChange
        opponent.y += opponent.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        ball.ballX = 600
        ball.ballY = 600
        pygame.display.set_icon(self.playerImage)

    def setupRankings(self):
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.playMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/powerbaseliner.png')
        self.r = 1 #ranking variable
        self.rankPosition = 100 #where the ranking text'x x position is
        self.i = 0 #name variable to increment in opponentNames list
        self.namePosition = 100 #where the player name's x position is.
        self.c = 0 # countries variable
        self.countryPosition = 100
        self.gameDisplay.blit(self.myPlayerCourt,[0,0])
        self.titleText = self.medFont.render(str("Rankings"),True,self.colors["black"])
        self.rankText = self.smallFont.render(str("Rank"),True,self.colors["black"])
        self.nameText = self.smallFont.render(str("Name"),True,self.colors["black"])
        self.countryText = self.smallFont.render(str("Country"),True,self.colors["black"])
        self.pointsText = self.smallFont.render(str("Points"),True,self.colors["black"])
        for i in range(15):
            self.rankNumberText = self.smallFont.render(str(self.r),True,self.colors["black"])
            self.playerNameText = self.smallFont.render(str(opponentNames[self.i]),True,self.colors["black"])
            self.playerCountryText = self.smallFont.render(str(opponentCountries[self.c]),True,self.colors["black"])
            window.gameDisplay.blit(self.rankNumberText,(10,self.rankPosition)),window.gameDisplay.blit(self.playerNameText,(100,self.namePosition))
            window.gameDisplay.blit(self.playerCountryText,(400,self.countryPosition))
            self.r += 1 #makes ranking increase by 1
            self.rankPosition += 50 #makes ranking y position increase by 50
            self.i += 1 #increases list index in opponentNames list by 1
            self.namePosition += 50 #increases x position of name by 50
            self.c += 1
            self.countryPosition += 50
        window.gameDisplay.blit(self.titleText,(520,5)),window.gameDisplay.blit(self.rankText,(10,60)),window.gameDisplay.blit(self.nameText,(100,60)),
        window.gameDisplay.blit(self.countryText,(400,60)),window.gameDisplay.blit(self.pointsText,(700,60)) #blits the text to the screen
        pygame.display.set_caption("Rankings")
        pygame.display.set_icon(self.playMatchIcon)

    def setupControls(self):
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.gameDisplay.blit(self.myPlayerCourt,[0,0])
        self.controlsText = self.largeFont.render(str("Controls"),True,self.colors["black"])
        self.controlsText2 = self.medFont.render(str("Use the arrow keys to move your player."),True,self.colors["black"])
        self.controlsText3 = self.medFont.render(str("Press space to serve."),True,self.colors["black"])
        self.controlsText4 = self.medFont.render(str("Press left CTRL to hit the ball to the left,"),True,self.colors["black"])
        self.controlsText5 = self.medFont.render(str("and left ALT to hit it to the right."),True,self.colors["black"])
        window.gameDisplay.blit(self.controlsText,(465,0)),window.gameDisplay.blit(self.controlsText2,(220,130)),window.gameDisplay.blit(self.controlsText3,(220,235))
        window.gameDisplay.blit(self.controlsText4,(220,360)),window.gameDisplay.blit(self.controlsText5,(220,500))
        pygame.display.set_caption("Controls")
        pygame.display.set_icon(self.myPlayerCourt)

    def setupPause(self):
        self.playMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/powerbaseliner.png')
        self.gameDisplay.blit(pauseMenu.pauseCourt,[0,0])
        self.pausedText = self.largeFont.render(str("Paused"),True,self.colors["black"])
        window.gameDisplay.blit(self.pausedText,(490,0))
        pygame.display.set_caption("Paused")
        pygame.display.set_icon(self.playMatchIcon)

    def setupTrainingMatch(self):
        self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
        if player.hand == 'Right':
            self.playerImage = pygame.image.load('C:/NEA Tennis Game/Player/player1upright.png')
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontright.png')
            self.playerImageRight = pygame.image.load('C:/NEA Tennis Game/Player/player1right.png')
        else:
            self.playerImage = pygame.image.load('C:/NEA Tennis Game/Player/player1upleft.png')
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontleft.png')
            self.playerImageLeft = pygame.image.load('C:/NEA Tennis Game/Player/player1left.png')
        self.trainingMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/volleyer.png')
        player.x += player.xChange
        player.y += player.yChange
        opponent.x += opponent.xChange
        opponent.y += opponent.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        window.gameDisplay.blit(window.playerImage, [player.x,player.y])
        window.gameDisplay.blit(self.opponentImage, [opponent.x,opponent.y])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        pygame.display.set_caption("Training Match")
        pygame.display.set_icon(self.playerImage)

    def setupGameIntro(self):
        self.introIcon = pygame.image.load('C:/NEA Tennis Game/Icons/Apple.png')
        self.bgIntro = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.gameDisplay.blit(self.bgIntro,[0,0])
        self.titleText = self.largeFont.render(str("Tennis Game"),True,self.colors["black"])
        self.versionText = self.smallFont.render(str("Version 1.6"),True,self.colors["black"])
        window.gameDisplay.blit(self.titleText,(375,0)),window.gameDisplay.blit(self.versionText,(10,880))
        pygame.display.set_caption("Tennis Game Intro")
        pygame.display.set_icon(self.introIcon)

    def setupAchievements(self):
        self.achievementsIcon = pygame.image.load('C:/NEA Tennis Game/Icons/Apple.png')
        self.achievementsCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.tick = pygame.image.load('C:/NEA Tennis Game/icons/tick.png')
        self.gameDisplay.blit(self.achievementsCourt,[0,0])
        self.titleText = self.medFont.render(str("Achievements"),True,self.colors["black"])
        self.title1Text = self.smallFont.render(str(winFirstMatch.title),True,self.colors["black"])
        self.name1Text = self.smallFont.render(str(winFirstMatch.name),True,self.colors["black"])
        self.title2Text = self.smallFont.render(str(winFirstTournament.title),True,self.colors["black"])
        self.name2Text = self.smallFont.render(str(winFirstTournament.name),True,self.colors["black"])
        self.title3Text = self.smallFont.render(str(completeAllAchievements.title),True,self.colors["black"])
        self.name3Text = self.smallFont.render(str(completeAllAchievements.name),True,self.colors["black"])
        self.title5Text = self.smallFont.render(str(win100Matches.title),True,self.colors["black"])
        self.name5Text = self.smallFont.render(str(win100Matches.name),True,self.colors["black"])
        self.title6Text = self.smallFont.render(str(winFirstMasters1000.title),True,self.colors["black"])
        self.name6Text = self.smallFont.render(str(winFirstMasters1000.name),True,self.colors["black"])
        self.title7Text = self.smallFont.render(str(winFirstGrandSlam.title),True,self.colors["black"])
        self.name7Text = self.smallFont.render(str(winFirstGrandSlam.name),True,self.colors["black"])
        self.title8Text = self.smallFont.render(str(win20GrandSlams.title),True,self.colors["black"])
        self.name8Text = self.smallFont.render(str(win20GrandSlams.name),True,self.colors["black"])
        self.title9Text = self.smallFont.render(str(beatDjokovic.title),True,self.colors["black"])
        self.name9Text = self.smallFont.render(str(beatDjokovic.name),True,self.colors["black"])
        self.title10Text = self.smallFont.render(str(beatFederer.title),True,self.colors["black"])
        self.name10Text = self.smallFont.render(str(beatFederer.name),True,self.colors["black"])
        self.title11Text = self.smallFont.render(str(beatNadal.title),True,self.colors["black"])
        self.name11Text = self.smallFont.render(str(beatNadal.name),True,self.colors["black"])
        self.title12Text = self.smallFont.render(str(worldNumber1.title),True,self.colors["black"])
        self.name12Text = self.smallFont.render(str(worldNumber1.name),True,self.colors["black"])
        self.title13Text = self.smallFont.render(str(maxUpgrades.title),True,self.colors["black"])
        self.name13Text = self.smallFont.render(str(maxUpgrades.name),True,self.colors["black"])
        
        achievementsMenu.achievementConditions()
            
        if winFirstMatch.completed == True:
            window.gameDisplay.blit(self.tick,(405,100))
        if win100Matches.completed == True:
            window.gameDisplay.blit(self.tick,(405,190))
        if winFirstTournament.completed == True:
            window.gameDisplay.blit(self.tick,(405,285))
        if winFirstMasters1000.completed == True:
            window.gameDisplay.blit(self.tick,(405,380))
        if winFirstGrandSlam.completed == True:
            window.gameDisplay.blit(self.tick,(405,475))
        if win20GrandSlams.completed == True:
            window.gameDisplay.blit(self.tick,(405,570))
        if beatDjokovic.completed == True:
            window.gameDisplay.blit(self.tick,(405,665))
        if beatFederer.completed == True:
            window.gameDisplay.blit(self.tick,(405,760))
        if beatNadal.completed == True:
            window.gameDisplay.blit(self.tick,(405,855))
        if worldNumber1.completed == True:
            window.gameDisplay.blit(self.tick,(905,100))
        if maxUpgrades.completed == True:
            window.gameDisplay.blit(self.tick,(905,195))
        if completeAllAchievements.completed == True:
            window.gameDisplay.blit(self.tick,(905,290))
            
        window.gameDisplay.blit(self.titleText,(475,10))
        window.gameDisplay.blit(self.title1Text,(10,75)),window.gameDisplay.blit(self.name1Text,(10,110))
        window.gameDisplay.blit(self.title5Text,(10,165)),window.gameDisplay.blit(self.name5Text,(10,200))
        window.gameDisplay.blit(self.title2Text,(10,260)),window.gameDisplay.blit(self.name2Text,(10,295))
        window.gameDisplay.blit(self.title6Text,(10,355)),window.gameDisplay.blit(self.name6Text,(10,390))
        window.gameDisplay.blit(self.title7Text,(10,450)),window.gameDisplay.blit(self.name7Text,(10,485))
        window.gameDisplay.blit(self.title8Text,(10,545)),window.gameDisplay.blit(self.name8Text,(10,580))
        window.gameDisplay.blit(self.title9Text,(10,640)),window.gameDisplay.blit(self.name9Text,(10,675))
        window.gameDisplay.blit(self.title10Text,(10,735)),window.gameDisplay.blit(self.name10Text,(10,770))
        window.gameDisplay.blit(self.title11Text,(10,830)),window.gameDisplay.blit(self.name11Text,(10,865))
        window.gameDisplay.blit(self.title12Text,(500,75)),window.gameDisplay.blit(self.name12Text,(500,110))
        window.gameDisplay.blit(self.title13Text,(500,165)),window.gameDisplay.blit(self.name13Text,(500,200))
        window.gameDisplay.blit(self.title3Text,(500,260)),window.gameDisplay.blit(self.name3Text,(500,295))
        pygame.display.set_caption("Achievements")
        pygame.display.set_icon(self.achievementsIcon)
        
    def setupTraining(self):
        self.trainingIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allcourtattacker.png')
        self.trainingCourt = pygame.image.load('C:/NEA Tennis Game/Courts/qatarcourt.png')
        self.gameDisplay.blit(self.trainingCourt,[0,0])
        self.trainingText = self.largeFont.render(str("Training"),True,self.colors["black"])
        window.gameDisplay.blit(self.trainingText,(450,0))
        pygame.display.set_caption("Training")
        pygame.display.set_icon(self.trainingIcon)

    def setupWall(self):
        self.wallIcon = pygame.image.load('C:/NEA Tennis Game/Icons/puncher.png')
        player.x += player.xChange
        player.y += player.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        self.wallHitsText = self.smallFont.render(str("Wall Hits:"+" "+str(player.ranking)),True,self.colors["black"])
        window.gameDisplay.blit(window.playerImage, [player.x,player.y])
        window.gameDisplay.blit(window.wallHitsText, [1010,5])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        pygame.display.set_caption("The Wall")
        pygame.display.set_icon(self.wallIcon)

    def setupMyPlayer(self):
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.coinImage = pygame.image.load('C:/NEA Tennis Game/Shop/coin.png')
        self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedkingdomflag.png')
        if player.hand == 'Left':
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontleft.png')
        elif player.hand == 'Right':
            self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1frontright.png')
        self.largePlayerName = self.medFont.render(str(player.name),True,self.colors["black"])
        self.rankingText = self.smallFont.render(str("Ranking:"+" "+str(player.ranking)),True,self.colors["black"])
        self.countryText = self.smallFont.render(str("Country:"+" "+str(player.country)),True,self.colors["black"])
        self.coinsText = self.smallFont.render(str(player.coins),True,self.colors["black"])
        self.powerText = self.smallFont.render(str("Power:"+" "+str(player.power))+str("%"),True,self.colors["black"])
        self.accuracyText = self.smallFont.render(str("Accuracy:"+" "+str(player.accuracy))+str("%"),True,self.colors["black"])
        self.speedText = self.smallFont.render(str("Speed:"+" "+str(player.speed))+str("%"),True,self.colors["black"])
        self.fitnessText = self.smallFont.render(str("Fitness:"+" "+str(player.fitness))+str("%"),True,self.colors["black"])
        self.difficultyText = self.smallFont.render(str("Difficulty:"+ " "+str(player.difficulty)),True,self.colors["black"])
        self.skillPointsText = self.smallFont.render(str("Skill Points:"+" "+str(player.skillPoints)),True,self.colors["black"])
        self.energyText = self.smallFont.render(str("Energy:"+" "+str(player.energy)),True,self.colors["black"])
        self.levelText = self.smallFont.render(str("Level "+" "+str(player.level)),True,self.colors["black"])
        self.rankingPointsText = self.smallFont.render(str("Ranking Points: "+" "+str(player.rankingPoints)),True,self.colors["black"])
        achievementsMenu.achievementConditions()
        self.gameDisplay.blit(myPlayerMenu.myPlayerCourt,[0,0]),window.gameDisplay.blit(self.playerImageFront, [555,125]),window.gameDisplay.blit(self.coinImage, [850,0])
        window.gameDisplay.blit(self.largePlayerName,(440,40)),window.gameDisplay.blit(self.rankingText,(5,0)),window.gameDisplay.blit(self.countryText,(440,0))
        window.gameDisplay.blit(self.powerText,(300,480)),window.gameDisplay.blit(self.accuracyText,(300,570)),window.gameDisplay.blit(self.speedText,(800,480))
        window.gameDisplay.blit(self.fitnessText,(800,570)),window.gameDisplay.blit(self.difficultyText,(5,50)),window.gameDisplay.blit(self.skillPointsText,(330,220))
        window.gameDisplay.blit(self.coinsText,(800,0)),window.gameDisplay.blit(self.energyText,(800,35)),window.gameDisplay.blit(self.levelText,(950,0)),
        window.gameDisplay.blit(self.rankingPointsText,(170,0)),window.gameDisplay.blit(self.flagImage, [1095,0])
        pygame.display.set_caption("My Player")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupCustomize(self):
        self.customizeIcon = pygame.image.load('C:/NEA Tennis Game/Icons/bulldog.png')
        self.title = self.medFont.render(str("Customize"),True,self.colors["black"])
        self.gameDisplay.blit(myPlayerMenu.myPlayerCourt,[0,0]),window.gameDisplay.blit(self.title,(510,10))
        pygame.display.set_caption("Customize")
        pygame.display.set_icon(self.customizeIcon)

    def setupShop(self):
        self.shopIcon = pygame.image.load('C:/NEA Tennis Game/Shop/coin.png')
        self.shopImage = pygame.image.load('C:/NEA Tennis Game/Shop/shop.png')
        self.coinImage = pygame.image.load('C:/NEA Tennis Game/Shop/coin.png')
        self.smallCoinImage = pygame.image.load('C:/NEA Tennis Game/Shop/smallcoin.png')
        self.skittlesImage = pygame.image.load('C:/NEA Tennis Game/Shop/skittles.png')
        self.skittlesShadow = pygame.image.load('C:/NEA Tennis Game/Shop/skittlesshadow.png')
        self.orangeJuiceImage = pygame.image.load('C:/NEA Tennis Game/Shop/orangejuice.png')
        self.orangeJuiceShadow = pygame.image.load('C:/NEA Tennis Game/Shop/orangejuiceshadow.png')
        self.orangeImage = pygame.image.load('C:/NEA Tennis Game/Shop/orange.png')
        self.orangeShadow = pygame.image.load('C:/NEA Tennis Game/Shop/orangeshadow.png')
        self.fruitShootImage = pygame.image.load('C:/NEA Tennis Game/Shop/fruitshoot.png')
        self.coffeeImage = pygame.image.load('C:/NEA Tennis Game/Shop/coffee.png')
        self.coffeeShadow = pygame.image.load('C:/NEA Tennis Game/Shop/coffeeshadow.png')
        self.doubleDeckerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doubledecker.png')
        self.doubleDeckerShadow = pygame.image.load('C:/NEA Tennis Game/Shop/doubledeckershadow.png')
        self.cokeImage = pygame.image.load('C:/NEA Tennis Game/Shop/coke.png')
        self.cokeShadow = pygame.image.load('C:/NEA Tennis Game/Shop/cokeshadow.png')
        self.lucozadeImage = pygame.image.load('C:/NEA Tennis Game/Shop/lucozade.png')
        self.lucozadeShadow = pygame.image.load('C:/NEA Tennis Game/Shop/lucozadeshadow.png')
        self.bottledWaterImage = pygame.image.load('C:/NEA Tennis Game/Shop/bottledwater.png')
        self.dietCokeImage = pygame.image.load('C:/NEA Tennis Game/Shop/dietcoke.png')
        self.dietCokeShadow = pygame.image.load('C:/NEA Tennis Game/Shop/dietcokeshadow.png')
        self.fruitSaladImage = pygame.image.load('C:/NEA Tennis Game/Shop/fruitsalad.png')
        self.fruitSaladShadow = pygame.image.load('C:/NEA Tennis Game/Shop/fruitsaladshadow.png')
        self.goldenFruitSaladShadow = pygame.image.load('C:/NEA Tennis Game/Shop/goldenfruitsaladshadow.png')
        self.goldenFruitSaladImage = pygame.image.load('C:/NEA Tennis Game/Shop/goldenfruitsalad.png')
        self.cheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/cheeseburger.png')
        self.cheeseburgerShadow = pygame.image.load('C:/NEA Tennis Game/Shop/cheeseburgershadow.png')
        self.doubleCheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doublecheeseburger.png')
        self.doubleCheeseburgerShadow = pygame.image.load('C:/NEA Tennis Game/Shop/doublecheeseburgershadow.png')
        self.doubleBaconCheeseburgerShadow = pygame.image.load('C:/NEA Tennis Game/Shop/doublebaconcheeseburgershadow.png')
        self.doubleBaconCheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doublebaconcheeseburger.png')
        self.shopText = self.medFont.render(str("Food Shop"),True,self.colors["black"])
        self.coinsText = self.smallFont.render(str(player.coins),True,self.colors["black"])
        self.bottledWaterText = self.smallFont.render(str("Water"),True,self.colors["black"])
        self.bottledWaterText2 = self.tinyFont.render(str("+5 energy"),True,self.colors["green"])
        self.bottledWaterCost = self.tinyFont.render(str("10"),True,self.colors["black"])
        self.fruitShootText = self.smallFont.render(str("Fruit Shoot"),True,self.colors["black"])
        self.fruitShootText2 = self.tinyFont.render(str("+10 energy"),True,self.colors["green"])
        self.fruitShootText3 = self.tinyFont.render(str("+0.5 speed"),True,self.colors["green"])
        self.fruitShootText4 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.fruitShootCost = self.tinyFont.render(str("15"),True,self.colors["black"])
        self.coffeeText = self.smallFont.render(str("Coffee"),True,self.colors["black"])
        self.coffeeText2 = self.tinyFont.render(str("+6 energy"),True,self.colors["green"])
        self.coffeeText3 = self.tinyFont.render(str("+1 speed"),True,self.colors["green"])
        self.coffeeText4 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.coffeeCost = self.tinyFont.render(str("13"),True,self.colors["black"])
        self.orangeJuiceText = self.smallFont.render(str("Orange Juice"),True,self.colors["black"])
        self.orangeJuiceText2 = self.tinyFont.render(str("+6 energy"),True,self.colors["green"])
        self.orangeJuiceCost = self.tinyFont.render(str("9"),True,self.colors["black"])
        self.cokeText = self.smallFont.render(str("Coke"),True,self.colors["black"])
        self.cokeText2 = self.tinyFont.render(str("+13 energy"),True,self.colors["green"])
        self.cokeText3 = self.tinyFont.render(str("+0.5 speed"),True,self.colors["green"])
        self.cokeText4 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.cokeCost = self.tinyFont.render(str("20"),True,self.colors["black"])
        self.dietCokeText = self.smallFont.render(str("Diet Coke"),True,self.colors["black"])
        self.dietCokeText2 = self.tinyFont.render(str("+5 energy"),True,self.colors["green"])
        self.dietCokeText3 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.dietCokeCost = self.tinyFont.render(str("8"),True,self.colors["black"])
        self.lucozadeText = self.smallFont.render(str("Lucozade"),True,self.colors["black"])
        self.lucozadeText2 = self.tinyFont.render(str("+15 energy"),True,self.colors["green"])
        self.lucozadeText3 = self.tinyFont.render(str("+1 speed"),True,self.colors["green"])
        self.lucozadeText4 = self.tinyFont.render(str("+1 power"),True,self.colors["green"])
        self.lucozadeCost = self.tinyFont.render(str("25"),True,self.colors["black"])
        self.monsterText = self.smallFont.render(str("Monster"),True,self.colors["black"])
        self.monsterText2 = self.tinyFont.render(str("+10 energy"),True,self.colors["green"])
        self.monsterText3 = self.tinyFont.render(str("+1 speed"),True,self.colors["green"])
        self.monsterCost = self.tinyFont.render(str("17"),True,self.colors["black"])
        self.doubleDeckerText = self.smallFont.render(str("Double Decker"),True,self.colors["black"])
        self.doubleDeckerText2 = self.tinyFont.render(str("+25 energy"),True,self.colors["green"])
        self.doubleDeckerText3 = self.tinyFont.render(str("+0.5 speed"),True,self.colors["green"])
        self.doubleDeckerText4 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.doubleDeckerCost = self.tinyFont.render(str("40"),True,self.colors["black"])
        self.fruitSaladText = self.smallFont.render(str("Fruit Salad"),True,self.colors["black"])
        self.fruitSaladText2 = self.tinyFont.render(str("+20 energy"),True,self.colors["green"])
        self.fruitSaladText3 = self.tinyFont.render(str("+1 accuracy"),True,self.colors["green"])
        self.fruitSaladCost = self.tinyFont.render(str("30"),True,self.colors["black"])
        self.skittlesText = self.smallFont.render(str("Skittles"),True,self.colors["black"])
        self.skittlesText2 = self.tinyFont.render(str("+22 energy"),True,self.colors["green"])
        self.skittlesText3 = self.tinyFont.render(str("+0.5 speed"),True,self.colors["green"])
        self.skittlesText4 = self.tinyFont.render(str("-1 accuracy"),True,self.colors["red"])
        self.skittlesCost = self.tinyFont.render(str("35"),True,self.colors["black"])
        self.proteinBarText = self.smallFont.render(str("Protein Bar"),True,self.colors["black"])
        self.proteinBarText2 = self.tinyFont.render(str("+26 energy"),True,self.colors["green"])
        self.proteinBarText3 = self.tinyFont.render(str("+1 speed"),True,self.colors["green"])
        self.proteinBarCost = self.tinyFont.render(str("35"),True,self.colors["black"])
        self.bananaText = self.smallFont.render(str("Banana"),True,self.colors["black"])
        self.bananaText2 = self.tinyFont.render(str("+15 energy"),True,self.colors["green"])
        self.bananaText3 = self.tinyFont.render(str("+1 fitness"),True,self.colors["green"])
        self.bananaCost = self.tinyFont.render(str("25"),True,self.colors["black"])
        self.orangeText = self.smallFont.render(str("Orange"),True,self.colors["black"])
        self.orangeText2 = self.tinyFont.render(str("+10 energy"),True,self.colors["green"])
        self.orangeText3 = self.tinyFont.render(str("+1 fitness"),True,self.colors["green"])
        self.orangeCost = self.tinyFont.render(str("22"),True,self.colors["black"])
        self.cheeseburgerText = self.smallFont.render(str("Cheeseburger"),True,self.colors["black"])
        self.cheeseburgerText2 = self.tinyFont.render(str("+30 energy"),True,self.colors["green"])
        self.cheeseburgerText3 = self.tinyFont.render(str("+1 power"),True,self.colors["green"])
        self.cheeseburgerText4 = self.tinyFont.render(str("-0.5 fitness"),True,self.colors["red"])
        self.cheeseburgerCost = self.tinyFont.render(str("50"),True,self.colors["black"])
        self.doubleCheeseburgerText = self.smallFont.render(str("Double"),True,self.colors["black"])
        self.doubleCheeseburgerText1 = self.smallFont.render(str("Cheeseburger"),True,self.colors["black"])
        self.doubleCheeseburgerText2 = self.tinyFont.render(str("+40 energy"),True,self.colors["green"])
        self.doubleCheeseburgerText3 = self.tinyFont.render(str("+1 speed and power"),True,self.colors["green"])
        self.doubleCheeseburgerText4 = self.tinyFont.render(str("-1 fitness"),True,self.colors["red"])
        self.doubleCheeseburgerCost = self.tinyFont.render(str("62"),True,self.colors["black"])
        self.goldenFruitSaladText = self.smallFont.render(str("Golden"),True,self.colors["black"])
        self.goldenFruitSaladText1 = self.smallFont.render(str("Fruit Salad"),True,self.colors["black"])
        self.goldenFruitSaladText2 = self.tinyFont.render(str("+42 energy"),True,self.colors["green"])
        self.goldenFruitSaladText3 = self.tinyFont.render(str("+1 accuracy"),True,self.colors["green"])
        self.goldenFruitSaladText4 = self.tinyFont.render(str("+1 power"),True,self.colors["green"])
        self.goldenFruitSaladCost = self.tinyFont.render(str("68"),True,self.colors["black"])
        self.doubleBaconCheeseburgerText = self.smallFont.render(str("Double Bacon"),True,self.colors["black"])
        self.doubleBaconCheeseburgerText1 = self.smallFont.render(str("Cheeseburger"),True,self.colors["black"])
        self.doubleBaconCheeseburgerText2 = self.tinyFont.render(str("+45 energy"),True,self.colors["green"])
        self.doubleBaconCheeseburgerText3 = self.tinyFont.render(str("+1 speed and power"),True,self.colors["green"])
        self.doubleBaconCheeseburgerText4 = self.tinyFont.render(str("+0.5 accuracy"),True,self.colors["green"])
        self.doubleBaconCheeseburgerText5 = self.tinyFont.render(str("-1 fitness"),True,self.colors["red"])
        self.doubleBaconCheeseburgerCost = self.tinyFont.render(str("75"),True,self.colors["black"])
        self.questionMarksText = self.tinyFont.render(str("???"),True,self.colors["black"])
        self.outOfStockText = self.medFont.render(str("Out of stock!"),True,self.colors["black"])
        self.energyText = self.smallFont.render(str("Energy:"+" "+str(player.energy)),True,self.colors["black"])
        self.gameDisplay.blit(self.shopImage,[0,0]),window.gameDisplay.blit(self.shopText, [500,5]),window.gameDisplay.blit(self.coinImage, [1160,0])
        window.gameDisplay.blit(self.coinsText,(1100,0)),window.gameDisplay.blit(self.bottledWaterImage, [50,100]),window.gameDisplay.blit(self.fruitShootImage, [190,95])
        window.gameDisplay.blit(self.bottledWaterText, [35,135]),window.gameDisplay.blit(self.bottledWaterText2, [40,170]),window.gameDisplay.blit(self.bottledWaterCost, [40,255]),window.gameDisplay.blit(self.smallCoinImage, [62,258])
        window.gameDisplay.blit(self.fruitShootText, [150,135]),window.gameDisplay.blit(self.fruitShootText2, [150,170]),window.gameDisplay.blit(self.fruitShootText3, [150,195]),window.gameDisplay.blit(self.fruitShootText4, [150,220]),window.gameDisplay.blit(self.fruitShootCost, [150,255]),window.gameDisplay.blit(self.smallCoinImage, [172,258])
        if player.level < 2:
            window.gameDisplay.blit(self.coffeeShadow, [340,110])
        elif player.level >= 2:
             window.gameDisplay.blit(self.coffeeImage, [340,110]),window.gameDisplay.blit(self.coffeeText, [325,135]),window.gameDisplay.blit(self.coffeeText2, [325,170]),window.gameDisplay.blit(self.coffeeText3, [325,195]),window.gameDisplay.blit(self.coffeeText4, [325,220]),window.gameDisplay.blit(self.coffeeCost, [325,255]),window.gameDisplay.blit(self.smallCoinImage, [347,258])
        if player.level < 3:
            window.gameDisplay.blit(self.orangeJuiceShadow, [505,100])
        elif player.level >= 3:
             window.gameDisplay.blit(self.orangeJuiceImage, [505,100]),window.gameDisplay.blit(self.orangeJuiceText, [450,135]),window.gameDisplay.blit(self.orangeJuiceText2, [450,170]),window.gameDisplay.blit(self.orangeJuiceCost, [450,255]),window.gameDisplay.blit(self.smallCoinImage, [472,258])
        if player.level < 5:
            window.gameDisplay.blit(self.cokeShadow, [635,100])
        elif player.level >= 5:
            window.gameDisplay.blit(self.cokeImage, [635,100]),window.gameDisplay.blit(self.cokeText, [635,135]),window.gameDisplay.blit(self.cokeText2, [635,170]),window.gameDisplay.blit(self.cokeText3, [635,195]),window.gameDisplay.blit(self.cokeText4, [635,220]),window.gameDisplay.blit(self.cokeCost, [635,255]),window.gameDisplay.blit(self.smallCoinImage, [657,258])
        if player.level < 10:
            window.gameDisplay.blit(self.dietCokeShadow, [765,100])
        elif player.level >= 10:
            window.gameDisplay.blit(self.dietCokeImage, [765,100]),window.gameDisplay.blit(self.dietCokeText, [740,135]),window.gameDisplay.blit(self.dietCokeText2, [740,170]),window.gameDisplay.blit(self.dietCokeText3, [740,195]),window.gameDisplay.blit(self.dietCokeCost, [740,255]),window.gameDisplay.blit(self.smallCoinImage, [762,258])
        if player.level < 15:
            window.gameDisplay.blit(self.lucozadeShadow, [905,100])
        elif player.level >= 15:
            window.gameDisplay.blit(self.lucozadeImage, [905,100]),window.gameDisplay.blit(self.lucozadeText, [880,135]),window.gameDisplay.blit(self.lucozadeText2, [880,170]),window.gameDisplay.blit(self.lucozadeText3, [880,195]),window.gameDisplay.blit(self.lucozadeText4, [880,220]),window.gameDisplay.blit(self.lucozadeCost, [880,255]),window.gameDisplay.blit(self.smallCoinImage, [902,258])
        if player.level < 20:
            pass
        elif player.level >= 20:
            window.gameDisplay.blit(self.monsterText, [1010,135]),window.gameDisplay.blit(self.monsterText2, [1010,170]),window.gameDisplay.blit(self.monsterText3, [1010,195]),window.gameDisplay.blit(self.monsterCost, [1010,255]),window.gameDisplay.blit(self.smallCoinImage, [1032,258])
        if player.level < 30:
            window.gameDisplay.blit(self.doubleDeckerShadow, [50,360])
        elif player.level >= 30:
            window.gameDisplay.blit(self.doubleDeckerImage, [50,360]),window.gameDisplay.blit(self.doubleDeckerText, [35,395]),window.gameDisplay.blit(self.doubleDeckerText2, [40,430]),window.gameDisplay.blit(self.doubleDeckerText3, [40,455]),window.gameDisplay.blit(self.doubleDeckerText4, [40,480]),window.gameDisplay.blit(self.doubleDeckerCost, [40,510]),window.gameDisplay.blit(self.smallCoinImage, [62,513])
        if player.level < 40:
            window.gameDisplay.blit(self.fruitSaladShadow, [268,360])
        elif player.level >= 40:
            window.gameDisplay.blit(self.fruitSaladImage, [268,360]),window.gameDisplay.blit(self.fruitSaladText, [230,395]),window.gameDisplay.blit(self.fruitSaladText2, [230,430]),window.gameDisplay.blit(self.fruitSaladText3, [230,455]),window.gameDisplay.blit(self.fruitSaladCost, [230,510]),window.gameDisplay.blit(self.smallCoinImage, [252,513])
        if player.level < 50:
            window.gameDisplay.blit(self.skittlesShadow, [395,360])
        elif player.level >= 50:
            window.gameDisplay.blit(self.skittlesImage, [395,360]),window.gameDisplay.blit(self.skittlesText, [380,395]),window.gameDisplay.blit(self.skittlesText2, [380,430]),window.gameDisplay.blit(self.skittlesText3, [380,455]),window.gameDisplay.blit(self.skittlesText4, [380,480]),window.gameDisplay.blit(self.skittlesCost, [380,510]),window.gameDisplay.blit(self.smallCoinImage, [402,513])
        if player.level < 60:
            pass
        elif player.level >= 60:
            window.gameDisplay.blit(self.proteinBarText, [500,395]),window.gameDisplay.blit(self.proteinBarText2, [500,430]),window.gameDisplay.blit(self.proteinBarText3, [500,455]),window.gameDisplay.blit(self.proteinBarCost, [500,510]),window.gameDisplay.blit(self.smallCoinImage, [522,513])
        if player.level < 65:
            pass
        elif player.level >= 65:
            window.gameDisplay.blit(self.bananaText, [660,395]),window.gameDisplay.blit(self.bananaText2, [660,430]),window.gameDisplay.blit(self.bananaText3, [660,455]),window.gameDisplay.blit(self.bananaCost, [660,510]),window.gameDisplay.blit(self.smallCoinImage, [682,513])
        if player.level < 68:
            window.gameDisplay.blit(self.orangeShadow, [790,360])
        elif player.level >= 68:
            window.gameDisplay.blit(self.orangeImage, [790,360]),window.gameDisplay.blit(self.orangeText, [770,395]),window.gameDisplay.blit(self.orangeText2, [770,430]),window.gameDisplay.blit(self.orangeText3, [770,455]),window.gameDisplay.blit(self.orangeCost, [770,510]),window.gameDisplay.blit(self.smallCoinImage, [792,513])
        if player.level < 75:
            window.gameDisplay.blit(self.cheeseburgerShadow, [915,360])
        elif player.level >= 75:
            window.gameDisplay.blit(self.cheeseburgerImage, [915,360]),window.gameDisplay.blit(self.cheeseburgerText, [870,395]),window.gameDisplay.blit(self.cheeseburgerText2, [880,430]),window.gameDisplay.blit(self.cheeseburgerText3, [880,455]),window.gameDisplay.blit(self.cheeseburgerText4, [880,480]),window.gameDisplay.blit(self.cheeseburgerCost, [880,510]),window.gameDisplay.blit(self.smallCoinImage, [902,513])
        if player.level < 80:
            window.gameDisplay.blit(self.doubleCheeseburgerShadow, [1035,360])
        elif player.level >= 80:
            window.gameDisplay.blit(self.doubleCheeseburgerImage, [1035,360]),window.gameDisplay.blit(self.doubleCheeseburgerText, [1085,370]),window.gameDisplay.blit(self.doubleCheeseburgerText1, [1040,395]),window.gameDisplay.blit(self.doubleCheeseburgerText2, [1040,430]),window.gameDisplay.blit(self.doubleCheeseburgerText3, [1040,455]),window.gameDisplay.blit(self.doubleCheeseburgerText4, [1040,480]),window.gameDisplay.blit(self.doubleCheeseburgerCost, [1040,510]),window.gameDisplay.blit(self.smallCoinImage, [1062,513])
        if player.level < 90:
            window.gameDisplay.blit(self.goldenFruitSaladShadow, [40,580])
        elif player.level >= 90:
            window.gameDisplay.blit(self.goldenFruitSaladImage, [50,580]),window.gameDisplay.blit(self.goldenFruitSaladText, [40,625]),window.gameDisplay.blit(self.goldenFruitSaladText1, [20,655]),window.gameDisplay.blit(self.goldenFruitSaladText2, [20,690]),window.gameDisplay.blit(self.goldenFruitSaladText3, [20,715]),window.gameDisplay.blit(self.goldenFruitSaladText4, [20,740]),window.gameDisplay.blit(self.goldenFruitSaladCost, [20,800]),window.gameDisplay.blit(self.smallCoinImage, [42,803])
        if player.level < 95:
            window.gameDisplay.blit(self.doubleBaconCheeseburgerShadow, [235,580])
        elif player.level >= 95:
            window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [235,580]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText, [195,625]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText1, [190,655]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText2, [190,690]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText3, [190,715]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText4, [190,740]),window.gameDisplay.blit(self.doubleBaconCheeseburgerText5, [190,765]),window.gameDisplay.blit(self.doubleBaconCheeseburgerCost, [190,800]),window.gameDisplay.blit(self.smallCoinImage, [212,803])
        pygame.display.set_caption("Shop"),window.gameDisplay.blit(self.energyText,(850,0)),
        pygame.display.set_icon(self.shopIcon)

    def setupStats(self):
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.coinImage = pygame.image.load('C:/NEA Tennis Game/Shop/coin.png')
        self.smallCoinImage = pygame.image.load('C:/NEA Tennis Game/Shop/smallcoin.png')
        self.statsTitle = self.medFont.render(str("Player Statistics:"+" "+str(player.name)),True,self.colors["black"])
        self.pointsPlayedText = self.smallFont.render(str("Total Points Played:"+" "+str(player.pointsPlayed)),True,self.colors["black"])
        self.matchesPlayedText = self.smallFont.render(str("Matches Played:"+" "+str(player.matchesPlayed)),True,self.colors["black"])
        self.winsText = self.smallFont.render(str("Match Wins/Losses:"+" "+str(player.wins)+"-"+str(player.losses)),True,self.colors["black"])
        self.pointsText = self.smallFont.render(str("Points Wins/Losses:"+" "+str(player.pointsWon)+"-"+str(player.pointsLost)),True,self.colors["black"])
        try:
            self.winPercentText = self.smallFont.render(str("Match Win/Loss %:"+" "+str(player.wins / (player.wins+player.losses) * 100)+"%"),True,self.colors["black"])
            self.winPointsPercentText = self.smallFont.render(str("Points Win/Loss %:"+" "+str(player.pointsWon / (player.pointsWon+player.pointsLost) * 100)+"%"),True,self.colors["black"])
        except ZeroDivisionError:
            self.winPercentText = self.smallFont.render(str("Match Win/Loss %:"+" "+str("0%")),True,self.colors["black"])
            self.winPointsPercentText = self.smallFont.render(str("Points Win/Loss %:"+" "+str("0%")),True,self.colors["black"])
            
        self.tournamentsPlayedText = self.smallFont.render(str("Tournaments Played:"+" "+str(player.tournamentsPlayed)),True,self.colors["black"])
        self.tournamentsWonText = self.smallFont.render(str("Tournaments Won:"+" "+str(player.tournamentWins)),True,self.colors["black"])
        self.grandSlamsWonText = self.smallFont.render(str("Grand Slam Wins:"+" "+str(player.grandSlamWins)),True,self.colors["black"])
        self.masters1000WonText = self.smallFont.render(str("Masters 1000 Wins:"+" "+str(player.masters1000Wins)),True,self.colors["black"])
        self.atp500WonText = self.smallFont.render(str("ATP 500 Wins:"+" "+str(player.atp500Wins)),True,self.colors["black"])
        self.earningsText = self.smallFont.render(str("Earnings:"+" "+str(player.earnings)),True,self.colors["black"])
        self.hitsText = self.smallFont.render(str("Shots Hit:"+" "+str(scoring.hits)),True,self.colors["black"])
        self.winnersText = self.smallFont.render(str("Winners:"+" "+str(scoring.winners)),True,self.colors["black"])
        self.errorsText = self.smallFont.render(str("Errors:"+" "+str(scoring.errors)),True,self.colors["black"])
        self.rallyLengthText = self.smallFont.render(str("Average Rally Length:"+" "+str(scoring.rallyLength)),True,self.colors["black"])
        self.gameDisplay.blit(self.myPlayerCourt,[0,0]),window.gameDisplay.blit(self.statsTitle, [350,20]),window.gameDisplay.blit(self.pointsText, [5,145]),window.gameDisplay.blit(self.winPointsPercentText, [5,185])
        window.gameDisplay.blit(self.pointsPlayedText, [5,100])
        window.gameDisplay.blit(self.winsText, [5,230]),window.gameDisplay.blit(self.matchesPlayedText, [5,275]),window.gameDisplay.blit(self.winPercentText, [5,325]),window.gameDisplay.blit(self.tournamentsPlayedText, [5,375])
        window.gameDisplay.blit(self.tournamentsWonText, [5,425]),window.gameDisplay.blit(self.grandSlamsWonText, [5,470]),window.gameDisplay.blit(self.masters1000WonText, [5,515])
        window.gameDisplay.blit(self.atp500WonText, [5,560]),window.gameDisplay.blit(self.earningsText, [5,605]),window.gameDisplay.blit(self.smallCoinImage, [160,615]),
        window.gameDisplay.blit(self.hitsText, [400,100]),window.gameDisplay.blit(self.winnersText, [400,140]),window.gameDisplay.blit(self.errorsText, [400,180])
        window.gameDisplay.blit(self.rallyLengthText, [400,220])
        pygame.display.set_caption("Player Statistics")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupSaveGame(self):
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot1') ) == 0:
            self.saveSlot1 = False
        else:
            self.saveSlot1 = True
            self.lastModified = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot1/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot2') ) == 0:
            self.saveSlot2 = False
        else:
            self.saveSlot2 = True
            self.lastModified2 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot2/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot3') ) == 0:
            self.saveSlot3 = False
        else:
            self.saveSlot3 = True
            self.lastModified3 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot3/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot4') ) == 0:
            self.saveSlot4 = False
        else:
            self.saveSlot4 = True
            self.lastModified4 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot4/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot5') ) == 0:
            self.saveSlot5 = False
        else:
            self.saveSlot5 = True
            self.lastModified5 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot5/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot6') ) == 0:
            self.saveSlot6 = False
        else:
            self.saveSlot6 = True
            self.lastModified6 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot6/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot7') ) == 0:
            self.saveSlot7 = False
        else:
            self.saveSlot7 = True
            try:
                self.lastModified7 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot7/power.txt'))
            except FileNotFoundError:
                self.lastModified7 = self.smallFont.render(str(""),True,self.colors["black"])
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot8') ) == 0:
            self.saveSlot8 = False
        else:
            self.saveSlot8 = True
            self.lastModified8 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot8/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot1') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot2') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot3') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot4') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot5') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot6') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot7') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot8') ) == 0:
            self.newNewGame = True
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.title = self.medFont.render(str("Save Game"),True,self.colors["black"])
        self.message = self.medFont.render(str("Saved Game!"),True,self.colors["black"])
        self.autoSaveSlot = self.smallFont.render(str("Auto save slot"+ " "),True,self.colors["black"])
        self.saveSlot7NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot7Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.autoSaveSlot2 = self.smallFont.render(str("Auto save slot"+ " "),True,self.colors["black"])
        self.saveSlot1Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlotNoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot2Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot2NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot3Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot3NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot4Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot4NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot5Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot5NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot6Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot6NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot8Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot8NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        window.gameDisplay.blit(self.myPlayerCourt, [0,0]),window.gameDisplay.blit(self.title, [520,20])
        if self.saveSlot1 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot1/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerNameText = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerNameText, [300,110])
            self.saveSlot1Date2 = self.smallFont.render(str(self.lastModified),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot1Date, [520,110]),window.gameDisplay.blit(self.saveSlot1Date2, [685,110])
        elif self.saveSlot1 == False:
            window.gameDisplay.blit(self.saveSlotNoDate, [520,110])
        if self.saveSlot2 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot2/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName2Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName2Text, [300,210])
            self.timeNow = datetime.datetime.now()
            self.saveSlot2Date2 = self.smallFont.render(str(self.lastModified2),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot2Date, [520,210]),window.gameDisplay.blit(self.saveSlot2Date2, [685,210]),window.gameDisplay.blit(self.saveSlot2NoDate, [-100,-100])
        elif self.saveSlot2 == False:
            window.gameDisplay.blit(self.saveSlot2NoDate, [520,210])
        if self.saveSlot3 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot3/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName3Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName3Text, [300,310])
            self.timeNow = datetime.datetime.now()
            self.saveSlot3Date2 = self.smallFont.render(str(self.lastModified3),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot3Date, [520,310]),window.gameDisplay.blit(self.saveSlot3Date2, [685,310]),window.gameDisplay.blit(self.saveSlot3NoDate, [-100,-100])
        elif self.saveSlot3 == False:
            window.gameDisplay.blit(self.saveSlot3NoDate, [520,310])
        if self.saveSlot4 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot4/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName4Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName4Text, [300,410])
            self.timeNow = datetime.datetime.now()
            self.saveSlot4Date2 = self.smallFont.render(str(self.lastModified4),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot4Date, [520,410]),window.gameDisplay.blit(self.saveSlot4Date2, [685,410]),window.gameDisplay.blit(self.saveSlot4NoDate, [-100,-100])
        elif self.saveSlot4 == False:
            window.gameDisplay.blit(self.saveSlot4NoDate, [520,410])
        if self.saveSlot5 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot5/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName5Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName5Text, [300,510])
            self.timeNow = datetime.datetime.now()
            self.saveSlot5Date2 = self.smallFont.render(str(self.lastModified5),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot5Date, [520,510]),window.gameDisplay.blit(self.saveSlot5Date2, [685,510]),window.gameDisplay.blit(self.saveSlot5NoDate, [-100,-100])
        elif self.saveSlot5 == False:
            window.gameDisplay.blit(self.saveSlot5NoDate, [520,510])
        if self.saveSlot6 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot6/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName6Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName6Text, [300,610])
            self.timeNow = datetime.datetime.now()
            self.saveSlot6Date2 = self.smallFont.render(str(self.lastModified6),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot6Date, [520,610]),window.gameDisplay.blit(self.saveSlot6Date2, [685,610]),window.gameDisplay.blit(self.saveSlot6NoDate, [-100,-100])
        elif self.saveSlot6 == False:
            window.gameDisplay.blit(self.saveSlot6NoDate, [520,610])
        if self.saveSlot7 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot7/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName7Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName7Text, [300,710])
            self.timeNow = datetime.datetime.now()
            self.saveSlot7Date2 = self.smallFont.render(str(self.lastModified7),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot7Date, [520,710]),window.gameDisplay.blit(self.saveSlot7Date2, [685,710]),window.gameDisplay.blit(self.saveSlot7NoDate, [-100,-100])
        elif self.saveSlot7 == False:
            window.gameDisplay.blit(self.saveSlot7NoDate, [520,710])

        window.gameDisplay.blit(self.autoSaveSlot, [100,710])
        window.gameDisplay.blit(self.autoSaveSlot, [100,810])
        if self.saveSlot8 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot8/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName8Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName8Text, [300,810])
            self.timeNow = datetime.datetime.now()
            self.saveSlot8Date2 = self.smallFont.render(str(self.lastModified8),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot8Date, [520,810]),window.gameDisplay.blit(self.saveSlot8Date2, [685,810]),window.gameDisplay.blit(self.saveSlot8NoDate, [-100,-100])
        elif self.saveSlot8 == False:
            window.gameDisplay.blit(self.saveSlot8NoDate, [520,810])
            
        pygame.display.set_caption("Save Game")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupLoadGame(self):
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot1') ) == 0:
            self.saveSlot1 = False
        else:
            self.saveSlot1 = True
            self.lastModified = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot1/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot2') ) == 0:
            self.saveSlot2 = False
        else:
            self.saveSlot2 = True
            self.lastModified2 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot2/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot3') ) == 0:
            self.saveSlot3 = False
        else:
            self.saveSlot3 = True
            self.lastModified3 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot3/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot4') ) == 0:
            self.saveSlot4 = False
        else:
            self.saveSlot4 = True
            self.lastModified4 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot4/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot5') ) == 0:
            self.saveSlot5 = False
        else:
            self.saveSlot5 = True
            self.lastModified5 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot5/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot6') ) == 0:
            self.saveSlot6 = False
        else:
            self.saveSlot6 = True
            self.lastModified6 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot6/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot7') ) == 0:
            self.saveSlot7 = False
        else:
            self.saveSlot7 = True
            try:
                self.lastModified7 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot7/power.txt'))
            except FileNotFoundError:
                self.lastModified7 = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot8') ) == 0:
            self.saveSlot8 = False
        else:
            self.saveSlot8 = True
            self.lastModified8 = time.ctime(os.path.getmtime('C:/NEA Tennis Game/Saves/saveslot8/power.txt'))
        if len(os.listdir('C:/NEA Tennis Game/Saves/saveslot1') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot2') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot3') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot4') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot5') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot6') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot7') ) == 0 and len(os.listdir('C:/NEA Tennis Game/Saves/saveslot8') ) == 0:
            window.newNewGame = True
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.title = self.medFont.render(str("Load Game"),True,self.colors["black"])
        self.message = self.medFont.render(str("Saved Game!"),True,self.colors["black"])
        self.saveSlot7NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot7Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot1Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlotNoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot2Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot2NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot3Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot3NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot4Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot4NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot5Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot5NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot6Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot6NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        self.saveSlot8Date = self.smallFont.render(str("Last saved on"+ " "),True,self.colors["black"])
        self.saveSlot8NoDate = self.smallFont.render(str("No game saved to this slot"+ " "),True,self.colors["black"])
        window.gameDisplay.blit(self.myPlayerCourt, [0,0]),window.gameDisplay.blit(self.title, [520,20])
        if self.saveSlot1 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot1/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerNameText = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerNameText, [300,110])
            self.saveSlot1Date2 = self.smallFont.render(str(self.lastModified),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot1Date, [520,110]),window.gameDisplay.blit(self.saveSlot1Date2, [685,110])
        elif self.saveSlot1 == False:
            window.gameDisplay.blit(self.saveSlotNoDate, [520,110])
        if self.saveSlot2 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot2/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName2Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName2Text, [300,210])
            self.timeNow = datetime.datetime.now()
            self.saveSlot2Date2 = self.smallFont.render(str(self.lastModified2),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot2Date, [520,210]),window.gameDisplay.blit(self.saveSlot2Date2, [685,210]),window.gameDisplay.blit(self.saveSlot2NoDate, [-100,-100])
        elif self.saveSlot2 == False:
            window.gameDisplay.blit(self.saveSlot2NoDate, [520,210])
        if self.saveSlot3 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot3/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName3Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName3Text, [300,310])
            self.timeNow = datetime.datetime.now()
            self.saveSlot3Date2 = self.smallFont.render(str(self.lastModified3),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot3Date, [520,310]),window.gameDisplay.blit(self.saveSlot3Date2, [685,310]),window.gameDisplay.blit(self.saveSlot3NoDate, [-100,-100])
        elif self.saveSlot3 == False:
            window.gameDisplay.blit(self.saveSlot3NoDate, [520,310])
        if self.saveSlot4 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot4/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName4Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName4Text, [300,410])
            self.timeNow = datetime.datetime.now()
            self.saveSlot4Date2 = self.smallFont.render(str(self.lastModified4),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot4Date, [520,410]),window.gameDisplay.blit(self.saveSlot4Date2, [685,410]),window.gameDisplay.blit(self.saveSlot4NoDate, [-100,-100])
        elif self.saveSlot4 == False:
            window.gameDisplay.blit(self.saveSlot4NoDate, [520,410])
        if self.saveSlot5 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot5/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName5Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName5Text, [300,510])
            self.timeNow = datetime.datetime.now()
            self.saveSlot5Date2 = self.smallFont.render(str(self.lastModified5),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot5Date, [520,510]),window.gameDisplay.blit(self.saveSlot5Date2, [685,510]),window.gameDisplay.blit(self.saveSlot5NoDate, [-100,-100])
        elif self.saveSlot5 == False:
            window.gameDisplay.blit(self.saveSlot5NoDate, [520,510])
        if self.saveSlot6 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot6/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName6Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName6Text, [300,610])
            self.timeNow = datetime.datetime.now()
            self.saveSlot6Date2 = self.smallFont.render(str(self.lastModified6),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot6Date, [520,610]),window.gameDisplay.blit(self.saveSlot6Date2, [685,610]),window.gameDisplay.blit(self.saveSlot6NoDate, [-100,-100])
        elif self.saveSlot6 == False:
            window.gameDisplay.blit(self.saveSlot6NoDate, [520,610])
        if self.saveSlot7 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot7/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName7Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName7Text, [300,710])
            self.timeNow = datetime.datetime.now()
            self.saveSlot7Date2 = self.smallFont.render(str(self.lastModified7),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot7Date, [520,710]),window.gameDisplay.blit(self.saveSlot7Date2, [685,710]),window.gameDisplay.blit(self.saveSlot7NoDate, [-100,-100])
        elif self.saveSlot7 == False:
            window.gameDisplay.blit(self.saveSlot7NoDate, [520,710])
        if self.saveSlot8 == True:
            contentsList = []
            try:
                file = open('C:/NEA Tennis Game/Saves/saveslot8/name.txt','r')
                contents = file.read()
                contentsList.append(contents)
                player.name = contents
            except FileNotFoundError:
                pass
            self.playerName8Text = self.smallFont.render(str(player.name),True,self.colors["black"])
            window.gameDisplay.blit(self.playerName8Text, [300,810])
            self.timeNow = datetime.datetime.now()
            self.saveSlot8Date2 = self.smallFont.render(str(self.lastModified8),True,self.colors["black"])
            window.gameDisplay.blit(self.saveSlot8Date, [520,810]),window.gameDisplay.blit(self.saveSlot8Date2, [685,810]),window.gameDisplay.blit(self.saveSlot8NoDate, [-100,-100])
        elif self.saveSlot8 == False:
            window.gameDisplay.blit(self.saveSlot8NoDate, [520,810])
            
        pygame.display.set_caption("Load Game")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupTournamentMenu(self):
        if player.monthCount == 1:
            player.currentMonth = 'January'
        if player.monthCount == 2:
            player.currentMonth = 'February'
        if player.monthCount == 3:
            player.currentMonth = 'March'
        elif player.monthCount == 4:
            player.currentMonth = 'April'
        elif player.monthCount == 5:
            player.currentMonth = 'May'
        elif player.monthCount == 6:
            player.currentMonth = 'June'
        elif player.monthCount == 7:
            player.currentMonth = 'July'
        elif player.monthCount == 8:
            player.currentMonth = 'August'
        elif player.monthCount == 9:
            player.currentMonth = 'September'
        elif player.monthCount == 10:
            player.currentMonth = 'October'
        elif player.monthCount == 11:
            player.currentMonth = 'November'
        elif player.monthCount == 12:
            player.currentMonth = 'December'
        elif player.monthCount == 13:
            player.monthCount = 1
            player.currentYear = player.currentYear + 1
        if player.energy == 0:
            pass
        self.wimbledonCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2image.png')
        self.australianOpenCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourtimage.png')
        self.usOpenCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1image.png')
        self.bgIntro = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.frenchOpenCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/claycourt1image.png')
        self.cincinattiCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/cincinatticourtimage.png')
        self.indianWellsCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/indianwellscourtimage.png')
        self.madridCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/madridcourtimage.png')
        self.miamiCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/miamicourtimage.png')
        self.monteCarloCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/montecarlocourtimage.png')
        self.parisCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/pariscourtimage.png')
        self.rogersCupCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/rogerscupcourtimage.png')
        self.romeCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/romecourtimage.png')
        self.shanghaiCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourtimage.png')
        self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1front.png')
        self.smallCoinImage = pygame.image.load('C:/NEA Tennis Game/Shop/smallcoin.png')
        self.laverCupCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/lavercupcourtimage.png')
        self.atpCupCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/atpcupcourtimage.png')
        self.atpFinalsCourtImage = pygame.image.load('C:/NEA Tennis Game/Courts/atpfinalscourtimage.png')
        self.atpFinalsNameText = self.smallFont.render(str(atpFinals.name),True,self.colors["black"])
        self.atpFinalsCityText = self.smallFont.render(str(atpFinals.city+", "+str(atpFinals.country)),True,self.colors["black"])
        self.atpFinalsLevelText = self.smallFont.render(str(atpFinals.level),True,self.colors["black"])
        self.atpFinalsPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(atpFinals.prizeMoney)),True,self.colors["black"])
        self.atpFinalsRankingPointsText = self.smallFont.render(str(atpFinals.rankingPoints),True,self.colors["green"])
        self.atpFinalsSkillPointsText = self.smallFont.render(str(atpFinals.skillPoints),True,self.colors["black"])
        self.atpCupNameText = self.smallFont.render(str(atpCup.name),True,self.colors["black"])
        self.atpCupCityText = self.smallFont.render(str(atpCup.city+", "+str(atpCup.country)),True,self.colors["black"])
        self.atpCupLevelText = self.smallFont.render(str(atpCup.level),True,self.colors["black"])
        self.atpCupPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(atpCup.prizeMoney)),True,self.colors["black"])
        self.atpCupRankingPointsText = self.smallFont.render(str(atpCup.rankingPoints),True,self.colors["green"])
        self.atpCupSkillPointsText = self.smallFont.render(str(atpCup.skillPoints),True,self.colors["black"])
        self.laverCupNameText = self.smallFont.render(str(laverCup.name),True,self.colors["black"])
        self.laverCupCityText = self.smallFont.render(str(laverCup.city+", "+str(laverCup.country)),True,self.colors["black"])
        self.laverCupLevelText = self.smallFont.render(str(laverCup.level),True,self.colors["black"])
        self.laverCupPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(laverCup.prizeMoney)),True,self.colors["black"])
        self.laverCupRankingPointsText = self.smallFont.render(str(laverCup.rankingPoints),True,self.colors["green"])
        self.laverCupSkillPointsText = self.smallFont.render(str(laverCup.skillPoints),True,self.colors["black"])
        self.tokyoOlympicsNameText = self.smallFont.render(str(tokyoOlympics.name),True,self.colors["black"])
        self.tokyoOlympicsCityText = self.smallFont.render(str(tokyoOlympics.city+", "+str(tokyoOlympics.country)),True,self.colors["black"])
        self.tokyoOlympicsLevelText = self.smallFont.render(str(tokyoOlympics.level),True,self.colors["black"])
        self.tokyoOlympicsPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(tokyoOlympics.prizeMoney)),True,self.colors["black"])
        self.tokyoOlympicsRankingPointsText = self.smallFont.render(str(tokyoOlympics.rankingPoints),True,self.colors["green"])
        self.tokyoOlympicsSkillPointsText = self.smallFont.render(str(tokyoOlympics.skillPoints),True,self.colors["black"])
        self.davisCupFinalsNameText = self.smallFont.render(str(davisCupFinals.name),True,self.colors["black"])
        self.davisCupFinalsCityText = self.smallFont.render(str(davisCupFinals.city+", "+str(davisCupFinals.country)),True,self.colors["black"])
        self.davisCupFinalsLevelText = self.smallFont.render(str(davisCupFinals.level),True,self.colors["black"])
        self.davisCupFinalsPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(davisCupFinals.prizeMoney)),True,self.colors["black"])
        self.davisCupFinalsRankingPointsText = self.smallFont.render(str(davisCupFinals.rankingPoints),True,self.colors["green"])
        self.davisCupFinalsSkillPointsText = self.smallFont.render(str(davisCupFinals.skillPoints),True,self.colors["black"])
        
        #Grand Slams
        self.title = self.medFont.render(str("Select Tournament -"+" "+player.currentMonth+" "+str(player.currentYear)),True,self.colors["black"])
        self.nameText1 = self.smallFont.render(str(wimbledon.name),True,self.colors["black"])
        self.countryText1 = self.smallFont.render(str(wimbledon.country),True,self.colors["black"])
        self.cityText1 = self.smallFont.render(str(wimbledon.city+", "+str(wimbledon.country)),True,self.colors["black"])
        self.nameText2 = self.smallFont.render(str(frenchOpen.name),True,self.colors["black"])
        self.cityText2 = self.smallFont.render(str(frenchOpen.city+", "+str(frenchOpen.country)),True,self.colors["black"])
        self.nameText3 = self.smallFont.render(str(australianOpen.name),True,self.colors["black"])
        self.cityText3 = self.smallFont.render(str(australianOpen.city+", "+str(australianOpen.country)),True,self.colors["black"])
        self.nameText4 = self.smallFont.render(str(usOpen.name),True,self.colors["black"])
        self.cityText4 = self.smallFont.render(str(usOpen.city+", "+str(usOpen.country)),True,self.colors["black"])
        self.nameText5 = self.smallFont.render(str(atpFinals.name),True,self.colors["black"])
        self.cityText5 = self.smallFont.render(str(atpFinals.city+", "+str(atpFinals.country)),True,self.colors["black"])
        self.levelText1 = self.smallFont.render(str(wimbledon.level),True,self.colors["black"])
        self.prizeMoneyText1 = self.smallFont.render(str("Prize Money:"+" "+str(wimbledon.prizeMoney)),True,self.colors["black"])
        self.prizeMoneyText2 = self.smallFont.render(str("Prize Money:"+" "+str(frenchOpen.prizeMoney)),True,self.colors["black"])
        self.prizeMoneyText3 = self.smallFont.render(str("Prize Money:"+" "+str(australianOpen.prizeMoney)),True,self.colors["black"])
        self.prizeMoneyText4 = self.smallFont.render(str("Prize Money:"+" "+str(usOpen.prizeMoney)),True,self.colors["black"])
        self.prizeMoneyText5 = self.smallFont.render(str("Prize Money:"+" "+str(atpFinals.prizeMoney)),True,self.colors["black"])
        self.rankingPointsText1 = self.smallFont.render(str(wimbledon.rankingPoints),True,self.colors["green"])
        self.skillPointsText1 = self.smallFont.render(str(wimbledon.skillPoints),True,self.colors["black"])
        #Masters 1000s
        self.masters1000SkillPointsText = self.smallFont.render(str(cincinatti.skillPoints),True,self.colors["black"])
        self.masters1000LevelText = self.smallFont.render(str(cincinatti.level),True,self.colors["black"])
        self.masters1000RankingPointsText = self.smallFont.render(str(cincinatti.rankingPoints),True,self.colors["yellow"])
        self.cincinattiNameText = self.smallFont.render(str(cincinatti.name),True,self.colors["black"])
        self.cincinattiCityText = self.smallFont.render(str(cincinatti.city+", "+str(cincinatti.country)),True,self.colors["black"])
        self.cincinattiPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(cincinatti.prizeMoney)),True,self.colors["black"])
        self.indianWellsNameText = self.smallFont.render(str(indianWells.name),True,self.colors["black"])
        self.indianWellsCityText = self.smallFont.render(str(indianWells.city+", "+str(indianWells.country)),True,self.colors["black"])
        self.indianWellsPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(indianWells.prizeMoney)),True,self.colors["black"])
        self.madridNameText = self.smallFont.render(str(madridOpen.name),True,self.colors["black"])
        self.madridCityText = self.smallFont.render(str(madridOpen.city+", "+str(madridOpen.country)),True,self.colors["black"])
        self.madridPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(madridOpen.prizeMoney)),True,self.colors["black"])
        self.miamiNameText = self.smallFont.render(str(miamiOpen.name),True,self.colors["black"])
        self.miamiCityText = self.smallFont.render(str(miamiOpen.city+", "+str(miamiOpen.country)),True,self.colors["black"])
        self.miamiPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(miamiOpen.prizeMoney)),True,self.colors["black"])
        self.monteCarloNameText = self.smallFont.render(str(monteCarlo.name),True,self.colors["black"])
        self.monteCarloCityText = self.smallFont.render(str(monteCarlo.city+", "+str(monteCarlo.country)),True,self.colors["black"])
        self.monteCarloPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(monteCarlo.prizeMoney)),True,self.colors["black"])
        self.parisNameText = self.smallFont.render(str(paris.name),True,self.colors["black"])
        self.parisCityText = self.smallFont.render(str(paris.city+", "+str(paris.country)),True,self.colors["black"])
        self.parisPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(paris.prizeMoney)),True,self.colors["black"])
        self.romeNameText = self.smallFont.render(str(rome.name),True,self.colors["black"])
        self.romeCityText = self.smallFont.render(str(rome.city+", "+str(rome.country)),True,self.colors["black"])
        self.romePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(rome.prizeMoney)),True,self.colors["black"])
        self.rogersCupNameText = self.smallFont.render(str(rogersCup.name),True,self.colors["black"])
        self.rogersCupCityText = self.smallFont.render(str(rogersCup.city+", "+str(rogersCup.country)),True,self.colors["black"])
        self.rogersCupPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(rogersCup.prizeMoney)),True,self.colors["black"])
        self.shanghaiNameText = self.smallFont.render(str(shanghai.name),True,self.colors["black"])
        self.shanghaiCityText = self.smallFont.render(str(shanghai.city+", "+str(shanghai.country)),True,self.colors["black"])
        self.shanghaiPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(shanghai.prizeMoney)),True,self.colors["black"])
        #ATP 500s
        self.atp500SkillPointsText = self.smallFont.render(str(dubai.skillPoints),True,self.colors["black"])
        self.atp500LevelText = self.smallFont.render(str(dubai.level),True,self.colors["black"])
        self.atp500RankingPointsText = self.smallFont.render(str(dubai.rankingPoints),True,self.colors["grey"])
        self.rotterdamNameText = self.smallFont.render(str(rotterdam.name),True,self.colors["black"])
        self.rotterdamCityText = self.smallFont.render(str(rotterdam.city+", "),True,self.colors["black"])
        self.rotterdamCityText2 = self.smallFont.render(str(rotterdam.country),True,self.colors["black"])
        self.rotterdamPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(rotterdam.prizeMoney)),True,self.colors["black"])
        self.rioNameText = self.smallFont.render(str(rio.name),True,self.colors["black"])
        self.rioCityText = self.smallFont.render(str(rio.city+", "+str(rio.country)),True,self.colors["black"])
        self.rioPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(rio.prizeMoney)),True,self.colors["black"])
        self.dubaiNameText = self.smallFont.render(str(dubai.name),True,self.colors["black"])
        self.dubaiCityText = self.smallFont.render(str(dubai.city+", "+str(dubai.country)),True,self.colors["black"])
        self.dubaiPrizeMoneyText = self.smallFont.render(str("Prize Money:"),True,self.colors["black"])
        self.dubaiPrizeMoneyText2 = self.smallFont.render(str(dubai.prizeMoney),True,self.colors["black"])
        self.acapulcoNameText = self.smallFont.render(str(acapulco.name),True,self.colors["black"])
        self.acapulcoCityText = self.smallFont.render(str(acapulco.city+", "+str(acapulco.country)),True,self.colors["black"])
        self.acapulcoPrizeMoneyText = self.smallFont.render(str("Prize Money:"),True,self.colors["black"])
        self.acapulcoPrizeMoneyText2 = self.smallFont.render(str(acapulco.prizeMoney),True,self.colors["black"])
        self.barcelonaNameText = self.smallFont.render(str(barcelona.name),True,self.colors["black"])
        self.barcelonaCityText = self.smallFont.render(str(barcelona.city+", "+str(barcelona.country)),True,self.colors["black"])
        self.barcelonaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(barcelona.prizeMoney)),True,self.colors["black"])
        self.londonNameText = self.smallFont.render(str(london.name),True,self.colors["black"])
        self.londonCityText = self.smallFont.render(str(london.city+", "+str(london.country)),True,self.colors["black"])
        self.londonPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(london.prizeMoney)),True,self.colors["black"])
        self.halleNameText = self.smallFont.render(str(halle.name),True,self.colors["black"])
        self.halleCityText = self.smallFont.render(str(halle.city+", "+str(halle.country)),True,self.colors["black"])
        self.hallePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(halle.prizeMoney)),True,self.colors["black"])
        self.hamburgNameText = self.smallFont.render(str(hamburg.name),True,self.colors["black"])
        self.hamburgCityText = self.smallFont.render(str(hamburg.city+", "+str(hamburg.country)),True,self.colors["black"])
        self.hamburgPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(hamburg.prizeMoney)),True,self.colors["black"])
        self.washingtonNameText = self.smallFont.render(str(washington.name),True,self.colors["black"])
        self.washingtonCityText = self.smallFont.render(str(washington.city+", "+str(washington.country)),True,self.colors["black"])
        self.washingtonPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(washington.prizeMoney)),True,self.colors["black"])
        self.beijingNameText = self.smallFont.render(str(beijing.name),True,self.colors["black"])
        self.beijingCityText = self.smallFont.render(str(beijing.city+", "+str(beijing.country)),True,self.colors["black"])
        self.beijingPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(beijing.prizeMoney)),True,self.colors["black"])
        self.tokyoNameText = self.smallFont.render(str(tokyo.name),True,self.colors["black"])
        self.tokyoCityText = self.smallFont.render(str(tokyo.city+", "+str(tokyo.country)),True,self.colors["black"])
        self.tokyoPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(tokyo.prizeMoney)),True,self.colors["black"])
        self.viennaNameText = self.smallFont.render(str(vienna.name),True,self.colors["black"])
        self.viennaCityText = self.smallFont.render(str(vienna.city+", "+str(vienna.country)),True,self.colors["black"])
        self.viennaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(vienna.prizeMoney)),True,self.colors["black"])
        self.baselNameText = self.smallFont.render(str(basel.name),True,self.colors["black"])
        self.baselCityText = self.smallFont.render(str(basel.city+", "+str(basel.country)),True,self.colors["black"])
        self.baselPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(basel.prizeMoney)),True,self.colors["black"])
        self.hamburgNameText = self.smallFont.render(str(hamburg.name),True,self.colors["black"])
        self.hamburgCityText = self.smallFont.render(str(hamburg.city+", "+str(hamburg.country)),True,self.colors["black"])
        self.hamburgPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(hamburg.prizeMoney)),True,self.colors["black"])
        self.hamburgNameText = self.smallFont.render(str(hamburg.name),True,self.colors["black"])
        self.hamburgCityText = self.smallFont.render(str(hamburg.city+", "+str(hamburg.country)),True,self.colors["black"])
        self.hamburgPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(hamburg.prizeMoney)),True,self.colors["black"])
        #ATP 250s
        self.atp250SkillPointsText = self.smallFont.render(str(adelaide.skillPoints),True,self.colors["black"])
        self.atp250LevelText = self.smallFont.render(str(adelaide.level),True,self.colors["black"])
        self.atp250RankingPointsText = self.smallFont.render(str(adelaide.rankingPoints),True,self.colors["darkBlue"])
        self.dohaNameText = self.smallFont.render(str(doha.name),True,self.colors["black"])
        self.dohaCityText = self.smallFont.render(str(doha.city+", "+str(doha.country)),True,self.colors["black"])
        self.dohaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(doha.prizeMoney)),True,self.colors["black"])
        
        self.adelaideNameText = self.smallFont.render(str(adelaide.name),True,self.colors["black"])
        self.adelaideCityText = self.smallFont.render(str(adelaide.city+", "+str(adelaide.country)),True,self.colors["black"])
        self.adelaidePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(adelaide.prizeMoney)),True,self.colors["black"])
        
        self.aucklandNameText = self.smallFont.render(str(auckland.name),True,self.colors["black"])
        self.aucklandCityText = self.smallFont.render(str(auckland.city+", "+str(auckland.country)),True,self.colors["black"])
        self.aucklandPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(auckland.prizeMoney)),True,self.colors["black"])
        
        self.cordobaNameText = self.smallFont.render(str(cordoba.name),True,self.colors["black"])
        self.cordobaCityText = self.smallFont.render(str(cordoba.city+", "+str(cordoba.country)),True,self.colors["black"])
        self.cordobaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(cordoba.prizeMoney)),True,self.colors["black"])
        
        self.puneNameText = self.smallFont.render(str(pune.name),True,self.colors["black"])
        self.puneCityText = self.smallFont.render(str(pune.city+", "+str(pune.country)),True,self.colors["black"])
        self.punePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(pune.prizeMoney)),True,self.colors["black"])
        
        self.montpellierNameText = self.smallFont.render(str(montpellier.name),True,self.colors["black"])
        self.montpellierCityText = self.smallFont.render(str(montpellier.city+", "+str(montpellier.country)),True,self.colors["black"])
        self.montpellierPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(montpellier.prizeMoney)),True,self.colors["black"])
        self.newYorkNameText = self.smallFont.render(str(newYork.name),True,self.colors["black"])
        self.newYorkCityText = self.smallFont.render(str(newYork.city+", "+str(newYork.country)),True,self.colors["black"])
        self.newYorkPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(newYork.prizeMoney)),True,self.colors["black"])
        self.buenosAiresNameText = self.smallFont.render(str(buenosAires.name),True,self.colors["black"])
        self.buenosAiresCityText = self.smallFont.render(str(buenosAires.city+", "+str(buenosAires.country)),True,self.colors["black"])
        self.buenosAiresPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(buenosAires.prizeMoney)),True,self.colors["black"])
        self.marseilleNameText = self.smallFont.render(str(marseille.name),True,self.colors["black"])
        self.marseilleCityText = self.smallFont.render(str(marseille.city+", "+str(marseille.country)),True,self.colors["black"])
        self.marseillePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(marseille.prizeMoney)),True,self.colors["black"])
        self.delrayBeachNameText = self.smallFont.render(str(delrayBeach.name),True,self.colors["black"])
        self.delrayBeachCityText = self.smallFont.render(str(delrayBeach.city+", "+str(delrayBeach.country)),True,self.colors["black"])
        self.delrayBeachPrizeMoneyText = self.smallFont.render(str("Prize Money:"),True,self.colors["black"])
        self.delrayBeachPrizeMoneyText2 = self.smallFont.render(str(delrayBeach.prizeMoney),True,self.colors["black"])
        self.santiagoNameText = self.smallFont.render(str(santiago.name),True,self.colors["black"])
        self.santiagoCityText = self.smallFont.render(str(santiago.city+", "+str(santiago.country)),True,self.colors["black"])
        self.santiagoPrizeMoneyText = self.smallFont.render(str("Prize Money:"),True,self.colors["black"])
        self.santiagoPrizeMoneyText2 = self.smallFont.render(str(santiago.prizeMoney),True,self.colors["black"])
        self.houstonNameText = self.smallFont.render(str(houston.name),True,self.colors["black"])
        self.houstonCityText = self.smallFont.render(str(houston.city+", "+str(houston.country)),True,self.colors["black"])
        self.houstonPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(houston.prizeMoney)),True,self.colors["black"])
        self.marrakechNameText = self.smallFont.render(str(marrakech.name),True,self.colors["black"])
        self.marrakechCityText = self.smallFont.render(str(marrakech.city+", "+str(marrakech.country)),True,self.colors["black"])
        self.marrakechPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(marrakech.prizeMoney)),True,self.colors["black"])
        self.budapestNameText = self.smallFont.render(str(budapest.name),True,self.colors["black"])
        self.budapestCityText = self.smallFont.render(str(budapest.city+", "+str(budapest.country)),True,self.colors["black"])
        self.budapestPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(budapest.prizeMoney)),True,self.colors["black"])
        self.munichNameText = self.smallFont.render(str(munich.name),True,self.colors["black"])
        self.munichCityText = self.smallFont.render(str(munich.city+", "+str(munich.country)),True,self.colors["black"])
        self.munichPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(munich.prizeMoney)),True,self.colors["black"])
        self.estorilNameText = self.smallFont.render(str(estoril.name),True,self.colors["black"])
        self.estorilCityText = self.smallFont.render(str(estoril.city+", "+str(estoril.country)),True,self.colors["black"])
        self.estorilPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(estoril.prizeMoney)),True,self.colors["black"])
        self.genevaNameText = self.smallFont.render(str(geneva.name),True,self.colors["black"])
        self.genevaCityText = self.smallFont.render(str(geneva.city+", "+str(geneva.country)),True,self.colors["black"])
        self.genevaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(geneva.prizeMoney)),True,self.colors["black"])
        self.lyonNameText = self.smallFont.render(str(lyon.name),True,self.colors["black"])
        self.lyonCityText = self.smallFont.render(str(lyon.city+", "+str(lyon.country)),True,self.colors["black"])
        self.lyonPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(lyon.prizeMoney)),True,self.colors["black"])
        self.stuttgartNameText = self.smallFont.render(str(stuttgart.name),True,self.colors["black"])
        self.stuttgartCityText = self.smallFont.render(str(stuttgart.city+", "+str(stuttgart.country)),True,self.colors["black"])
        self.stuttgartPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(stuttgart.prizeMoney)),True,self.colors["black"])
        self.sHertogenboschNameText = self.smallFont.render(str(sHertogenbosch.name),True,self.colors["black"])
        self.sHertogenboschCityText = self.smallFont.render(str(sHertogenbosch.city+", "+str(sHertogenbosch.country)),True,self.colors["black"])
        self.sHertogenboschPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(sHertogenbosch.prizeMoney)),True,self.colors["black"])
        self.mallorcaNameText = self.smallFont.render(str(mallorca.name),True,self.colors["black"])
        self.mallorcaCityText = self.smallFont.render(str(mallorca.city+", "+str(mallorca.country)),True,self.colors["black"])
        self.mallorcaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(mallorca.prizeMoney)),True,self.colors["black"])
        self.eastbourneNameText = self.smallFont.render(str(eastbourne.name),True,self.colors["black"])
        self.eastbourneCityText = self.smallFont.render(str(eastbourne.city+", "+str(eastbourne.country)),True,self.colors["black"])
        self.eastbournePrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(eastbourne.prizeMoney)),True,self.colors["black"])
        self.newportNameText = self.smallFont.render(str(newport.name),True,self.colors["black"])
        self.newportCityText = self.smallFont.render(str(newport.city+", "+str(newport.country)),True,self.colors["black"])
        self.newportPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(newport.prizeMoney)),True,self.colors["black"])
        self.bastadNameText = self.smallFont.render(str(bastad.name),True,self.colors["black"])
        self.bastadCityText = self.smallFont.render(str(bastad.city+", "+str(bastad.country)),True,self.colors["black"])
        self.bastadPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(bastad.prizeMoney)),True,self.colors["black"])
        self.losCabosNameText = self.smallFont.render(str(losCabos.name),True,self.colors["black"])
        self.losCabosCityText = self.smallFont.render(str(losCabos.city+", "+str(losCabos.country)),True,self.colors["black"])
        self.losCabosPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(losCabos.prizeMoney)),True,self.colors["black"])
        self.gstaadNameText = self.smallFont.render(str(gstaad.name),True,self.colors["black"])
        self.gstaadCityText = self.smallFont.render(str(gstaad.city+", "+str(gstaad.country)),True,self.colors["black"])
        self.gstaadPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(gstaad.prizeMoney)),True,self.colors["black"])
        self.umagNameText = self.smallFont.render(str(umag.name),True,self.colors["black"])
        self.umagCityText = self.smallFont.render(str(umag.city+", "+str(umag.country)),True,self.colors["black"])
        self.umagPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(umag.prizeMoney)),True,self.colors["black"])
        self.atlantaNameText = self.smallFont.render(str(atlanta.name),True,self.colors["black"])
        self.atlantaCityText = self.smallFont.render(str(atlanta.city+", "+str(atlanta.country)),True,self.colors["black"])
        self.atlantaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(atlanta.prizeMoney)),True,self.colors["black"])
        self.kitzbuhelNameText = self.smallFont.render(str(kitzbuhel.name),True,self.colors["black"])
        self.kitzbuhelCityText = self.smallFont.render(str(kitzbuhel.city+", "+str(kitzbuhel.country)),True,self.colors["black"])
        self.kitzbuhelPrizeMoneyText = self.smallFont.render(str("Prize Money:"),True,self.colors["black"])
        self.kitzbuhelPrizeMoneyText2 = self.smallFont.render(str(kitzbuhel.prizeMoney),True,self.colors["black"])
        self.winstonSalemNameText = self.smallFont.render(str(winstonSalem.name),True,self.colors["black"])
        self.winstonSalemCityText = self.smallFont.render(str(winstonSalem.city+", "+str(winstonSalem.country)),True,self.colors["black"])
        self.winstonSalemPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(winstonSalem.prizeMoney)),True,self.colors["black"])
        self.stPetersburgNameText = self.smallFont.render(str(stPetersburg.name),True,self.colors["black"])
        self.stPetersburgCityText = self.smallFont.render(str(stPetersburg.city+", "+str(stPetersburg.country)),True,self.colors["black"])
        self.stPetersburgPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(stPetersburg.prizeMoney)),True,self.colors["black"])
        self.metzNameText = self.smallFont.render(str(metz.name),True,self.colors["black"])
        self.metzCityText = self.smallFont.render(str(metz.city+", "+str(metz.country)),True,self.colors["black"])
        self.metzPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(metz.prizeMoney)),True,self.colors["black"])
        self.chengduNameText = self.smallFont.render(str(chengdu.name),True,self.colors["black"])
        self.chengduCityText = self.smallFont.render(str(chengdu.city+", "+str(chengdu.country)),True,self.colors["black"])
        self.chengduPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(chengdu.prizeMoney)),True,self.colors["black"])
        self.zhuhaiNameText = self.smallFont.render(str(zhuhai.name),True,self.colors["black"])
        self.zhuhaiCityText = self.smallFont.render(str(zhuhai.city+", "+str(zhuhai.country)),True,self.colors["black"])
        self.zhuhaiPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(zhuhai.prizeMoney)),True,self.colors["black"])
        self.sofiaNameText = self.smallFont.render(str(sofia.name),True,self.colors["black"])
        self.sofiaCityText = self.smallFont.render(str(sofia.city+", "+str(sofia.country)),True,self.colors["black"])
        self.sofiaPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(sofia.prizeMoney)),True,self.colors["black"])
        self.moscowNameText = self.smallFont.render(str(moscow.name),True,self.colors["black"])
        self.moscowCityText = self.smallFont.render(str(moscow.city+", "+str(moscow.country)),True,self.colors["black"])
        self.moscowPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(moscow.prizeMoney)),True,self.colors["black"])
        self.antwerpNameText = self.smallFont.render(str(antwerp.name),True,self.colors["black"])
        self.antwerpCityText = self.smallFont.render(str(antwerp.city+", "+str(antwerp.country)),True,self.colors["black"])
        self.antwerpPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(antwerp.prizeMoney)),True,self.colors["black"])
        self.stockholmNameText = self.smallFont.render(str(stockholm.name),True,self.colors["black"])
        self.stockholmCityText = self.smallFont.render(str(stockholm.city+", "+str(stockholm.country)),True,self.colors["black"])
        self.stockholmPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(stockholm.prizeMoney)),True,self.colors["black"])
        self.metzNameText = self.smallFont.render(str(metz.name),True,self.colors["black"])
        self.metzCityText = self.smallFont.render(str(metz.city+", "+str(metz.country)),True,self.colors["black"])
        self.metzPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(metz.prizeMoney)),True,self.colors["black"])
        self.metzNameText = self.smallFont.render(str(metz.name),True,self.colors["black"])
        self.metzCityText = self.smallFont.render(str(metz.city+", "+str(metz.country)),True,self.colors["black"])
        self.metzPrizeMoneyText = self.smallFont.render(str("Prize Money:"+" "+str(metz.prizeMoney)),True,self.colors["black"])
        self.gameDisplay.blit(self.bgIntro,[0,0])
        window.gameDisplay.blit(self.title,[300,0])

        if player.currentMonth == 'January':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            
            window.gameDisplay.blit(self.atpCupNameText,[10,70])
            window.gameDisplay.blit(self.atpCupRankingPointsText,[180,112]),window.gameDisplay.blit(self.atpCupPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.atpCupCityText,[10,240])
            
            window.gameDisplay.blit(self.dohaNameText,[10,300])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,340]),window.gameDisplay.blit(self.dohaPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.dohaCityText,[10,470])

            window.gameDisplay.blit(self.adelaideNameText,[10,520])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,565]),window.gameDisplay.blit(self.adelaidePrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.adelaideCityText,[10,695])

            window.gameDisplay.blit(self.aucklandNameText,[10,740])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,785]),window.gameDisplay.blit(self.aucklandPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.aucklandCityText,[180,860])

            window.gameDisplay.blit(self.nameText3,[420,70])
            window.gameDisplay.blit(self.rankingPointsText1,[600,112]),window.gameDisplay.blit(self.prizeMoneyText1,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.cityText3,[420,240])
        elif player.currentMonth == 'February':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340]),self.gameDisplay.blit(self.monteCarloCourtImage,[420,560]),self.gameDisplay.blit(self.madridCourtImage,[420,780])
            self.gameDisplay.blit(self.romeCourtImage,[840,110]),self.gameDisplay.blit(self.rogersCupCourtImage,[840,340]),self.gameDisplay.blit(self.cincinattiCourtImage,[840,560])
            self.gameDisplay.blit(self.shanghaiCourtImage,[840,780])
            
            window.gameDisplay.blit(self.cordobaNameText,[10,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,112]),window.gameDisplay.blit(self.cordobaPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.cordobaCityText,[10,240])
            
            window.gameDisplay.blit(self.puneNameText,[10,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,340]),window.gameDisplay.blit(self.punePrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.puneCityText,[10,470])

            window.gameDisplay.blit(self.montpellierNameText,[10,520])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,565]),window.gameDisplay.blit(self.montpellierPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.montpellierCityText,[10,695])

            window.gameDisplay.blit(self.rotterdamNameText,[10,740])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,785]),window.gameDisplay.blit(self.rotterdamPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.rotterdamCityText,[180,850]),window.gameDisplay.blit(self.rotterdamCityText2,[180,880])

            window.gameDisplay.blit(self.newYorkNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.newYorkPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.newYorkCityText,[420,240])

            window.gameDisplay.blit(self.buenosAiresNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.buenosAiresPrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.buenosAiresCityText,[420,470])

            window.gameDisplay.blit(self.rioNameText,[420,520])
            window.gameDisplay.blit(self.atp500RankingPointsText,[600,565]),window.gameDisplay.blit(self.rioPrizeMoneyText,[600,600]),window.gameDisplay.blit(self.smallCoinImage, [805,610])
            window.gameDisplay.blit(self.rioCityText,[420,695])

            window.gameDisplay.blit(self.marseilleNameText,[420,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,785]),window.gameDisplay.blit(self.marseillePrizeMoneyText,[600,820]),window.gameDisplay.blit(self.smallCoinImage, [805,830])
            window.gameDisplay.blit(self.marseilleCityText,[600,860])

            window.gameDisplay.blit(self.delrayBeachNameText,[840,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[1020,112]),window.gameDisplay.blit(self.delrayBeachPrizeMoneyText,[1020,145]),window.gameDisplay.blit(self.delrayBeachPrizeMoneyText2,[1020,180])
            window.gameDisplay.blit(self.smallCoinImage, [1070,190]),window.gameDisplay.blit(self.delrayBeachCityText,[840,240])

            window.gameDisplay.blit(self.dubaiNameText,[840,300])
            window.gameDisplay.blit(self.atp500RankingPointsText,[1020,340]),window.gameDisplay.blit(self.dubaiPrizeMoneyText,[1020,375]),window.gameDisplay.blit(self.dubaiPrizeMoneyText2,[1020,410])
            window.gameDisplay.blit(self.smallCoinImage, [1070,420]),window.gameDisplay.blit(self.dubaiCityText,[840,470])

            window.gameDisplay.blit(self.acapulcoNameText,[840,520])
            window.gameDisplay.blit(self.atp500RankingPointsText,[1020,565]),window.gameDisplay.blit(self.acapulcoPrizeMoneyText,[1020,600]),window.gameDisplay.blit(self.acapulcoPrizeMoneyText2,[1020,640])
            window.gameDisplay.blit(self.smallCoinImage, [1070,650]),window.gameDisplay.blit(self.acapulcoCityText,[840,695])

            window.gameDisplay.blit(self.santiagoNameText,[840,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[1020,785]),window.gameDisplay.blit(self.santiagoPrizeMoneyText,[1020,820]),window.gameDisplay.blit(self.santiagoPrizeMoneyText2,[1020,850])
            window.gameDisplay.blit(self.smallCoinImage, [1070,860]),window.gameDisplay.blit(self.santiagoCityText,[1020,880])

        elif player.currentMonth == 'March':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            
            window.gameDisplay.blit(self.indianWellsNameText,[10,70])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,112]),window.gameDisplay.blit(self.indianWellsPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.indianWellsCityText,[10,240])
            
            window.gameDisplay.blit(self.miamiNameText,[10,300])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,340]),window.gameDisplay.blit(self.miamiPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.miamiCityText,[10,470])

        elif player.currentMonth == 'April':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340]),self.gameDisplay.blit(self.monteCarloCourtImage,[420,560])
            
            window.gameDisplay.blit(self.houstonNameText,[10,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,112]),window.gameDisplay.blit(self.houstonPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.houstonCityText,[10,240])
            
            window.gameDisplay.blit(self.marrakechNameText,[10,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,340]),window.gameDisplay.blit(self.marrakechPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.marrakechCityText,[10,470])

            window.gameDisplay.blit(self.monteCarloNameText,[10,520])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,565]),window.gameDisplay.blit(self.monteCarloPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.monteCarloCityText,[10,695])

            window.gameDisplay.blit(self.barcelonaNameText,[10,740])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,785]),window.gameDisplay.blit(self.barcelonaPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.barcelonaCityText,[180,850])

            window.gameDisplay.blit(self.budapestNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.budapestPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.budapestCityText,[420,240])

            window.gameDisplay.blit(self.munichNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.munichPrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.munichCityText,[420,470])

            window.gameDisplay.blit(self.estorilNameText,[420,520])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,565]),window.gameDisplay.blit(self.estorilPrizeMoneyText,[600,600]),window.gameDisplay.blit(self.smallCoinImage, [805,610])
            window.gameDisplay.blit(self.estorilCityText,[420,695])

        elif player.currentMonth == 'May':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            
            window.gameDisplay.blit(self.madridNameText,[10,70])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,112]),window.gameDisplay.blit(self.madridPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.madridCityText,[10,240])
            
            window.gameDisplay.blit(self.romeNameText,[10,300])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,340]),window.gameDisplay.blit(self.romePrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.romeCityText,[10,470])

            window.gameDisplay.blit(self.genevaNameText,[10,520])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,565]),window.gameDisplay.blit(self.genevaPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.genevaCityText,[10,695])

            window.gameDisplay.blit(self.lyonNameText,[10,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,785]),window.gameDisplay.blit(self.lyonPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.lyonCityText,[180,850])

            window.gameDisplay.blit(self.nameText2,[420,70])
            window.gameDisplay.blit(self.rankingPointsText1,[600,112]),window.gameDisplay.blit(self.prizeMoneyText2,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.cityText2,[420,240])

        elif player.currentMonth == 'June':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340]),self.gameDisplay.blit(self.monteCarloCourtImage,[420,560])
            
            window.gameDisplay.blit(self.stuttgartNameText,[10,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,112]),window.gameDisplay.blit(self.stuttgartPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.stuttgartCityText,[10,240])
            
            window.gameDisplay.blit(self.sHertogenboschNameText,[10,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,340]),window.gameDisplay.blit(self.sHertogenboschPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.sHertogenboschCityText,[10,470])

            window.gameDisplay.blit(self.londonNameText,[10,520])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,565]),window.gameDisplay.blit(self.londonPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.londonCityText,[10,695])

            window.gameDisplay.blit(self.halleNameText,[10,740])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,785]),window.gameDisplay.blit(self.hallePrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.halleCityText,[180,850])

            window.gameDisplay.blit(self.mallorcaNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.mallorcaPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.mallorcaCityText,[420,240])

            window.gameDisplay.blit(self.eastbourneNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.eastbournePrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.eastbourneCityText,[420,470])

            window.gameDisplay.blit(self.nameText1,[420,520])
            window.gameDisplay.blit(self.rankingPointsText1,[600,565]),window.gameDisplay.blit(self.prizeMoneyText1,[600,600]),window.gameDisplay.blit(self.smallCoinImage, [805,610])
            window.gameDisplay.blit(self.cityText1,[420,695])

        elif player.currentMonth == 'July' and player.currentYear == 2020:        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340]),self.gameDisplay.blit(self.monteCarloCourtImage,[420,560]),self.gameDisplay.blit(self.madridCourtImage,[420,780])
            self.gameDisplay.blit(self.romeCourtImage,[840,110])
            
            window.gameDisplay.blit(self.hamburgNameText,[10,70])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,112]),window.gameDisplay.blit(self.hamburgPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.hamburgCityText,[10,240])
            
            window.gameDisplay.blit(self.newportNameText,[10,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,340]),window.gameDisplay.blit(self.newportPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.newportCityText,[10,470])

            window.gameDisplay.blit(self.bastadNameText,[10,520])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,565]),window.gameDisplay.blit(self.bastadPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.bastadCityText,[10,695])

            window.gameDisplay.blit(self.losCabosNameText,[10,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,785]),window.gameDisplay.blit(self.losCabosPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.losCabosCityText,[180,850])

            window.gameDisplay.blit(self.gstaadNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.gstaadPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.gstaadCityText,[420,240])

            window.gameDisplay.blit(self.umagNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.umagPrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.umagCityText,[420,470])

            window.gameDisplay.blit(self.tokyoOlympicsNameText,[420,520])
            window.gameDisplay.blit(self.tokyoOlympicsRankingPointsText,[600,565]),window.gameDisplay.blit(self.tokyoOlympicsPrizeMoneyText,[600,600]),window.gameDisplay.blit(self.smallCoinImage, [805,610])
            window.gameDisplay.blit(self.tokyoOlympicsCityText,[420,695])

            window.gameDisplay.blit(self.atlantaNameText,[420,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,785]),window.gameDisplay.blit(self.atlantaPrizeMoneyText,[600,820]),window.gameDisplay.blit(self.smallCoinImage, [805,830])
            window.gameDisplay.blit(self.atlantaCityText,[600,860])

            window.gameDisplay.blit(self.kitzbuhelNameText,[840,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[1020,112]),window.gameDisplay.blit(self.kitzbuhelPrizeMoneyText,[1020,145]),window.gameDisplay.blit(self.kitzbuhelPrizeMoneyText2,[1020,180])
            window.gameDisplay.blit(self.smallCoinImage, [1070,190]),window.gameDisplay.blit(self.kitzbuhelCityText,[840,240])

        elif player.currentMonth == 'August':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            
            window.gameDisplay.blit(self.washingtonNameText,[10,70])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,112]),window.gameDisplay.blit(self.washingtonPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.washingtonCityText,[10,240])
            
            window.gameDisplay.blit(self.rogersCupNameText,[10,300])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,340]),window.gameDisplay.blit(self.rogersCupPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.rogersCupCityText,[10,470])

            window.gameDisplay.blit(self.cincinattiNameText,[10,520])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,565]),window.gameDisplay.blit(self.cincinattiPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.cincinattiCityText,[10,695])

            window.gameDisplay.blit(self.winstonSalemNameText,[10,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,785]),window.gameDisplay.blit(self.winstonSalemPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.winstonSalemCityText,[180,850])

            window.gameDisplay.blit(self.nameText4,[420,70])
            window.gameDisplay.blit(self.rankingPointsText1,[600,112]),window.gameDisplay.blit(self.prizeMoneyText4,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.cityText4,[420,240])

        elif player.currentMonth == 'September':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340])
            
            window.gameDisplay.blit(self.stPetersburgNameText,[10,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,112]),window.gameDisplay.blit(self.stPetersburgPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.stPetersburgCityText,[10,240])
            
            window.gameDisplay.blit(self.metzNameText,[10,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,340]),window.gameDisplay.blit(self.metzPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.metzCityText,[10,470])

            window.gameDisplay.blit(self.laverCupNameText,[10,520])
            window.gameDisplay.blit(self.laverCupRankingPointsText,[180,565]),window.gameDisplay.blit(self.laverCupPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.laverCupCityText,[10,695])

            window.gameDisplay.blit(self.chengduNameText,[10,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,785]),window.gameDisplay.blit(self.chengduPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.chengduCityText,[180,850])

            window.gameDisplay.blit(self.zhuhaiNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.zhuhaiPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.zhuhaiCityText,[420,240])

            window.gameDisplay.blit(self.sofiaNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.sofiaPrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.sofiaCityText,[420,470])

        elif player.currentMonth == 'October':
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            self.gameDisplay.blit(self.wimbledonCourtImage,[0,560]),self.gameDisplay.blit(self.usOpenCourtImage,[0,780]),self.gameDisplay.blit(self.australianOpenCourtImage,[420,110])
            self.gameDisplay.blit(self.miamiCourtImage,[420,340]),self.gameDisplay.blit(self.monteCarloCourtImage,[420,560]),self.gameDisplay.blit(self.madridCourtImage,[420,780])
            
            window.gameDisplay.blit(self.beijingNameText,[10,70])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,112]),window.gameDisplay.blit(self.beijingPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.beijingCityText,[10,240])
            
            window.gameDisplay.blit(self.tokyoNameText,[10,300])
            window.gameDisplay.blit(self.atp500RankingPointsText,[180,340]),window.gameDisplay.blit(self.tokyoPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.tokyoCityText,[10,470])

            window.gameDisplay.blit(self.shanghaiNameText,[10,520])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,565]),window.gameDisplay.blit(self.shanghaiPrizeMoneyText,[180,600]),window.gameDisplay.blit(self.smallCoinImage, [385,610])
            window.gameDisplay.blit(self.shanghaiCityText,[10,695])

            window.gameDisplay.blit(self.moscowNameText,[10,740])
            window.gameDisplay.blit(self.atp250RankingPointsText,[180,785]),window.gameDisplay.blit(self.moscowPrizeMoneyText,[180,820]),window.gameDisplay.blit(self.smallCoinImage, [385,830])
            window.gameDisplay.blit(self.moscowCityText,[180,850])

            window.gameDisplay.blit(self.antwerpNameText,[420,70])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,112]),window.gameDisplay.blit(self.antwerpPrizeMoneyText,[600,145]),window.gameDisplay.blit(self.smallCoinImage, [805,155])
            window.gameDisplay.blit(self.antwerpCityText,[420,240])

            window.gameDisplay.blit(self.stockholmNameText,[420,300])
            window.gameDisplay.blit(self.atp250RankingPointsText,[600,340]),window.gameDisplay.blit(self.stockholmPrizeMoneyText,[600,375]),window.gameDisplay.blit(self.smallCoinImage, [805,385])
            window.gameDisplay.blit(self.stockholmCityText,[420,470])

            window.gameDisplay.blit(self.viennaNameText,[420,520])
            window.gameDisplay.blit(self.atp500RankingPointsText,[600,565]),window.gameDisplay.blit(self.viennaPrizeMoneyText,[600,600]),window.gameDisplay.blit(self.smallCoinImage, [805,610])
            window.gameDisplay.blit(self.viennaCityText,[420,695])

            window.gameDisplay.blit(self.baselNameText,[420,740])
            window.gameDisplay.blit(self.atp500RankingPointsText,[600,785]),window.gameDisplay.blit(self.baselPrizeMoneyText,[600,820]),window.gameDisplay.blit(self.smallCoinImage, [805,830])
            window.gameDisplay.blit(self.baselCityText,[600,860])

        elif player.currentMonth == 'November':        
            self.gameDisplay.blit(self.atpCupCourtImage,[0,110]),self.gameDisplay.blit(self.miamiCourtImage,[0,340])
            
            window.gameDisplay.blit(self.parisNameText,[10,70])
            window.gameDisplay.blit(self.masters1000RankingPointsText,[180,112]),window.gameDisplay.blit(self.parisPrizeMoneyText,[180,145]),window.gameDisplay.blit(self.smallCoinImage, [385,155])
            window.gameDisplay.blit(self.parisCityText,[10,240])
            
            window.gameDisplay.blit(self.atpFinalsNameText,[10,300])
            window.gameDisplay.blit(self.atpFinalsRankingPointsText,[180,340]),window.gameDisplay.blit(self.atpFinalsPrizeMoneyText,[180,375]),window.gameDisplay.blit(self.smallCoinImage, [385,385])
            window.gameDisplay.blit(self.atpFinalsCityText,[10,470])
        pygame.display.set_caption("Select Tournament")
        pygame.display.set_icon(self.playerImageFront)


    def setupOpponentMenu(self):
        if opponent.name == 'Novak Djokovic':
            opponent.country = 'Serbia'
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/player1front.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/serbiaflag.png')
        elif opponent.name == 'Roger Federer':
            opponent.country = 'Switzerland'
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/federer.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/switzerlandflag.png')
        elif opponent.name == 'Rafael Nadal':
            opponent.country = 'Spain'
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/nadal.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/spainflag.png')
        elif opponent.name == 'Daniil Medvedev':
            opponent.country = 'Russia'
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/medvedev.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/russiaflag.png')
        elif opponent.name == 'Dominic Thiem':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/thiem.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/austriaflag.png')
            opponent.country = 'Austria'
        elif opponent.name == 'Alexander Zverev':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/zverev.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/germanyflag.png')
            opponent.country = 'Germany'
        elif opponent.name == 'Matteo Berrettini':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/berrettini.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/italyflag.png')
            opponent.country = 'Italy'
        elif opponent.name == 'Gael Monfils':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/franceflag.png')
            opponent.country = 'France'
        elif opponent.name == 'Stan Wawrinka':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/switzerlandflag.png')
            opponent.country = 'Switzerland'
        elif opponent.name == 'Light Togami':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/japanflag.png')
            opponent.country = 'Japan'
        elif opponent.name == 'Alex de Minaur':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/australiaflag.png')
            opponent.country = 'Australia'
        elif opponent.name == 'Nick Kyrgios':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/australiaflag.png')
            opponent.country = 'Australia'
        elif opponent.name == 'Stefanos Tsitsipas':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/tsitsipas.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/greeceflag.png')
            opponent.country = 'Greece'
        elif opponent.name == 'Ivo Karlovic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/croatiaflag.png')
            opponent.country = 'Croatia'
        elif opponent.name == 'Bernard Tomic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/australiaflag.png')
            opponent.country = 'Australia'
        elif opponent.name == 'Krittin Koaykul':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/thialandflag.png')
            opponent.country = 'Thialand'
        elif opponent.name == 'Artem Bahmet':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/ukraineflag.png')
            opponent.country = 'Ukraine'
        elif opponent.name == 'Jimmy Connors':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedstatesflag.png')
            opponent.country = 'USA'
        elif opponent.name == 'John Mcenroe':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedstatesflag.png')
            opponent.country = 'USA'
        elif opponent.name == 'Brad Gilbert':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedstatesflag.png')
            opponent.country = 'USA'
        elif opponent.name == 'Andre Agassi':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedstatesflag.png')
            opponent.country = 'USA'
        elif opponent.name == 'Bjorn Borg':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/swedenflag.png')
            opponent.country = 'Sweden'
        elif opponent.name == 'Stefan Edberg':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/swedenflag.png')
            opponent.country = 'Sweden'
        elif opponent.name == 'David Goffin':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/belgiumflag.png')
            opponent.country = 'Belgium'
        elif opponent.name == 'Marcus Willis':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedkingdomflag.png')
            opponent.country = 'United Kingdom'
        elif opponent.name == 'Fabio Fognini':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/italyflag.png')
            opponent.country = 'Italy'
        elif opponent.name == 'Denis Shapovalov':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/canadaflag.png')
            opponent.country = 'Canada'
        elif opponent.name == 'Milos Raonic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/canadaflag.png')
            opponent.country = 'Canada'
        elif opponent.name == 'Marin Cilic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/croatiaflag.png')
            opponent.country = 'Croatia'
        elif opponent.name == 'Benoit Paire':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/franceflag.png')
            opponent.country = 'France'
        elif opponent.name == 'Grigor Dimitrov':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/bulgariaflag.png')
            opponent.country = 'Bulgaria'
        elif opponent.name == 'Andy Murray':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedkingdomflag.png')
            opponent.country = 'United Kingdom'
        elif opponent.name == 'Dan Evans':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/unitedkingdomflag.png')
            opponent.country = 'United Kingdom'
        elif opponent.name == 'Ernests Gulbis':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/latviaflag.png')
            opponent.country = 'Latvia'
        elif opponent.name == 'Dustin Brown':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
            self.flagImage = pygame.image.load('C:/NEA Tennis Game/Flags/germanyflag.png')
            opponent.country = 'Germany'
        if opponentImageChance > 95:
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1ultimate.png')
            opponent.ultimate = True
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.youArePlayingText = self.smallFont.render(str("You are playing:"+""),True,self.colors["black"])
        self.largeOpponentName = self.medFont.render(str(opponent.name),True,self.colors["black"])
        self.opponentRankingText = self.smallFont.render(str("Ranking:"+" "+str(opponent.ranking)),True,self.colors["black"])
        self.opponentCountryText = self.smallFont.render(str("Country:"+" "+str(opponent.country)),True,self.colors["black"])
        self.opponentPowerText = self.smallFont.render(str("Power:"+" "+str(opponent.power))+str("%"),True,self.colors["black"])
        self.opponentAccuracyText = self.smallFont.render(str("Accuracy:"+" "+str(opponent.accuracy))+str("%"),True,self.colors["black"])
        self.opponentSpeedText = self.smallFont.render(str("Speed:"+" "+str(opponent.speed))+str("%"),True,self.colors["black"])
        self.opponentFitnessText = self.smallFont.render(str("Fitness:"+" "+str(opponent.fitness))+str("%"),True,self.colors["black"])
        self.opponentConsistencyText = self.smallFont.render(str("Consistency:"+" "+str(opponent.consistency))+str("%"),True,self.colors["black"])
        self.difficultyText = self.smallFont.render(str("Difficulty:"+" "+str(player.difficulty)),True,self.colors["black"])
        self.gameDisplay.blit(opponentMenu.opponentMenuCourt,[0,0]),window.gameDisplay.blit(self.youArePlayingText,(520,0))
        window.gameDisplay.blit(self.opponentImage, [555,125]),window.gameDisplay.blit(self.flagImage, [1095,0])
        window.gameDisplay.blit(self.largeOpponentName,(460,40)),window.gameDisplay.blit(self.opponentRankingText,(800,30)),window.gameDisplay.blit(self.opponentCountryText,(800,0)),
        window.gameDisplay.blit(self.opponentPowerText,(300,480)),window.gameDisplay.blit(self.opponentAccuracyText,(300,520)),
        window.gameDisplay.blit(self.opponentSpeedText,(800,480)),window.gameDisplay.blit(self.opponentFitnessText,(800,520)),
        window.gameDisplay.blit(self.opponentConsistencyText,(300,560)),window.gameDisplay.blit(self.difficultyText,(5,200))
        self.currentRoundText = self.smallFont.render(str(player.currentTournament+"-"+str(player.currentRound)),True,self.colors["black"])
        window.gameDisplay.blit(self.currentRoundText,(5,0))
        if player.difficulty == 'Amateur':
            opponent.power = random.randint(20,40)
            opponent.accuracy = random.randint(20,40)
            opponent.consistency = random.randint(40,50)
            opponent.speed = random.randint(40,50)
            opponent.fitness = random.randint(40,50)
            #opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(20,40),random.randint(20,40),random.randint(40,50),random.randint(20,40),random.randint(20,40),100,100,0,0,60,180,'',0,0,0,0)
        elif player.difficulty == 'Intermediate':
            opponent.power = random.randint(50,80)
            opponent.accuracy = random.randint(50,80)
            opponent.consistency = random.randint(50,80)
            opponent.speed = random.randint(45,50)
            opponent.fitness = random.randint(50,80)
            #opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(50,80),random.randint(50,80),random.randint(50,80),random.randint(50,80),random.randint(50,80),100,100,0,0,60,180,'',0,0,0,0)
        elif player.difficulty == 'Pro':
            opponent.power = random.randint(75,95)
            opponent.accuracy = random.randint(75,95)
            opponent.consistency = random.randint(75,95)
            opponent.speed = random.randint(45,55)
            opponent.fitness = random.randint(75,95)
            #opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(75,95),random.randint(75,95),random.randint(70,80),random.randint(75,95),random.randint(75,95),100,100,0,0,60,180,'',0,0,0,0)
        elif player.difficulty == 'Master':
            opponent.power = random.randint(90,100)
            opponent.accuracy = random.randint(90,100)
            opponent.consistency = random.randint(90,100)
            opponent.speed = random.randint(55,65)
            opponent.fitness = random.randint(90,100)
            #opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(90,100),random.randint(90,100),random.randint(70,80),random.randint(90,100),random.randint(90,100),100,100,0,0,60,180,'',0,0,0,0)
        elif player.difficulty == 'Impossible':
            opponent.power = random.randint(100,150)
            opponent.accuracy = random.randint(100,150)
            opponent.consistency = random.randint(100,150)
            opponent.speed = random.randint(65,75)
            opponent.fitness = random.randint(100,150)
            #opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(100,150),random.randint(100,150),random.randint(70,80),random.randint(100,150),random.randint(100,150),100,100,0,0,60,180,'',0,0,0,0)
        else:
            player.difficulty = 'Unknown'
            opponent.power = random.randint(20,100)
            opponent.accuracy = random.randint(20,100)
            opponent.consistency = random.randint(20,100)
            opponent.speed = random.randint(20,80)
            opponent.fitness = random.randint(20,100)
        pygame.display.set_caption("Opponent")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupLevelUpMenu(self):
        self.skittlesImage = pygame.image.load('C:/NEA Tennis Game/Shop/skittles.png')
        self.orangeJuiceImage = pygame.image.load('C:/NEA Tennis Game/Shop/orangejuice.png')
        self.orangeImage = pygame.image.load('C:/NEA Tennis Game/Shop/orange.png')
        self.coffeeImage = pygame.image.load('C:/NEA Tennis Game/Shop/coffee.png')
        self.doubleDeckerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doubledecker.png')
        self.cokeImage = pygame.image.load('C:/NEA Tennis Game/Shop/coke.png')
        self.lucozadeImage = pygame.image.load('C:/NEA Tennis Game/Shop/lucozade.png')
        self.dietCokeImage = pygame.image.load('C:/NEA Tennis Game/Shop/dietcoke.png')
        self.fruitSaladImage = pygame.image.load('C:/NEA Tennis Game/Shop/fruitsalad.png')
        self.goldenFruitSaladImage = pygame.image.load('C:/NEA Tennis Game/Shop/goldenfruitsalad.png')
        self.cheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/cheeseburger.png')
        self.doubleCheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doublecheeseburger.png')
        self.doubleBaconCheeseburgerImage = pygame.image.load('C:/NEA Tennis Game/Shop/doublebaconcheeseburger.png')
        self.playerImageRight = pygame.image.load('C:/NEA Tennis Game/Player/player1right.png')
        self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1front.png')
        self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.levelUpText = self.medFont.render(str("Level Up!"+""),True,self.colors["black"])
        self.levelUpText2 = self.smallFont.render(str("You have leveled up to level"+" "+str(player.level)+"!"),True,self.colors["black"])
        self.gameDisplay.blit(self.opponentMenuCourt,[0,0])
        window.gameDisplay.blit(self.playerImageFront, [500,125])
        window.gameDisplay.blit(self.levelUpText,(520,10)),window.gameDisplay.blit(self.levelUpText2,(410,400))
        if player.level == 2:
            self.levelUp2Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp2Text,(370,500))
            window.gameDisplay.blit(self.coffeeImage, [585,530])
        elif player.level == 3:
            self.levelUp3Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp3Text,(370,500))
            window.gameDisplay.blit(self.orangeJuiceImage, [585,530])
        elif player.level == 5:
            self.levelUp5Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp5Text,(370,500))
            window.gameDisplay.blit(self.cokeImage, [585,530])
        elif player.level == 10:
            self.levelUp10Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp10Text,(370,500))
            window.gameDisplay.blit(self.dietCokeImage, [585,530])
        elif player.level == 15:
            self.levelUp15Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp15Text,(370,500))
            window.gameDisplay.blit(self.lucozadeImage, [585,530])
        elif player.level == 20:
            self.levelUp20Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp20Text,(370,500))
            #window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [585,530])
        elif player.level == 30:
            self.levelUp30Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp30Text,(370,500))
            window.gameDisplay.blit(self.doubleDeckerImage, [585,530])
        elif player.level == 40:
            self.levelUp30Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp30Text,(370,500))
            window.gameDisplay.blit(self.fruitSaladImage, [585,530])
        elif player.level == 50:
            self.levelUp50Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp50Text,(370,500))
            window.gameDisplay.blit(self.skittlesImage, [585,530])
        elif player.level == 60:
            self.levelUp60Text = self.smallFont.render(str("You have unlocked the ATP Finals Tournament!"),True,self.colors["black"])
            self.levelUp602Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp60Text,(370,500)),window.gameDisplay.blit(self.levelUp602Text,(370,450))
            #window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [585,530])
        elif player.level == 65:
            self.levelUp65Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp65Text,(370,500))
            #window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [585,530])
        elif player.level == 68:
            self.levelUp68Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp68Text,(370,500))
            #window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [585,530])
        elif player.level == 75:
            self.levelUp75Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp75Text,(370,500))
            window.gameDisplay.blit(self.cheeseburgerImage, [585,530])
        elif player.level == 80:
            self.levelUp80Text = self.smallFont.render(str("You have unlocked the master difficulty level!"),True,self.colors["black"])
            self.levelUp802Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp80Text,(370,500)),window.gameDisplay.blit(self.levelUp802Text,(370,450))
            window.gameDisplay.blit(self.doubleCheeseburgerImage, [585,530])
        elif player.level == 90:
            self.levelUp90Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp90Text,(370,500))
            window.gameDisplay.blit(self.goldenFruitSaladImage, [585,530])
        elif player.level == 95:
            self.levelUp95Text = self.smallFont.render(str("You have unlocked a new item in the shop!"),True,self.colors["black"])
            window.gameDisplay.blit(self.levelUp95Text,(370,500))
            window.gameDisplay.blit(self.doubleBaconCheeseburgerImage, [585,530])
        elif player.level == 100:
            self.congratsText = self.smallFont.render(str("You have unlocked everything in the game! Congradulations!"),True,self.colors["black"])
            self.levelUp100Text = self.smallFont.render(str("As a reward, you have unlocked the impossible difficulty level!"),True,self.colors["black"])
            window.gameDisplay.blit(self.congratsText,(270,500))
            window.gameDisplay.blit(self.levelUp100Text,(270,560))
        pygame.display.set_caption("Level Up!")
        pygame.display.set_icon(self.playerImageRight)

    def text(self): #holds the text variables for displaying the score
        self.scorePoints = self.smallFont.render(str(scoring.playerPoints),True,window.colors["black"])
        self.opponentScorePoints = self.smallFont.render(str(scoring.opponentPoints),True,window.colors["black"])
        self.scoreGames = self.smallFont.render(str(scoring.playerGames),True,window.colors["black"])
        self.opponentScoreGames = self.smallFont.render(str(scoring.opponentGames),True,window.colors["black"])
        self.scoreSets = self.smallFont.render(str(scoring.playerSets),True,window.colors["black"])
        self.opponentScoreSets = self.smallFont.render(str(scoring.opponentSets),True,window.colors["black"])
        self.playerName = self.smallFont.render(str(player.name),True,window.colors["black"])
        self.opponentName = self.smallFont.render(str(opponent.name),True,window.colors["black"])
        
    def draw(self):
        window.gameDisplay.blit(self.playerName,(display_width - 300,display_height / 90)),window.gameDisplay.blit(self.opponentName,(display_width - 300,display_height / 20))
        window.gameDisplay.blit(self.scorePoints,(display_width - 30,display_height / 90)),window.gameDisplay.blit(self.opponentScorePoints,(display_width - 30,display_height / 20))
        window.gameDisplay.blit(self.scoreGames,(display_width - 60,display_height / 90)),window.gameDisplay.blit(self.opponentScoreGames,(display_width - 60,display_height / 20))
        window.gameDisplay.blit(self.scoreSets,(display_width - 90,display_height / 90)),window.gameDisplay.blit(self.opponentScoreSets,(display_width - 90,display_height / 20))

    def quit(self):
        pygame.quit()
        quit()

class Player:
    def __init__(self,name,country,ranking,rankingPoints,power,accuracy,speed,fitness,consistency,x,y,xChange,yChange,width,height,difficulty,skillPoints,coins,energy,level,xp
                 ,matchesPlayed,wins,losses,tournamentsPlayed,tournamentWins,grandSlamWins,masters1000Wins,atp500Wins,currentTournament,currentTournamentMatchWins,currentRound,earnings
                 ,pointsPlayed,pointsWon,pointsLost,hand,opponentsAlreadyPlayed,currentMonth,currentYear,currentMonthTournamentPlays,currentMonthTournamentsAlreadyPlayed,monthCount):
        self.name = str(name)
        self.country = country
        self.ranking = ranking
        self.rankingPoints = rankingPoints
        self.power = power
        self.accuracy = accuracy
        self.speed = speed
        self.fitness = fitness
        self.consistency = consistency
        self.x = x
        self.y = y
        self.xChange = xChange
        self.yChange = yChange
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.skillPoints = skillPoints
        self.coins = coins
        self.energy = energy
        self.level = level
        self.xp = xp
        self.matchesPlayed = matchesPlayed
        self.wins = wins
        self.losses = losses
        self.tournamentsPlayed = tournamentsPlayed
        self.tournamentWins = tournamentWins
        self.grandSlamWins = grandSlamWins
        self.masters1000Wins = masters1000Wins
        self.atp500Wins = atp500Wins
        self.currentTournament = currentTournament
        self.currentTournamentMatchWins = currentTournamentMatchWins
        self.currentRound = currentRound
        self.earnings = earnings
        self.pointsPlayed = pointsPlayed
        self.pointsWon = pointsWon
        self.pointsLost = pointsLost
        self.hand = hand
        self.opponentsAlreadyPlayed = opponentsAlreadyPlayed
        self.currentMonth = currentMonth
        self.currentYear = currentYear
        self.currentMonthTournamentPlays = currentMonthTournamentPlays
        self.currentMonthTournamentsAlreadyPlayed = currentMonthTournamentsAlreadyPlayed
        self.monthCount = monthCount


    def playerControls(self): 
        ballBounceChance = random.randint(1,100)
        ballBounceTime = 100000
        for event in pygame.event.get(): #if user clicks on x on start screen
            if event.type == pygame.QUIT:
                autoSave()
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
                    player.yChange = - player.speed / 2.6
                elif event.key == pygame.K_DOWN:
                    player.yChange = player.speed / 2.6
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.fitness = player.fitness - 0.000015625
                    if player.fitness <= 100:
                        player.speed = player.speed - 0.003125
                    if player.fitness <= 80:
                        player.speed = player.speed - 0.003125
                    if player.fitness <= 40:
                        player.speed = player.speed - 0.00625
                    if player.fitness <= 20:
                        player.speed = player.speed - 0.03125
                    elif player.fitness == 0:
                        player.speed = player.speed - 15625
                if event.key == pygame.K_SPACE and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    scoring.hits = scoring.hits + 1
                    scoring.rallyLength = scoring.rallyLength + 1
                elif event.key == pygame.K_SPACE and event.key == pygame.K_LEFT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player.x + player1.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    ball.ballXChange = 0
                    scoring.hits = scoring.hits + 1
                    scoring.rallyLength = scoring.rallyLength + 1
                elif event.key == pygame.K_SPACE  and event.key == pygame.K_RIGHT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height and ball.ballX <= player1.x + player1.width: #player and ball collision
                    ball.ballYChange = + ball.ballSpeed
                    scoring.hits = scoring.hits + 1
                    scoring.rallyLength = scoring.rallyLength + 1
                elif event.key == pygame.K_LCTRL and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height - 70 and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10 #/1.5 + 10
                    ball.ballXChange = - int(player.power / player.accuracy * random.randint(1,10)) #5.8
                    scoring.hits = scoring.hits + 1
                    scoring.rallyLength = scoring.rallyLength + 1
                elif event.key == pygame.K_LALT and ball.ballY >= player.y and ball.ballX >= player.x and ball.ballY <= player.y + player.height - 70 and ball.ballX <= player.x + player.width: #player and ball collision
                    ball.ballYChange = - int(player.power / 1.5) + 10
                    ball.ballXChange = - int(-player.power / player.accuracy * random.randint(1,10)) #5.8
                    scoring.hits = scoring.hits + 1
                    scoring.rallyLength = scoring.rallyLength + 1
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
    def __init__(self,name,country,ranking,rankingPoints,power,accuracy,speed,fitness,consistency,x,y,xChange,yChange,width,height,difficulty,skillPoints,coins,energy,level,xp,
                 matchesPlayed,wins,losses,tournamentsPlayed,tournamentWins,grandSlamWins,masters1000Wins,atp500Wins,currentTournament,currentTournamentMatchWins,currentRound,earnings
                 ,pointsPlayed,pointsWon,pointsLost,hand,ultimate,opponentsAlreadyPlayed,currentMonth,currentYear,currentMonthTournamentPlays,currentMonthTournamentsAlreadyPlayed,monthCount):
        super().__init__(name,country,ranking,rankingPoints,power,accuracy,speed,fitness,consistency,x,y,xChange,yChange,width,height,difficulty,skillPoints,coins,energy,level,xp
                         ,matchesPlayed,wins,losses,tournamentsPlayed,tournamentWins,grandSlamWins,masters1000Wins,atp500Wins,currentTournament,currentTournamentMatchWins,currentRound,earnings
                         ,pointsPlayed,pointsWon,pointsLost,hand,opponentsAlreadyPlayed,currentMonth,currentYear,currentMonthTournamentPlays,currentMonthTournamentsAlreadyPlayed,monthCount) #calls Player class
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
        netErrorChance = random.randint(1,100)
        outErrorChance = random.randint(1,100)
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
            scoring.rallyLength = scoring.rallyLength + 1
        '''if netErrorChance < 100:
            ball.ballXChange = 0
            ball.ballYChange = 0
            scoring.playerWinPoint()'''

    def opponentAnimations(self):
        pass       
player = Player('Sam Gibb','United Kingdom',36,0,30,30,60,30,30,(display_width * 0.45),(display_height * 0.8),0,0,60,180,'Amateur',0,100,100,1,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0,0,0,0,'Right',
                [],'January',2020,0,[],13)#an instance of the Player class

class Scoring:
    def __init__(self):
        self.playerScore = 0
        self.opponentScore = 0
        self.playerPoints = 0
        self.opponentPoints = 0
        self.playerGames = 0
        self.opponentGames = 0
        self.playerSets = 0
        self.opponentSets = 0
        self.winText = window.medFont.render(str("You won against "+str(opponent.name)+ "!"),True,window.colors["black"])
        self.opponentWinText = window.medFont.render(str(opponent.name+str(" beat you!")),True,window.colors["black"])
        self.hits = 0
        self.rallyLength = 0
        self.winners = 0
        self.errors = 0

    def resetMatch(self):
        if opponent.name in player.opponentsAlreadyPlayed:
            opponent.name = random.choice(opponentNames)
        self.opponentPoints = 0
        self.opponentScore = 0
        self.playerPoints = 0
        self.playerScore = 0
        self.opponentGames = 0
        self.playerGames = 0
        self.opponentGames = 0
        self.playerSets = 0
        self.opponentSets = 0

    def playerWinPoint(self):
        player.opponentsAlreadyPlayed.append(opponent.name)
        scoring.rallyLength = 0
        self.playerScore = self.playerScore + 1
        player.pointsPlayed = player.pointsPlayed + 1
        player.pointsWon = player.pointsWon + 1
        if self.playerScore == 0:
            self.playerPoints = 0
        elif self.playerScore == 1:
            self.playerPoints = 15
        elif self.playerScore == 2:
            self.playerPoints = 30
        elif self.playerScore == 3:
            self.playerPoints = 40
        elif self.playerScore == 3 and self.opponentScore == 3:
            if self.playerScore == 4:
                self.playerPoints == 45
            elif self.playerScore == 5:
                self.playerPoints = 0
                self.playerScore = 0
                self.opponentPoints = 0
                self.playerGames = self.playerGames + 1
        elif self.playerScore == 4 and self.opponentScore != 3:
            self.playerPoints = 0
            self.playerScore = 0
            self.opponentScore = 0
            self.opponentPoints = 0
            self.playerGames = self.playerGames + 1
        if self.playerGames == 6 and self.opponentGames < 5 or self.playerGames == 7 and self.opponentGames == 5:
            self.opponentPoints = 0
            self.opponentScore = 0
            self.playerPoints = 0
            self.playerScore = 0
            self.opponentGames = 0
            self.playerGames = 0
            self.opponentGames = 0
            self.playerSets = self.playerSets + 1
        window.setupNextPoint()
        if self.playerScore == 2 and self.opponentSets < 2: #when you win a match
            self.youWonText = window.smallMedFont.render(str("You won the "+str(player.currentTournament)+"!"),True,window.colors["black"])
            player.wins = player.wins + 1
            player.matchesPlayed = player.matchesPlayed + 1
            player.currentTournamentMatchWins = player.currentTournamentMatchWins + 1
            player.skillPoints = player.skillPoints + 1
        
            if player.currentTournamentMatchWins == 0:
                player.currentRound = 'Round of 128'
            elif player.currentTournamentMatchWins == 1:
                player.currentRound = 'Round of 64'
            elif player.currentTournamentMatchWins == 2:
                player.currentRound = 'Round of 32'
            elif player.currentTournamentMatchWins == 3:
                player.currentRound = 'Round of 16'
            elif player.currentTournamentMatchWins == 4:
                player.currentRound = 'Quarterfinals'
            elif player.currentTournamentMatchWins == 5:
                player.currentRound = 'Semifinals'
            elif player.currentTournamentMatchWins == 6:
                player.currentRound = 'Finals'
            elif player.currentTournamentMatchWins == 7: #when you win a tournament
                player.opponentsAlreadyPlayed = []
                player.currentMonthTournamentsAlreadyPlayed = []
                window.gameDisplay.blit(self.youWonText,[175,530])
                player.currentMonthTournamentPlays = player.currentMonthTournamentPlays + 1
                if player.currentMonthTournamentPlays == 1:
                    player.monthCount = player.monthCount + 1

                if player.currentTournament == 'Australian Open' or player.currentTournament == 'Roland Garros' or player.currentTournament == 'Wimbledon' or player.currentTournament == 'US Open':
                    player.grandSlamWins = player.grandSlamWins + 1
                    player.coins = player.coins + 200
                    player.earnings = player.earnings + 200
                    player.rankingPoints = player.rankingPoints + 2000
                elif player.currentTournament == 'Paris' or player.currentTournament == 'Rolex Shanghai Masters' or player.currentTournament == 'Internazionali BNL d\'Italia' or player.currentTournament == 'Western & Southern Open' or player.currentTournament == 'Madrid Open' or player.currentTournament == 'Rolex Monte Carlo Masters' or player.currentTournament == 'Miami Open' or player.currentTournament == 'BNP Paribas Open' or player.currentTournament == 'Rogers Cup':
                    player.masters1000Wins = player.masters1000Wins + 1
                    player.coins = player.coins + 100
                    player.earnings = player.earnings + 100
                    player.rankingPoints = player.rankingPoints + 1000
                else:
                    player.atp500Wins = player.atp500Wins + 1
                    player.coins = player.coins + 50
                    player.earnings = player.earnings + 50
                    player.rankingPoints = player.rankingPoints + 500
                player.currentTournament = ''
                player.currentTournamentMatchWins = 0
                player.currentRound = 'Round of 128'
                player.tournamentWins = player.tournamentWins + 1
                player.tournamentsPlayed = player.tournamentsPlayed + 1
                player.level = player.level + 1
                player.skillPoints = player.skillPoints + 2
                opponent.losses = opponent.losses + 1
                player.energy = player.energy - 35
                player.currentMonthTournamentPlays = 0

            scoring.playerWin()

    def playerWin(self):
        window = Window()
        window.setupPlayerWin()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        if window.levelUp == True:
                            levelUpMenu.levelUp()
                        else:
                            gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        if window.levelUp == True:
                            levelUpMenu.levelUp()
                        if player.currentTournament == '':
                            tournamentMenu.tournament()
                        else:
                            opponentMenu.showOpponent()
            if window.levelUp == True:
                button('Play Again', 270,700,150,50, window.colors["green"], window.colors["lightGreen"], action='levelUp')
                button('Training', 450,700,150,50, window.colors["blue"], window.colors["lightBlue"], action='levelUp')
                button('My Player', 630,700,150,50, window.colors["purple"], window.colors["lightPurple"], action='levelUp')
                button('Main Menu', 820,700,150,50, window.colors["yellow"], window.colors["lightYellow"], action='levelUp')
            else:
                button('Play Again', 270,700,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
                button('Training', 450,700,150,50, window.colors["blue"], window.colors["lightBlue"], action='training')
                button('My Player', 630,700,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
                button('Main Menu', 820,700,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')

            ball.ballBoundaries()
            pygame.display.update()
            window.clock.tick(window.FPS)
            scoring.resetMatch()

    def opponentWinPoint(self):
        scoring.rallyLength = 0
        self.opponentScore = self.opponentScore + 1
        player.pointsPlayed = player.pointsPlayed + 1
        player.pointsLost = player.pointsLost + 1
        if self.opponentScore == 0:
            self.opponentPoints = 0
        elif self.opponentScore == 1:
            self.opponentPoints = 15
        elif self.opponentScore == 2:
            self.opponentPoints = 30
        elif self.opponentScore == 3:
            self.opponentPoints = 40
        elif self.playerScore == 3 and self.opponentScore == 3:
            if self.opponentScore == 4:
                self.opponentPoints == 45
            elif self.opponentScore == 5:
                self.playerPoints = 0
                self.playerScore = 0
                self.opponentPoints = 0
                self.opponentGames = self.opponentGames + 1            
        elif self.opponentScore == 4 and self.playerScore != 3:
            self.opponentPoints = 0
            self.opponentScore = 0
            self.playerPoints = 0
            self.playerScore = 0
            self.opponentGames = self.opponentGames + 1
        if self.opponentGames == 6 and self.playerGames < 5 or self.opponentGames == 7 and self.playerGames == 5:
            self.opponentPoints = 0
            self.opponentScore = 0
            self.playerPoints = 0
            self.playerScore = 0
            self.opponentGames = 0
            self.playerGames = 0
            self.opponentSets = self.opponentSets + 1
        window.setupNextPoint()
        if self.opponentPoints == 2 and self.playerSets < 2: #when you lose a match
            if player.currentTournament == 'Australian Open' or player.currentTournament == 'Roland Garros' or player.currentTournament == 'Wimbledon' or player.currentTournament == 'US Open':
                if player.currentTournamentMatchWins == 0:
                    player.rankingPoints = player.rankingPoints + 10
                    player.earnings = player.earnings + 2
                    player.coins = player.coins + 2
                elif player.currentTournamentMatchWins == 1:
                    player.rankingPoints = player.rankingPoints + 45
                    player.earnings = player.earnings + 15
                    player.coins = player.coins + 15
                elif player.currentTournamentMatchWins == 2:
                    player.rankingPoints = player.rankingPoints + 90
                    player.earnings = player.earnings + 35
                    player.coins = player.coins + 35
                elif player.currentTournamentMatchWins == 3:
                    player.rankingPoints = player.rankingPoints + 180
                    player.earnings = player.earnings + 50
                    player.coins = player.coins + 50
                elif player.currentTournamentMatchWins == 4:
                    player.rankingPoints = player.rankingPoints + 360
                    player.earnings = player.earnings + 75
                    player.coins = player.coins + 75
                elif player.currentTournamentMatchWins == 5:
                    player.rankingPoints = player.rankingPoints + 720
                    player.earnings = player.earnings + 100
                    player.coins = player.coins + 100
                elif player.currentTournamentMatchWins == 6:
                    player.rankingPoints = player.rankingPoints + 1200
                    player.earnings = player.earnings + 120
                    player.coins = player.coins + 120

            elif player.currentTournament == 'Paris' or player.currentTournament == 'Rolex Shanghai Masters' or player.currentTournament == 'Internazionali BNL d\'Italia' or player.currentTournament == 'Western & Southern Open' or player.currentTournament == 'Madrid Open' or player.currentTournament == 'Rolex Monte Carlo Masters' or player.currentTournament == 'Miami Open' or player.currentTournament == 'BNP Paribas Open' or player.currentTournament == 'Rogers Cup':
                if player.currentTournamentMatchWins == 0:
                    player.rankingPoints = player.rankingPoints + 10
                    player.earnings = player.earnings + 1
                    player.coins = player.coins + 1
                elif player.currentTournamentMatchWins == 1:
                    player.rankingPoints = player.rankingPoints + 25
                    player.earnings = player.earnings + 7
                    player.coins = player.coins + 7
                elif player.currentTournamentMatchWins == 2:
                    player.rankingPoints = player.rankingPoints + 45
                    player.earnings = player.earnings + 17
                    player.coins = player.coins + 17
                elif player.currentTournamentMatchWins == 3:
                    player.rankingPoints = player.rankingPoints + 90
                    player.earnings = player.earnings + 25
                    player.coins = player.coins + 25
                elif player.currentTournamentMatchWins == 4:
                    player.rankingPoints = player.rankingPoints + 180
                    player.earnings = player.earnings + 42
                    player.coins = player.coins + 42
                elif player.currentTournamentMatchWins == 5:
                    player.rankingPoints = player.rankingPoints + 360
                    player.earnings = player.earnings + 50
                    player.coins = player.coins + 50
                elif player.currentTournamentMatchWins == 6:
                    player.rankingPoints = player.rankingPoints + 600
                    player.earnings = player.earnings + 60
                    player.coins = player.coins + 60

            else: #ATP 500
                if player.currentTournamentMatchWins == 2:
                    player.rankingPoints = player.rankingPoints + 20
                    player.earnings = player.earnings + 7
                    player.coins = player.coins + 7
                elif player.currentTournamentMatchWins == 3:
                    player.rankingPoints = player.rankingPoints + 45
                    player.earnings = player.earnings + 17
                    player.coins = player.coins + 17
                elif player.currentTournamentMatchWins == 4:
                    player.rankingPoints = player.rankingPoints + 90
                    player.earnings = player.earnings + 21
                    player.coins = player.coins + 21
                elif player.currentTournamentMatchWins == 5:
                    player.rankingPoints = player.rankingPoints + 180
                    player.earnings = player.earnings + 25
                    player.coins = player.coins + 25
                elif player.currentTournamentMatchWins == 6:
                    player.rankingPoints = player.rankingPoints + 300
                    player.earnings = player.earnings + 30
                    player.coins = player.coins + 30

            '''else: #ATP 250
                if player.currentTournamentMatchWins == 2:
                    player.rankingPoints = player.rankingPoints + 5
                    player.earnings = player.earnings + 4
                    player.coins = player.coins + 4
                elif player.currentTournamentMatchWins == 3:
                    player.rankingPoints = player.rankingPoints + 20
                    player.earnings = player.earnings + 8
                    player.coins = player.coins + 8
                elif player.currentTournamentMatchWins == 4:
                    player.rankingPoints = player.rankingPoints + 45
                    player.earnings = player.earnings + 10
                    player.coins = player.coins + 10
                elif player.currentTournamentMatchWins == 5:
                    player.rankingPoints = player.rankingPoints + 90
                    player.earnings = player.earnings + 12
                    player.coins = player.coins + 12
                elif player.currentTournamentMatchWins == 6:
                    player.rankingPoints = player.rankingPoints + 150
                    player.earnings = player.earnings + 15
                    player.coins = player.coins + 15'''

            '''else: #Challenger
                if player.currentTournamentMatchWins == 2:
                    player.rankingPoints = player.rankingPoints + 5
                    player.earnings = player.earnings + 1
                    player.coins = player.coins + 1
                elif player.currentTournamentMatchWins == 3:
                    player.rankingPoints = player.rankingPoints + 8
                    player.earnings = player.earnings + 2
                    player.coins = player.coins + 2
                elif player.currentTournamentMatchWins == 4:
                    player.rankingPoints = player.rankingPoints + 18
                    player.earnings = player.earnings + 3
                    player.coins = player.coins + 3
                elif player.currentTournamentMatchWins == 5:
                    player.rankingPoints = player.rankingPoints + 35
                    player.earnings = player.earnings + 4
                    player.coins = player.coins + 4
                elif player.currentTournamentMatchWins == 6:
                    player.rankingPoints = player.rankingPoints + 60
                    player.earnings = player.earnings + 5
                    player.coins = player.coins + 5'''
            player.opponentsAlreadyPlayed = []
            opponent.wins = opponent.wins + 1
            player.losses = player.losses + 1

            scoring.opponentWin()
            player.currentTournament = ''
            player.currentTournamentMatchWins = 0
            player.currentMonthTournamentPlays = player.currentMonthTournamentPlays + 1

    def opponentWin(self):
        window = Window()
        window.setupOpponentWin()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        playMatch.playMatchControls

            button('Play Again', 270,700,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
            button('Training', 450,700,150,50, window.colors["blue"], window.colors["lightBlue"], action='training')
            button('My Player', 630,700,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Main Menu', 820,700,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')

            ball.ballBoundaries()
            pygame.display.update()
            window.clock.tick(window.FPS)
            scoring.resetMatch()

class Ball:
    def __init__(self,ballX,ballY,ballXChange,ballYChange,ballRadius,ballSpeed):
        self.ballX = ballX
        self.ballY = ballY
        self.ballXChange = ballXChange
        self.ballYChange = ballYChange
        self.ballRadius = ballRadius
        self.ballSpeed = ballSpeed
        
    def ballBoundaries(self):
        if ball.ballX <= 0:
            ball.ballXChange += ball.ballSpeed
        if ball.ballX > display_width:
            ball.ballXChange -= ball.ballSpeed
        if ball.ballY > display_height:
            ball.ballXChange = 0
            ball.ballYChange = 0
            scoring.opponentWinPoint()
        if ball.ballY <= -1:
            ball.ballXChange = 0
            ball.ballYChange = 0
            scoring.winners = scoring.winners + 1
            scoring.playerWinPoint()

    def wallBoundaries(self): #makes the ball bounce off the wall.
        if ball.ballX <= 0:
            ball.ballX = int(600)
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
        if ball.ballX > display_width:
            ball.ballX = int(600)
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
        if ball.ballY < display_height / 3:
            ball.ballYChange += ball.ballSpeed
        if ball.ballY > display_height:
            ball.ballX = int(600) #if the ball goes below the screen, it is returned to the player to hit at the wall.
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
            
            
    def ballBounce(self):
        pass

    def playerBallIn(self):
        pass

    def playerBallOut(self):
        pass
    
ball = Ball(int(600),int(600),0,0,10,20)

class SmallButton(pygame.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.tinyFont.render(text, True, window.colors["black"])
        self.image = pygame.Surface((self.text_surf.get_width()+20,
                                 self.text_surf.get_height()+10))
        self.image.fill(window.colors["blue"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (10, 5))
        self.rect = self.image.get_rect(topleft=pos)

class UpgradeButton(pygame.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.tinyFont.render(text, True, window.colors["black"])
        self.image = pygame.Surface((self.text_surf.get_width()+20,
                                 self.text_surf.get_height()+10))
        self.image.fill(window.colors["green"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (10, 5))
        self.rect = self.image.get_rect(topleft=pos)

class AchievementsButton(pygame.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.tinyFont.render(text, True, window.colors["black"])
        self.image = pygame.Surface((self.text_surf.get_width()+20,
                                 self.text_surf.get_height()+10))
        #self.image.fill(None)
        # Now blit the text onto the self.image.
        #self.image.blit(self.text_surf, (10, 5))
        self.rect = self.image.get_rect(topleft=pos)
        
class Button(pygame.sprite.Sprite):

    def __init__(self, pos, text, window):
        super().__init__()  # Call __init__ of the parent class.
        # Render the text.
        self.text_surf = window.smallFont.render(text, True, window.colors["black"])
        self.image = pygame.Surface((self.text_surf.get_width()+40,
                                 self.text_surf.get_height()+20))
        self.image.fill(window.colors["green"])
        # Now blit the text onto the self.image.
        self.image.blit(self.text_surf, (20, 10))
        self.rect = self.image.get_rect(topleft=pos)

def textObjects(text, colour, size): #whatever, fonts
    global textSurface
    if size == 'small':
        textSurface = window.smallFont.render(text, True, colour)
    elif size == 'medium':
        textSurface = window.medFont.render(text, True, colour)
    elif size == 'large':
        textSurface = window.largeFont.render(text, True, colour)

    return textSurface, textSurface.get_rect()

def textToButton(msg, colour, buttonx, buttony, buttonwidth, buttonheight, size = 'small'):
    textSurf, textRect = textObjects(msg, colour, size)
    textRect.center = ((buttonx+(buttonwidth/2), buttony+(buttonheight/2))) #finds button center
    window.gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactiveColour, activeColour, action = None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cursor[0] > x and y + height > cursor[1] > y: #x of tl of button > xval of where mouse is
        pygame.draw.rect(window.gameDisplay, activeColour, (x,y,width,height))
        if click[0] == 1 and action!= None: #0th element, means left click. 1 is True, 0 is False.
            if action == 'quit':
                autoSave()
                pygame.quit()
                quit()
            if action == 'playMatch':
                playMatch.playMatchControls()
            if action == 'playTrainingMatch':
                trainingMenu.playTrainingMatch()
            if action == 'wall':
                trainingMenu.wall()
            if action == 'training':
                trainingMenu.training()
            if action == 'myPlayer':
                myPlayerMenu.myPlayer()
            if action == 'shop':
                shopMenu.shop()
            if action == 'statistics':
                statsMenu.stats()
            if action == 'customize':
                customizeMenu.customize()
            if action == 'rankings':
                rankingsMenu.rankings()
            if action == 'controls':
                controlsMenu.controls()
            if action == 'amateur':
                player.difficulty = 'Amateur'
            if action == 'intermediate':
                player.difficulty = 'Intermediate'
            if action == 'pro':
                player.difficulty = 'Pro'
            if action == 'master':
                player.difficulty = 'Master'
            if action == 'impossible':
                player.difficulty = 'Impossible'
            if action == 'tournamentMenu':
                tournamentMenu.tournament()
            if action == 'levelUp':
                levelUpMenu.levelUp()
            if action == 'mainMenu':
                gameIntroMenu.gameIntro()
            if action == 'resume':
                window.gameExit = False
            if action == 'saveGame':
                saveGame.save()
            if action == 'saveSlot1' or action == 'saveSlot2' or action == 'saveSlot3' or action == 'saveSlot4' or action == 'saveSlot5' or action == 'saveSlot6' or action == 'saveSlot7':
                fileList = ['name.txt','ranking.txt','country.txt','power.txt','accuracy.txt','speed.txt','fitness.txt','consistency.txt','x.txt','y.txt','xchange.txt','ychange.txt','width.txt','height.txt','difficulty.txt','skillpoints.txt','coins.txt','energy.txt','level.txt','xp.txt','matchesplayed.txt','wins.txt','losses.txt',
                            'matchwinloss%.txt','tournamentsplayed.txt','tournamentwins.txt','grandslamwins.txt','masters1000wins.txt','atp500wins.txt','currenttournament.txt','currenttournamentmatchwins.txt','currentround.txt','earnings.txt','pointsplayed.txt','pointswon.txt','pointslost.txt','pointswinloss%.txt','hand.txt','opponentsalreadyplayed.txt',
                            'opponentname.txt','opponentcountry.txt','opponentranking.txt','opponentrankingpoints.txt','opponentpower.txt','opponentaccuracy.txt','opponentspeed.txt','opponentfitness.txt','opponentconsistency.txt','opponentx.txt','opponenty.txt','opponentxchange.txt','opponentychange.txt','opponentwidth.txt','opponentheight.txt','playerscore.txt','opponentscore.txt','playerpoints.txt','opponentpoints.txt','playergames.txt','opponentgames.txt','playersets.txt','opponentsets.txt','hits.txt','rallylength.txt','winners.txt','errors.txt','ballx.txt','bally.txt','ballxchange.txt','ballychange.txt','ballradius.txt','ballspeed.txt'
                            ,'winfirstmatch.txt','winfirsttournament.txt','win100matches.txt','winfirstmasters1000.txt','winfirstgrandslam.txt','win20grandslams.txt','beatdjokovic.txt','beatfederer.txt','beatnadal.txt','worldnumber1.txt','maxupgrades.txt','completeallachievements.txt','currentMonthTournamentPlays.txt','currentMonthTournamentsAlreadyPlayed.txt','monthCount.txt','currentYear.txt']
                toWrite = [player.name,player.ranking,player.country,player.power,player.accuracy,player.speed,player.fitness,player.consistency,player.x,player.y,player.xChange,player.yChange,player.width,player.height,player.difficulty,player.skillPoints,player.coins,player.energy,player.level,player.xp,player.matchesPlayed,player.wins,player.losses,
                            0,player.tournamentsPlayed,player.tournamentWins,player.grandSlamWins,player.masters1000Wins,player.atp500Wins,player.currentTournament,player.currentTournamentMatchWins,player.currentRound,player.earnings,player.pointsPlayed,player.pointsWon,player.pointsLost,0,player.hand,player.opponentsAlreadyPlayed,
                            opponent.name,opponent.country,opponent.ranking,opponent.rankingPoints,opponent.power,opponent.accuracy,opponent.speed,opponent.fitness,opponent.consistency,opponent.x,opponent.y,opponent.xChange,opponent.yChange,opponent.width,opponent.height,scoring.playerScore,scoring.opponentScore,scoring.playerPoints,scoring.opponentPoints,scoring.playerGames,scoring.opponentGames,scoring.playerSets,scoring.opponentSets,scoring.hits,scoring.rallyLength,scoring.winners,scoring.errors,ball.ballX,ball.ballY,ball.ballXChange,ball.ballYChange,ball.ballRadius,ball.ballSpeed
                            ,winFirstMatch.completed,winFirstTournament.completed,win100Matches.completed,winFirstMasters1000.completed,winFirstGrandSlam.completed,win20GrandSlams.completed,beatDjokovic.completed,beatFederer.completed,beatNadal.completed,worldNumber1.completed,maxUpgrades.completed,completeAllAchievements.completed,player.currentMonthTournamentPlays,player.currentMonthTournamentsAlreadyPlayed,player.monthCount,player.currentYear]

                if action == 'saveSlot1':
                    window.saveSlot1 = True
                    directory = 'saveslot1'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot1/'+fileList[i],'w')
                        playerNameText = window.medFont.render(str(player.name),True,window.colors["black"])
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                
                elif action == 'saveSlot2':
                    window.saveSlot2 = True
                    directory = 'saveslot2'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot2/'+fileList[i],'w')
                        playerName2Text = window.medFont.render(str(player.name),True,window.colors["black"])
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                elif action == 'saveSlot3':
                    window.saveSlot3 = True
                    directory = 'saveslot3'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot3/'+fileList[i],'w')
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                elif action == 'saveSlot4':
                    window.saveSlot4 = True
                    directory = 'saveslot4'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot4/'+fileList[i],'w')
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                elif action == 'saveSlot5':
                    window.saveSlot5 = True
                    directory = 'saveslot5'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot5/'+fileList[i],'w')
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                elif action == 'saveSlot6':
                    window.saveSlot6 = True
                    directory = 'saveslot6'
                    i = 0
                    j = 0
                    while i < len(fileList):
                        file = open('C:/NEA Tennis Game/Saves/saveslot6/'+fileList[i],'w')
                        for element in str(toWrite[j]):
                            file.write(element)
                        i = i+1
                        j = j+1
                file.close()
            if action == 'newGame':
                newGame()
            if action == 'deleteSlot1':
                folder = 'C:/NEA Tennis Game/Saves/saveslot1/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot2':
                folder = 'C:/NEA Tennis Game/Saves/saveslot2/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot3':
                folder = 'C:/NEA Tennis Game/Saves/saveslot3/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot4':
                folder = 'C:/NEA Tennis Game/Saves/saveslot4/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot5':
                folder = 'C:/NEA Tennis Game/Saves/saveslot5/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot6':
                folder = 'C:/NEA Tennis Game/Saves/saveslot6/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot7':
                folder = 'C:/NEA Tennis Game/Saves/saveslot7/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'deleteSlot8':
                folder = 'C:/NEA Tennis Game/Saves/saveslot8/'
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        os.remove(os.path.join(root, file))
            if action == 'loadGame':
                loadGame.load()
            if action == 'loadSlot1' or action == 'loadSlot2' or action == 'loadSlot3' or action == 'loadSlot4' or action == 'loadSlot5' or action == 'loadSlot6' or action == 'loadSlot7':
               fileList = ['name.txt','ranking.txt','country.txt','power.txt','accuracy.txt','speed.txt','fitness.txt','consistency.txt','x.txt','y.txt','xchange.txt','ychange.txt','width.txt','height.txt','difficulty.txt','skillpoints.txt','coins.txt','energy.txt','level.txt','xp.txt','matchesplayed.txt','wins.txt','losses.txt',
                            'matchwinloss%.txt','tournamentsplayed.txt','tournamentwins.txt','grandslamwins.txt','masters1000wins.txt','atp500wins.txt','currenttournament.txt','currenttournamentmatchwins.txt','currentround.txt','earnings.txt','pointsplayed.txt','pointswon.txt','pointslost.txt','pointswinloss%.txt','hand.txt','opponentsalreadyplayed.txt',
                            'opponentname.txt','opponentcountry.txt','opponentranking.txt','opponentrankingpoints.txt','opponentpower.txt','opponentaccuracy.txt','opponentspeed.txt','opponentfitness.txt','opponentconsistency.txt','opponentx.txt','opponenty.txt','opponentxchange.txt','opponentychange.txt','opponentwidth.txt','opponentheight.txt','playerscore.txt','opponentscore.txt','playerpoints.txt','opponentpoints.txt','playergames.txt','opponentgames.txt','playersets.txt','opponentsets.txt','hits.txt','rallylength.txt','winners.txt','errors.txt','ballx.txt','bally.txt','ballxchange.txt','ballychange.txt','ballradius.txt','ballspeed.txt'
                            ,'winfirstmatch.txt','winfirsttournament.txt','win100matches.txt','winfirstmasters1000.txt','winfirstgrandslam.txt','win20grandslams.txt','beatdjokovic.txt','beatfederer.txt','beatnadal.txt','worldnumber1.txt','maxupgrades.txt','completeallachievements.txt','currentMonthTournamentPlays.txt','currentMonthTournamentsAlreadyPlayed.txt','monthCount.txt','currentYear.txt']
               toLoad = [player.name,player.ranking,player.country,player.power,player.accuracy,player.speed,player.fitness,player.consistency,player.x,player.y,player.xChange,player.yChange,player.width,player.height,player.difficulty,player.skillPoints,player.coins,player.energy,player.level,player.xp,player.matchesPlayed,player.wins,player.losses,
                            0,player.tournamentsPlayed,player.tournamentWins,player.grandSlamWins,player.masters1000Wins,player.atp500Wins,player.currentTournament,player.currentTournamentMatchWins,player.currentRound,player.earnings,player.pointsPlayed,player.pointsWon,player.pointsLost,0,player.hand,player.opponentsAlreadyPlayed,
                            opponent.name,opponent.country,opponent.ranking,opponent.rankingPoints,opponent.power,opponent.accuracy,opponent.speed,opponent.fitness,opponent.consistency,opponent.x,opponent.y,opponent.xChange,opponent.yChange,opponent.width,opponent.height,scoring.playerScore,scoring.opponentScore,scoring.playerPoints,scoring.opponentPoints,scoring.playerGames,scoring.opponentGames,scoring.playerSets,scoring.opponentSets,scoring.hits,scoring.rallyLength,scoring.winners,scoring.errors,ball.ballX,ball.ballY,ball.ballXChange,ball.ballYChange,ball.ballRadius,ball.ballSpeed
                            ,winFirstMatch.completed,winFirstTournament.completed,win100Matches.completed,winFirstMasters1000.completed,winFirstGrandSlam.completed,win20GrandSlams.completed,beatDjokovic.completed,beatFederer.completed,beatNadal.completed,worldNumber1.completed,maxUpgrades.completed,completeAllAchievements.completed,player.currentMonthTournamentPlays,player.currentMonthTournamentsAlreadyPlayed,player.monthCount,player.currentYear]


               if action == 'loadSlot1':
                    try:
                        directory = 'saveslot1'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot1/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot2':
                    try:
                        directory = 'saveslot2'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot2/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot3':
                    try:
                        directory = 'saveslot3'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot3/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot4':
                    try:
                        directory = 'saveslot4'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot4/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot5':
                    try:
                        directory = 'saveslot5'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot5/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot6':
                    try:
                        directory = 'saveslot6'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot6/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot7':
                    try:
                        directory = 'saveslot7'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot7/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass
               elif action == 'loadSlot8':
                    try:
                        directory = 'saveslot8'
                        i = 0
                        j = 0
                        contentsList = []
                        while i < len(fileList):
                            file = open('C:/NEA Tennis Game/Saves/saveslot8/'+fileList[i],'r')
                            contents = file.read()
                            contentsList.append(contents)
                            i = i+1
                        player.name = contentsList[0]
                        player.ranking = contentsList[1]
                        player.country = contentsList[2]
                        player.power = int(contentsList[3])
                        player.accuracy = int(contentsList[4])
                        player.speed = float(contentsList[5])
                        player.fitness = float(contentsList[6])
                        player.consistency = int(contentsList[7])
                        player.x = float(contentsList[8])
                        player.y = float(contentsList[9])
                        player.xChange = float(contentsList[10])
                        player.yChange = float(contentsList[11])
                        player.width = float(contentsList[12])
                        player.height = float(contentsList[13])
                        player.difficulty = contentsList[14]
                        player.skillPoints = int(contentsList[15])
                        player.coins = int(contentsList[16])
                        player.energy = int(contentsList[17])
                        player.level = int(contentsList[18])
                        player.xp = int(contentsList[19])
                        player.matchesPlayed = int(contentsList[20])
                        player.wins = int(contentsList[21])
                        player.losses = int(contentsList[22])
                        blah = int(contentsList[23])
                        player.tournamentsPlayed = int(contentsList[24])
                        player.tournamentWins = int(contentsList[25])
                        player.grandSlamWins = int(contentsList[26])
                        player.masters1000Wins = int(contentsList[27])
                        player.atp500Wins = int(contentsList[28])
                        player.currentTournament = contentsList[29]
                        player.currentTournamentMatchWins = int(contentsList[30])
                        player.currentRound = contentsList[31]
                        player.earnings = int(contentsList[32])
                        player.pointsPlayed = int(contentsList[33])
                        player.pointsWon = int(contentsList[34])
                        player.pointsLost = int(contentsList[35])
                        blah2 = int(contentsList[36])
                        player.hand = contentsList[37]
                        player.opponentsAlreadyPlayed = list(contentsList[38])
                        opponent.name = contentsList[39]
                        opponent.country = contentsList[40]
                        opponent.ranking = contentsList[41]
                        opponent.rankingPoints = int(contentsList[42])
                        opponent.power = int(contentsList[43])
                        opponent.accuracy = int(contentsList[44])
                        opponent.speed = int(contentsList[45])
                        opponent.fitness = int(contentsList[46])
                        opponent.consistency = int(contentsList[47])
                        opponent.x = float(contentsList[48])
                        opponent.y = float(contentsList[49])
                        opponent.xChange = float(contentsList[50])
                        opponent.yChange = float(contentsList[51])
                        opponent.width = float(contentsList[52])
                        opponent.height = float(contentsList[53])
                        scoring.playerScore = int(contentsList[54])
                        scoring.opponentScore = int(contentsList[55])
                        scoring.playerPoints = int(contentsList[56])
                        scoring.opponentPoints = int(contentsList[57])
                        scoring.playerGames = int(contentsList[58])
                        scoring.opponentGames = int(contentsList[59])
                        scoring.playerSets = int(contentsList[60])
                        scoring.opponentSets = int(contentsList[61])
                        scoring.hits = int(contentsList[62])
                        scoring.rallyLength = int(contentsList[63])
                        scoring.winners = int(contentsList[64])
                        scoring.errors = int(contentsList[65])
                        ball.ballX = int(contentsList[66])
                        ball.ballY = int(contentsList[67])
                        ball.ballXChange = int(contentsList[68])
                        ball.ballYChange = int(contentsList[69])
                        ball.ballRadius = int(contentsList[70])
                        ball.ballSpeed = int(contentsList[71])
                        player.monthCount = int(contentsList[84])
                        player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
                        player.currentMonthTournamentPlays = int(contentsList[86])
                        player.currentYear = int(contentsList[87])
        
                        file.close()
                    except FileNotFoundError:
                        pass

            if action == 'quitTournament':
                player.currentTournament = ''
                player.currentTournamentMatchWins = 0
                player.currentRound = 'Round of 128'
                player.opponentsAlreadyPlayed = []
                autoSave()
                gameIntroMenu.gameIntro()
            if action == 'opponentMenu':
                if player.currentTournament == '':
                    tournamentMenu.tournament()
                else:
                    opponentMenu.showOpponent()

                
    else:
        pygame.draw.rect(window.gameDisplay, inactiveColour,(x,y,width,height))

    textToButton(text,window.colors["black"],x,y,width,height)

class Tournament:
    def __init__(self,name,image,country,city,month,level,surface,prizeMoney,rankingPoints,skillPoints):
        self.name = name
        self.image = image
        self.country = country
        self.city = city
        self.month = month
        self.level = level
        self.surface = surface
        self.prizeMoney = prizeMoney
        self.rankingPoints = rankingPoints
        self.skillPoints = skillPoints

australianOpen = Tournament('Australian Open','','Australia','Melbourne','Jan','Grand Slam','Hard',500,2000,1)
frenchOpen = Tournament('Roland Garros','','France','Paris','May','Grand Slam','Clay',500,2000,1)
wimbledon = Tournament('Wimbledon','','United Kingdom','London','Jun','Grand Slam','Grass',500,2000,1)
usOpen = Tournament('US Open','','USA','New York','Aug','Grand Slam','Hard',500,2000,1)
atpFinals = Tournament('ATP Finals','','United Kingdom','London','Nov','ATP Finals','Hard',500,2000,1)
atpCup = Tournament('ATP Cup','','Australia','Sydney','Jan','ATP Cup','Hard',500,1500,1)
laverCup = Tournament('Laver Cup','','USA','Boston, Massechusetts','Sep','Laver Cup','Hard',380,1000,1)
davisCupFinals = Tournament('Davis Cup Finals','','Spain','Madrid','Nov','Davis Cup','Hard',380,1000,1)
tokyoOlympics = Tournament('Tokyo Olympic Games','','Japan','Tokyo','Jul','Tokyo Olympics','Hard',0,0,1)
indianWells = Tournament('BNP Paribas Open','','USA','Indian Wells, California','Mar','Masters 1000','Hard',380,1000,1)
miamiOpen = Tournament('Miami Open','','USA','Miami, Florida','Mar','Masters 1000','Hard',380,1000,1)
monteCarlo = Tournament('Rolex Monte Carlo Masters','','Monaco','Monte Carlo','Apr','Masters 1000','Clay',380,1000,1)
madridOpen = Tournament('Madrid Open','','Spain','Madrid','May','Masters 1000','Clay',380,1000,1)
rogersCup = Tournament('Rogers Cup','','Canada','Toronto','Aug','Masters 1000','Hard',380,1000,1)
cincinatti = Tournament('Western & Southern Open','','USA','Cincinatti, Ohio','Aug','Masters 1000','Hard',380,1000,1)
rome = Tournament('Internazionali BNL d\'Italia','','Italy','Rome','May','Masters 1000','Clay',380,1000,1)
shanghai = Tournament('Rolex Shanghai Masters','','China','Shanghai','Oct','Masters 1000','Hard',380,1000,1)
paris = Tournament('Rolex Paris Masters','','France','Paris','Nov','Masters 1000','Hard',380,1000,1)
doha = Tournament('Qatar ExxonMobil Open','','Qatar','Doha','Jan','ATP 250','Hard',380,1000,1)
adelaide = Tournament('Adelaide International','','Australia','Adelaide','Jan','ATP 250','Hard',380,250,1)
auckland = Tournament('ASB Classic','','New Zealand','Auckland','Jan','ATP 250','Hard',380,1000,1)
cordoba = Tournament('Cordoba Open','','Argentina','Cordoba','Feb','ATP 250','Clay',380,1000,1)
pune = Tournament('Tata Open Maharashtra','','India','Pune','Feb','ATP 250','Hard',380,1000,1)
montpellier = Tournament('Open Sud de France','','France','Montpellier','Feb','ATP 250','Hard',380,1000,1)
rotterdam = Tournament('AMRO World Tennis Tournament','','Netherlands','Rotterdam','Feb','ATP 500','Hard',380,1000,1)
newYork = Tournament('New York Open','','USA','New York, New York','Feb','ATP 250','Hard',380,1000,1)
buenosAires = Tournament('Argentina Open','','Argentina','Buenos Aires','Feb','ATP 250','Clay',380,1000,1)
rio = Tournament('Rio Open','','Brazil','Rio de Janeiro','Feb','ATP 500','Clay',380,1000,1)
marseille = Tournament('Open 13 Provence','','France','Marseille','Feb','ATP 250','Hard',380,1000,1)
delrayBeach = Tournament('Delray Beach Open','','USA','Delray Beach, Florida','Feb','ATP 250','Hard',380,1000,1)
dubai = Tournament('Dubai Tennis Championships','','UAE','Dubai','Feb','ATP 500','Hard',380,500,1)
acapulco = Tournament('Acapulco Open','','Mexico','Acapulco','Feb','ATP 500','Hard',380,1000,1)
santiago = Tournament('Santiago Open','','Chile','Santiago','Feb','ATP 250','Clay',380,1000,1)
houston = Tournament('US Men\'s Clay Court Champs','','USA','Houston, Texas','Apr','ATP 250','Clay',380,1000,1)
marrakech = Tournament('Grand Prix Hassan II','','Monaco','Marrakech','Apr','ATP 250','Clay',380,1000,1)
barcelona = Tournament('Barcelona Open','','Spain','Barcelona','Apr','ATP 500','Clay',380,1000,1)
budapest = Tournament('Hungarian Open','','Hungary','Budapest','Apr','ATP 250','Clay',380,1000,1)
munich = Tournament('Munich Open','','Germany','Munich','Apr','ATP 250','Clay',380,1000,1)
estoril = Tournament('Millennium Estoril Open','','Portugal','Estoril','Apr','ATP 250','Clay',380,1000,1)
geneva = Tournament('Geneva Open','','Switzerland','Geneva','May','ATP 250','Clay',380,1000,1)
lyon = Tournament('Open Parc Rhone-Alpes Lyon','','France','Lyon','May','ATP 250','Clay',380,1000,1)
stuttgart = Tournament('MercedesCup','','Germany','Stuttgart','May','ATP 250','Grass',380,1000,1)
sHertogenbosch = Tournament('Libema Open','','Netherlands','s-Hertogenbosch','Jun','ATP 250','Grass',380,1000,1)
london = Tournament('Fever-Tree Championships','','United Kingdom','London','Jun','ATP 500','Grass',380,1000,1)
halle = Tournament('Halle Open','','Germany','Halle','Jun','ATP 500','Grass',380,1000,1)
mallorca = Tournament('Mallorca Championships','','Spain','Mallorca','Jun','ATP 250','Grass',380,1000,1)
eastbourne = Tournament('Nature Valley International','','United Kingdom','Eastbourne','Jun','ATP 250','Grass',380,1000,1)
hamburg = Tournament('Hamburg European Open','','Germany','Hamburg','Jul','ATP 500','Clay',380,1000,1)
newport = Tournament('Hall of Fame Open','','USA','Newport, Rhode Island','Jul','ATP 250','Grass',380,1000,1)
bastad = Tournament('Nordea Open','','Sweden','Bastad','Jul','ATP 250','Clay',380,1000,1)
losCabos = Tournament('Abierto de Tenis Mifel','','Mexico','Los Cabos','Jul','ATP 250','Hard',380,1000,1)
gstaad = Tournament('Swiss Open Gstaad','','Switzerland','Gstaad','Jul','ATP 250','Clay',380,1000,1)
umag = Tournament('Croatia Open Umag','','Croatia','Umag','Jul','ATP 250','Clay',380,1000,1)
atlanta = Tournament('Atlanta Open','','USA','Atlanta, Georgia','Jul','ATP 250','Hard',380,1000,1)
kitzbuhel = Tournament('Generali Open','','Austria','Kitzbuhel','Jul','ATP 250','Clay',380,1000,1)
washington = Tournament('Citi Open','','USA','Washington DC','Aug','ATP 500','Hard',380,1000,1)
winstonSalem = Tournament('Winston Salem Open','','USA','Winston-Salem, North Carolina','Aug','ATP 250','Hard',380,1000,1)
stPetersburg = Tournament('St. Petersburg Open','','Russia','St. Petersburg','Sep','ATP 250','Hard',380,1000,1)
metz = Tournament('Moselle Open','','France','Metz','Aug','ATP 250','Hard',380,1000,1)
chengdu = Tournament('Chengdu Open','','China','Chengdu','Aug','ATP 250','Hard',380,1000,1)
zhuhai = Tournament('Zhuhai Championships','','China','Zhuhai','Aug','ATP 250','Hard',380,1000,1)
sofia = Tournament('Sofia Open','','Bulgaria','Sofia','Aug','ATP 250','Hard',380,1000,1)
beijing = Tournament('China Open','','China','Beijing','Oct','ATP 500','Hard',380,1000,1)
tokyo = Tournament('Japan Open Tennis Championships','','Japan','Tokyo','Oct','ATP 500','Hard',380,1000,1)
moscow = Tournament('VTB Kremlin Cup','','Russia','Moscow','Oct','ATP 250','Hard',380,1000,1)
antwerp = Tournament('European Open','','Belgium','Antwerp','Oct','ATP 250','Hard',380,1000,1)
stockholm = Tournament('Stockholm Open','','Sweden','Stockholm','Oct','ATP 250','Hard',380,1000,1)
vienna = Tournament('Erste Bank Open','','Austria','Vienna','Oct','ATP 500','Hard',380,1000,1)
basel = Tournament('Swiss Indors Basel','','Switzerland','Basel','Oct','ATP 500','Hard',380,1000,1)

class TournamentMenu:
    def __init__(self):
        pass
    
    def tournament(self):
        window = Window()
        window.setupTournamentMenu()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        if player.currentMonth == 'January':
            atpCupButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            dohaButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            adelaideButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            aucklandButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            australianOpenButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            gui.add(atpCupButton,dohaButton,adelaideButton,aucklandButton,australianOpenButton)

        elif player.currentMonth == 'February':
            cordobaButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            puneButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            montpellierButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            rotterdamButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            newYorkButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            buenosAiresButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            rioButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            marseilleButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            delrayBeachButton = SmallButton(
                pos=(window.rect.w/4 + 646
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            dubaiButton = SmallButton(
                pos=(window.rect.w/4 + 646
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            acapulcoButton = SmallButton(
                pos=(window.rect.w/4 + 646
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            santiagoButton = SmallButton(
                pos=(window.rect.w/4 + 646
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            gui.add(cordobaButton,puneButton,montpellierButton,rotterdamButton,newYorkButton,buenosAiresButton,rioButton,marseilleButton,
                    delrayBeachButton,dubaiButton,acapulcoButton,santiagoButton)

        elif player.currentMonth == 'March':
            indianWellsButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            miamiButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            gui.add(indianWellsButton,miamiButton)

        elif player.currentMonth == 'April':
            houstonButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            marrakechButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            monteCarloButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            barcelonaButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            budapestButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            munichButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            estorilButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            gui.add(houstonButton,marrakechButton,monteCarloButton,barcelonaButton,budapestButton,munichButton,estorilButton)

        elif player.currentMonth == 'May':
            madridButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            romeButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            genevaButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            lyonButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            parisButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            gui.add(madridButton,romeButton,genevaButton,lyonButton,parisButton)

        elif player.currentMonth == 'June':
            stuttgartButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            sHertogenboschButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            londonButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            halleButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            mallorcaButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            eastbourneButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            wimbledonButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            gui.add(stuttgartButton,sHertogenboschButton,londonButton,halleButton,mallorcaButton,eastbourneButton,wimbledonButton)

        elif player.currentMonth == 'July' and player.currentYear == 2020:
            hamburgButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            newportButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            bastadButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            losCabosButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            gstaadButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            umagButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            tokyoOlympicsButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            atlantaButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            kitzbuhelButton = SmallButton(
                pos=(window.rect.w/4 + 646
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            gui.add(hamburgButton,newportButton,bastadButton,losCabosButton,gstaadButton,umagButton,tokyoOlympicsButton,atlantaButton,kitzbuhelButton)
        elif player.currentMonth == 'July' and player.currentYear != 2020:
            hamburgButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            newportButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            bastadButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            losCabosButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            gstaadButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            umagButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            atlantaButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            kitzbuhelButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            gui.add(hamburgButton,newportButton,bastadButton,losCabosButton,gstaadButton,umagButton,atlantaButton,kitzbuhelButton)
        elif player.currentMonth == 'August':
            washingtonButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            rogersCupButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            cincinattiButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            winstonSalemButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            usOpenButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            gui.add(washingtonButton,rogersCupButton,cincinattiButton,winstonSalemButton,usOpenButton)
        elif player.currentMonth == 'September':
            stPetersburgButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            metzButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            laverCupButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            chengduButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            zhuhaiButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            sofiaButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            gui.add(stPetersburgButton,metzButton,laverCupButton,chengduButton,zhuhaiButton,sofiaButton)
        elif player.currentMonth == 'October':
            beijingButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            tokyoButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            shanghaiButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            moscowButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            antwerpButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 55),
                text="Select",
                window=window,
                )
            stockholmButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            viennaButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 505),
                text="Select",
                window=window,
                )
            baselButton = SmallButton(
                pos=(window.rect.w/4 + 226
                     , window.rect.h/6 + 725),
                text="Select",
                window=window,
                )
            gui.add(beijingButton,tokyoButton,shanghaiButton,moscowButton,antwerpButton,stockholmButton,viennaButton,baselButton)
        elif player.currentMonth == 'November':
            parisButton = SmallButton(
            pos=(window.rect.w/4 - 194
                 , window.rect.h/6 + 55),
            text="Select",
            window=window,
            )
            atpFinalsButton = SmallButton(
                pos=(window.rect.w/4 - 194
                     , window.rect.h/6 + 285),
                text="Select",
                window=window,
                )
            gui.add(parisButton,atpFinalsButton)


        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player.coins = player.coins - 60
                    if player.currentMonth == 'January':
                        if atpCupButton.rect.collidepoint(event.pos):
                            self.atpCupCourt = pygame.image.load('C:/NEA Tennis Game/Courts/atpcupcourt.png')
                            player.currentTournament = 'ATP Cup'
                            opponentMenu.showOpponent()
                        elif dohaButton.rect.collidepoint(event.pos):
                            self.dohaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
                            player.currentTournament = 'Qatar ExxonMobil Open'
                            opponentMenu.showOpponent()
                        elif adelaideButton.rect.collidepoint(event.pos):
                            self.adelaideCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2.png')
                            player.currentTournament = 'Adelaide International'
                            opponentMenu.showOpponent()
                        elif aucklandButton.rect.collidepoint(event.pos):
                            self.aucklandCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'ASB Classic'
                            opponentMenu.showOpponent()
                        elif australianOpenButton.rect.collidepoint(event.pos):
                            self.australianOpenCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'Australian Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'February':
                        if cordobaButton.rect.collidepoint(event.pos):
                            self.cordobaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Cordoba Open'
                            opponentMenu.showOpponent()
                        elif puneButton.rect.collidepoint(event.pos):
                            self.puneCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Tata Open Maharashtra'
                            opponentMenu.showOpponent()
                        elif montpellierButton.rect.collidepoint(event.pos):
                            self.montpellierCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Open Sud de France'
                            opponentMenu.showOpponent()
                        elif rotterdamButton.rect.collidepoint(event.pos):
                            self.rotterdamCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'AMRO World Tennis Tournament'
                            opponentMenu.showOpponent()
                        elif newYorkButton.rect.collidepoint(event.pos):
                            self.newYorkCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'New York Open'
                            opponentMenu.showOpponent()
                        elif buenosAiresButton.rect.collidepoint(event.pos):
                            self.buenosAiresCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Argentina Open'
                            opponentMenu.showOpponent()
                        elif rioButton.rect.collidepoint(event.pos):
                            self.rioCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Rio Open'
                            opponentMenu.showOpponent()
                        elif marseilleButton.rect.collidepoint(event.pos):
                            self.marseilleCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Open 13 Provence'
                            opponentMenu.showOpponent()
                        elif delrayBeachButton.rect.collidepoint(event.pos):
                            self.delrayBeachCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Delray Beach Open'
                            opponentMenu.showOpponent()
                        elif dubaiButton.rect.collidepoint(event.pos):
                            self.dubaiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Dubai Tennis Championships'
                            opponentMenu.showOpponent()
                        elif acapulcoButton.rect.collidepoint(event.pos):
                            self.acapulcoCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Acapulco Open'
                            opponentMenu.showOpponent()
                        elif santiagoButton.rect.collidepoint(event.pos):
                            self.santiagoCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Santiago Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'March':
                        if indianWellsButton.rect.collidepoint(event.pos):
                            self.indianWellsCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'BNP Paribas Open'
                            opponentMenu.showOpponent()
                        elif miamiButton.rect.collidepoint(event.pos):
                            self.miamiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Miami Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'April':
                        if houstonButton.rect.collidepoint(event.pos):
                            self.houstonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'US Men\'s Clay Court Champs'
                            opponentMenu.showOpponent()
                        elif marrakechButton.rect.collidepoint(event.pos):
                            self.marrakechCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Grand Prix Hassan II'
                            opponentMenu.showOpponent()
                        elif monteCarloButton.rect.collidepoint(event.pos):
                            self.monteCarloCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Rolex Monte Carlo Masters'
                            opponentMenu.showOpponent()
                        elif barcelonaButton.rect.collidepoint(event.pos):
                            self.barcelonaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Barcelona Open'
                            opponentMenu.showOpponent()
                        elif budapestButton.rect.collidepoint(event.pos):
                            self.budapestCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Hungarian Open'
                            opponentMenu.showOpponent()
                        elif munichButton.rect.collidepoint(event.pos):
                            self.munichCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Munich Open'
                            opponentMenu.showOpponent()
                        elif estorilButton.rect.collidepoint(event.pos):
                            self.estorilCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Millennium Estoril Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'May':
                        if madridButton.rect.collidepoint(event.pos):
                            self.madridCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Madrid Open'
                            opponentMenu.showOpponent()
                        elif romeButton.rect.collidepoint(event.pos):
                            self.romeCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Internazionali BNL d\'Italia'
                            opponentMenu.showOpponent()
                        elif genevaButton.rect.collidepoint(event.pos):
                            self.genevaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Geneva Open'
                            opponentMenu.showOpponent()
                        elif lyonButton.rect.collidepoint(event.pos):
                            self.lyonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Open Parc Rhone-Alpes Lyon'
                            opponentMenu.showOpponent()
                        elif parisButton.rect.collidepoint(event.pos):
                            self.parisCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Roland Garros'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'June':
                        if stuttgartButton.rect.collidepoint(event.pos):
                            self.stuttgartCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'MercedesCup'
                            opponentMenu.showOpponent()
                        elif sHertogenboschButton.rect.collidepoint(event.pos):
                            self.sHertogenboschCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Libema Open'
                            opponentMenu.showOpponent()
                        elif londonButton.rect.collidepoint(event.pos):
                            self.londonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Fever Tree Championships'
                            opponentMenu.showOpponent()
                        elif halleButton.rect.collidepoint(event.pos):
                            self.halleCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Noventi Open'
                            opponentMenu.showOpponent()
                        elif mallorcaButton.rect.collidepoint(event.pos):
                            self.mallorcaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Mallorca Championships'
                            opponentMenu.showOpponent()
                        elif eastbourneButton.rect.collidepoint(event.pos):
                            self.eastbourneCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Nature Valley International'
                            opponentMenu.showOpponent()
                        elif wimbledonButton.rect.collidepoint(event.pos):
                            self.wimbledonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Wimbledon'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'July' and player.currentYear == 2020:
                        if hamburgButton.rect.collidepoint(event.pos):
                            self.hamburgCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Hamburg European Open'
                            opponentMenu.showOpponent()
                        elif newportButton.rect.collidepoint(event.pos):
                            self.newportCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Hall of Fame Open'
                            opponentMenu.showOpponent()
                        elif bastadButton.rect.collidepoint(event.pos):
                            self.bastadCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Nordea Open'
                            opponentMenu.showOpponent()
                        elif losCabosButton.rect.collidepoint(event.pos):
                            self.losCabosCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Abierto de Tenis Mifel'
                            opponentMenu.showOpponent()
                        elif gstaadButton.rect.collidepoint(event.pos):
                            self.gstaadCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Swiss Open Gstaad'
                            opponentMenu.showOpponent()
                        elif umagButton.rect.collidepoint(event.pos):
                            self.umagCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Croatia Open Umag'
                            opponentMenu.showOpponent()
                        elif tokyoOlympicsButton.rect.collidepoint(event.pos):
                            self.tokyoOlympicsCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Tokyo Olympic Games'
                            opponentMenu.showOpponent()
                        elif atlantaButton.rect.collidepoint(event.pos):
                            self.atlantaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Atlanta Open'
                            opponentMenu.showOpponent()
                        elif kitzbuhelButton.rect.collidepoint(event.pos):
                            self.kitzbuhelCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Generali Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'July' and player.currentYear != 2020:
                        if hamburgButton.rect.collidepoint(event.pos):
                            self.hamburgCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Hamburg European Open'
                            opponentMenu.showOpponent()
                        elif newportButton.rect.collidepoint(event.pos):
                            self.newportCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Hall of Fame Open'
                            opponentMenu.showOpponent()
                        elif bastadButton.rect.collidepoint(event.pos):
                            self.bastadCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Nordea Open'
                            opponentMenu.showOpponent()
                        elif losCabosButton.rect.collidepoint(event.pos):
                            self.losCabosCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Abierto de Tenis Mifel'
                            opponentMenu.showOpponent()
                        elif gstaadButton.rect.collidepoint(event.pos):
                            self.gstaadCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Swiss Open Gstaad'
                            opponentMenu.showOpponent()
                        elif umagButton.rect.collidepoint(event.pos):
                            self.umagCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Croatia Open Umag'
                            opponentMenu.showOpponent()
                        elif atlantaButton.rect.collidepoint(event.pos):
                            self.atlantaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Atlanta Open'
                            opponentMenu.showOpponent()
                        elif kitzbuhelButton.rect.collidepoint(event.pos):
                            self.kitzbuhelCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Generali Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'August':
                        if washingtonButton.rect.collidepoint(event.pos):
                            self.washingtonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Citi Open'
                            opponentMenu.showOpponent()
                        elif rogersCupButton.rect.collidepoint(event.pos):
                            self.rogersCupCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Rogers Cup'
                            oppnentMenu.showOpponent()
                        elif cincinattiButton.rect.collidepoint(event.pos):
                            self.cincinattiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Western & Southern Open'
                            opponentMenu.showOpponent()
                        elif winstonSalemButton.rect.collidepoint(event.pos):
                            self.winstonSalemCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Winston-Salem Open'
                            opponentMenu.showOpponent()
                        elif usOpenButton.rect.collidepoint(event.pos):
                            self.usOpenCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'US Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'September':
                        if stPetersburgButton.rect.collidepoint(event.pos):
                            self.stPetersburgCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'St. Petersburg Open'
                            opponentMenu.showOpponent()
                        elif metzButton.rect.collidepoint(event.pos):
                            self.metzCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Moselle Open'
                            opponentMenu.showOpponent()
                        elif laverCupButton.rect.collidepoint(event.pos):
                            self.laverCupCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Laver Cup'
                            opponentMenu.showOpponent()
                        elif chengduButton.rect.collidepoint(event.pos):
                            self.chengduCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Chengdu Open'
                            opponentMenu.showOpponent()
                        elif zhuhaiButton.rect.collidepoint(event.pos):
                            self.zhuhaiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Zhuhai Championships'
                            opponentMenu.showOpponent()
                        elif sofiaButton.rect.collidepoint(event.pos):
                            self.sofiaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Sofia Open'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'October':
                        if beijingButton.rect.collidepoint(event.pos):
                            self.beijingCourt = pygame.image.load('C:/NEA Tennis Game/Courts/atpcupcourt.png')
                            player.currentTournament = 'China Open'
                            opponentMenu.showOpponent()
                        elif tokyoButton.rect.collidepoint(event.pos):
                            self.tokyoCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
                            player.currentTournament = 'Japan Open Tennis Championships'
                            opponentMenu.showOpponent()
                        elif shanghaiButton.rect.collidepoint(event.pos):
                            self.shanghaiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2.png')
                            player.currentTournament = 'Rolex Shanghai Masters'
                            opponentMenu.showOpponent()
                        elif moscowButton.rect.collidepoint(event.pos):
                            self.moscowCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'VTB Kremlin Cup'
                            opponentMenu.showOpponent()
                        elif antwerpButton.rect.collidepoint(event.pos):
                            self.antwerpCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'European Open'
                            opponentMenu.showOpponent()
                        elif stockholmButton.rect.collidepoint(event.pos):
                            self.stockholmCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'Stockholm Open'
                            opponentMenu.showOpponent()
                        elif viennaButton.rect.collidepoint(event.pos):
                            self.viennaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'Erste Bank Open'
                            opponentMenu.showOpponent()
                        elif antwerpButton.rect.collidepoint(event.pos):
                            self.antwerpCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'European Open'
                            opponentMenu.showOpponent()
                        elif baselButton.rect.collidepoint(event.pos):
                            self.baselCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
                            player.currentTournament = 'Swiss Indoors Basel'
                            opponentMenu.showOpponent()
                    elif player.currentMonth == 'November':
                        if parisButton.rect.collidepoint(event.pos):
                            self.parisCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'Rolex Paris Masters'
                            opponentMenu.showOpponent()
                        elif atpFinalsButton.rect.collidepoint(event.pos):
                            self.atpFinalsCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
                            player.currentTournament = 'ATP Finals'
                            opponentMenu.showOpponent()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()

            button('Back', 10,0,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')
                        
            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            pygame.display.update()
            window.setupTournamentMenu()
            window.clock.tick(window.FPS)
        
class OpponentMenu:
    def __init__(self):
        pass
    
    def showOpponent(self):
        print(player.currentTournament)
        if player.currentTournament == 'Australian Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        elif player.currentTournament == 'Roland Garros':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/claycourt1.png')
        elif player.currentTournament == 'Wimbledon':
            self.wimbledonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2.png')
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2.png')
        elif player.currentTournament == 'US Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        elif player.currentTournament == 'ATP Finals':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/atpfinalscourt.png')
        elif player.currentTournament == 'ATP Cup':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/atpcupcourt.png')
        elif player.currentTournament == 'Tokyo Olympic Games':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/tokyoolympicgamescourt.png')
        elif player.currentTournament == 'Davis Cup Finals':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/daviscupfinalscourt.png')
        elif player.currentTournament == 'BNP Paribas Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/indianwellscourt.png')
        elif player.currentTournament == 'Miami Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/miamicourt.png')
        elif player.currentTournament == 'Rolex Monte Carlo Masters':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/montecarlocourt.png')
        elif player.currentTournament == 'Madrid Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/madridcourt.png')
        elif player.currentTournament == 'Internazionali BNL d\'Italia':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/romecourt.png')
        elif player.currentTournament == 'Rogers Cup':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/rogerscupcourt.png')
        elif player.currentTournament == 'Western & Southern Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/cincinatticourt.png')
        elif player.currentTournament == 'Rolex Shanghai Masters':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Rolex Shanghai Masters':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Qatar ExxonMobil Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Adelaide International':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'ASB Classic':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Cordoba Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Tata Open Maharashtra':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Open Sud de France':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'AMRO World Tennis Tournament':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'New York Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Argentina Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Rio Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Open 13 Provence':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Delray Beach Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Dubai Tennis Championships':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Acapulco Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Santiago Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'US Men\'s Clay Court Champs':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Grand Prix Hassan II':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Barcelona Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Hungarian Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Munich Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Millennium Estoril Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Geneva Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Open Parc Rhone-Alpes Lyon':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'MercedesCup':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Libema Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Fever-Tree Championships':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Halle Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Mallorca Championships':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Nature Valley International':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Hamburg European Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Hall of Fame Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Nordea Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Abierto de Tenis Mifel':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Swiss Open Gstaad':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Croatia Open Umag':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Atlanta Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Genrali Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Citi Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Winston Salem Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'St. Petersburg Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Moselle Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Chengdu Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Zhuhai Championships':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Sofia Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'China Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Japan Open Tennis Championships':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'VTB Kremlin Cup':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'European Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Stockholm Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Erste Bank Open':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        elif player.currentTournament == 'Swiss Indoors Basel':
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        else:
            self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourtstatic.png')
        window = Window()
        window.setupOpponentMenu()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                        if player.currentTournament == '':
                            tournamentMenu.tournament()
                        else:
                            gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        playMatch.playMatchControls()

            button('Play!', 250,700,150,50, window.colors["green"], window.colors["lightGreen"], action='playMatch')
            button('My Player', 530,700,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Back', 830,700,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')
            button('Rankings', 0,50,150,50, window.colors["green"], window.colors["lightGreen"], action='rankings')
            button('Controls', 0,105,150,50, window.colors["yellow"], window.colors["lightYellow"], action='controls')
            button('Amateur', 0,250,150,50, window.colors["green"], window.colors["lightGreen"], action='amateur')
            button('Intermediate', 0,305,170,50, window.colors["green"], window.colors["lightGreen"], action='intermediate')
            button('Pro', 0,360,150,50, window.colors["green"], window.colors["lightGreen"], action='pro')
            if player.level >= 80:
                button('Master', 0,415,150,50, window.colors["green"], window.colors["lightGreen"], action='master')
            if player.level >= 100:
                button('Impossible', 0,470,150,50, window.colors["green"], window.colors["lightGreen"], action='impossible')
                    
                        
            pygame.display.update()
            window.setupOpponentMenu()
            window.clock.tick(window.FPS)

if player.difficulty == 'Amateur':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(20,40),random.randint(20,40),random.randint(40,50),random.randint(20,40),random.randint(20,40),100,100,0,0,60,180,'',0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0
                        ,0,0,0,'Right',False,[],'','',0,0,0)
elif player.difficulty == 'Intermediate':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(50,80),random.randint(50,80),random.randint(50,60),random.randint(50,80),random.randint(50,80),100,100,0,0,60,180,'',0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0
                        ,0,0,0,'Right',False,[],'','',0,0,0)
elif player.difficulty == 'Pro':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(75,95),random.randint(75,95),random.randint(60,70),random.randint(75,95),random.randint(75,95),100,100,0,0,60,180,'',0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0
                        ,0,0,0,'Right',False,[],'','',0,0,0)
elif player.difficulty == 'Master':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(90,100),random.randint(90,100),random.randint(60,70),random.randint(90,100),random.randint(90,100),100,100,0,0,60,180,'',0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0
                        ,0,0,0,'Right',False,[],'','',0,0,0)
elif player.difficulty == 'Impossible':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(100,150),random.randint(100,150),random.randint(65,75),random.randint(100,150),random.randint(100,150),100,100,0,0,60,180,'',0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'Round of 128',0
                        ,0,0,0,'Right',False,[],'','',0,0,0)

class LevelUpMenu:
    def __init__(self):
        pass
    
    def levelUp(self):
        window = Window()
        window.setupLevelUpMenu()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        opponentMenu.showOpponent()
                    if event.key == pygame.K_RETURN:
                        myPlayerMenu.myPlayer()

            button('OK', 250,700,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
                                            
            pygame.display.update()
            window.setupLevelUpMenu()
            window.clock.tick(window.FPS)


class MyPlayer:
    def __init__(self):
        pass

    def myPlayer(self):
        autoSaveCurrentTournament()
        try:
            autoLoad()
        except FileNotFoundError:
            pass
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        window = Window()
        window.setupMyPlayer()
        print(player.currentTournament)
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        plusButton1 = UpgradeButton(
            pos=(window.rect.w/8+340, window.rect.h/8+370),
            text="+",
            window=window,
            )
        plusButton2 = UpgradeButton(
            pos=(window.rect.w/8+340, window.rect.h/8+450),
            text="+",
            window=window,
            )
        plusButton3 = UpgradeButton(
            pos=(window.rect.w/8+590, window.rect.h/8+370),
            text="+",
            window=window,
            )
        plusButton4 = UpgradeButton(
            pos=(window.rect.w/8+590, window.rect.h/8+450),
            text="+",
            window=window,
            )

        gui.add(plusButton1,plusButton2,plusButton3,plusButton4)
        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if player.skillPoints >= 1:
                        if plusButton1.rect.collidepoint(event.pos) and player.power < 100:
                            player.power += 1
                            player.skillPoints -= 1
                        elif plusButton2.rect.collidepoint(event.pos) and player.accuracy < 100:
                            player.accuracy += 1
                            player.skillPoints -= 1
                        elif plusButton3.rect.collidepoint(event.pos) and player.speed < 100:
                            player.speed += 1
                            player.skillPoints -= 1
                        elif plusButton4.rect.collidepoint(event.pos) and player.fitness < 100:
                            player.fitness += 1
                            player.skillPoints -= 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        if player.currentTournament == '':
                            tournamentMenu.tournament()
                        else:
                            opponentMenu.showOpponent()

            button('Play', 250,700,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
            button('Right Handed', 350,400,200,50, window.colors["yellow"], window.colors["lightYellow"], action='leftHand')
            button('Left Handed', 350,400,200,50, window.colors["yellow"], window.colors["lightYellow"], action='rightHand')
            button('Shop', 0,100,150,50, window.colors["purple"], window.colors["lightPurple"], action='shop')
            button('Statistics', 0,155,150,50, window.colors["green"], window.colors["lightGreen"], action='statistics')
            button('Customize', 0,210,150,50, window.colors["green"], window.colors["lightGreen"], action='customize')
            button('Back', 820,700,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')
            button('New Game', 0,445,150,50, window.colors["green"], window.colors["lightGreen"], action='newGame')
            button('Save Game', 0,500,150,50, window.colors["green"], window.colors["lightGreen"], action='saveGame')
            button('Load Game', 0,555,150,50, window.colors["green"], window.colors["lightGreen"], action='loadGame')

            gui.update()
            gui.draw(window.gameDisplay)
            pygame.display.update()
            window.setupMyPlayer() #updates the text from setupMyPlayer method from the window class
            window.clock.tick(window.FPS)

class CustomizeMenu:
    def __init__(self):
        pass
    
    def customize(self):
        window = Window()
        window.setupCustomize()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myPlayerMenu.myPlayer()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        myPlayerMenu.myPlayer()

            button('Back', display_width/2-68,600,150,50, window.colors["yellow"], window.colors["lightYellow"], action='myPlayer')
                                            
            pygame.display.update()
            window.setupCustomize()
            window.clock.tick(window.FPS)


class Shop:
    def __init__(self):
        pass
               
    def shop(self):
        window = Window()
        window.setupShop()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        waterButton = SmallButton(
            pos=(window.rect.w/2 - 558, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        fruitShootButton = SmallButton(
            pos=(window.rect.w/2 - 450, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        coffeeButton = SmallButton(
            pos=(window.rect.w/2 - 275, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        orangeJuiceButton = SmallButton(
            pos=(window.rect.w/2 - 150, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        cokeButton = SmallButton(
            pos=(window.rect.w/2 + 35, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        dietCokeButton = SmallButton(
            pos=(window.rect.w/2 + 140, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        lucozadeButton = SmallButton(
            pos=(window.rect.w/2 + 280, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        monsterButton = SmallButton(
            pos=(window.rect.w/2 + 410, window.rect.h/2 - 175),
            text="Buy",
            window=window,
            )
        doubleDeckerButton = SmallButton(
            pos=(window.rect.w/2 - 560, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        fruitSaladButton = SmallButton(
            pos=(window.rect.w/2 - 370, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        skittlesButton = SmallButton(
            pos=(window.rect.w/2 - 220, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        proteinBarButton = SmallButton(
            pos=(window.rect.w/2 - 100, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        bananaButton = SmallButton(
            pos=(window.rect.w/2 + 60, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        orangeButton = SmallButton(
            pos=(window.rect.w/2 + 170, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        cheeseburgerButton = SmallButton(
            pos=(window.rect.w/2 + 280, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        doubleCheeseburgerButton = SmallButton(
            pos=(window.rect.w/2 + 440, window.rect.h/2 + 80),
            text="Buy",
            window=window,
            )
        goldenFruitSaladButton = SmallButton(
            pos=(window.rect.w/2 - 580, window.rect.h/2 + 370),
            text="Buy",
            window=window,
            )
        doubleBaconCheeseburgerButton = SmallButton(
            pos=(window.rect.w/2 - 410, window.rect.h/2 + 370),
            text="Buy",
            window=window,
            )

        if player.level < 2:
            gui.add(waterButton,fruitShootButton)
        if player.level >= 2:
            gui.add(waterButton,fruitShootButton,coffeeButton)
        if player.level >= 3:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton)
        if player.level >= 5:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton)
        if player.level >= 10:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton)
        if player.level >= 15:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton)
        if player.level >= 20:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton)
        if player.level >= 30:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton)
        if player.level >= 40:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton)
        if player.level >= 50:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton)
        if player.level >= 65:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton)
        if player.level >= 68:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton,orangeButton)
        if player.level >= 75:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton,orangeButton,cheeseburgerButton)
        if player.level >= 80:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton,orangeButton,cheeseburgerButton,doubleCheeseburgerButton)
        if player.level >= 90:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton,orangeButton,cheeseburgerButton,doubleCheeseburgerButton,goldenFruitSaladButton)
        if player.level >= 95:
            gui.add(waterButton,fruitShootButton,coffeeButton,orangeJuiceButton,cokeButton,dietCokeButton,lucozadeButton,monsterButton
                ,doubleDeckerButton,fruitSaladButton,skittlesButton,proteinBarButton,bananaButton,orangeButton,cheeseburgerButton,doubleCheeseburgerButton,goldenFruitSaladButton,doubleBaconCheeseburgerButton)
            

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if waterButton.rect.collidepoint(event.pos) and player.coins < 10 or fruitShootButton.rect.collidepoint(event.pos) and player.coins < 15 or coffeeButton.rect.collidepoint(event.pos) and player.coins < 13 or orangeJuiceButton.rect.collidepoint(event.pos) and player.coins < 9 or cokeButton.rect.collidepoint(event.pos) and player.coins < 20 or dietCokeButton.rect.collidepoint(event.pos) and player.coins < 8 or lucozadeButton.rect.collidepoint(event.pos) and player.coins < 25 or monsterButton.rect.collidepoint(event.pos) and player.coins < 17or doubleDeckerButton.rect.collidepoint(event.pos) and player.coins < 40 or fruitSaladButton.rect.collidepoint(event.pos) and player.coins < 30 or skittlesButton.rect.collidepoint(event.pos) and player.coins < 35 or proteinBarButton.rect.collidepoint(event.pos) and player.coins < 35 or bananaButton.rect.collidepoint(event.pos) and player.coins < 25 or orangeButton.rect.collidepoint(event.pos) and player.coins < 22 or cheeseburgerButton.rect.collidepoint(event.pos) and player.coins < 50 or doubleCheeseburgerButton.rect.collidepoint(event.pos) and player.coins < 62:
                        self.noCoinsText = window.smallFont.render(str("Not enough coins!"),True,window.colors["black"])
                        window.gameDisplay.blit(self.noCoinsText,(450,700))
                    elif player.coins >= 1:
                        if waterButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 5
                            player.coins = player.coins - 10
                        elif fruitShootButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 10
                            player.speed = player.speed + 0.5
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 15
                        if player.level >= 2 and coffeeButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 6
                            player.speed = player.speed + 1
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 13
                        if player.level >= 3 and orangeJuiceButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 6
                            player.coins = player.coins - 9
                        if player.level >= 5 and cokeButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 13
                            player.speed = player.speed + 0.5
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 20
                        if player.level >= 10 and dietCokeButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 5
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 8
                        if player.level >= 15 and lucozadeButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 15
                            player.speed = player.speed + 1
                            player.power = player.power + 1
                            player.coins = player.coins - 25
                        if player.level >= 20 and monsterButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 10
                            player.speed = player.speed + 1
                            player.coins = player.coins - 17
                        if player.level >= 30 and doubleDeckerButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 25
                            player.speed = player.speed + 0.5
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 40
                        if player.level >= 40 and fruitSaladButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 20
                            player.accuracy = player.accuracy + 1
                            player.coins = player.coins - 30
                        if player.level >= 50 and skittlesButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 22
                            player.speed = player.speed + 0.5
                            player.accuracy = player.accuracy - 1
                            player.coins = player.coins - 35
                        if player.level >= 60 and proteinBarButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 26
                            player.speed = player.speed + 1
                            player.coins = player.coins - 35
                        if player.level >= 65 and bananaButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 15
                            player.fitness = player.fitness + 1
                            player.coins = player.coins - 25
                        if player.level >= 68 and orangeButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 10
                            player.fitness = player.fitness + 1
                            player.coins = player.coins - 22
                        if player.level >= 75 and cheeseburgerButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 30
                            player.power = player.power + 1
                            player.fitness = player.fitness - 0.5
                            player.coins = player.coins - 50
                        if player.level >= 80 and doubleCheeseburgerButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 40
                            player.power = player.power + 1
                            player.speed = player.speed + 1
                            player.fitness = player.fitness - 1
                            player.coins = player.coins - 62
                        if player.level >= 90 and goldenFruitSaladButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 42
                            player.accuracy = player.accuracy + 1
                            player.power = player.power + 1
                            player.coins = player.coins - 68
                        if player.level >= 95 and doubleBaconCheeseburgerButton.rect.collidepoint(event.pos):
                            player.energy = player.energy + 45
                            player.power = player.power + 1
                            player.speed = player.speed + 1
                            player.fitness = player.fitness - 1
                            player.coins = player.coins - 75
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:
                        myPlayerMenu.myPlayer()

            button('Play', 250,800,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
            button('Training', 520,800,200,50, window.colors["blue"], window.colors["lightBlue"], action='training')
            button('Back', 830,800,200,50, window.colors["yellow"], window.colors["lightYellow"], action='myPlayer')

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            pygame.display.update()
            window.setupShop() #updates the text from setupMyPlayer method from the window class
            window.clock.tick(window.FPS)

        pygame.quit()
        quit()

class StatsMenu:
    def __init__(self):
        pass
    
    def stats(self):
        window = Window()
        window.setupStats()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myPlayerMenu.myPlayer()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        myPlayerMenu.myPlayer()

            button('Back', 10,10,150,50, window.colors["yellow"], window.colors["lightYellow"], action='myPlayer')
                                            
            pygame.display.update()
            window.setupStats()
            window.clock.tick(window.FPS)

class SaveGame:
    def __init__(self):
        pass
    
    def save(self):
        window = Window()
        window.setupSaveGame()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myPlayerMenu.myPlayer()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        myPlayerMenu.myPlayer()

            button('Save to slot 1', 100,100,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot1')
            button('Save to slot 2', 100,200,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot2')
            button('Save to slot 3', 100,300,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot3')
            button('Save to slot 4', 100,400,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot4')
            button('Save to slot 5', 100,500,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot5')
            button('Save to slot 6', 100,600,175,50, window.colors["green"], window.colors["lightGreen"], action='saveSlot6')
            button('x', 1000,110,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot1')
            button('x', 1000,210,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot2')
            button('x', 1000,310,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot3')
            button('x', 1000,410,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot4')
            button('x', 1000,510,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot5')
            button('x', 1000,610,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot6')
            button('x', 1000,710,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot7')
            button('x', 1000,810,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot8')
            button('Back', 10,10,150,50, window.colors["yellow"], window.colors["lightYellow"], action='myPlayer')
                                            
            pygame.display.update()
            window.setupSaveGame()
            window.clock.tick(window.FPS)

class LoadGame:
    def __init__(self):
        pass
    
    def load(self):
        window = Window()
        window.setupLoadGame()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myPlayerMenu.myPlayer()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        myPlayerMenu.myPlayer()

            button('Load Slot 1', 100,100,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot1')
            button('Load Slot 2', 100,200,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot2')
            button('Load Slot 3', 100,300,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot3')
            button('Load Slot 4', 100,400,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot4')
            button('Load Slot 5', 100,500,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot5')
            button('Load Slot 6', 100,600,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot6')
            button('Load Slot 7', 100,700,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot7')
            button('Load Slot 8', 100,800,175,50, window.colors["green"], window.colors["lightGreen"], action='loadSlot8')
            button('x', 1000,110,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot1')
            button('x', 1000,210,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot2')
            button('x', 1000,310,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot3')
            button('x', 1000,410,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot4')
            button('x', 1000,510,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot5')
            button('x', 1000,610,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot6')
            button('x', 1000,710,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot7')
            button('x', 1000,810,30,30, window.colors["green"], window.colors["lightRed"], action='deleteSlot8')
            button('Back', 10,10,150,50, window.colors["yellow"], window.colors["lightYellow"], action='myPlayer')
                                            
            pygame.display.update()
            window.setupLoadGame()
            window.clock.tick(window.FPS)

class Training:
    def __init__(self):
        pass
    def playTrainingMatch(self):
        self.trainingCourt = pygame.image.load('C:/NEA Tennis Game/Courts/qatarcourt.png')
        control = True
        while control: #   Events   #
                    
            player.playerControls()
            window.setupTrainingMatch()

            #   Player Boundaries   #
            player.playerBoundaries()
            
            #   Opponent Boundaries   #
            opponent.opponentBoundaries()
                
            #   Ball Boundaries   #
            ball.ballBoundaries()
            
            #   Opponent Movement  #
            opponent.opponentMovement()
            pygame.display.update()

            window.clock.tick(window.FPS)
            
            window.gameDisplay.blit(self.trainingCourt, (0,0))
        
    def wall(self):
        self.wallCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt2.png')
        control = True
        while control: #   Events   #
            player.playerControls()
            window.setupWall()

            player.playerBoundaries()
                
            ball.wallBoundaries() #no opponent needed.

            pygame.display.update()

            window.clock.tick(window.FPS)
            
            window.gameDisplay.blit(self.wallCourt, (0,0))
        
    def training(self):
        window = Window()
        window.setupTraining()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        trainingPlayButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 - 25),
            text="Play Match",
            window=window,
            )
        wallButton = Button(
            pos=(window.rect.w/4+200, window.rect.h/1.5 - 25),
            text="Wall",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/4+330, window.rect.h/1.5 - 25),
            text="My Player",
            window=window,
            )
        backButton = Button(
            pos=(window.rect.w/8+700, window.rect.h/1.5 - 25),
            text="Back",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(trainingPlayButton,wallButton,myPlayerButton,backButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        trainingMenu.playTrainingMatch()
                    if event.key == pygame.K_w:
                        trainingMenu.wall()

            button('Play Match', 290,600,150,50, window.colors["green"], window.colors["lightGreen"], action='playTrainingMatch')
            button('Wall', 465,600,150,50, window.colors["blue"], window.colors["lightBlue"], action='wall')
            button('My Player', 640,600,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Back', 815,600,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')

            pygame.display.update()
            window.clock.tick(window.FPS)

def autoSave():
    fileList = ['name.txt','ranking.txt','country.txt','power.txt','accuracy.txt','speed.txt','fitness.txt','consistency.txt','x.txt','y.txt','xchange.txt','ychange.txt','width.txt','height.txt','difficulty.txt','skillpoints.txt','coins.txt','energy.txt','level.txt','xp.txt','matchesplayed.txt','wins.txt','losses.txt',
                'matchwinloss%.txt','tournamentsplayed.txt','tournamentwins.txt','grandslamwins.txt','masters1000wins.txt','atp500wins.txt','currenttournament.txt','currenttournamentmatchwins.txt','currentround.txt','earnings.txt','pointsplayed.txt','pointswon.txt','pointslost.txt','pointswinloss%.txt','hand.txt','opponentsalreadyplayed.txt',
                'opponentname.txt','opponentcountry.txt','opponentranking.txt','opponentrankingpoints.txt','opponentpower.txt','opponentaccuracy.txt','opponentspeed.txt','opponentfitness.txt','opponentconsistency.txt','opponentx.txt','opponenty.txt','opponentxchange.txt','opponentychange.txt','opponentwidth.txt','opponentheight.txt','playerscore.txt','opponentscore.txt','playerpoints.txt','opponentpoints.txt','playergames.txt','opponentgames.txt','playersets.txt','opponentsets.txt','hits.txt','rallylength.txt','winners.txt','errors.txt','ballx.txt','bally.txt','ballxchange.txt','ballychange.txt','ballradius.txt','ballspeed.txt'
                ,'winfirstmatch.txt','winfirsttournament.txt','win100matches.txt','winfirstmasters1000.txt','winfirstgrandslam.txt','win20grandslams.txt','beatdjokovic.txt','beatfederer.txt','beatnadal.txt','worldnumber1.txt','maxupgrades.txt','completeallachievements.txt','currentMonthTournamentPlays.txt','currentMonthTournamentsAlreadyPlayed.txt','monthCount.txt','currentYear.txt']
    toWrite = [player.name,player.ranking,player.country,player.power,player.accuracy,player.speed,player.fitness,player.consistency,player.x,player.y,player.xChange,player.yChange,player.width,player.height,player.difficulty,player.skillPoints,player.coins,player.energy,player.level,player.xp,player.matchesPlayed,player.wins,player.losses,
                0,player.tournamentsPlayed,player.tournamentWins,player.grandSlamWins,player.masters1000Wins,player.atp500Wins,player.currentTournament,player.currentTournamentMatchWins,player.currentRound,player.earnings,player.pointsPlayed,player.pointsWon,player.pointsLost,0,player.hand,player.opponentsAlreadyPlayed,
                opponent.name,opponent.country,opponent.ranking,opponent.rankingPoints,opponent.power,opponent.accuracy,opponent.speed,opponent.fitness,opponent.consistency,opponent.x,opponent.y,opponent.xChange,opponent.yChange,opponent.width,opponent.height,scoring.playerScore,scoring.opponentScore,scoring.playerPoints,scoring.opponentPoints,scoring.playerGames,scoring.opponentGames,scoring.playerSets,scoring.opponentSets,scoring.hits,scoring.rallyLength,scoring.winners,scoring.errors,ball.ballX,ball.ballY,ball.ballXChange,ball.ballYChange,ball.ballRadius,ball.ballSpeed
                ,winFirstMatch.completed,winFirstTournament.completed,win100Matches.completed,winFirstMasters1000.completed,winFirstGrandSlam.completed,win20GrandSlams.completed,beatDjokovic.completed,beatFederer.completed,beatNadal.completed,worldNumber1.completed,maxUpgrades.completed,completeAllAchievements.completed,player.currentMonthTournamentPlays,player.currentMonthTournamentsAlreadyPlayed,player.monthCount,player.currentYear]
    window.saveSlot7 = True
    directory = 'saveslot7'
    i = 0
    j = 0
    while i < len(fileList):
        file = open('C:/NEA Tennis Game/Saves/saveslot7/'+fileList[i],'w')
        for element in str(toWrite[j]):
            file.write(element)
        i = i+1
        j = j+1

def autoSaveCurrentTournament():
    fileList = ['currenttournament.txt']
    toWrite = [player.currentTournament]
    window.saveSlot7 = True
    directory = 'saveslot7'
    i = 0
    j = 0
    while i < len(fileList):
        file = open('C:/NEA Tennis Game/Saves/saveslot7/'+fileList[i],'w')
        for element in str(toWrite[j]):
            file.write(element)
        i = i+1
        j = j+1

def autoLoad():
    fileList = ['name.txt','ranking.txt','country.txt','power.txt','accuracy.txt','speed.txt','fitness.txt','consistency.txt','x.txt','y.txt','xchange.txt','ychange.txt','width.txt','height.txt','difficulty.txt','skillpoints.txt','coins.txt','energy.txt','level.txt','xp.txt','matchesplayed.txt','wins.txt','losses.txt',
                'matchwinloss%.txt','tournamentsplayed.txt','tournamentwins.txt','grandslamwins.txt','masters1000wins.txt','atp500wins.txt','currenttournament.txt','currenttournamentmatchwins.txt','currentround.txt','earnings.txt','pointsplayed.txt','pointswon.txt','pointslost.txt','pointswinloss%.txt','hand.txt','opponentsalreadyplayed.txt',
                'opponentname.txt','opponentcountry.txt','opponentranking.txt','opponentrankingpoints.txt','opponentpower.txt','opponentaccuracy.txt','opponentspeed.txt','opponentfitness.txt','opponentconsistency.txt','opponentx.txt','opponenty.txt','opponentxchange.txt','opponentychange.txt','opponentwidth.txt','opponentheight.txt','playerscore.txt','opponentscore.txt','playerpoints.txt','opponentpoints.txt','playergames.txt','opponentgames.txt','playersets.txt','opponentsets.txt','hits.txt','rallylength.txt','winners.txt','errors.txt','ballx.txt','bally.txt','ballxchange.txt','ballychange.txt','ballradius.txt','ballspeed.txt'
                ,'winfirstmatch.txt','winfirsttournament.txt','win100matches.txt','winfirstmasters1000.txt','winfirstgrandslam.txt','win20grandslams.txt','beatdjokovic.txt','beatfederer.txt','beatnadal.txt','worldnumber1.txt','maxupgrades.txt','completeallachievements.txt','currentMonthTournamentPlays.txt','currentMonthTournamentsAlreadyPlayed.txt','monthCount.txt','currentYear.txt']
    toLoad = [player.name,player.ranking,player.country,player.power,player.accuracy,player.speed,player.fitness,player.consistency,player.x,player.y,player.xChange,player.yChange,player.width,player.height,player.difficulty,player.skillPoints,player.coins,player.energy,player.level,player.xp,player.matchesPlayed,player.wins,player.losses,
                0,player.tournamentsPlayed,player.tournamentWins,player.grandSlamWins,player.masters1000Wins,player.atp500Wins,player.currentTournament,player.currentTournamentMatchWins,player.currentRound,player.earnings,player.pointsPlayed,player.pointsWon,player.pointsLost,0,player.hand,player.opponentsAlreadyPlayed,
                opponent.name,opponent.country,opponent.ranking,opponent.rankingPoints,opponent.power,opponent.accuracy,opponent.speed,opponent.fitness,opponent.consistency,opponent.x,opponent.y,opponent.xChange,opponent.yChange,opponent.width,opponent.height,scoring.playerScore,scoring.opponentScore,scoring.playerPoints,scoring.opponentPoints,scoring.playerGames,scoring.opponentGames,scoring.playerSets,scoring.opponentSets,scoring.hits,scoring.rallyLength,scoring.winners,scoring.errors,ball.ballX,ball.ballY,ball.ballXChange,ball.ballYChange,ball.ballRadius,ball.ballSpeed
                ,winFirstMatch.completed,winFirstTournament.completed,win100Matches.completed,winFirstMasters1000.completed,winFirstGrandSlam.completed,win20GrandSlams.completed,beatDjokovic.completed,beatFederer.completed,beatNadal.completed,worldNumber1.completed,maxUpgrades.completed,completeAllAchievements.completed,player.currentMonthTournamentPlays,player.currentMonthTournamentsAlreadyPlayed,player.monthCount,player.currentYear]


    directory = 'saveslot7'
    i = 0
    j = 0
    contentsList = []
    while i < len(fileList):
        file = open('C:/NEA Tennis Game/Saves/saveslot7/'+fileList[i],'r')
        contents = file.read()
        contentsList.append(contents)
        i = i+1
    player.name = contentsList[0]
    player.ranking = contentsList[1]
    player.country = contentsList[2]
    player.power = int(contentsList[3])
    player.accuracy = int(contentsList[4])
    player.speed = float(contentsList[5])
    player.fitness = float(contentsList[6])
    player.consistency = int(contentsList[7])
    player.x = float(contentsList[8])
    player.y = float(contentsList[9])
    player.xChange = float(contentsList[10])
    player.yChange = float(contentsList[11])
    player.width = float(contentsList[12])
    player.height = float(contentsList[13])
    player.difficulty = contentsList[14]
    player.skillPoints = int(contentsList[15])
    player.coins = int(contentsList[16])
    player.energy = int(contentsList[17])
    player.level = int(contentsList[18])
    player.xp = int(contentsList[19])
    player.matchesPlayed = int(contentsList[20])
    player.wins = int(contentsList[21])
    player.losses = int(contentsList[22])
    blah = int(contentsList[23])
    player.tournamentsPlayed = int(contentsList[24])
    player.tournamentWins = int(contentsList[25])
    player.grandSlamWins = int(contentsList[26])
    player.masters1000Wins = int(contentsList[27])
    player.atp500Wins = int(contentsList[28])
    player.currentTournament = contentsList[29]
    player.currentTournamentMatchWins = int(contentsList[30])
    player.currentRound = contentsList[31]
    player.earnings = int(contentsList[32])
    player.pointsPlayed = int(contentsList[33])
    player.pointsWon = int(contentsList[34])
    player.pointsLost = int(contentsList[35])
    blah2 = int(contentsList[36])
    player.hand = contentsList[37]
    player.opponentsAlreadyPlayed = list(contentsList[38])
    opponent.name = contentsList[39]
    opponent.country = contentsList[40]
    opponent.ranking = contentsList[41]
    opponent.rankingPoints = int(contentsList[42])
    opponent.power = int(contentsList[43])
    opponent.accuracy = int(contentsList[44])
    opponent.speed = int(contentsList[45])
    opponent.fitness = int(contentsList[46])
    opponent.consistency = int(contentsList[47])
    opponent.x = float(contentsList[48])
    opponent.y = float(contentsList[49])
    opponent.xChange = float(contentsList[50])
    opponent.yChange = float(contentsList[51])
    opponent.width = float(contentsList[52])
    opponent.height = float(contentsList[53])
    scoring.playerScore = int(contentsList[54])
    scoring.opponentScore = int(contentsList[55])
    scoring.playerPoints = int(contentsList[56])
    scoring.opponentPoints = int(contentsList[57])
    scoring.playerGames = int(contentsList[58])
    scoring.opponentGames = int(contentsList[59])
    scoring.playerSets = int(contentsList[60])
    scoring.opponentSets = int(contentsList[61])
    scoring.hits = int(contentsList[62])
    scoring.rallyLength = int(contentsList[63])
    scoring.winners = int(contentsList[64])
    scoring.errors = int(contentsList[65])
    ball.ballX = int(contentsList[66])
    ball.ballY = int(contentsList[67])
    ball.ballXChange = int(contentsList[68])
    ball.ballYChange = int(contentsList[69])
    ball.ballRadius = int(contentsList[70])
    ball.ballSpeed = int(contentsList[71])
    player.monthCount = int(contentsList[84])
    player.currentMonthTournamentsAlreadyPlayed = list(contentsList[85])
    player.currentMonthTournamentPlays = int(contentsList[86])
    player.currentYear = int(contentsList[87])

    file.close()

def newGame():
    player.name = 'Sam Gibb'
    player.ranking = 13
    player.country = 'United Kingdom'
    player.power = 30
    player.accuracy = 30
    player.speed = 60
    player.fitness = 30
    player.consistency = 30
    player.x = (display_width * 0.45)
    player.y = (display_height * 0.8)
    player.difficulty = 'Amateur'
    player.skillPoints = 0
    player.coins = 100
    player.energy = 100
    player.level = 1
    player.xp = 0
    player.matchesPlayed = 0
    player.wins = 0
    player.losses = 0
    blah = 0
    player.tournamentsPlayed = 0
    player.tournamentWins = 0
    player.grandSlamWins = 0
    player.masters1000Wins = 0
    player.atp500Wins = 0
    player.currentTournament = ''
    player.currentTournamentMatchWins = 0
    player.currentRound = 'Round of 128'
    player.earnings = 0
    player.pointsPlayed = 0
    player.pointsWon = 0
    player.pointsLost = 0
    blah2 = 0
    player.hand = 'Right'
    player.opponentsAlreadyPlayed = []
    opponent.name = random.choice(opponentNames)
    opponent.country = 'Serbia'
    opponent.ranking = 1
    opponent.rankingPoints = 1000
    if player.difficulty == 'Amateur':
        opponent.power = random.randint(20,40)
        opponent.accuracy = random.randint(20,40)
        opponent.speed = random.randint(40,50)
        opponent.fitness = random.randint(20,40)
        opponent.consistency = random.randint(20,40)
    elif player.difficulty == 'Intermediate':
        opponent.power = random.randint(50,80)
        opponent.accuracy = random.randint(50,80)
        opponent.speed = random.randint(50,60)
        opponent.fitness = random.randint(50,80)
        opponent.consistency = random.randint(50,80)
    elif player.difficulty == 'Pro':
        opponent.power = random.randint(75,95)
        opponent.accuracy = random.randint(75,95)
        opponent.speed = random.randint(60,70)
        opponent.fitness = random.randint(75,95)
        opponent.consistency = random.randint(75,95)
    elif player.difficulty == 'Master':
        opponent.power = random.randint(90,100)
        opponent.accuracy = random.randint(90,100)
        opponent.speed = random.randint(60,70)
        opponent.fitness = random.randint(90,100)
        opponent.consistency = random.randint(90,100)
    elif player.difficulty == 'Impossible':
        opponent.power = random.randint(100,150)
        opponent.accuracy = random.randint(100,150)
        opponent.speed = random.randint(65,75)
        opponent.fitness = random.randint(100,150)
        opponent.consistency = random.randint(100,150)
    

    opponent.x = 100
    opponent.y = 100
    opponent.xChange = 0
    opponent.yChange = 0
    scoring.playerScore = 0
    scoring.opponentScore = 0
    scoring.playerPoints = 0
    scoring.opponentPoints = 0
    scoring.playerGames = 0
    scoring.opponentGames = 0
    scoring.playerSets = 0
    scoring.opponentSets = 0
    scoring.hits = 0
    scoring.rallyLength = 0
    scoring.winners = 0
    scoring.errors = 0
    ball.ballX = 600
    ball.ballY = 600
    ball.ballXChange = 0
    ball.ballYChange = 0
    winFirstMatch.completed = False
    winFirstTournament.completed = False
    win100Matches.completed = False
    winFirstMasters1000.completed = False
    winFirstGrandSlam.completed = False
    win20GrandSlams.completed = False
    beatDjokovic.completed = False
    beatFederer.completed = False
    beatNadal.completed = False
    worldNumber1.completed = False
    maxUpgrades.completed = False
    completeAllAchievements.completed = False
    player.currentMonthTournamentPlays = 0
    player.currentMonthTournamentsAlreadyPlayed = []
    player.monthCount = 1
    player.currentYear = 2020
    fileList = ['name.txt','ranking.txt','country.txt','power.txt','accuracy.txt','speed.txt','fitness.txt','consistency.txt','x.txt','y.txt','xchange.txt','ychange.txt','width.txt','height.txt','difficulty.txt','skillpoints.txt','coins.txt','energy.txt','level.txt','xp.txt','matchesplayed.txt','wins.txt','losses.txt',
                'matchwinloss%.txt','tournamentsplayed.txt','tournamentwins.txt','grandslamwins.txt','masters1000wins.txt','atp500wins.txt','currenttournament.txt','currenttournamentmatchwins.txt','currentround.txt','earnings.txt','pointsplayed.txt','pointswon.txt','pointslost.txt','pointswinloss%.txt','hand.txt','opponentsalreadyplayed.txt',
                'opponentname.txt','opponentcountry.txt','opponentranking.txt','opponentrankingpoints.txt','opponentpower.txt','opponentaccuracy.txt','opponentspeed.txt','opponentfitness.txt','opponentconsistency.txt','opponentx.txt','opponenty.txt','opponentxchange.txt','opponentychange.txt','opponentwidth.txt','opponentheight.txt','playerscore.txt','opponentscore.txt','playerpoints.txt','opponentpoints.txt','playergames.txt','opponentgames.txt','playersets.txt','opponentsets.txt','hits.txt','rallylength.txt','winners.txt','errors.txt','ballx.txt','bally.txt','ballxchange.txt','ballychange.txt','ballradius.txt','ballspeed.txt'
                ,'winfirstmatch.txt','winfirsttournament.txt','win100matches.txt','winfirstmasters1000.txt','winfirstgrandslam.txt','win20grandslams.txt','beatdjokovic.txt','beatfederer.txt','beatnadal.txt','worldnumber1.txt','maxupgrades.txt','completeallachievements.txt','currentMonthTournamentPlays.txt','currentMonthTournamentsAlreadyPlayed.txt','monthCount.txt','currentYear.txt']
    toWrite = [player.name,player.ranking,player.country,player.power,player.accuracy,player.speed,player.fitness,player.consistency,player.x,player.y,player.xChange,player.yChange,player.width,player.height,player.difficulty,player.skillPoints,player.coins,player.energy,player.level,player.xp,player.matchesPlayed,player.wins,player.losses,
                0,player.tournamentsPlayed,player.tournamentWins,player.grandSlamWins,player.masters1000Wins,player.atp500Wins,player.currentTournament,player.currentTournamentMatchWins,player.currentRound,player.earnings,player.pointsPlayed,player.pointsWon,player.pointsLost,0,player.hand,player.opponentsAlreadyPlayed,
                opponent.name,opponent.country,opponent.ranking,opponent.rankingPoints,opponent.power,opponent.accuracy,opponent.speed,opponent.fitness,opponent.consistency,opponent.x,opponent.y,opponent.xChange,opponent.yChange,opponent.width,opponent.height,scoring.playerScore,scoring.opponentScore,scoring.playerPoints,scoring.opponentPoints,scoring.playerGames,scoring.opponentGames,scoring.playerSets,scoring.opponentSets,scoring.hits,scoring.rallyLength,scoring.winners,scoring.errors,ball.ballX,ball.ballY,ball.ballXChange,ball.ballYChange,ball.ballRadius,ball.ballSpeed
                ,winFirstMatch.completed,winFirstTournament.completed,win100Matches.completed,winFirstMasters1000.completed,winFirstGrandSlam.completed,win20GrandSlams.completed,beatDjokovic.completed,beatFederer.completed,beatNadal.completed,worldNumber1.completed,maxUpgrades.completed,completeAllAchievements.completed,player.currentMonthTournamentPlays,player.currentMonthTournamentsAlreadyPlayed,player.monthCount,player.currentYear]
    window.saveSlot8 = True
    directory = 'saveslot8'
    i = 0
    j = 0
    while i < len(fileList):
        file = open('C:/NEA Tennis Game/Saves/saveslot8/'+fileList[i],'w')
        for element in str(toWrite[j]):
            file.write(element)
        i = i+1
        j = j+1
        
    folder = 'C:/NEA Tennis Game/Saves/saveslot7/'
    for root, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(root, file))

            
class GameIntro:
    def __init__(self):
        pass
               
    def gameIntro(self):
        try:
            autoLoad()
        except FileNotFoundError:
            print('You have no saves lol')
        self.achievementsButton = pygame.image.load('C:/NEA Tennis Game/Icons/achievementsbutton.png')
        window = Window()
        trainingMenu = Training()
        window.setupGameIntro()
        if window.newNewGame == True:
            newGame()
            window.newNewGame = False
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        achievementsButton = AchievementsButton(
            pos=(window.rect.w/2-589, window.rect.h/2-448),
            text="",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(achievementsButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if achievementsButton.rect.collidepoint(event.pos):
                        achievementsMenu.achievementsMenu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        autoSave()
                        window.quit()
                    if event.key == pygame.K_t:
                        trainingMenu.training()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        if player.currentTournament == '':
                            tournamentMenu.tournament()
                        else:
                            opponentMenu.showOpponent()

            button('Play', 290,600,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
            button('Training', 465,600,150,50, window.colors["blue"], window.colors["lightBlue"], action='training')
            button('My Player', 640,600,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Quit', 815,600,150,50, window.colors["red"], window.colors["lightRed"], action='quit')


            ball.ballBoundaries()
            window.gameDisplay.blit(self.achievementsButton,[0,0])
            pygame.display.update()
            window.clock.tick(window.FPS)

        pygame.quit()
        quit()

class AchievementsMenu:
    def __init__(self):
        pass
    
    def achievementsMenu(self):
        window = Window()
        window.setupAchievements()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        gameIntroMenu.gameIntro()

            button('Back', 10,10,150,50, window.colors["green"], window.colors["lightGreen"], action='mainMenu')
                                        
            pygame.display.update()
            window.setupAchievements()
            window.clock.tick(window.FPS)

    def achievementConditions(self):
        if player.wins >= 1: #achievement conditions
            winFirstMatch.completed = True
        if player.tournamentWins >= 1:
            winFirstTournament.completed = True
        if winFirstMatch.completed == True and winFirstTournament.completed == True and win100Matches.completed == True and winFirstMasters1000.completed == True and winFirstGrandSlam.completed == True and win20GrandSlams.completed == True and beatDjokovic.completed == True and beatFederer.completed == True and beatNadal.completed == True and worldNumber1.completed == True and maxUpgrades.completed == True:
            completeAllAchievements.completed = True #complete all achievements
        if player.wins >= 100:
            win100Matches.completed = True
        if player.masters1000Wins >= 1:
            winFirstMasters1000.completed = True
        if player.grandSlamWins >= 1:
            winFirstGrandSlam.completed = True
        if player.grandSlamWins >= 20:
            win20GrandSlams.completed = True
        if player.wins >= 1 and opponent.name == 'Novak Djokovic':
            beatDjokovic.completed = True
        if player.wins >= 1 and opponent.name == 'Roger Federer':
            beatFederer.completed = True
        if player.wins >= 1 and opponent.name == 'Rafael Nadal':
            beatNadal.completed = True
        if player.ranking == 1:
            worldNumber1.completed = True
        if player.power == 100 and player.accuracy == 100 and player.speed == 100 and player.fitness == 100 and player.level == 100:
            maxUpgrades.completed = True
            
class Achievements:
    
    def __init__(self,title,name,completed,image):
        self.title = title
        self.name = name
        self.completed = completed
        self.image = image

winFirstMatch = Achievements ('Getting Started','Win your first match',False,'')
winFirstTournament = Achievements ('Win Tournament','Win your first tournament',False,'')
win100Matches = Achievements ('Pro','Win 100 matches',False,'')
winFirstMasters1000 = Achievements ('Masters 1000','Win your first masters 1000 title',False,'')
winFirstGrandSlam = Achievements ('Grand Slam','Win your first grand slam',False,'')
win20GrandSlams = Achievements ('20 Slams','Win 20 grand slams',False,'')
beatDjokovic = Achievements ('Beat Djokovic','Beat Novak Djokovic in a match',False,'')
beatFederer = Achievements ('Beat Federer','Beat Roger Federer in a match',False,'')
beatNadal = Achievements ('Beat Nadal','Beat Rafael Nadal in a match',False,'')
worldNumber1 = Achievements ('World Number One','Become world number one',False,'')
maxUpgrades = Achievements ('Max Upgrades','Fully upgrade your player',False,'')
completeAllAchievements = Achievements ('Legend','Complete all achievements',False,'')

class PauseMenu:
    def __init__(self):
        pass

    def pause(self):
        self.pauseCourt = pygame.image.load('C:/NEA Tennis Game/Courts/trainingcourt.png')
        window = Window()
        window.setupPause()
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        resumeButton = Button(
            pos=(window.rect.w/4+10
                 , window.rect.h/1.5-15),
            text="Resume",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(resumeButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if resumeButton.rect.collidepoint(event.pos):
                        window.gameExit = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        window.gameExit = False
                    if event.key == pygame.K_RETURN or event.key == pygame.K_p:
                        window.gameExit = False
                        
            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            #button('Resume', 290,600,150,50, window.colors["green"], window.colors["lightGreen"], action='resume')
            button('My Player', 455,600,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Main Menu', 620,600,150,50, window.colors["green"], window.colors["lightGreen"], action='mainMenu')
            button('Quit Tournament', 785,600,210,50, window.colors["red"], window.colors["lightRed"], action='quitTournament')
                        
            pygame.display.update()
            window.clock.tick(window.FPS)

class RankingsMenu:
    def __init__(self):
        pass

    def orderRankings(self):
        self.rankings.sort()

    def rankings(self):
        window = Window()
        window.setupRankings()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()

            button('Main Menu', 5,0,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')
            button('Back', 175,0,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
                    
            pygame.display.update()
            window.clock.tick(window.FPS)

class ControlsMenu:
    def __init__(self):
        pass

    def controls(self):
        window = Window()
        window.setupControls()

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    autoSave()
                    window.quit()

            button('Main Menu', 300,600,150,50, window.colors["yellow"], window.colors["lightYellow"], action='mainMenu')
            button('Training', 465,600,150,50, window.colors["blue"], window.colors["lightBlue"], action='training')
            button('My Player', 630,600,150,50, window.colors["purple"], window.colors["lightPurple"], action='myPlayer')
            button('Back', 795,600,150,50, window.colors["green"], window.colors["lightGreen"], action='opponentMenu')
            
            pygame.display.update()
            window.clock.tick(window.FPS)

class PlayMatch(Opponent):
    def __init__(self):
        pass
    
    def playMatchControls(self):
        self.australianOpenCourt = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.frenchOpenCourt = pygame.image.load('C:/NEA Tennis Game/Courts/claycourt1.png')
        self.wimbledonCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt2.png')
        self.usOpenCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png')
        self.indianWellsCourt = pygame.image.load('C:/NEA Tennis Game/Courts/indianwellscourt.png')
        self.miamiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/miamicourt.png')
        self.monteCarloCourt = pygame.image.load('C:/NEA Tennis Game/Courts/montecarlocourt.png')
        self.madridCourt = pygame.image.load('C:/NEA Tennis Game/Courts/madridcourt.png')
        self.romeCourt = pygame.image.load('C:/NEA Tennis Game/Courts/romecourt.png')
        self.rogersCupCourt = pygame.image.load('C:/NEA Tennis Game/Courts/rogerscupcourt.png')
        self.cincinattiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/cincinatticourt.png')
        self.shanghaiCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        self.atpCupCourt = pygame.image.load('C:/NEA Tennis Game/Courts/atpcupcourt.png')
        self.dohaCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        self.adelaideCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        self.aucklandCourt = pygame.image.load('C:/NEA Tennis Game/Courts/shanghaicourt.png')
        control = True
        while control: #   Events   #
            window.text()
            window.draw()
                    
            player.playerControls()
            window.setupPlayMatch()

            player.playerBoundaries()
            
            opponent.opponentBoundaries()
                
            ball.ballBoundaries()

            opponent.opponentMovement()
            pygame.display.update()

            if player.currentTournament == 'Australian Open':
                window.gameDisplay.blit(self.australianOpenCourt, (0,0))
            elif player.currentTournament == 'Roland Garros':
                window.gameDisplay.blit(self.frenchOpenCourt, (0,0))
            elif player.currentTournament == 'Wimbledon':
                window.gameDisplay.blit(self.wimbledonCourt, (0,0))
            elif player.currentTournament == 'US Open':
                window.gameDisplay.blit(self.usOpenCourt, (0,0))
            elif player.currentTournament == 'ATP Finals':
                window.gameDisplay.blit(self.atpFinalsCourt, (0,0))
            elif player.currentTournament == 'ATP Cup':
                window.gameDisplay.blit(self.atpCupCourt, (0,0))
            elif player.currentTournament == 'Laver Cup':
                window.gameDisplay.blit(self.laverCupCourt, (0,0))
            elif player.currentTournament == 'Davis Cup Finals':
                window.gameDisplay.blit(self.davisCupFinalsCourt, (0,0))
            elif player.currentTournament == 'Tokyo Olympics':
                window.gameDisplay.blit(self.olympicsCourt, (0,0))
            elif player.currentTournament == 'BNP Paribas Open':
                window.gameDisplay.blit(self.indianWellsCourt, (0,0))
            elif player.currentTournament == 'Miami Open':
                window.gameDisplay.blit(self.miamiCourt, (0,0))
            elif player.currentTournament == 'Rolex Monte Carlo Masters':
                window.gameDisplay.blit(self.monteCarloCourt, (0,0))
            elif player.currentTournament == 'Madrid Open':
                window.gameDisplay.blit(self.madridCourt, (0,0))
            elif player.currentTournament == 'Internazionali BNL d\'Italia':
                window.gameDisplay.blit(self.romeCourt, (0,0))
            elif player.currentTournament == 'Rogers Cup':
                window.gameDisplay.blit(self.rogersCupCourt, (0,0))
            elif player.currentTournament == 'Western & Southern Open':
                window.gameDisplay.blit(self.cincinattiCourt, (0,0))
            elif player.currentTournament == 'Rolex Shanghai Masters':
                window.gameDisplay.blit(self.shanghaiCourt, (0,0))
            elif player.currentTournament == 'Qatar ExxonMobil Open':
                window.gameDisplay.blit(self.dohaCourt, (0,0))
            elif player.currentTournament == 'Adelaide International':
                window.gameDisplay.blit(self.adelaideCourt, (0,0))
            elif player.currentTournament == 'ASB Classic':
                window.gameDisplay.blit(self.aucklandCourt, (0,0))
            elif player.currentTournament == 'Cordoba Open':
                window.gameDisplay.blit(self.cordobaCourt, (0,0))
            elif player.currentTournament == 'Tata Open Maharashtra':
                window.gameDisplay.blit(self.puneCourt, (0,0))
            elif player.currentTournament == 'Open Sud de France':
                window.gameDisplay.blit(self.montpellierCourt, (0,0))
            elif player.currentTournament == 'AMRO World Tennis Tournament':
                window.gameDisplay.blit(self.rotterdamCourt, (0,0))
            elif player.currentTournament == 'New York Open':
                window.gameDisplay.blit(self.newYorkCourt, (0,0))
            elif player.currentTournament == 'Argentina Open':
                window.gameDisplay.blit(self.buenosAiresCourt, (0,0))
            elif player.currentTournament == 'Rio Open':
                window.gameDisplay.blit(self.rioCourt, (0,0))
            elif player.currentTournament == 'Open 13 Provence':
                window.gameDisplay.blit(self.marseilleCourt, (0,0))
            elif player.currentTournament == 'Delray Beach Open':
                window.gameDisplay.blit(self.delrayBeachCourt, (0,0))
            elif player.currentTournament == 'Dubai Tennis Championships':
                window.gameDisplay.blit(self.dubaiCourt, (0,0))
            elif player.currentTournament == 'Acapulco Open':
                window.gameDisplay.blit(self.aacpulcoCourt, (0,0))
            elif player.currentTournament == 'Santiago Open':
                window.gameDisplay.blit(self.santiagoCourt, (0,0))
            elif player.currentTournament == 'US Men\'s Clay Court Champs':
                window.gameDisplay.blit(self.houstonCourt, (0,0))
            elif player.currentTournament == 'Grand Prix Hassan II':
                window.gameDisplay.blit(self.marrakechCourt, (0,0))
            elif player.currentTournament == 'Barcelona Open':
                window.gameDisplay.blit(self.barcelonaCourt, (0,0))
            elif player.currentTournament == 'Hungarian Open':
                window.gameDisplay.blit(self.budapestCourt, (0,0))
            elif player.currentTournament == 'Munich Open':
                window.gameDisplay.blit(self.munichCourt, (0,0))
            elif player.currentTournament == 'Millennium Estoril Open':
                window.gameDisplay.blit(self.estorilCourt, (0,0))
            elif player.currentTournament == 'Geneva Open':
                window.gameDisplay.blit(self.genevaCourt, (0,0))
            elif player.currentTournament == 'Open Parc Rhone-Alpes Lyon':
                window.gameDisplay.blit(self.lyonCourt, (0,0))
            elif player.currentTournament == 'MercedesCup':
                window.gameDisplay.blit(self.stuttgartCourt, (0,0))
            elif player.currentTournament == 'Libema Open':
                window.gameDisplay.blit(self.sHertogenboschCourt, (0,0))
            elif player.currentTournament == 'Fever-Tree Championships':
                window.gameDisplay.blit(self.londonCourt, (0,0))
            elif player.currentTournament == 'Halle Open':
                window.gameDisplay.blit(self.halleCourt, (0,0))
            elif player.currentTournament == 'Mallorca Championships':
                window.gameDisplay.blit(self.mallorcaCourt, (0,0))
            elif player.currentTournament == 'Nature Valley International':
                window.gameDisplay.blit(self.eastbourneCourt, (0,0))
            elif player.currentTournament == 'Hamburg European Open':
                window.gameDisplay.blit(self.hamburgCourt, (0,0))
            elif player.currentTournament == 'Hall of Fame Open':
                window.gameDisplay.blit(self.newportCourt, (0,0))
            elif player.currentTournament == 'Nordea Open':
                window.gameDisplay.blit(self.bastadCourt, (0,0))
            elif player.currentTournament == 'Abierto de Tenis Mifel':
                window.gameDisplay.blit(self.losCabosCourt, (0,0))
            elif player.currentTournament == 'Sarasin Swiss Open Gstaad':
                window.gameDisplay.blit(self.gstaadCourt, (0,0))
            elif player.currentTournament == 'Croatia Open Umag':
                window.gameDisplay.blit(self.umagCourt, (0,0))
            elif player.currentTournament == 'Atlanta Open':
                window.gameDisplay.blit(self.atlantaCourt, (0,0))
            elif player.currentTournament == 'Genrali Open':
                window.gameDisplay.blit(self.kitzbuhelCourt, (0,0))
            elif player.currentTournament == 'Citi Open':
                window.gameDisplay.blit(self.washingtonCourt, (0,0))
            elif player.currentTournament == 'Winston Salem Open':
                window.gameDisplay.blit(self.winstonSalemCourt, (0,0))
            elif player.currentTournament == 'St. Petersburg Open':
                window.gameDisplay.blit(self.stPetersburgCourt, (0,0))
            elif player.currentTournament == 'Moselle Open':
                window.gameDisplay.blit(self.metzCourt, (0,0))
            elif player.currentTournament == 'Chengdu Open':
                window.gameDisplay.blit(self.chengduCourt, (0,0))
            elif player.currentTournament == 'Zhuhai Championships':
                window.gameDisplay.blit(self.zhuhaiCourt, (0,0))
            elif player.currentTournament == 'Sofia Open':
                window.gameDisplay.blit(self.sofiaCourt, (0,0))
            elif player.currentTournament == 'China Open':
                window.gameDisplay.blit(self.beijingCourt, (0,0))
            elif player.currentTournament == 'Japan Open Tennis Championships':
                window.gameDisplay.blit(self.tokyoCourt, (0,0))
            elif player.currentTournament == 'VTB Kremlin Cup':
                window.gameDisplay.blit(self.moscowCourt, (0,0))
            elif player.currentTournament == 'European Open':
                window.gameDisplay.blit(self.antwerpCourt, (0,0))
            elif player.currentTournament == 'Stockholm Open':
                window.gameDisplay.blit(self.stockholmCourt, (0,0))
            elif player.currentTournament == 'Erste Bank Open':
                window.gameDisplay.blit(self.viennaCourt, (0,0))
            elif player.currentTournament == 'Swiss Indoors Basel':
                window.gameDisplay.blit(self.baselCourt, (0,0))
            else:
                window.gameDisplay.blit(tournamentMenu.australianOpenStaticCourt, (0,0))

            window.clock.tick(window.FPS)

window = Window()
scoring = Scoring()
gameIntroMenu = GameIntro()
achievementsMenu = AchievementsMenu()
trainingMenu = Training()
myPlayerMenu = MyPlayer()
customizeMenu = CustomizeMenu()
shopMenu = Shop()
statsMenu = StatsMenu()
saveGame = SaveGame()
loadGame = LoadGame()
tournamentMenu = TournamentMenu()
opponentMenu = OpponentMenu()
levelUpMenu = LevelUpMenu()
playMatch = PlayMatch()
rankingsMenu = RankingsMenu()
controlsMenu = ControlsMenu()
pauseMenu = PauseMenu()
gameIntroMenu.gameIntro()
