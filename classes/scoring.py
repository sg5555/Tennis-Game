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

    def playerWinPoint(self):
        self.playerScore = self.playerScore + 1
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
        if self.playerSets == 2 and self.opponentSets < 2:
            scoring.playerWin()
            player.rankingPoints = player.rankingPoints + 100
            player.skilPoints = player.skillPoints + 2

    def playerWin(self):
        window = Window()
        window.setupPlayerWin()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        playButton = Button(
            pos=(window.rect.w/4-20
                 , window.rect.h/1.5 + 100),
            text="Play again",
            window=window,
            )
        trainingButton = Button(
            pos=(window.rect.w/4+160, window.rect.h/1.5 + 100),
            text="Training",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/4+320, window.rect.h/1.5 + 100),
            text="My Player",
            window=window,
            )
        mainMenuButton = Button(
            pos=(window.rect.w/4+500, window.rect.h/1.5 + 100),
            text="Main menu",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(playButton,trainingButton,myPlayerButton,mainMenuButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if playButton.rect.collidepoint(event.pos):
                        playMatch.playMatchControls
                    elif trainingButton.rect.collidepoint(event.pos):
                        trainingMenu.training()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif mainMenuButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        playMatch.playMatchControls

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            ball.ballBoundaries()
            pygame.display.update()
            window.clock.tick(window.FPS)

    def opponentWinPoint(self):
        self.opponentScore = self.opponentScore + 1
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
        if self.opponentSets == 2 and self.playerSets < 2:
            scoring.opponentWin()
            opponent.rankingPoints = opponent.rankingPoints + 100

    def opponentWin(self):
        window = Window()
        window.setupOpponentWin()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        playButton = Button(
            pos=(window.rect.w/4-20
                 , window.rect.h/1.5 + 100),
            text="Play again",
            window=window,
            )
        trainingButton = Button(
            pos=(window.rect.w/4+160, window.rect.h/1.5 + 100),
            text="Training",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/4+320, window.rect.h/1.5 + 100),
            text="My Player",
            window=window,
            )
        mainMenuButton = Button(
            pos=(window.rect.w/4+500, window.rect.h/1.5 + 100),
            text="Main menu",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(playButton,trainingButton,myPlayerButton,mainMenuButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if playButton.rect.collidepoint(event.pos):
                        playMatch.playMatchControls
                    elif trainingButton.rect.collidepoint(event.pos):
                        trainingMenu.training()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif mainMenuButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        playMatch.playMatchControls

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            ball.ballBoundaries()
            pygame.display.update()
            window.clock.tick(window.FPS)
scoring = Scoring()
