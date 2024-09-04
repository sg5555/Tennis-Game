class PauseMenu:
    def __init__(self):
        pass

    def pause(self):
        window = Window()
        window.setupPause()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        resumeButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 - 25),
            text="Resume",
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
        mainMenuButton = Button(
            pos=(window.rect.w/8+650, window.rect.h/1.5 - 25),
            text="Main Menu",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(resumeButton,trainingButton,myPlayerButton,mainMenuButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if resumeButton.rect.collidepoint(event.pos):
                        window.gameExit = False
                    elif trainingButton.rect.collidepoint(event.pos):
                        trainingMenu.training()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif mainMenuButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                        
            gui.update()  #Update buttons.
            gui.draw(window.gameDisplay)  # Draw buttons.
            pygame.display.update()
            window.clock.tick(window.FPS)

pauseMenu = PauseMenu()
