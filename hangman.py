# Name: Austin Purtell
# hangman.py
#
# Purpose: plays a game of hangman
#
# Certification of Authenticity:
# I certify that this lab is entirely my own work.

from graphics import *
import random
from Chapter10 import Button

def fileRead():
    #reads file
    file = open("wordlist.txt")
    wordList = []
    for line in file:
        lineStr = line.split()
        for word in lineStr:
            wordList.append(word)
    file.close()
    return wordList

def randWord(wordList):
    #picks random word from data
    word = random.choice(wordList)
    return word

def returnGuess(blank, letter, word):
    #replaces the blank with guessed letter if it belongs there
    for i in range(len(word)):
        if letter == word[i]:
            blank[i] = letter

def letterTest(letter, word):
    #if the letter is in word return true
    return letter in word

def guessLeft(guesses):
    #deducts a guess
    guesses -= 1
    return guesses

def blankMake(num):
    #makes blank to display
    blank = []
    for i in range(num):
        blank.append("_ ")
    return blank

def winTest(blank, word):
    #returns true if the word = the guessed string
    blankStr = ''.join(blank)
    return blankStr == word

def guessDisplay(guessList,win):
    #displays all the incorrect guesses
    guessTxt = ""
    for i in range(len(guessList)):
        guessTxt += guessList[i] + "   "
    guessMsg = Text(Point(200,360),guessTxt)
    guessMsg.setSize(24)
    guessMsg.setStyle("bold")
    guessMsg.draw(win)
    return guessMsg

def playGame(word, guesses, blank, guessList, win, messages):
    #word progress
    blankStr = ' '.join(blank)
    msgWord = Text(Point(300,580),"Word: \t" + blankStr)
    msgWord.setSize(30)
    msgWord.setStyle("bold")
    #guesses left, incorrect guesses, input
    msgLeft = Text(Point(160,450),"Guesses left:   " + str(guesses))
    msgFail = Text(Point(160,300),"Incorrect Guesses: ")
    msgLetter = Text(Point(160,200),"Guess a letter: ")

    guessMsg = guessDisplay(guessList, win)
    letterBox = Entry(Point(300,200),3)
    #parameters
    msgSingle = Text(Point(300,240),"Single Letters Only!")
    msgSingle.setTextColor("red")
    msgOnly = Text(Point(300,240),"Letters Only!")
    msgOnly.setSize(20)
    msgOnly.setTextColor("red")
    msgContinue = Text(Point(300,270),"Click to continue.")
    msgContinue.setTextColor("red")
    #uses less lines to build display
    messages2 = [msgWord,msgLeft,msgFail,msgLetter,letterBox,
                 msgSingle,msgOnly,msgContinue,guessMsg]

    for i in range(5):
        messages2[i+1].setSize(20)
        messages2[i].draw(win)

    win.getMouse()
    letter = letterBox.getText()
    #checks to make sure letter is being input
    if len(letter) > 1:
        msgSingle.draw(win)
        msgContinue.draw(win)
        win.getMouse()
    elif not letter.isalpha():
        msgOnly.draw(win)
        msgContinue.draw(win)
        win.getMouse()
    #clears for next iteration
    for i in range(len(messages)):
        messages[i].undraw()
    for i in range(len(messages2)):
        messages2[i].undraw()

    letter = letter.lower()
    return letter

#----

#def graphics():
    
def main():
    #initializations
    guesses = 7
    guessList = []
    wordList = fileRead()
    word = randWord(wordList)
    wordLen = len(word)
    blank = blankMake(wordLen)

    #build and display window
    width = 1000
    height = 700
    win = GraphWin("Hangman", width, height)
    win.setBackground("#ddddf0")
    centerX = width/2
    centerY = height/2
    
    intro = Text(Point(centerX, 40),"HANG MAN")
    intro.setFace("courier")
    intro.setSize(24)
    intro.setStyle("bold")
    intro.draw(win)

    gallow1 = Line(Point(width-200,100),Point(width-200,height-100))
    gallow2 = Line(Point(width-330,height-100),
                   Point(width-70,height-100))
    gallow3 = Line(Point(width-280,100),Point(width-200,180))
    gallow4 = Line(Point(width-440,100),Point(width-195,100))
    gallow5 = Line(Point(width-440,95),Point(width-440,120))

    rope1 = Line(Point(width-440,120),Point(width-440,200))
    rope1.setWidth(6)
    rope1.setFill("brown")
    rope2 = Oval(Point(width-460,200),Point(width-420,260))
    rope2.setWidth(6)
    rope2.setOutline("brown")

    head = Circle(Point(width-440,225), 30)
    head.setFill("black")
    body = Line(Point(width-440,220),Point(width-440,380))
    arm1 = Line(Point(width-440,265),Point(width-395,310))
    arm2 = Line(Point(width-440,265),Point(width-485,310))
    leg1 = Line(Point(width-440,370),Point(width-420,430))
    leg2 = Line(Point(width-440,370),Point(width-460,430))

    thing1 = Line(Point(width-455,220),Point(width-445,230))
    thing2 = Line(Point(width-455,230),Point(width-445,220))
    thing3 = Line(Point(width-435,220),Point(width-425,230))
    thing4 = Line(Point(width-435,230),Point(width-425,220))

    things = [thing2,thing3,thing4,thing1]
    for i in range(4):
        things[i].setFill("red")
        things[i].setWidth(3)

    msgWin = Text(Point(150,210),"You Win!")
    msgLose = Text(Point(150,210),"You Lose!")
    msgCorrect = Text(Point(140,110),"Correct!")
    msgWrong = Text(Point(140,110),"Wrong!")
    msgWordWas = Text(Point(260,310),"The word was " + word + "!")

    gallows = [gallow1,gallow2,gallow3,gallow4,gallow5]
    man = [thing1,leg2, leg1, arm2, arm1, body, head]
    messages = [msgWin, msgLose, msgCorrect, msgWrong, msgWordWas]

    for i in range(5):
        gallows[i].setWidth(10)
        gallows[i].draw(win)
        man[i+1].setWidth(10)
        messages[i].setSize(30)
        messages[i].setTextColor("red")

    rope1.draw(win)
    rope2.draw(win)

    #runs game
    while guesses > 0:
        letter = playGame(word, guesses, blank,
                          guessList, win, messages)
        #fixes clicking elsewhere on screen displaying "correct"
        if letter == "":
            guesses += 0
        #if correct
        elif letterTest(letter, word):
            msgCorrect.draw(win)
            returnGuess(blank, letter, word)
            if winTest(blank, word):
                msgWin.draw(win)
                msgWordWas.draw(win)
                break
        #if incorrect
        else:
            msgWrong.draw(win)
            guessList.append(letter)
            guesses = guessLeft(guesses)
            man[guesses].draw(win)
    #if user loses game
    if guesses == 0:
        msgLose.draw(win)
        msgWordWas.draw(win)
        for i in range(3):
            things[i].draw(win)
            
    #builds buttons and displays text
    playAgain = Text(Point(260,400),"Play Again?")
    playAgain.setSize(30)
    playAgain.setTextColor("gray")
    playAgain.draw(win)
    
    buttonYes = Button(Point(160,440),Point(240,500),"Yes","green")
    buttonNo = Button(Point(280,440),Point(360,500),"No","red")
    buttonYes.draw(win)
    buttonNo.draw(win)

    #restarts game or closes window based on input
    pt = win.getMouse()
    clickYes = buttonYes.wasClicked(pt)
    clickNo = buttonNo.wasClicked(pt)
    while clickYes == False and clickNo == False:
        pt = win.getMouse()
        clickYes = buttonYes.wasClicked(pt)
        clickNo = buttonNo.wasClicked(pt)
    if clickYes:
        win.close()
        main()
    win.close()
    
main()
