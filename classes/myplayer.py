class MyPlayer:
    def __init__(self):
        pass

    def hand(self):
        pass

    def difficulty(self):
        pass

    def myPlayer(self):
        window = Window()
        window.setupMyPlayer()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        playButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 + 100),
            text="Play",
            window=window,
            )
        handButton = Button(
            pos=(window.rect.w/4+50, window.rect.h/1.5 - 225),
            text="Right Handed",
            window=window,
            )
        plusButton1 = Button(
            pos=(window.rect.w/8+340, window.rect.h/8+370),
            text="+",
            window=window,
            )
        plusButton2 = Button(
            pos=(window.rect.w/8+340, window.rect.h/8+450),
            text="+",
            window=window,
            )
        plusButton3 = Button(
            pos=(window.rect.w/8+550, window.rect.h/8+370),
            text="+",
            window=window,
            )
        plusButton4 = Button(
            pos=(window.rect.w/8+550, window.rect.h/8+450),
            text="+",
            window=window,
            )
        backButton = Button(
            pos=(window.rect.w/8+700, window.rect.h/1.5 + 100),
            text="Back",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(playButton,backButton,handButton,plusButton1,plusButton2,plusButton3,plusButton4)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if playButton.rect.collidepoint(event.pos):
                        opponentMenu.showOpponent()
                    elif backButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                    elif handButton.rect.collidepoint(event.pos):
                        myPlayerMenu.hand()
                    if plusButton1.rect.collidepoint(event.pos) and player.skillPoints == 0 or plusButton2.rect.collidepoint(event.pos) and player.skillPoints == 0 or plusButton3.rect.collidepoint(event.pos) and player.skillPoints == 0 or plusButton4.rect.collidepoint(event.pos) and player.skillPoints == 0:
                        self.noSkillPointsText = window.smallFont.render(str("Not enough skill points!"),True,window.colors["black"])
                        window.gameDisplay.blit(self.noSkillPointsText,(450,700))
                    elif player.skillPoints >= 1:
                        if plusButton1.rect.collidepoint(event.pos):
                            player.power += 1
                            player.skillPoints -= 1
                        elif plusButton2.rect.collidepoint(event.pos):
                            player.accuracy += 1
                            player.skillPoints -= 1
                        elif plusButton3.rect.collidepoint(event.pos):
                            player.speed += 1
                            player.skillPoints -= 1
                        elif plusButton4.rect.collidepoint(event.pos):
                            player.fitness += 1
                            player.skillPoints -= 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        opponentMenu.showOpponent()
                        

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            pygame.display.update()
            window.setupMyPlayer() #updates the text from setupMyPlayer method from the window class
            window.clock.tick(window.FPS)

myPlayerMenu = MyPlayer()
