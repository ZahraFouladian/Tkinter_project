
#####################Import#############################
from tkinter import *
import random
import tkinter.messagebox
#####################Setting############################
root = Tk()
root.title('Rock-Paper-Scissor')
root.geometry("300x320")
root.resizable(width = False, height = False)
color = '#eb4034'
root.configure(bg = color)
####################Frame###########################
Top_1 = Frame(root, width=400, height=50, bg=color)
Top_1.pack(side='top')
Top_2 = Frame(root, width=400, height=50, bg=color)
Top_2.pack(side='top')
Top_3 = Frame(root, width=400, height=50, bg=color)
Top_3.pack(side='top')
Top_4 = Frame(root, width=400, height=50, bg=color)
Top_4.pack(side='top')
Top_5 = Frame(root, width=400, height=50, bg=color)
Top_5.pack(side='top')
Top_6 = Frame(root, width=400, height=50, bg=color)
Top_6.pack(side='top')
Top_7 = Frame(root, width=400, height=50, bg=color)
Top_7.pack(side='top')
Top_8 = Frame(root, width=400, height=50, bg=color)
Top_8.pack(side='top')
#####################Buttons########################
btn_1= Button(Top_1, text = 'Rock', width = 30, highlightbackground = color, command= lambda: rock() )
btn_1.pack(side=LEFT, padx=5, pady=5)
btn_2= Button(Top_2, text = 'Paper', width = 30, highlightbackground = color, command=lambda: paper() )
btn_2.pack(side=LEFT, padx=5, pady=5)
btn_3= Button(Top_3, text = 'Scissor', width = 30, highlightbackground = color, command=lambda: scissor() )
btn_3.pack(side=LEFT, padx=5, pady=5)

btn_4= Button(Top_5, text = '', width = 30, highlightbackground = color)
btn_4.pack(side=LEFT, padx=5, pady=5)
btn_5= Button(Top_7, text = '', width = 30, highlightbackground = color,)
btn_5.pack(side=LEFT, padx=5, pady=5)

btn_6= Button(Top_8, text = 'creator', width = 5, highlightbackground = color, command=lambda: creator() )
btn_6.pack(side=LEFT, padx=5, pady=5)
btn_7= Button(Top_8, text = 'clear', width = 5, highlightbackground = color, command=lambda: clear() )
btn_7.pack(side=LEFT, padx=5, pady=5)
#####################Function#######################
def creator():
    tkinter.messagebox.showinfo('CREATOR', 'This game has been create by zahra fouladian')

def rock():
    z = random.choice(['Rock','Paper','Scissor'])
    btn_4['text'] = z
    if z == 'Rock':
        btn_5['text'] = 'Tie'
    elif z == 'Paper':
        btn_5['text'] = 'You Lose!'
    elif z == 'Scissor':
        btn_5['text'] = 'You Win!'    

def scissor():
    z = random.choice(['Rock','Paper','Scissor'])
    btn_4['text'] = z
    if z == 'Paper':
        btn_5['text'] = 'You Win!'
    elif z == 'Scissor':
        btn_5['text'] = 'Tie!'
    elif z == 'Rock':
        btn_5['text'] = 'You Lose!' 

def paper():
    z = random.choice(['Rock','Paper','Scissor'])
    btn_4['text'] = z
    if z == 'Paper':
        btn_5['text'] = 'Tie'
    elif z == 'Scissor':
        btn_5['text'] = 'You Lose!'
    elif z == 'Rock':
        btn_5['text'] = 'You Win!'    

def clear():
    btn_4['text'] = ''
    btn_5['text'] = ''

#####################Lable##########################
computer_choise = Label(Top_4, text= 'Computer Move', bg=color)
computer_choise.pack(side = LEFT, padx=5, pady=5)

result = Label(Top_6, text= 'Result:', bg=color)
result.pack(side = LEFT, padx=5, pady=5)

#####################Run############################
root.mainloop()