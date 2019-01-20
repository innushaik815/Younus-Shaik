from tkinter import *        ## // tkinter is the package which can help to create ui

import tkinter.messagebox         ## //message box is to create pop up message 

root = Tk()                            ##             // simple window
root.title("TIC TAC TOE")              ## // name of the window
bclick = True                                    ##  //helping variable


def tictac(buttons):                          ##//function of game 
    global bclick                              
    if buttons["text"] == " " and bclick == True:         
        buttons["text"] = "X"
        bclick = False




    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True






    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
        #print " --- x is winner"
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")
##//in this button 1 == button 2 == button3 == x means if all the button of player get equal then player x is winner and that will pop up with messagebox.showinfo
        exit()
    elif (button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")
    elif (button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")
    elif (button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")
    elif (button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")

    elif (button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")
    elif (button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
        tkinter.messagebox.showinfo("Player X", "Winner is X !!!")

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
                          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
                          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
                          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
                          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
                          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        tkinter.messagebox.showinfo("WINNER O", "PLAYER O WON THE GAME")
        exit()


button1 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button1))
button1.grid(row=0, column=0, sticky=S + N + E+ W)
button2 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button2))
button2.grid(row=0, column=1, sticky=S + N + E+ W)
button3 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button3))
button3.grid(row=0, column=2, sticky=S + N + E+ W)
button4 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button4))
button4.grid(row=1, column=0, sticky=S + N + E+ W)
button5 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button5))
button5.grid(row=1, column=1, sticky=S + N + E+ W)
button6 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button6))
button6.grid(row=1, column=2, sticky=S + N + E+ W)
button7 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button7))
button7.grid(row=2, column=0, sticky=S + N + E+ W)
button8 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button8))
button8.grid(row=2, column=1, sticky=S + N + E+ W)
button9 = Button(root, text=" ", font=('Arial 30 bold'), height=4, width=8, command=lambda: tictac(button9))
button9.grid(row=2, column=2, sticky=S + N + E+ W)

root.mainloop()
