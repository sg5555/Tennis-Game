class GameIntro:
    def __init__(self):
        pass
               
    def gameIntro(self):
        window = Window()
        trainingMenu = Training()
        window.setupGameIntro()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        playButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 - 25),
            text="Play",
            window=window,
            )
        trainingButton = Button(
            pos=(window.rect.w/4+140, window.rect.h/1.5 - 25),
            text="Training",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/4+330, window.rect.h/1.5 - 25),
            text="My Player",
            window=window,
            )
        quitButton = Button(
            pos=(window.rect.w/8+700, window.rect.h/1.5 - 25),
            text="Quit",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(playButton,trainingButton,myPlayerButton,quitButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if playButton.rect.collidepoint(event.pos):
                        opponentMenu.showOpponent()
                    elif trainingButton.rect.collidepoint(event.pos):
                        trainingMenu.training()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif quitButton.rect.collidepoint(event.pos):
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_t:
                        trainingMenu.training()
                    if event.key == pygame.K_RETURN:
                        opponentMenu.showOpponent()

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            ball.ballBoundaries()
            pygame.display.update()
            window.clock.tick(window.FPS)

        pygame.quit()
        quit()
        
gameIntroMenu = GameIntro()
