# It's christmas time but you wont be celebrating anything tonight as you need to defend your home from
# Santa's murderous army! They've found out where you have been hiding all these years and have planned meticously 
# to bring you down. However you have your own contingency plan as well, fire. It has been the oldest and most reliable
# tool to fighting back the armies of the festive holiday. Pinned down with no options left you are ready to defend 
# yourself. But watch out! Innocent carolers have gathered to watch the spectacle unfold and you dont want to waste
# time trying to burn them! You've got more pressing matters at hand obvously! Can you survive the endless waves 
# of Santa's army or will you fold to their immeasurable numbers?

# Particle values
INITIAL_SIZE = 16
SQR_SIZE = 12
SMALLER = .04

# Enemy hp
enemyHP = 100

startPos = None
particles = []
r = 0

#time variables
time = 100
startTime = millis()
booler = False
counter = 0
waiting = False

# Booleans
drawn = False
alive = True

# Enemy coordinates
midTL = PVector(270, 190)
midBR = PVector(370, 290)
rightTL = PVector(460, 190)
rightBR = PVector(560, 290)
leftTL = PVector(70, 190)
leftBR = PVector(180, 290)

# Enemy Spawner values
chosen = False
choose = 0
e1 = 1
e2 = 2
e3 = 3

# Spawn coordinates and values
spotMid = PVector(320,240)
spotLeft = PVector(130,240)
spotRight = PVector(510,240)
posRandom = 0

# Score values
score = 0

# NPC values
neutralOne = 0
neutralTwo = 0

def setup():
    global img1, img2, img3, img4, img5, img6, back
    size(640,480)
    #background(255)
    rectMode(CENTER)
    imageMode(CENTER)
    img1 = loadImage("boy.png")
    img2 = loadImage("girl.png")
    img3 = loadImage("dog.png")
    img4 = loadImage("Elve.png")
    img5 = loadImage("snowman.png")
    img6 = loadImage("gingy.png")
    back = loadImage("bakground.png")
    textMode(CENTER)
    
def draw():
    global enemyHP, booler, startTime, time, waiting, drawn, chosen, choose, posRandom, imgList, neutralOne, neutralTwo, score, alive
    #background(255)
    image(back, spotMid.x, spotMid.y)
    startTime = 0
    alive = False
    
    # Logic
    if drawn == True:
        if chosen == False:
            choose = floor(random(e1, 4))
            posRandom = floor(random(e1, 4))
            neutralOne = floor(random(0, 3))
            neutralTwo = floor(random(0, 3))            
            
        # Enemy variant 1
        if choose == e1:
            if(posRandom == 3):
                image(img4, spotRight.x, spotRight.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotMid.x, spotMid.y, neutralTwo)
            elif(posRandom == 2):
                image(img4, spotMid.x, spotMid.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            else:
                image(img4, spotLeft.x, spotLeft.y)
                drawNPC(spotMid.x, spotMid.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            chosen = True
            
        # Enemy variant 2
        elif choose == e2:
            if(posRandom == 3):
                image(img5, spotRight.x, spotRight.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotMid.x, spotMid.y, neutralTwo)
            elif(posRandom == 2):
                image(img5, spotMid.x, spotMid.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            else:
                image(img5, spotLeft.x, spotLeft.y)
                drawNPC(spotMid.x, spotMid.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            chosen = True
            
        # Enemy variant 3
        elif choose == e3:
            if(posRandom == 3):
                image(img6, spotRight.x, spotRight.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotMid.x, spotMid.y, neutralTwo)
            elif(posRandom == 2):
                image(img6, spotMid.x, spotMid.y)
                drawNPC(spotLeft.x, spotLeft.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            else:
                image(img6, spotLeft.x, spotLeft.y)
                drawNPC(spotMid.x, spotMid.y, neutralOne)
                drawNPC(spotRight.x, spotRight.y, neutralTwo)
            chosen = True
            
    # Draw an enemy at 3 sec
    if frameCount % 180 == 0:
        drawn = True
        alive = True
        
    # Remove enemy after 3 sec
    if frameCount % 360 == 0:
        drawn = False
        chosen = False
        alive = False
        if enemyHP > 0:
            alive = True
        if alive == True:
            score -= 1
            alive = False
            fail()
        enemyHP = 100
    drawParticles()
    removeParticles()
    pushStyle()
    fill(255)
    #text("Enemy Health:"+ str(enemyHP), 10, 60)
    text("Score:" + str(score), 10, 80)
    popStyle()
    
# Will draw the NPCs in the remaining two boxes where the enemy is not
def drawNPC(posX, posY, condition):
    if condition == 0:
        image(img1, posX, posY)
    elif condition == 1:
        image(img2, posX, posY)
    elif condition == 2:
        image(img3, posX, posY)
    if condition == 0:
        image(img1, posX, posY)
    elif condition == 1:
        image(img2, posX, posY)
    elif condition == 2:
        image(img3, posX, posY)
    
# Calls the Particle class and populates it with values, checks to see if the mouse is in the correct box and burns the enemy if it is, and will add 1 to the score if it kills the enemy
def drawParticles():
    global enemyHP, startTime, drawn, score
    if mousePressed:
        startPos = PVector(mouseX,mouseY)
        vel = PVector(random(-1,1),random(-5,-1))
        sqrVel = PVector(random(-3,3),random(-9,-1))
        alfa = 255
        randColor = color(255,random(0,255),0)
        if(startPos.x > midTL.x and startPos.y > midTL.y and startPos.x < midBR.x and startPos.y < midBR.y and posRandom == e2):
            burnEnemy()
        elif(startPos.x > leftTL.x and startPos.y > leftTL.y and startPos.x < leftBR.x and startPos.y < leftBR.y and posRandom == e1):
            burnEnemy()
        elif(startPos.x > rightTL.x and startPos.y > rightTL.y and startPos.x < rightBR.x and startPos.y < rightBR.y and posRandom == e3):
            burnEnemy()
        if enemyHP == 0 and drawn == True:
            image(back, spotMid.x, spotMid.y)
            drawn = False
            score += 1

        if(floor(random(2))) == 0:
            particles.append(Particle(startPos, vel, alfa, randColor))  
        else:
            particles.append(SqrParticle(startPos, sqrVel, alfa, randColor))  
            
# Delete the particles from existance
def removeParticles():
    bin = []
    for prt in particles:
        prt.update()
        prt.render()  
        if prt.alf <= 0:
            particles.remove(prt)
            
# Damages the enemy
def burnEnemy():
    global enemyHP, booler, startTime
    if enemyHP > 0 and drawn == True:
        enemyHP = enemyHP - 1

# Checks to see if the player has lost
def fail():
    if score < 0:
        pushStyle()
        fill(255, 0, 0)
        textAlign(CENTER)
        textSize(50)
        text("YOU LOSE", width/2, height/2)
        noLoop()
        popStyle()

# Particle Class
class Particle:
    def __init__(self, tempPos, tempVel, tempAlpha, tempColor):
        self.pos = tempPos
        self.vel = tempVel
        self.alf = tempAlpha
        self.clr = tempColor
        
    # updates the position of the particle
    def update(self):
        self.pos += self.vel
        self.alf -= 5
        
    # draws the particle
    def render(self):
        noStroke()
        fill(self.clr, self.alf)
        circle(self.pos.x, self.pos.y, INITIAL_SIZE)
        
# Inherited Particle Class
class SqrParticle(Particle):
    
    # updates the position of the particle
    def update(self):
        self.pos += self.vel/2
        self.alf -= 2
    
    # draws the "fire" particle
    def render(self):
        global r
        x = self.pos.x
        y = self.pos.y
        pushMatrix()
        translate(x, y)
        rotate(radians(60+r))
        noStroke()
        fill(self.clr, self.alf)
        rect(0, 0, SQR_SIZE, SQR_SIZE)
        r += .23
        popMatrix()
