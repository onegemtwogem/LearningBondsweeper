#dead code from term project
"""
    row = (event.x - canvas.data.margin)/canvas.data.cellSize
    col = (event.y - canvas.data.margin)/canvas.data.cellSize

    #create board
    rows, cols = canvas.data.rows, canvas.data.cols
    minesweeperBoard = []
    for row in range(rows): minesweeperBoard += [[-1] * cols]
    #then place mines
    mines = []
    while len(mines) < 15:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (minesweeperBoard[row][col] == -1):
            minesweeperBoard[row][col] = -2
            mines.append((row, col))
    canvas.data.minesweeperBoard = minesweeperBoard

#from drawMinesweeperBoard
    rows, cols = len(minesweeperBoard), len(minesweeperBoard[0])
    for col in xrange(cols):
        for row in xrange(rows):
            drawMinesweeperCell(canvas, row, col)

def drawMinesweeperCell(canvas, row, col):
    margin = canvas.data.margin
    cellSize = canvas.data.cellSize
    left = margin + col * cellSize
    right = left + cellSize
    top = margin + row * cellSize
    bottom = top + cellSize
    minesweeperBoard = canvas.data.minesweeperBoard
    if minesweeperBoard[row][col] == -1: #hidden cell
        canvas.create_rectangle(left, top, right, bottom, fill = canvas.data.hiddenColor)
    if minesweeperBoard[row][col] == -2: #hidden cell
        canvas.create_rectangle(left, top, right, bottom, fill = "red")
    elif minesweeperBoard[row][col] == 0: #cell that touches no mines
        canvas.create_rectangle(left, top, right, bottom)
    else: #display number of adjacent mines
        canvas.create_rectangle(left, top, right, bottom)
        canvas.create_text(left, top, text="%d"%(minesweeperBoard[row][col]))

from randomly place minesweeperBoard    
for country in countries:
        if nMines < canvas.data.numberMines:
            x = random.randint(0, len(countries))
            if x < canvas.data.numberMines:
                countries[country].isMine = True

    def placeFlag(self, canvas):
        #flags will be red, for now
        pass

if not self.isVisible: #create hidden cell
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize, 
                fill = canvas.data.hiddenColor)
        elif self.isFlagged:
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize, 
                fill = "red")
            canvas.create_text(self.location[0], self.location[1], 
                text = "  %s"%("!!"), anchor = NW) 
        elif self.isQuestion:
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize, 
                fill = "green")
            canvas.create_text(self.location[0], self.location[1], 
                text = "  %s"%("?"), anchor = NW) 
        else: #create visible cell
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize)
            canvas.create_text(self.location[0], self.location[1], 
                text = "  %s"%(self.adjMines), anchor = NW)


def rightMousePressed(canvas, event): #controller
    countries = canvas.data.countries
    if mousePressedHelper(canvas, event) == False: 
        print "No country" #####
    elif (countries[mousePressedHelper(canvas, event)].isVisible == True): 
        pass #if it is visible, do nothing
    elif (countries[mousePressedHelper(canvas, event)].isFlagged == True):
        #if it is flagged, make it a question mark
        #countries[mousePressedHelper(canvas, event)].isFlagged = False
        #countries[mousePressedHelper(canvas, event)].isQuestion = True
        [mousePressedHelper(canvas, event)].placeQuestion(canvas)
    elif (countries[mousePressedHelper(canvas, event)].isQuestion == True):
        #if it is questioned, make if blank
        #countries[mousePressedHelper(canvas, event)].isQuestion = False
        countries[mousePressedHelper(canvas, event)].removeQuestion(canvas)
    else: #if it is blank, make it questioned
        countries[mousePressedHelper(canvas, event)].placeFlag(canvas)
    redrawAll(canvas)


        for x in xrange(canvas.data.squareSize):
            for y in xrange(canvas.data.squareSize):
                if ((event.x == countries[country].location[0] + x) and 
                    (event.y == countries[country].location[1] + y)):
                    return country
    #change to check greater than location and less than location + sqaureSize

def drawStartScreen(canvas):
    canvas.data.bg = PhotoImage(file = "blank_europe_map_resized.gif")
    canvas.create_image(canvas.data.width/2, canvas.data.height/2, 
        image = canvas.data.bg)

    countries["Germany"] = MinesweeperCountry("Germany", (0.3*width, 0.3*height), 
        ["Luxembourg", "Netherlands", "Belgium", "Poland", "Austria", "Switzerland",
        "Czech Republic", "Liechtenstein", "France"], False, False, 0)
    countries["France"] = MinesweeperCountry("France", (0.2*width, 0.5*height), ["Spain",
        "Germany", "Switzerland", "Belgium", "Italy", "Luxembourg", "Andorra"], 
        False, False, 0)
    countries["Hungary"] = MinesweeperCountry("Hungary", (0.6*width, 0.6*height),
        ["Slovakia", "Austria", "Ukraine", "Romania", "Serbia", "Croatia", 
        "Slovenia"], False, False, 0)
    countries["Spain"] = MinesweeperCountry("Spain", (0.2*width, 0.8*height), 
        ["Portugal", "France", "Andorra"], False, False, 0) 
    countries["Belgium"] = MinesweeperCountry("Belgium", (0.25*width, 0.3*height), 
        ["Germany", "France", "Luxembourg", "Netherlands"], False, False, 0)
    countries["Switzerland"] = MinesweeperCountry("Switzerland", 
        (0.3*width, 0.5*height), ["Germany", "France", "Italy", "Liechtenstein"], 
        False, False, 0)
    countries["Portugal"] = MinesweeperCountry("Portugal", (0.15*width, 0.8*height), 
        ["Spain"], False, False, 0) 
    countries["Netherlands"] = MinesweeperCountry("Netherlands", (0.27*width, 0.27*height), 
        ["Germany", "Belgium"], False, False, 0) #
    countries["Liechtenstein"] = MinesweeperCountry("Liechtenstein", (0.35*width, 0.5*height), 
        ["Switzerland", "Austria", "Germany", "Italy"], False, False, 0)
    countries["Italy"] = MinesweeperCountry("Italy", (0.4*width, 0.7*height), 
        ["France", "Austria", "Switzerland", "Liechtenstein", "Slovenia"], False, False, 0)
    countries["Austria"] = MinesweeperCountry("Austria", (0.5*width, 0.5*height), 
        ["Czech Republic", "Germany", "Italy", "Hungary", "Liechtenstein", "Slovenia", "Slovakia"], False, False, 0)
    countries["Slovakia"] = MinesweeperCountry("Slovakia", (0.6*width, 0.5*height), 
        ["Austria", "Hungary", "Poland", "Ukraine", "Czech Republic"], False, False, 0)
    countries["Slovenia"] = MinesweeperCountry("Slovenia", (0.6*width, 0.6*height), 
        ["Hungary", "Austria", "Croatia", "Italy"], False, False, 0)
    countries["Croatia"] = MinesweeperCountry("Croatia", (0.65*width, 0.65*height), 
        ["Slovenia", "Hungary", "Serbia", "Bosnia and Herzegovina", "Montenegro"], False, False, 0)
    countries["Bosnia and Herzegovina"] = MinesweeperCountry("Bosnia and Herzegovina", (0.7*width, 0.7*height), 
        ["Croatia", "Serbia", "Montenegro"], False, False, 0)
    countries["Serbia"] = MinesweeperCountry("Serbia", (0.75*width, 0.7*height), 
        ["Hungary", "Croatia", "Bosnia and Herzegovina", "Romania", "Bulgaria", 
        "Montenegro", "Kosovo", "Macedonia"], False, False, 0)
    countries["Montenegro"] = MinesweeperCountry("Montenegro", (0.7*width, 0.75*height), 
        ["Serbia", "Bosnia and Herzegovina", "Croatia", "Albania", "Kosovo"], False, False, 0)
    countries["Kosovo"] = MinesweeperCountry("Kosovo", (0.75*width, 0.78*height), 
        ["Montenegro", "Albania", "Serbia", "Macedonia"], False, False, 0)
    countries["Macedonia"] = MinesweeperCountry("Macedonia", (0.7*width, 0.85*height), 
        ["Kosovo", "Bulgaria", "Albania", "Greece", "Serbia"], False, False, 0)
    countries["Bulgaria"] = MinesweeperCountry("Bulgaria", (0.75*width, 0.8*height), 
        ["Macedonia", "Serbia", "Romania", "Greece"], False, False, 0)
    countries["Romania"] = MinesweeperCountry("Romania", (0.8*width, 0.55*height), 
        ["Serbia", "Bulgaria", "Hungary", "Moldova", "Ukraine"], False, False, 0)
    countries["Ukraine"] = MinesweeperCountry("Ukraine", (0.95*width, 0.4*height), 
        ["Moldova", "Slovakia", "Romania", "Hungary", "Poland", "Belarus"], False, False, 0)
    countries["Andorra"] = MinesweeperCountry("Andorra", (0.2*width, 0.65*height), 
        ["France", "Spain"], False, False, 0)
    countries["Poland"] = MinesweeperCountry("Poland", (0.35*width, 0.5*height), 
        ["Ukraine", "Slovakia", "Germany", "Belarus", "Czech Republic", "Lithuania"], False, False, 0)
    countries["Moldova"] = MinesweeperCountry("Moldova", (0.9*width, 0.45*height), 
        ["Romania", "Ukraine"], False, False, 0)
    countries["Czech Republic"] = MinesweeperCountry("Czech Republic", (0.35*width, 0.5*height), 
        ["Poland", "Austria", "Germany", "Slovakia"], False, False, 0)
    countries["Belarus"] = MinesweeperCountry("Belarus", (0.9*width, 0.15*height), 
        ["Lithuania", "Latvia", "Poland", "Ukraine"], False, False, 0)
    countries["Lithuania"] = MinesweeperCountry("Lithuania", (0.85*width, 0.1*height), 
        ["Latvia", "Poland", "Belarus"], False, False, 0)
    countries["Latvia"] = MinesweeperCountry("Latvia", (0.9*width, 0.05*height), 
        ["Lithuania", "Belarus", "Estonia"], False, False, 0)
    countries["Estonia"] = MinesweeperCountry("Estonia", (0.95*width, 0.03*height), 
        ["Latvia"], False, False, 0)
    countries["Albania"] = MinesweeperCountry("Albania", (0.65*width, 0.85*height), 
        ["Greece", "Kosovo", "Macedonia", "Montenegro"], False, False, 0)
    countries["Greece"] = MinesweeperCountry("Greece", (0.8*width, 0.9*height), 
        ["Albania", "Macedonia", "Bulgaria"], False, False, 0)
    countries["Luxembourg"] = MinesweeperCountry("Luxembourg", (0.25*width, 0.4*height), 
        ["France", "Belgium", "Germany"], False, False, 0)


class MinesweeperCountry(object): 
    "attributes: location, name, neighbors, mine, visibility, adjacent mines
    methods: uncover, place flag"
    def __init__(self, name, location, neighbors, isMine, isVisible, adjMines):
        self.name = name
        self.location = location
        self.neighbors = neighbors
        self.isMine = isMine
        self.isVisible = isVisible
        self.adjMines = adjMines
        self.isFlagged = False
        self.isQuestion = False
"""
"""
#before Africa
#Goal: 500+ lines of good code, not bunches of text, nonsense, dead code, etc.
from Tkinter import *
import random
import tkMessageBox
import tkSimpleDialog

class MinesweeperCountry(object): 
    """"""attributes: location, name, neighbors, mine, visibility, adjacent mines
    methods: uncover, place flag""""""
    def __init__(self, name, location, neighbors):
        self.name = name
        self.location = location
        self.neighbors = neighbors
        self.isMine = False
        self.isVisible = False
        self.adjMines = 0
        self.isFlagged = False
        self.isQuestion = False

    def uncover(self, canvas):
        if (self.isVisible == False) and (self.isMine == False): 
            self.isVisible = True 
            #this is similar to memoizing, because it keeps track of visited mines
            self.drawCountryBox(canvas)
            canvas.data.uncoveredCountries += [self.name]
            if len(canvas.data.uncoveredCountries) == len(canvas.data.freeCountries):
                youWin(canvas)
            if self.adjMines == 0: self.uncoverAdjZeros(canvas)
            #this  bit is a common minesweeper function, to avoid tedious 
            #uncovering

    def uncoverAdjZeros(self, canvas):
        countries = canvas.data.countries
        for country in self.neighbors:
            #if countries[country].adjMines == 0:
            countries[country].uncover(canvas) #RECURSION!!!!!!!!!!!!!!!!!!!!!!!

    def nameCountry(self, canvas): #CITE?
        message = "Which country is this?"
        title = ""
        options = self.getOptions(canvas)
        for i in xrange(len(options)):
            message += "\n" + options[i]
        response = tkSimpleDialog.askstring(title, message) 
        #type(response) = string
        return response

    def getOptions(self, canvas): #model
        weightedOptions = canvas.data.listOfCountries
        for country in self.neighbors:
            weightedOptions += 7*[country]
            #IS THIS TOO EXPENSIVE???? ie does it take too much time?
        options = [self.name]
        while len(options) < 5:
            country = weightedOptions[random.randint(0, len(weightedOptions)-1)]
            if country not in options: options += [country]
        random.shuffle(options)
        return options

    def placeFlag(self, canvas):
        self.isFlagged = True
        self.drawCountryBox(canvas)
        namedCountry = self.nameCountry(canvas)
        if namedCountry != self.name: 
            gameOver(canvas, self.location[0], self.location[1], "Wrong country.")

    def placeQuestion(self, canvas):
        self.isFlagged = False
        self.isQuestion = True
        self.drawCountryBox(canvas)

    def removeQuestion(self, canvas):
        self.isQuestion = False
        self.drawCountryBox(canvas)

    def mineDetonated(self, canvas): #DO I NEED THIS??
        pass

    def printCountryName(self,canvas):
        canvas.create_rectangle(self.location[0], self.location[1], 
            self.location[0] + canvas.data.squareSize, 
            self.location[1] + canvas.data.squareSize, fill = "white", 
            width = 0)
        canvas.create_text(self.location[0], 
            self.location[1] + canvas.data.squareSize/2, 
            text = "%s"%(self.name), anchor = W, 
            font=("Helvetica 16 bold")) 

    def drawCountryBox(self, canvas): #view
        if self.isVisible:
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize, fill = "white", 
                width = 2)
            canvas.create_text(self.location[0] + canvas.data.squareSize/2, 
                self.location[1] + canvas.data.squareSize/2, 
                text = "%s"%(self.adjMines), anchor = CENTER, 
                font=("Helvetica 11 bold")) 
        else:
            if self.isFlagged: fill, phrase = "red", ""
            elif self.isQuestion: fill, phrase = "green", "?"
            else: fill, phrase = canvas.data.hiddenColor, ""
            canvas.create_rectangle(self.location[0], self.location[1], 
                self.location[0] + canvas.data.squareSize, 
                self.location[1] + canvas.data.squareSize, fill = fill, width = 2)
            canvas.create_text(self.location[0] + canvas.data.squareSize/2, 
                self.location[1] + canvas.data.squareSize/2, 
                text = phrase, anchor = CENTER, font=("Helvetica 11 bold"))

def drawMinesweeperBoard(canvas): #view
    canvas.create_image(canvas.data.width/2, canvas.data.height/2, image = canvas.data.bg)
    if canvas.data.newGameButton != False:
        canvas.create_window(40, 610, window = canvas.data.newGameButton)
    canvas.create_window(112, 610, window = canvas.data.instructionsButton)
    countries = canvas.data.countries
    for country in countries: 
        countries[country].drawCountryBox(canvas)

def gameOver(canvas, x, y, reason): #model
    canvas.data.isGameOver = True
    canvas.data.inPlay = False
    index = random.randint(0, len(canvas.data.jamesBond)-1)
    canvas.data.bond = canvas.data.jamesBond[index]
    canvas.data.reason = reason
    redrawAll(canvas, x, y)

def youWin(canvas):
    canvas.data.isGameOver = True
    canvas.data.youWon = True
    redrawAll(canvas, 0, 0)

def redrawAll(canvas, x, y): #view
    canvas.delete(ALL)
    width, height = canvas.data.width, canvas.data.height
    drawMinesweeperBoard(canvas)
    if (canvas.data.isGameOver == True) and (canvas.data.youWon == True):
        canvas.create_text(width/2, height/2, text="You WON!", anchor=CENTER, 
            font=("Helvetica", 48, "bold"))
        fact = canvas.data.facts[random.randint(0,len(canvas.data.facts)-1)]
        #print a fun fact if you win!
        canvas.create_text(width/2, height/2 - 0.4*height, text=fact, 
            anchor = CENTER, font=("Helvetica 36 bold"), width = 0.7*canvas.data.width)
    elif canvas.data.isGameOver == True:
        canvas.create_image(x, y, image = canvas.data.bond)
        canvas.create_text(width/2, height/2, text="Game Over!", anchor=CENTER, 
            font=("Helvetica", 48, "bold"))
        canvas.create_text(width/2, height/2 - 0.1*height, 
            text=canvas.data.reason, anchor=CENTER, font=("Helvetica 36 bold"))

def mousePressedHelper(canvas, event): #model
    """"""Returns country name if the mouse was pressed in a box, otherwise 
    returns False """"""
    countries = canvas.data.countries
    for country in countries:
        if ((countries[country].location[0] <= event.x <= 
            countries[country].location[0] + canvas.data.squareSize) 
            and (countries[country].location[1] <= event.y <= 
                countries[country].location[1] + canvas.data.squareSize)):
            return country
    return False

def saveYourself(canvas):
    trivia = loadTextList("trivia.txt")
    index = 2*(random.randint(0, (len(trivia)-1)/2))
    question = trivia[index]
    answer = trivia[index+1]
    message = "Bond found you. He'll let you go if you answer his question: '%s'"%(question)
    title = ""
    #options = ["Antarctica", "Europe"]
    #for i in xrange(len(options)):
    #    message += "\n" + options[i]
    response = tkSimpleDialog.askstring(title, message) 
    #type(response) = string
    return (response == answer)

def leftMousePressed(canvas, event): #controller, wrapper
    """"""If square is a bomb, game over. If it's a hidden country, uncover it.
    Otherwise, do nothing.""""""
    print event.x, event.y
    if canvas.data.inPlay == False: return
    countries = canvas.data.countries
    if mousePressedHelper(canvas, event) == False: #no country pressed
        pass
    elif countries[mousePressedHelper(canvas, event)].isMine == True:
        if saveYourself(canvas): pass
        else:
            countries[mousePressedHelper(canvas, event)].mineDetonated(canvas)
            x, y = event.x, event.y
            gameOver(canvas, x, y, "Bond got you.")
    else: 
        countries[mousePressedHelper(canvas, event)].uncover(canvas)

def rightMousePressed(canvas, event): #controller
    if canvas.data.inPlay == False: return
    countries = canvas.data.countries
    if mousePressedHelper(canvas, event) == False: 
        pass
    #elif (countries[mousePressedHelper(canvas, event)].isVisible == True): 
    #    pass #if it is visible, do nothing
    elif (countries[mousePressedHelper(canvas, event)].isFlagged == True):
        #if it is flagged, make it a question mark
        countries[mousePressedHelper(canvas, event)].placeQuestion(canvas)
        redrawAll(canvas, 0, 0)
    elif (countries[mousePressedHelper(canvas, event)].isQuestion == True):
        #if it is questioned, make if blank
        countries[mousePressedHelper(canvas, event)].removeQuestion(canvas)
        redrawAll(canvas, 0, 0)
    else: #if it is blank, make it questioned
        countries[mousePressedHelper(canvas, event)].placeFlag(canvas)

def reviewCountries(canvas, event): 
    init(canvas)
    canvas.data.inPlay = False
    countries = canvas.data.countries
    country = mousePressedHelper(canvas, event) #get country name
    if country != False: #mousePressedHelper may return false
        countries[country].printCountryName(canvas)

def mouseMotion(canvas, event): #controller
    canvas.data.mousePosition = (event.x, event.y) 
    if canvas.data.reviewCountries == True:
        reviewCountries(canvas, event)
#    redrawAll(canvas, 0, 0)

def randomlyPlaceMines(canvas): #model
    countries = canvas.data.countries
    mines = []
    while len(mines) < canvas.data.numberMines: #random indices, no repeats
        index = random.randint(0, len(countries)-1)
        if index not in mines: mines.append(index)
    for mine in mines:
        countries[canvas.data.listOfCountries[mine]].isMine = True
    #countries[mine].isMine = True for mine in mines

def findAdjMines(canvas):
    countries = canvas.data.countries
    for country in countries:
        adjMines = 0
        for neighbor in countries[country].neighbors:
            if countries[neighbor].isMine == True:
                adjMines += 1
        countries[country].adjMines = adjMines

def loadTextList(fileName): #From course website, fall 2010
    fileHandler = open(fileName, "rt") # rt stands for read text
    text = fileHandler.readlines() # read the entire file into a list
    fileHandler.close() # close the file
    return text

def getCountriesInfo(canvas): 
    #name, location, neighbors, isMine, isVisible, adjmines
    width, height = canvas.data.width, canvas.data.height
    countries = canvas.data.countries
    countriesList = loadTextList("Countries.txt")
    #the following code pulls from the adjacency list stored in Countries.txt to
    #create a graph where countries are nodes and edges connect each country
    #to its neighbors
    for country in xrange(len(countriesList)):
        #key name
        indx = countriesList[country].index(",")
        key = countriesList[country][0:indx]
        countriesList[country] = countriesList[country][indx+1:]
        #country name, same as key name
        indx = countriesList[country].index(",")
        name = countriesList[country][0:indx]
        countriesList[country] = countriesList[country][indx+1:]
        #width
        indx = countriesList[country].index(",")
        xlocation = countriesList[country][0:indx]
        countriesList[country] = countriesList[country][indx+1:]
        #height
        indx = countriesList[country].index(",")
        ylocation = countriesList[country][0:indx]
        countriesList[country] = countriesList[country][indx+1:]
        #neighbors
        neighbors = []
        while "," in countriesList[country]:
            indx = countriesList[country].index(",")
            neighbors.append(countriesList[country][0:indx])
            countriesList[country] = countriesList[country][indx+1:]
        countries[key] = MinesweeperCountry(name, 
            (int(xlocation)-canvas.data.squareSize/2, 
                int(ylocation)-canvas.data.squareSize/2), neighbors)

def loadMinesweeperBoard(canvas): 
    width, height = canvas.data.width, canvas.data.height
    countries = {}
    canvas.data.countries = countries
    getCountriesInfo(canvas)
    listOfCountries = []
    for country in countries: 
        listOfCountries.append(countries[country].name)
    canvas.data.listOfCountries = listOfCountries
    if canvas.data.reviewCountries == False:
        randomlyPlaceMines(canvas)
        findAdjMines(canvas)
        freeCountries = []
        mineCountries = []
        for country in listOfCountries:
            if countries[country].isMine == False: freeCountries += [country]
            else: mineCountries += [country]
        canvas.data.countries = countries
        canvas.data.freeCountries = freeCountries #countries w/o mine
        canvas.data.mineCountries = mineCountries #countries w/ mine
        canvas.data.uncoveredCountries = [] #to add countries that get uncovered

def init(canvas):
    canvas.data.numberMines = 1
    canvas.data.squareSize = 15
    canvas.data.hiddenColor = "blue"
    canvas.data.isGameOver = False
    canvas.data.youWon = False
    canvas.data.margin = 5
    canvas.data.cellSize = 15
    canvas.data.bg = PhotoImage(file = "blank_europe_map_resized.gif") 
    bond1 = PhotoImage(file = "bond_1.gif")
    bond2 = PhotoImage(file = "bond_2.gif")
    bond3 = PhotoImage(file = "bond_3.gif")
    bond4 = PhotoImage(file = "bond_4.gif")
    canvas.data.jamesBond = [bond1, bond2, bond3, bond4]
    canvas.data.facts = loadTextList("facts.txt")
    loadMinesweeperBoard(canvas)
    redrawAll(canvas, 0, 0)

def run():
    root = Tk()
    width, height = 875, 600
    canvas = Canvas(root, width = width, height = height)
    canvas.pack()
    root.resizable(width=0, height=0)
    root.title("Creating World Peace (and geographical literacy)")
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width, canvas.data.height = width, height
    initStart(root, canvas)
    # set up events
    root.bind("<Button-1>", lambda event: leftMousePressed(canvas, event))
    root.bind("<Button-3>", lambda event: rightMousePressed(canvas, event))
    root.bind("<Motion>", lambda event: mouseMotion(canvas, event))
    #timerFired(canvas)
    # and launch the app
    root.mainloop()  
    # This call BLOCKS (so your program waits until you close the window!)

# START SCREEN

def drawStart(canvas):
    canvas.delete(ALL)
    canvas.data.bg = PhotoImage(file = "blank_europe_map_resized.gif")
    canvas.create_image(canvas.data.width/2, canvas.data.height/2, 
        image = canvas.data.bg)
    if canvas.data.showInstructions == True:
        displayInstructions(canvas)
    elif canvas.data.reviewCountries == True:
        reviewCountries(canvas)
    else:
        canvas.create_rectangle(15, 
            canvas.data.height/2-15, canvas.data.width-15, 
            canvas.data.height/2+15, fill = "white", width = 0)
        canvas.create_text(canvas.data.width/2, canvas.data.height/2, 
            anchor = CENTER, text="Select 'Begin' or 'Instructions' or 'Review Countries'", 
            font="Helvetica 26 bold",)

def createButtons(root, canvas):
    #create begin button
    def begin(): 
        canvas.data.inPlay = True
        canvas.data.reviewCountries = False
        canvas.delete(canvas.data.beginButton)
        newGameButton = Button(root, text="New Game", command=begin)
        newGameButton.pack()
        canvas.data.newGameButton = newGameButton
        init(canvas)
    beginButton = Button(root, text="Begin", command=begin)
    beginButton.pack()
    #instructions button
    canvas.data.showInstructions = False
    def instructions(): 
        canvas.data.showInstructions = True
        canvas.data.reviewCountries = False
        displayInstructions(canvas)
        drawStart(canvas)
    instructionsButton = Button(root, text="Instructions", command=instructions)
    instructionsButton.pack()
    #review countries button
    canvas.data.reviewCountries = False
    def review():
        canvas.data.newGameButton = False
        canvas.data.reviewCountries = True
    reviewButton = Button(root, text="Review Countries", command=review)
    reviewButton.pack()
    canvas.data.beginButton = beginButton
    canvas.data.instructionsButton = instructionsButton

def initStart(root, canvas):
    canvas.data.inPlay = False
    createButtons(root, canvas)
    drawStart(canvas)

def displayInstructions(canvas):
    width, height = canvas.data.width, canvas.data.height
    instructions = loadTextList("instructions.txt")[0]
    canvas.create_rectangle(width/2-210, 0.15*height, width/2+210, 0.8*height, fill = "white")
    canvas.create_text(width/2, height/2, text="%s"%(instructions), font="Helvetica 14", width = 400)

run()
"""
"""
class SimpleDialog(object):

    def __init__(self, master,
                 text='', buttons=[], default=None, cancel=None,
                 title=None, class_=None):
        if class_:
            self.root = Toplevel(master, class_=class_)
        else:
            self.root = Toplevel(master)
        if title:
            self.root.title(title)
            self.root.iconname(title)
        self.message = Message(self.root, text=text, aspect=400)
        self.message.pack(expand=1, fill=BOTH)
        self.frame = Frame(self.root)
        self.frame.pack()
        self.num = default
        self.cancel = cancel
        self.default = default
        self.root.bind('<Return>', self.return_event)
        for num in range(len(buttons)):
            s = buttons[num]
            b = Button(self.frame, text=s,
                       command=(lambda self=self, num=num: self.done(num)))
            if num == default:
                b.config(relief=RIDGE, borderwidth=8)
            b.pack(side=LEFT, fill=BOTH, expand=1)
        self.root.protocol('WM_DELETE_WINDOW', self.wm_delete_window)
        self._set_transient(master)

    def _set_transient(self, master, relx=0.5, rely=0.3):
        widget = self.root
        widget.withdraw() # Remain invisible while we figure out the geometry
        widget.transient(master)
        widget.update_idletasks() # Actualize geometry information
        if master.winfo_ismapped():
            m_width = master.winfo_width()
            m_height = master.winfo_height()
            m_x = master.winfo_rootx()
            m_y = master.winfo_rooty()
        else:
            m_width = master.winfo_screenwidth()
            m_height = master.winfo_screenheight()
            m_x = m_y = 0
        w_width = widget.winfo_reqwidth()
        w_height = widget.winfo_reqheight()
        x = m_x + (m_width - w_width) * relx
        y = m_y + (m_height - w_height) * rely
        if x+w_width > master.winfo_screenwidth():
            x = master.winfo_screenwidth() - w_width
        elif x < 0:
            x = 0
        if y+w_height > master.winfo_screenheight():
            y = master.winfo_screenheight() - w_height
        elif y < 0:
            y = 0
        widget.geometry("+%d+%d" % (x, y))
        widget.deiconify() # Become visible at the desired location

    def go(self):
        self.root.wait_visibility()
        self.root.grab_set()
        self.root.mainloop()
        self.root.destroy()
        return self.num

    def return_event(self, event):
        if self.default is None:
            self.root.bell()
        else:
            self.done(self.default)

    def wm_delete_window(self):
        if self.cancel is None:
            self.root.bell()
        else:
            self.done(self.cancel)

    def done(self, num):
        self.num = num
        self.root.quit()


#MY CODE


    def nameCountry(self, canvas): #CITE?
        message = "Which country is this?"
        title = ""
        options = self.getOptions(canvas)
        #for i in xrange(len(options)):
        #    message += "\n" + options[i]
        #response = tkSimpleDialog.askstring(title, message) 
        #type(response) = string
        response = SimpleDialog(canvas, text="Which country is this?", buttons = options)
        return response
        """
"""
def reviewCountries(canvas, event): 
    init(canvas)
    canvas.data.inPlay = False
    countries = canvas.data.countries
    country = mousePressedHelper(canvas, event) #get country name
    if country != False: #mousePressedHelper may return false
        countries[country].printCountryName(canvas)

def numberOfMinesUnmarked(canvas):
    flaggedMines = 0
    countries = canvas.data.countries
    for country in canvas.data.listOfCountries:
        if countries[country].isFlagged == True:
            flaggedMines += 1
    return (canvas.data.numberMines - flaggedMines)

"""