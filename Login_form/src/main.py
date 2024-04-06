#=======================Import===========================
from tkinter import *
#=======================Setting==========================
root = Tk()
root.title('Login form')
root.geometry('280x200')
root.resizable(width = False, height = False)
color = '#333333'
root.configure(bg = color)

#=========================Frame=========================
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
#=========================Wiget=========================
lable_1 = Label(Top_1, text = 'Log in', bg=color, fg='#eb3492')
lable_1.pack(side=LEFT, padx=5, pady=5)
lable_2 = Label(Top_2, text = 'Username:', bg=color, fg='#FFFFFF')
lable_2.pack(side=LEFT, padx=5, pady=5)
entry_2 = Entry(Top_2)
entry_2.pack(side=LEFT, padx=5, pady=5)
lable_3 = Label(Top_3, text = 'Password:', bg=color, fg='#FFFFFF')
lable_3.pack(side=LEFT, padx=5, pady=5)
entry_3 = Entry(Top_3, show='*')
entry_3.pack(side=LEFT, padx=5, pady=5)
btn_1 = Button(Top_4, text='Login', bg='#eb3492', fg='#FFFFFF', command= lambda:login())
btn_1.pack(side=LEFT, padx=5, pady=5)
lable_3 = Label(Top_5, width=25, bg= color, fg='#FFFFFF')
lable_3.pack(side=LEFT)

#=========================Function=============================
def login():
    user = 'ZahraFouladian'
    password = '123456'
    if entry_2.get() == user and entry_3.get() == password :
        lable_3['text'] = 'Successfully Logged in'
    else:
        lable_3['text'] = 'Invalid login'  

#=========================Run============================
root.mainloop()