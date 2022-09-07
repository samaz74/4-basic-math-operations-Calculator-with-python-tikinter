import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *

#create window
window = Tk()
window.title("calculator test")
window.geometry("340x400")
window.resizable(width=False, height=False)
window.configure(bg="gray")
style= Style()
style.configure('W.TButton', font =
               ('calibri', 12, 'bold'),
                foreground = 'black')
photo_bg=PhotoImage(file=r'\cl.png') #add the backgound image
lable_bg=Label(window, image=photo_bg)
lable_bg.place(x=1, y=1)
#variable defining
num=tk.StringVar() #for entry value
ac=float(0)    #for resoults cal
op='' #for operator storing
exper1='' # for changing in entry data
con=0 # . controller


def cliker (number):  #enter the buttons data in entry
    global exper1
    global con
    if (number=='.'):
        if (con==0):
            con=1
            exper1 = exper1 + str(number)
            num.set(exper1)
        elif (con==1):
             con=1
    else:
        exper1=exper1+str(number)
        num.set(exper1)

def reset_entry (a): #reset the entry data
    global ac
    global num
    global exper1
    global con
    if (ac==0):
        ac=float(num.get())
    elif (a=='+'):
        ac=ac+float(num.get())
    elif (a == '-'):
        ac=ac-float(num.get())
    elif (a == '*'):
        ac=ac*float(num.get())
    elif (a == '/'):
        ac=ac/float(num.get())
    input_num1.delete(0, END)
    exper1=''
    num.set(exper1)
    con=0


def result (b):
    global ac
    global num
    global exper1
    global con
    if (b=='+'):
        ac=ac+float(num.get())
    elif (b == '-'):
        ac=ac-float(num.get())
    elif (b == '*'):
        ac=ac*float(num.get())
    elif (b == '/'):
        ac=ac/float(num.get())
    input_num1.delete(0, END)
    exper1=''
    num.set(ac)
    input_num1.setvar(str(ac))
    con=0


def operator(a): #save operator
    global op
    op=a
    reset_entry('op')

def clear_all (): #reset the callculator
    global num
    global exper1
    global ac
    input_num1.delete(0, END)
    exper1 = ''
    num.set(exper1)
    ac=0

def clear (): #only clear this entury data
    global num
    global exper1
    input_num1.delete(0, END)
    exper1=''
    num.set(exper1)


# create the button and Entry
#..................... Entry..........................#
input_num1= Entry(window,textvariable=num,font=('Century 20'))
input_num1.place (x=42, y=50, height=60, width=265)
#.................1 buttons row .......................#
but_f1=Button(window, text="clr",style='W.TButton',command=lambda: clear())
but_f1.place(x=40,y=150,height=30 , width=60)
but_f2=Button(window, text="clr all",style='W.TButton',command=lambda: clear_all ())
but_f2.place(x=110,y=150,height=30 , width=60)
#.................2 buttons row.......................#
but_0=Button(window, text="0",style='W.TButton',command=lambda: cliker ('0'))
but_0.place(x=40,y=342,height=38 , width=60)
but_n=Button(window, text=".",style='W.TButton',command=lambda: cliker ('.'))
but_n.place(x=110,y=342,height=38 , width=60)
but_plus=Button(window, text="+",style='W.TButton',command=lambda: operator('+'))
but_plus.place(x=180,y=342,height=38 , width=60)
but_equal=Button(window, text="=",style='W.TButton',command=lambda: result(op))
but_equal.place(x=250,y=342,height=38 , width=60)
#.................3 buttons row.......................#
but_1=Button(window, text="1",style='W.TButton',command=lambda: cliker ('1'))
but_1.place(x=40,y=292,height=38 , width=60)
but_2=Button(window, text="2",style='W.TButton',command=lambda: cliker ('2'))
but_2.place(x=110,y=292,height=38 , width=60)
but_3=Button(window, text="3",style='W.TButton',command=lambda: cliker ('3'))
but_3.place(x=180,y=292,height=38 , width=60)
but_mines=Button(window, text="-",style='W.TButton',command=lambda: operator('-'))
but_mines.place(x=250,y=292,height=38 , width=60)
#.................4 buttons row.......................#
but_4=Button(window, text="4",style='W.TButton',command=lambda: cliker ('4'))
but_4.place(x=40,y=242,height=38 , width=60)
but_5=Button(window, text="5",style='W.TButton',command=lambda: cliker ('5'))
but_5.place(x=110,y=242,height=38 , width=60)
but_6=Button(window, text="6",style='W.TButton',command=lambda: cliker ('6'))
but_6.place(x=180,y=242,height=38 , width=60)
but_stal=Button(window, text="*",style='W.TButton',command=lambda: operator('*'))
but_stal.place(x=250,y=242,height=38 , width=60)
#.................4 button row.......................#
but_7=Button(window, text="7",style='W.TButton',command=lambda: cliker ('7'))
but_7.place(x=40,y=192,height=38 , width=60)
but_8=Button(window, text="8",style='W.TButton',command=lambda: cliker ('8'))
but_8.place(x=110,y=192,height=38 , width=60)
but_9=Button(window, text="9",style='W.TButton',command=lambda: cliker ('9'))
but_9.place(x=180,y=192,height=38 , width=60)
but_tag=Button(window, text="/",style='W.TButton',command=lambda: operator("/"))
but_tag.place(x=250,y=192,height=38 , width=60)



window.mainloop()
