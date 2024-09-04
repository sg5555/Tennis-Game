class Ball:
    def __init__(self,ballX,ballY,ballXChange,ballYChange,ballRadius,ballSpeed):
        self.ballX = ballX
        self.ballY = ballY
        self.ballXChange = ballXChange
        self.ballYChange = ballYChange
        self.ballRadius = ballRadius
        self.ballSpeed = ballSpeed
        
    def ballBoundaries(self):
        if ball.ballX <= 0:
            ball.ballXChange += ball.ballSpeed
        if ball.ballX > display_width:
            ball.ballXChange -= ball.ballSpeed
        if ball.ballY > display_height:
            ball.ballXChange = 0
            ball.ballYChange = 0
            scoring.opponentWinPoint()
        if ball.ballY <= -1:
            ball.ballXChange = 0
            ball.ballYChange = 0
            scoring.playerWinPoint()

    def wallBoundaries(self): #makes the ball bounce off the wall.
        if ball.ballX <= 0:
            ball.ballX = int(600)
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
        if ball.ballX > display_width:
            ball.ballX = int(600)
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
        if ball.ballY < display_height / 3:
            ball.ballYChange += ball.ballSpeed
        if ball.ballY > display_height:
            ball.ballX = int(600) #if the ball goes below the screen, it is returned to the player to hit at the wall.
            ball.ballY = int(600)
            ball.ballXChange = 0
            ball.ballYChange = 0
            
            
    def ballBounce(self):
        pass

    def playerBallIn(self):
        pass

    def playerBallOut(self):
        pass
    
ball = Ball(int(600),int(600),0,0,10,20)
