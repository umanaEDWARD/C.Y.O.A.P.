# Choose.py
# by Brick Squad 
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you are going to choose a gun and you'll go in avendture. " + \
                        " You are gonna be sent to different area based on your gun" + \
                        "You are going to go threw many challenges and You may not surive.")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1. M8A1, 2. MSMC, 3. DSR50 or 4. HAMR." + \
                                     " Just input 1, 2, 3, or 4 to continue.")
    if choice == 1:
        choice1("M8A1")
    elif choice == 2:
        choice2("MSMC")
    elif choice == 3:
        choice3("DSR50")
    elif choice == 4:
        choice4("HAMR")
    else:
        intro()

################ EDWARD #####################
def choice1(M8A1):
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            " You train with the narkz." " You got jumped and sent to a care center."
                            "You chose wrong.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End", " You decide to go train wiht th N.O.V.A. goverment, when you are well trained you fight the seals and became a vetern."
                            "You chose ok.  THE END")
    else:
        choice1()


def choice2(MSMC):
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End", " You work with the Alien govermant they want to do tests on you, so you deicde to run far away and become a framer and live a happpy life ."
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End", " You go solo you trying to fight on your on the narkz caught you become a salve and you later on die."
                            "You chose ok.  THE END")
    else:
        choice2()

################ TJ #####################
def choice3():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ CODY #####################
def choice4():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()


################ Main #####################
intro()

root.destroy()
