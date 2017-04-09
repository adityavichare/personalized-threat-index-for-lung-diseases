#!/usr/bin/python
import runme 

def calc():
    c=indinput.get()*8*0.001*60*8*dinput.get()
    ans.insert(0,c)

def clear():
    indEnt.delete(0,END)
    ans.delete(0,END)

from math import *
from tkinter import *

root=Tk()
root.title("8 hours Calculation")

root["bg"] = "dodgerblue"
#-------------------------------------------------------


indlbl=Label(root,text='Index',font='Calibri 15 bold ',bg='dodgerblue',fg='white' )

indinput=IntVar()
indEnt=Entry(root,textvariable=indinput)


dlbl=Label(root,text='Days',font='Calibri 15 bold ',bg='dodgerblue',fg='white' )

dinput=IntVar()
dEnt=Entry(root,textvariable=dinput)

anslbl=Label(root,text='Total Pollutant',font='Calibri 15 bold ',bg='dodgerblue',fg='white' )
ans=Entry(root)

metbt=Button(text="submit",command=calc,activebackground='orangered2',activeforeground='white',font='Arial 15 ',bg='firebrick1',fg='white')
clrbt=Button(text="clear",command=clear,activebackground='green3',activeforeground='white',font='Arial 15 ',bg='lime green',fg='white')


indlbl.grid(row=3,column=1,padx=6,pady=6)
indEnt.grid(row=3,column=2,padx=6,pady=6)

dlbl.grid(row=4,column=1,padx=6,pady=6)
dEnt.grid(row=4,column=2,padx=6,pady=6)


metbt.grid(row=6,column=1,padx=6,pady=6)
clrbt.grid(row=6,column=2,padx=6,pady=6)

anslbl.grid(row=7,column=1,padx=6,pady=6)
ans.grid(row=7,column=2,padx=6,pady=6)
