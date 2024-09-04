class OpponentMenu:
    def __init__(self):
        pass
    
    def showOpponent(self):
        window = Window()
        window.setupOpponentMenu()
        # gui is a sprite group which will contain the button sprites.
        gui = pygame.sprite.Group()
        # Instantiate some buttons.
        rankingsButton = Button(
            pos=(window.rect.w/4 - 305, window.rect.h/4 - 180),
            text="Rankings",
            window=window,
            )
        controlsButton = Button(
            pos=(window.rect.w/4 - 305, window.rect.h/4 - 120),
            text="Controls",
            window=window,
            )
        difficulty1Button = Button(
            pos=(window.rect.w/8-150, window.rect.h/8+140),
            text="Amateur",
            window=window,
            )
        difficulty2Button = Button(
            pos=(window.rect.w/8-150, window.rect.h/8+200),
            text="Intermediate",
            window=window,
            )
        difficulty3Button = Button(
            pos=(window.rect.w/8-150, window.rect.h/8+260),
            text="Pro",
            window=window,
            )
        difficulty4Button = Button(
            pos=(window.rect.w/8-150, window.rect.h/8+320),
            text="Master",
            window=window,
            )
        difficulty5Button = Button(
            pos=(window.rect.w/8-150, window.rect.h/8+380),
            text="Impossible",
            window=window,
            )
        playButton = Button(
            pos=(window.rect.w/4
                 , window.rect.h/1.5 - 25),
            text="Play!",
            window=window,
            )
        myPlayerButton = Button(
            pos=(window.rect.w/8+380, window.rect.h/1.5 - 25),
            text="My Player",
            window=window,
            )
        backButton = Button(
            pos=(window.rect.w/8+700, window.rect.h/1.5 - 25),
            text="Back",
            window=window,
            )
        # Add the buttons to the gui group.
        gui.add(rankingsButton,controlsButton,difficulty1Button,difficulty2Button,difficulty3Button,difficulty4Button,difficulty5Button,playButton,myPlayerButton,backButton)

        while window.gameExit == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    window.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Handle button events.
                    if rankingsButton.rect.collidepoint(event.pos):
                        rankingsMenu.rankings()
#rankingsMenu.rankings([opponent.rankingPoints],[opponent2.rankingPoints],[opponent3.rankingPoints],[opponent4.rankingPoints],[opponent5.rankingPoints],[opponent6.rankingPoints],
                                  #[opponent7.rankingPoints],[opponent8.rankingPoints],[opponent9.rankingPoints][opponent10.rankingPoints],[opponent11.rankingPoints],[opponent12.rankingPoints])
                    elif controlsButton.rect.collidepoint(event.pos):
                        controlsMenu.controls()
                    elif playButton.rect.collidepoint(event.pos):
                        playMatch.playMatchControls()
                    elif myPlayerButton.rect.collidepoint(event.pos):
                        myPlayerMenu.myPlayer()
                    elif backButton.rect.collidepoint(event.pos):
                        gameIntroMenu.gameIntro()
                    elif difficulty1Button.rect.collidepoint(event.pos): #opponent
                        player.difficulty = 'Amateur'
                        opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(20,40),random.randint(20,40),random.randint(40,50),random.randint(20,40),100,100,0,0,60,180,'',0)
                    elif difficulty2Button.rect.collidepoint(event.pos):
                        player.difficulty = 'Intermediate'
                        opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(50,80),random.randint(50,80),random.randint(50,80),random.randint(50,80),100,100,0,0,60,180,'',0)
                    elif difficulty3Button.rect.collidepoint(event.pos):
                        player.difficulty = 'Pro'
                        opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(75,95),random.randint(75,95),random.randint(70,80),random.randint(75,95),100,100,0,0,60,180,'',0)
                    elif difficulty4Button.rect.collidepoint(event.pos):
                        player.difficulty = 'Master'
                        opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(90,100),random.randint(90,100),random.randint(70,80),random.randint(90,100),100,100,0,0,60,180,'',0)
                    elif difficulty5Button.rect.collidepoint(event.pos):
                        player.difficulty = 'Impossible'
                        opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(100,150),random.randint(100,150),random.randint(70,80),random.randint(100,150),100,100,0,0,60,180,'',0)
                        opponent.accuracy = random.randint(100,120)
                        print(opponent.accuracy)
                        window.setupOpponentMenu()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                        gameIntroMenu.gameIntro()
                    if event.key == pygame.K_RETURN:
                        playMatch.playMatchControls()
                        

            gui.update()  # Call update methods of contained sprites.
            gui.draw(window.gameDisplay)  # Draw all sprites.
            pygame.display.update()
            window.setupOpponentMenu()
            window.clock.tick(window.FPS)

if player.difficulty == 'Amateur':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(20,40),random.randint(20,40),random.randint(40,50),random.randint(20,40),100,100,0,0,60,180,'',0)
elif player.difficulty == 'Intermediate':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(50,80),random.randint(50,80),random.randint(50,80),random.randint(50,80),100,100,0,0,60,180,'',0)
elif player.difficulty == 'Pro':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(75,95),random.randint(75,95),random.randint(70,80),random.randint(75,95),100,100,0,0,60,180,'',0)
elif player.difficulty == 'Master':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(90,100),random.randint(90,100),random.randint(70,80),random.randint(90,100),100,100,0,0,60,180,'',0)
elif player.difficulty == 'Impossible':        
    opponent = Opponent(random.choice(opponentNames),'Serbia',1,10200,random.randint(100,150),random.randint(100,150),random.randint(70,80),random.randint(100,150),100,100,0,0,60,180,'',0)

opponentMenu = OpponentMenu()    
