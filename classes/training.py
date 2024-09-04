class Training:
    def __init__(self):
        pass
    def playTrainingMatch(self):
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
            
            window.gameDisplay.blit(window.trainingCourt, (0,0))
        
    def wall(self):
        control = True
        while control: #   Events   #
            player.playerControls()
            window.setupWall()

            player.playerBoundaries()
                
            ball.wallBoundaries() #no opponent needed.

            pygame.display.update()

            window.clock.tick(window.FPS)
            
            window.gameDisplay.blit(window.wallCourt, (0,0))
        
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
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if trainingPlayButton.rect.collidepoint(event.pos):
                        trainingMenu.playTrainingMatch()
                    elif wallButton.rect.collidepoint(event.pos):
                        trainingMenu.wall()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif backButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        trainingMenu.playTrainingMatch()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_w:
                        trainingMenu.wall()

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            pygame.display.update()
            window.clock.tick(window.FPS)

trainingMenu = Training()
