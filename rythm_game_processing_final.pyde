
song1Data = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 140, 140, 140, 140, 140, 140, 140, 
             140, 140, 140, 140, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
             0, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             70,70,71,72,73, 75, 76, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 201, 202, 203, 204, 205, 206,
             207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223, 0, 0, 0, 0, 130, 130, 130, 130, 130, 130, 130,
             130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130,
             130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130,
             130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130,
             130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 
             130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130, 130,
             ] # the y coordinates for each note (0 means there won't be a circle drawn)
song1Data.reverse() # the array is reversed so that the circles are read left to right


startingBreath = 150


def setup():
    global trombone, x, score, breath, startingBreath, song1Data, highScore
    size (700,700)
    frameRate(60) #mostly runs at 60 fps. having an image as a bakground makes it runs slower sometimes.
    noCursor() #doesn't show the cursor I mean why not
    
    textFont(loadFont("ComicSansMS.vlw"))
    textSize(32)
    
    trombone = loadImage("trombone.jpg") #trombone.jpg is located in this project's data folder.
    # reset/ declare variables
    x = 0
    score = 0
    breath = startingBreath
    highScore = 0
    
def draw():
    global song1Data, x, score, trombone, breath, startingBreath, highScore
    currentFrameCircleYCoordinates = {} # declare the array now so that it resets with each draw() loop
    #background(255,255,255) 
    image(trombone, 0,0,700,700) #trombone acts as the backgroung (its stretched to be 700, 700
    
    stroke(10) #you need to enable stroke, make a line and then disable stroke for the line to be visible
    line(50,0,50,700)
    noStroke()
    

    fill(0,0,0)
    text("High Score: " + str(highScore), 240, 40)
    text("score: " + str(score), 300, 600)
    text("breath: " + str(breath), 280, 630)
    text("press r to restart", 240, 670)
    
    
    for i in song1Data: #for each entry in the song1Data array, run this 
        circleX = 700+(2*len(song1Data))-x #circles' x coordinate should start at the right side of the screen. I have the (2*len(song1Data)) so that the song will always start at the end regardless of the song size
        if i != 0: #any entries that are 0 just won't show a circle
            circle(circleX, i, 20)
            currentFrameCircleYCoordinates[circleX] = int(i) # fill a dictionary with the y and x position of each circle
            # a dictionary entry would look like currentFrameCircleYCoordinates[x] = [y]
        x += 2
        #move the next circle to the left

    x -= 2* len(song1Data) #reset x to what it was before the for loop
    x += 2 # the circles will slowly go across the screen
    
    
    if mousePressed:
        fill (255,0,0)
        circle(50, mouseY, 30)
        breath -=1 
    
        for currentCircleX, currentCircleY in currentFrameCircleYCoordinates.items(): #for each row in the currentFrameCircleYCoordinates check if the X and Y coordinates are where the "cursor" is
                if mouseY + 15 > currentCircleY > mouseY - 15 and 40 < currentCircleX < 60:
                    score += 1            
    else:
        fill (0,0,255)
        circle(50, mouseY, 30)
        if breath > 0: #you can't get your breath back after going to zero - since the game is over
            breath = startingBreath
        
    if breath <= 0:
        #when the breath reaches zero, it resets all the variables aside for highScore and put the game into a game over state.
        x = 0 - len(song1Data) #moves all the notes way off screen
        score = 0 #resets the score
        breath = 0 #breath won't underflow
        fill(0,0,0)
        text("ran out of breath", 200, 100)
    
    if score > highScore: #if the score is higher than the high Score, it becomes the high score
        highScore = score
        
    
def keyPressed():
    global x, score, breath, startingBreath, song1Data
    if key == "r":
        #reset all the variables (aside for highScore)
        x = 0
        score = 0
        breath = startingBreath
        
    
        
