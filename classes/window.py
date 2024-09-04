import pygame, random

from scoring import Scoring

pygame.mixer.pre_init(44100,16,2,4096) #music
pygame.init()
display_width = 1200
display_height = 920
opponentNames = ["Novak Djokovic","Roger Federer","Rafael Nadal","Daniil Medvedev","Alexander Zverev","Light Togami","Alex de Minaur","Nick Kyrgios","Stefanos Tsitsipas", "Ivo Karlovic","Bernard Tomic",
                 "Krittin Koaykul","Artem Bahmet","Jimmy Connors","John Mcenroe"]
opponentCountries = ["Serbia","Switzerland","Spain","Russia","Germany","Japan","Australia","Australia","Greece","Croatia","Australia","Thialand","Ukraine","USA","USA"]
opponentImageChance = random.randint(1,100)
#pygame.mixer.music.load('[AMIGA MUSIC] Super Tennis Champs - Title Screen.mp3')
#pygame.mixer.music.set_volume(1)
#pygame.mixer.music.play(-1)

class Window:

    def __init__(self): #holds all of the constants
        self.bgIntro = pygame.image.load('C:/NEA Tennis Game/Courts/australianopencourt.png')
        self.wallCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt2.png')
        self.trainingCourt = pygame.image.load('C:/NEA Tennis Game/Courts/qatarcourt.png')
        self.myPlayerCourt = pygame.image.load('C:/NEA Tennis Game/Courts/hardcourt1.png') 
        self.opponentMenuCourt = pygame.image.load('C:/NEA Tennis Game/Courts/grasscourt1.png')
        self.pauseCourt = pygame.image.load('C:/NEA Tennis Game/Courts/trainingcourt.png')
        self.playerImage = pygame.image.load('C:/NEA Tennis Game/Player/player1up1.png')
        self.playerImageFront = pygame.image.load('C:/NEA Tennis Game/Player/player1front.png')
        self.playerImageRight = pygame.image.load('C:/NEA Tennis Game/Player/player1right.png')
        self.playerImageLeft = pygame.image.load('C:/NEA Tennis Game/Player/player1left.png')
        if opponent.name == 'Novak Djokovic':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/djokovic.png.ink')
        elif opponent.name == 'Roger Federer':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/federer.png')
        elif opponent.name == 'Rafael Nadal':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/nadal.png')
        elif opponent.name == 'Daniil Medvedev':
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/medvedev.png')
        elif opponentImageChance > 90:
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1ultimate.png')
        else:
            self.opponentImage = pygame.image.load('C:/NEA Tennis Game/Player/opponent1.png')
        self.introIcon = pygame.image.load('C:/NEA Tennis Game/Icons/Apple.png')
        self.playMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/powerbaseliner.png')
        self.trainingMatchIcon = pygame.image.load('C:/NEA Tennis Game/Icons/volleyer.png')
        self.trainingIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allcourtattacker.png')
        self.wallIcon = pygame.image.load('C:/NEA Tennis Game/Icons/puncher.png')
        self.myPlayerIcon = pygame.image.load('C:/NEA Tennis Game/Icons/allrounder.png')
        self.gameDisplay = pygame.display.set_mode((display_width,display_height))
        self.rect = self.gameDisplay.get_rect()
        self.time = pygame.time.get_ticks()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.tinyFont = pygame.font.SysFont('comicsansms', 16)
        self.smallFont = pygame.font.SysFont('comicsansms', 25)
        self.medFont = pygame.font.SysFont('comicsansms', 40)
        self.largeFont = pygame.font.SysFont('comicsansms', 80)
        self.gameExit = True
        self.colors = {"red": (255,0,0),
                       "green": (0,150,0),
                       "blue": (48,138,255),
                       "white": (255,255,255),
                       "black": (0,0,0),
                       "grey": (80,80,80),
                       "lightRed": (255,0,0),
                       "yellow": (230,218,0),
                       "lightYellow": (200,200,0),
                       "lightGreen": (0,200,0),
                       "lightBlue": (26,156,255)}

    def setupPlayMatch(self):
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
        window.gameDisplay.blit(window.opponentImage, [opponent.x,opponent.y])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        energyBar0 = pygame.draw.rect(window.gameDisplay,(self.colors["green"]),(display_width-46,display_height-150,40,120))
        #energyBar1 = pygame.draw.rect(window.gameDisplay,(self.colors["green"]),(display_width-50,display_height-150,50-(5*(10-player.fitness)),120))
        pygame.display.set_caption("Play Match")
        pygame.display.set_icon(self.playerImageRight)

    def setupPlayerWin(self):
        self.winText = self.medFont.render(str("You won against:"+" "+str(opponent.name+"!")),True,self.colors["black"])
        self.youGotText = self.medFont.render(str("You got 2 skill points!"),True,self.colors["black"])
        self.youGotText2 = self.medFont.render(str("You have gained 100 ranking points."),True,self.colors["black"])
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
        window.gameDisplay.blit(self.youGotText,[330,480]),window.gameDisplay.blit(self.youGotText2,[330,550])
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
        pygame.display.set_icon(self.playerImageRight)

    def setupRankings(self):
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
        self.gameDisplay.blit(self.myPlayerCourt,[0,0])
        self.controlsText = self.largeFont.render(str("Controls"),True,self.colors["black"])
        self.controlsText2 = self.medFont.render(str("Use the arrow keys to move your player."),True,self.colors["black"])
        self.controlsText3 = self.medFont.render(str("Press space to serve."),True,self.colors["black"])
        self.controlsText4 = self.medFont.render(str("Press left CTRL to hit the ball to the left,"),True,self.colors["black"])
        self.controlsText5 = self.medFont.render(str("and left ALT to hit it to the right."),True,self.colors["black"])
        window.gameDisplay.blit(self.controlsText,(465,0)),window.gameDisplay.blit(self.controlsText2,(220,130)),window.gameDisplay.blit(self.controlsText3,(220,235))
        window.gameDisplay.blit(self.controlsText4,(220,360)),window.gameDisplay.blit(self.controlsText5,(220,500))
        pygame.display.set_caption("Controls")
        pygame.display.set_icon(self.wallCourt)

    def setupPause(self):
        self.gameDisplay.blit(self.bgIntro,[0,0])
        self.pausedText = self.largeFont.render(str("Paused"),True,self.colors["black"])
        window.gameDisplay.blit(self.pausedText,(490,0))
        pygame.display.set_caption("Paused")
        pygame.display.set_icon(self.playMatchIcon)

    def setupTrainingMatch(self):
        player.x += player.xChange
        player.y += player.yChange
        opponent.x += opponent.xChange
        opponent.y += opponent.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        window.gameDisplay.blit(window.playerImage, [player.x,player.y])
        window.gameDisplay.blit(window.opponentImage, [opponent.x,opponent.y])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        pygame.display.set_caption("Training Match")
        pygame.display.set_icon(self.playerImageRight)

    def setupGameIntro(self):
        self.gameDisplay.blit(self.bgIntro,[0,0])
        self.titleText = self.largeFont.render(str("Tennis Game"),True,self.colors["black"])
        self.versionText = self.smallFont.render(str("Version 1.6"),True,self.colors["black"])
        window.gameDisplay.blit(self.titleText,(375,0)),window.gameDisplay.blit(self.versionText,(10,880))
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        pygame.display.set_caption("Tennis Game Intro")
        pygame.display.set_icon(self.introIcon)
        
    def setupTraining(self):
        self.gameDisplay.blit(self.trainingCourt,[0,0])
        self.trainingText = self.largeFont.render(str("Training"),True,self.colors["black"])
        window.gameDisplay.blit(self.trainingText,(450,0))
        pygame.display.set_caption("Training")
        pygame.display.set_icon(self.trainingIcon)

    def setupWall(self):
        player.x += player.xChange
        player.y += player.yChange
        ball.ballX += ball.ballXChange
        ball.ballY += ball.ballYChange
        self.wallHitsText = self.smallFont.render(str("Wall Hits:"+" "+str(player.ranking)),True,self.colors["black"])
        window.gameDisplay.blit(window.playerImage, [player.x,player.y])
        window.gameDisplay.blit(window.wallHitsText, [1010,5])
        tennisBall = pygame.draw.circle(window.gameDisplay,window.colors["lightGreen"],[ball.ballX,ball.ballY],ball.ballRadius)
        pygame.display.set_caption("The Wall")
        pygame.display.set_icon(self.playerImageRight)

    def setupMyPlayer(self):
        self.largePlayerName = self.medFont.render(str(player.name),True,self.colors["black"])
        self.rankingText = self.smallFont.render(str("Ranking:"+" "+str(player.ranking)),True,self.colors["black"])
        self.countryText = self.smallFont.render(str("Country:"+" "+str(player.country)),True,self.colors["black"])
        self.powerText = self.smallFont.render(str("Power:"+" "+str(player.power))+str("%"),True,self.colors["black"])
        self.accuracyText = self.smallFont.render(str("Accuracy:"+" "+str(player.accuracy))+str("%"),True,self.colors["black"])
        self.speedText = self.smallFont.render(str("Speed:"+" "+str(player.speed))+str("%"),True,self.colors["black"])
        self.fitnessText = self.smallFont.render(str("Fitness:"+" "+str(player.fitness))+str("%"),True,self.colors["black"])
        self.difficultyText = self.smallFont.render(str("Difficulty:"+ " "+str(player.difficulty)),True,self.colors["black"])
        self.skillPointsText = self.smallFont.render(str("Skill Points:"+" "+str(player.skillPoints)),True,self.colors["black"])
        self.gameDisplay.blit(self.myPlayerCourt,[0,0]),window.gameDisplay.blit(window.playerImageFront, [555,125])
        window.gameDisplay.blit(self.largePlayerName,(440,40)),window.gameDisplay.blit(self.rankingText,(5,0)),window.gameDisplay.blit(self.countryText,(880,0)),
        window.gameDisplay.blit(self.powerText,(300,480)),window.gameDisplay.blit(self.accuracyText,(300,570)),window.gameDisplay.blit(self.speedText,(800,480))
        window.gameDisplay.blit(self.fitnessText,(800,570)),window.gameDisplay.blit(self.difficultyText,(5,50)),window.gameDisplay.blit(self.skillPointsText,(330,220))
        pygame.display.set_caption("My Player")
        pygame.display.set_icon(self.myPlayerIcon)

    def setupOpponentMenu(self):
        self.youArePlayingText = self.smallFont.render(str("You are playing:"+""),True,self.colors["black"])
        self.largeOpponentName = self.medFont.render(str(opponent.name),True,self.colors["black"])
        self.opponentRankingText = self.smallFont.render(str("Ranking:"+" "+str(opponent.ranking)),True,self.colors["black"])
        self.opponentCountryText = self.smallFont.render(str("Country:"+" "+str(opponent.country)),True,self.colors["black"])
        self.opponentPowerText = self.smallFont.render(str("Power:"+" "+str(opponent.power))+str("%"),True,self.colors["black"])
        self.opponentAccuracyText = self.smallFont.render(str("Accuracy:"+" "+str(opponent.accuracy))+str("%"),True,self.colors["black"])
        self.opponentSpeedText = self.smallFont.render(str("Speed:"+" "+str(opponent.speed))+str("%"),True,self.colors["black"])
        self.opponentFitnessText = self.smallFont.render(str("Fitness:"+" "+str(opponent.fitness))+str("%"),True,self.colors["black"])
        self.difficultyText = self.smallFont.render(str("Difficulty:"+" "+str(player.difficulty)),True,self.colors["black"])
        self.gameDisplay.blit(self.opponentMenuCourt,[0,0]),window.gameDisplay.blit(self.youArePlayingText,(500,0))
        window.gameDisplay.blit(window.opponentImage, [555,125])
        window.gameDisplay.blit(self.largeOpponentName,(440,40)),window.gameDisplay.blit(self.opponentRankingText,(5,0)),window.gameDisplay.blit(self.opponentCountryText,(880,0)),
        window.gameDisplay.blit(self.opponentPowerText,(300,480)),window.gameDisplay.blit(self.opponentAccuracyText,(300,520)),
        window.gameDisplay.blit(self.opponentSpeedText,(800,480)),window.gameDisplay.blit(self.opponentFitnessText,(800,520)),window.gameDisplay.blit(self.difficultyText,(5,200))
        pygame.display.set_caption("Opponent")
        pygame.display.set_icon(self.myPlayerIcon)

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

window = Window()
