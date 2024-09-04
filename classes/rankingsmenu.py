class RankingsMenu:
    def __init__(self):
        pass

    def orderRankings(self):
        self.rankings.sort()

    def rankings(self):
        window = Window()
        window.setupRankings()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        backButton = Button(
            pos=(window.rect.w/2-590
                 , window.rect.h/1.5 - 610),
            text="Back",
            window=window,
            )
        mainMenuButton = Button(
            pos=(window.rect.w/2-400, window.rect.h/1.5 - 610),
            text="Main menu",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(backButton,mainMenuButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if backButton.rect.collidepoint(event.pos):
                        opponentMenu.showOpponent()
                    elif mainMenuButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                        
            gui.update()  #Update buttons.
            gui.draw(window.gameDisplay)  # Draw buttons.
            pygame.display.update()
            window.clock.tick(window.FPS)

rankingsMenu = RankingsMenu()
