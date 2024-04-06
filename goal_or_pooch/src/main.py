
#====================Import========================
from tkinter import *
import random
import tkinter.messagebox
#====================Setting=======================
root = Tk()
root.title('Goal or Pooch')
root.geometry("280x270")
root.resizable(width = False, height = False)
color = '#f7ef05'
root.configure(bg = color)
#====================Frame=========================
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
#=======================Buttons========================
btn_1= Button(Top_2, text = 'Right hand', width = 10, highlightbackground = color, command= lambda: right_hand() )
btn_1.pack(side=LEFT, padx=5, pady=5)
btn_2= Button(Top_2, text = 'Left hand', width = 10, highlightbackground = color, command=lambda: left_hand() )
btn_2.pack(side=LEFT, padx=5, pady=5)

btn_4= Button(Top_4, text = '', width = 30, highlightbackground = color)
btn_4.pack(side=LEFT, padx=5, pady=5)
btn_5= Button(Top_6, text = '', width = 30, highlightbackground = color,)
btn_5.pack(side=LEFT, padx=5, pady=5)

btn_6= Button(Top_7, text = 'creator', width = 5, highlightbackground = color, command=lambda: creator() )
btn_6.pack(side=LEFT, padx=5, pady=5)
btn_7= Button(Top_7, text = 'clear', width = 5, highlightbackground = color, command=lambda: clear() )
btn_7.pack(side=LEFT, padx=5, pady=5)
#========================Function=========================
def creator():
    tkinter.messagebox.showinfo('CREATOR', 'This game has been create by zahra fouladian')

def right_hand():
    z = random.choice(['Goal','Pooch'])
    btn_4['text'] = z
    btn_5['text'] = 'You Win!' if z == 'Goal' else 'You Lose!'

 
def left_hand():
    z = random.choice(['Goal','Pooch'])
    btn_4['text'] = z
    btn_5['text'] = 'You Win!' if z == 'Goal' else 'You Lose!'
   
def clear():
    btn_4['text'] = ''
    btn_5['text'] = ''

#=======================Lable===========================
choose = Label(Top_1, text= 'Guess which hand???', bg=color)
choose.pack(side = LEFT, padx=5, pady=5)

computer_choise = Label(Top_3, text= 'Your guess is', bg=color)
computer_choise.pack(side = LEFT, padx=5, pady=5)

result = Label(Top_5, text= 'Result:', bg=color)
result.pack(side = LEFT, padx=5, pady=5)

#=========================Run==========================
root.mainloop()