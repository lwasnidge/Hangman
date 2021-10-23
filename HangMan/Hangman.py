#Logan Wasnidge
#SDEV 220
#Final proj Proj.py
#12/20/2019

import random
from tkinter import*
#import random to pick random word from list, tkinter

def draw(count, msg1, msg2):
    
    canvas.create_line(10, 390, 50, 390)
    canvas.create_line(30, 390, 30, 50)
    canvas.create_line(30, 50, 200, 50)
    print(msg1)
    print(msg2, "\n")           #Here we create the frame for the gallows(?) and display the messages from the other functions.
    
    if count == 1:
        canvas.create_line(200, 50, 200, 70, tags = "hangman")      #draw the rope
    if count == 2:
        canvas.create_oval(170, 70, 230, 130, tags = "hangman")     #draw the head
    if count == 3:
        canvas.create_line(170, 100, 100, 150, tags = "hangman")    #draw the left
    if count == 4:
        canvas.create_line(230, 100, 300, 150, tags = "hangman")    #draw the other arm
    if count == 5:
        canvas.create_line(200, 130, 200, 250, tags = "hangman")    #draw the body
    if count == 6:
        canvas.create_line(200, 250, 100, 300, tags = "hangman")    #draw the left leg
    if count >= 7:
        canvas.create_line(200, 250, 300, 300, tags = "hangman")    #draw the right leg
    if count == 8:
        exit()
        
def keyPressed(event):
    global count, latestStr, missedLetters #When adding local variables to the global pool
    press = event.char    #getting our pressed key, which will be the users guess
  
    if not press.isalpha():
        print(press, " is not a letter")        #Checks to see that the pressed key is a letter or not
        return
    
    if press in missedLetters:
        print("You already guessed ", press ," wrong")  #Checks to see if the key was already guessed
        return
    
    if press in word:
        latestStrList = list(latestStr.replace(" ",""))     #Checks to see if the key was in the word. First we replace and spaces
        for i in range(0,len(word)):                        #Converts the word into a list
            if word[i] == press:
                latestStrList[i] = word[i]                  #check to see if the letter that was pressed is in the word
        latestStr = ''.join(latestStrList)
        msg1 = "Correct guess! Word: " +latestStr
        msg2 = "Missed letters: " +missedLetters            #let the user know if they got it right
                
    else:                       
        missedLetters += (press+'')
        count += 1
                                 #if the letter isn't in the word, then we add it to count
        if count < 7:
            msg1 = "Word: " +latestStr
            msg2 = "Missed letters: " +missedLetters
                                
        else:                   #if count is 7, then we tell the user they lost and end the game
            msg1 = "You lose! The word is: " +word
            msg2 = "Please exit program"
                                #I tried setting to count = 7 to count = 8 in draw so that it would draw and then end the program, but the last leg never got drawn, so I had to make the user go through twice.
            
    if '*' not in latestStr:        #Checks to see if all the *'s were elminated, meaning that all the letters were guessed.
        msg1 = "You win! The word was: " +word
        msg2 = "Please exit program"
        count = 8 #set to count 8 so that when it goes back to draw the function can exit

    draw(count, msg1, msg2)     #call the draw function so that we can draw if needed
    return


def newGame():
    global count, latestStr, word, missedLetters, canvas, window, size
    window = Tk()
    window.title("Hangman")         #Setting up our window
    word = latestStr= missedLetters ="" #making sure we start with no missed letters
    count=0             #setting our count at 0
    
    size = 500          #seeting the size of the window
    canvas = Canvas(window, width=size, height=size)
    canvas.pack()       #Canvas settings
    
    words = ["hello", "this", "is", "python", "project", "about", "hangman", "merry", "christmas"]      #small word list i put together
    word = random.choice(words)     #randomly chooses a word from the choices
    latestStr = "*" *len(word)      #sets the string to be *'s so the user can't see the guesses
    missedLetters = ""
    msg1 = "Guess the word! " +latestStr      #Setting the starting message
    msg2 = ""
    draw(count, msg1, msg2)
    
def play(event):
    newGame()
    
newGame()
canvas.focus_set()
canvas.bind("<Key>",play)       #making sure the user key inputs are set in the game
canvas.bind("<Key>",keyPressed)
window.mainloop()               #creating our window event
