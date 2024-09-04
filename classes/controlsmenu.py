class ControlsMenu:
    def __init__(self):
        pass

    def controls(self):
        window = Window()
        window.setupControls()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        mainMenuButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 - 25),
            text="Main Menu",
            window=window,
            )
        trainingButton = Button(
            pos=(window.rect.w/8+320, window.rect.h/1.5 - 25),
            text="Training",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/8+480, window.rect.h/1.5 - 25),
            text="My Player",
            window=window,
            )
        backButton = Button(
            pos=(window.rect.w/8+700, window.rect.h/1.5 - 25),
            text="Back",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(mainMenuButton,trainingButton,myPlayerButton,backButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if mainMenuButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                    elif trainingButton.rect.collidepoint(event.pos):
                        trainingMenu.training()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif backButton.rect.collidepoint(event.pos):
                        opponentMenu.showOpponent()
                        
            gui.update()  #Update buttons.
            gui.draw(window.gameDisplay)  # Draw buttons.
            pygame.display.update()
            window.clock.tick(window.FPS)

controlsMenu = ControlsMenu()
