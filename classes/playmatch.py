class PlayMatch(Opponent):
    def __init__(self):
        pass
    
    def playMatchControls(self):
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

            window.clock.tick(window.FPS)
            
            window.gameDisplay.blit(window.bgIntro, (0,0))

playMatch = PlayMatch()
