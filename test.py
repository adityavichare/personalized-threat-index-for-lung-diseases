from math import *
from tkinter import *

root=Tk()
root.title("Prediction Mechanism")

root["bg"] = "dodgerblue"
#-----------------------Age--------------------------------


albl=Label(root,text='AGE',font='Calibri 15 bold ',bg='dodgerblue',fg='white' )
amenu= Menubutton ( root,text="Select Age ˅",activebackground='orange',activeforeground='white',font='Arial 12 ',bg='darkorange',fg='white' )

amenu.menu  =  Menu ( amenu, tearoff = 0 )
amenu["menu"]  =  amenu.menu
    
ageVar  = IntVar()
 

amenu.menu.add_radiobutton ( label="15-19",
                          variable=ageVar,value=1 )
amenu.menu.add_radiobutton ( label="20-24",
                          variable=ageVar,value=2 )
amenu.menu.add_radiobutton ( label="25-29",
                          variable=ageVar,value=3)
amenu.menu.add_radiobutton ( label="30-34",
                          variable=ageVar,value=4 )
amenu.menu.add_radiobutton ( label="35-39",
                          variable=ageVar,value=5 )
amenu.menu.add_radiobutton ( label="40-44",
                          variable=ageVar,value=6 )
amenu.menu.add_radiobutton ( label="45-49",
                          variable=ageVar,value=7 )
amenu.menu.add_radiobutton ( label="50-54",
                          variable=ageVar,value=8 )
amenu.menu.add_radiobutton ( label="55-60",
                          variable=ageVar,value=9 )
amenu.menu.add_radiobutton ( label="60-",
                          variable=ageVar,value=10 )


#---------------------------Work----------------------------

citlbl=Label(root,text='WORK',font='Calibri 15 bold ',bg='dodgerblue',fg='white' )

cityLbl=Label(root,text='CITY',font='Calibri 15 bold ',bg='dodgerblue',fg='white')
input1=()
cityEnt=Entry(root,textvariable=input1)



plbl=Label(root,text='Work Place/locality',font='Arial 12 ',bg='dodgerblue',fg='white')

pEnt=Entry(root)
pmenu= Menubutton ( root,text="Work Hours",activebackground='orange',activeforeground='white',bg='darkorange',fg='white' )

pmenu.menu  =  Menu ( pmenu, tearoff = 0 )
pmenu["menu"]  =  pmenu.menu
    
pVar  = IntVar()


pmenu.menu.add_radiobutton ( label="1",
                          variable=pVar,value=1 )
pmenu.menu.add_radiobutton ( label="2",
                          variable=pVar,value=2 )
pmenu.menu.add_radiobutton ( label="3",
                          variable=pVar,value=3 )
pmenu.menu.add_radiobutton ( label="4",
                          variable=pVar,value=4 )
pmenu.menu.add_radiobutton ( label="5",
                          variable=pVar,value=5 )
pmenu.menu.add_radiobutton ( label="6",
                          variable=pVar,value=6)
pmenu.menu.add_radiobutton ( label="7",
                          variable=pVar,value=7 )
pmenu.menu.add_radiobutton ( label="8",
                          variable=pVar,value=8 )
pmenu.menu.add_radiobutton ( label="9",
                          variable=pVar,value=9 )
pmenu.menu.add_radiobutton ( label="10",
                          variable=pVar,value=10 )


#------------------------------Commuting-------------------------
clbl=Label(root,text='COMMUTING',font='Calibri 15 bold  ',bg='dodgerblue',fg='white')

cEnt=Entry(root)
cmenu= Menubutton ( root,text="Total commuting Hours ↓",activebackground='orange',activeforeground='white',bg='darkorange',fg='white' )

cmenu.menu  =  Menu ( cmenu, tearoff = 0 )
cmenu["menu"]  =  cmenu.menu
   
cVar  = IntVar()

cmenu.menu.add_radiobutton ( label="0.5",activebackground='lime green',activeforeground='white' ,
                          variable=cVar,value=1 )
cmenu.menu.add_radiobutton ( label="1",activebackground='lime green',activeforeground='white' ,
                          variable=cVar,value=2 )
cmenu.menu.add_radiobutton ( label="1.5",
                          variable=cVar,value=3 )
cmenu.menu.add_radiobutton ( label="2",
                          variable=cVar,value=4 )
cmenu.menu.add_radiobutton ( label="2.5",
                          variable=cVar,value=5 )
cmenu.menu.add_radiobutton ( label="3",
                          variable=cVar,value=6)
cmenu.menu.add_radiobutton ( label="3.5",
                          variable=cVar,value=7 )
cmenu.menu.add_radiobutton ( label="4",
                          variable=cVar,value=8 )
cmenu.menu.add_radiobutton ( label="4.5",
                          variable=cVar,value=9 )
cmenu.menu.add_radiobutton ( label="5",
                          variable=cVar,value=10 )



vmenu= Menubutton ( root,text="commuting type",relief=RAISED,activebackground='orange',activeforeground='white' ,bg='darkorange',fg='white')
vmenu.menu  =  Menu ( vmenu, tearoff = 0 )
vmenu["menu"]  =  vmenu.menu
  
vVar  = IntVar()


vmenu.menu.add_radiobutton ( label="Car",activebackground='lime green',activeforeground='white' ,
                          variable=vVar,value=0 )
vmenu.menu.add_radiobutton ( label="Rail",activebackground='green yellow',activeforeground='white' ,
                          variable=vVar,value=2 )
vmenu.menu.add_radiobutton ( label="Bus",activebackground='yellow2',activeforeground='white' ,
                          variable=vVar,value=4 )
vmenu.menu.add_radiobutton ( label="AutoRickshaw",activebackground='goldenrod1',activeforeground='white' ,
                          variable=vVar,value=6 )
vmenu.menu.add_radiobutton ( label="walk",activebackground='indianred1',activeforeground='white' ,
                          variable=vVar,value=8 )
vmenu.menu.add_radiobutton ( label="Bike",activebackground='brown1',activeforeground='white' ,
                          variable=vVar,value=10 )





#-------------------------------Home------------------------
homplabl=Label(root,text='Home place/locality',font='Arial 12 ',bg='dodgerblue',fg='white')
hlbl=Label(root,text='Home',font='Calibri 15 bold  ',bg='dodgerblue',fg='white')

hEnt=Entry(root)


tlbl=Label(root,text='Time (in days)',font='Arial 12 ',bg='dodgerblue',fg='white')
tEnt=Entry(root)

pdaylbl=Label(root,text='Work',font='Arial 12 bold',bg='dodgerblue',fg='white')
avglbl=Label(root,text='Commuting',font='Arial 12 bold',bg='dodgerblue',fg='white')


met1lbl=Label(root,text='PM 2.5',font='Arial 12 bold',bg='dodgerblue',fg='white')
met2lbl=Label(root,text='PM 10',font='Arial 12 bold',bg='dodgerblue',fg='white')
met3lbl=Label(root,text='NO 2',font='Arial 12 bold',bg='dodgerblue',fg='white')
met4lbl=Label(root,text='SO 2',font='Arial 12 bold',bg='dodgerblue',fg='white')

thrlbl=Label(root,text='Threat Level',font='Arial 15 bold',bg='dodgerblue',fg='gold')
#-----------------------------databse connection--------------------------

from mysql.connector import (connection)
db=connection.MySQLConnection(host='127.0.0.1',port=3306,user='root',passwd='manisha',db='copd')

print('Connected')

cursor=db.cursor()
from decimal import *



def meter():
    x=pEnt.get()
    y=int(tEnt.get())
    z=cityEnt.get()
#work
    try:
    
        a1="select PM2_5 from city where loc_name = '%s' "%x
        zx=cursor.execute(a1)
        result1=cursor.fetchone()
        sx1=result1[0] * pVar.get()* 0.001*480*y
        met1Ent.insert(0,sx1)

    except TypeError:
        result1[0]=1
        met1Ent.insert(0,'NA')
    try:
    
        a2= "select PM10 from city where loc_name = '%s' "%x
        cursor.execute(a2)
        result2=cursor.fetchone()
        sx2=result2[0] * pVar.get()*0.001*480*y
        met2Ent.insert(0,sx2)
    except TypeError:
        result2[0]=1
        met2Ent.insert(0,'NA')
        
    try:        
        a3= "select NO2 from city where loc_name = '%s' "%x
        cursor.execute(a3)
        result3=cursor.fetchone()
        sx3=result3[0] * pVar.get()*0.001*480*y
        met3Ent.insert(0,sx3)
    except TypeError:
        result3[0]=1
        met3Ent.insert(0,'NA')
        
    try:
        a4= "select SO2 from city where loc_name = '%s' "%x
        cursor.execute(a4)
        result4=cursor.fetchone()
        sx4=result4[0] * pVar.get()*0.001*480*y
        met4Ent.insert(0,sx4)
        
    except TypeError:
        result4=1
        met4Ent.insert(0,'NA')
        
    #---------------------------------------------
#this if else statement is for for car and other trans 
    vVarval=vVar.get()
    vval=0 #if trans=car 
    if  vVarval == 0:
        vval=0    
    else:   #else unity
        vval=1
#---------------------trans---------------
    try:    
        a1a="select avg(PM2_5) from city where city_name ='%s' "%z
        cursor.execute(a1a)
        result1a=cursor.fetchone()
        sx1a=int(result1a[0]) * cVar.get()* 0.001 * 480 * y * vval
        met5Ent.insert(0,sx1a)
    except TypeError:
        result1a[0]=1
    try:    
        a2a= "select avg(PM10) from city where city_name = '%s' "%z
        cursor.execute(a2a)
        result2a=cursor.fetchone()
        sx2a=int(result2a[0]) *  cVar.get()* 0.001 * 480 * y * vval
        met6Ent.insert(0,sx2a)
    except TypeError:
        result2a[0]=1
    try:    
        a3a= "select avg(NO2) from city where city_name = '%s' "%z
        cursor.execute(a3a)
        result3a=cursor.fetchone()
        sx3a=int(result3a[0]) *  cVar.get() * 0.001 * 480 * y * vval
        met7Ent.insert(0,sx3a)
    except TypeError:
        result3a[0]=1
    
    try:
        a4a= "select avg(SO2) from city where city_name = '%s' "%z
        cursor.execute(a4a)
        result4a=cursor.fetchone()
        sx4a=int(result4a[0])* cVar.get()*0.001*480*y*vval
        met8Ent.insert(0,sx4a)
    except TypeError:
        result4a=1
        met8Ent.insert(0,'NA')    

    
    #-------------Home ----------------------------------------
    xh=hEnt.get()

    try:
        a1h="select PM2_5 from city where loc_name ='%s' "%xh
        cursor.execute(a1h)
        result1h=cursor.fetchone()
        a1h=float(result1h[0])
    except TypeError:
        result4a[0]=1    

    try:   
        a2h= "select PM10 from city where loc_name = '%s' "%xh
        cursor.execute(a2h)
        result2h=cursor.fetchone()
        a2h=float(result1h[0])
    except TypeError:
        result4a[0]=1    

    try:   
        a3h= "select NO2 from city where loc_name = '%s' "%xh
        cursor.execute(a3h)
        result3h=cursor.fetchone()
        a3h=float(result1h[0])
    except TypeError:
        result4a[0]=1    

    try:   
        a4h= "select SO2 from city where loc_name = '%s' "%xh
        cursor.execute(a4)
        result4h=cursor.fetchone()
        a4h=float(result1h[0])
    except TypeError:
        result4a[0]=1
   
     
  
    #Threat formulation--------------------------------------------------
    if (result1[0]>250 or result2[0]>90 or result3[0]>180 or result4>380)or(result1a[0]>250 or result2a[0]>90 or result3a[0]>180 or result4a>380)or(result1h[0]>250 or result2h[0]>90 or result3h[0]>180 or result4h[0]>380):
        Aqivar=1
    elif (result1[0]<51 and result2[0]<30 and result3[0]<40 and result4[0]<40)and(result1a[0]<51 and result2a[0]<30 and result3a[0]<40 and result4a<40)and(result1h[0]<51 and result2h[0]<30 and result3h[0]<40 and result4h[0]<40):
        Aqivar=0
    else:
        Aqivar=0.5    
     
     




               #-----
        
    den= ((ageVar.get()+cVar.get()+ vVar.get()+pVar.get())/4)*Aqivar

    if (den <4)and(den >=0) :
        denEnt=Entry(root,bg='green2',fg='white')
        denEnt.grid(row=20,column=2)
        denEnt.insert(0,den)
    
    elif (den < 7)and(den >=4):
        denEnt=Entry(root,bg='darkorange',fg='white')
        denEnt.grid(row=20,column=2)
        denEnt.insert(0,den)
        
    else:
        denEnt=Entry(root,bg='red2',fg='white')
        denEnt.grid(row=20,column=2)
        denEnt.insert(0,den)
    #-------------------------clearing screen------------------------------------------------
        
    
    
def clear():
    met1.delete(0,END)
    met2.delete(0,END)
    met3.delete(0,END)
    met4.delete(0,END)
    met1a.delete(0,END)
    met2a.delete(0,END)
    met3a.delete(0,END)
    met4a.delete(0,END)
    
    
    met1Ent.delete(0,END)
    met2Ent.delete(0,END)
    met3Ent.delete(0,END)
    met4Ent.delete(0,END)
    met5Ent.delete(0,END)
    met6Ent.delete(0,END)
    met7Ent.delete(0,END)
    met8Ent.delete(0,END)

    met1h.delete(0,END)
    met2h.delete(0,END)
    met3h.delete(0,END)
    met4h.delete(0,END)

    

    
#-----------------------------------------

met1=Entry(root)
met2=Entry(root)
met3=Entry(root)
met4=Entry(root)
met1a=Entry(root)
met2a=Entry(root)
met3a=Entry(root)
met4a=Entry(root)


met1Ent=Entry(root)
met2Ent=Entry(root)
met3Ent=Entry(root)
met4Ent=Entry(root)

met5Ent=Entry(root)
met6Ent=Entry(root)
met7Ent=Entry(root)
met8Ent=Entry(root)

met1h=Entry(root)
met2h=Entry(root)
met3h=Entry(root)
met4h=Entry(root)




metbt=Button(text="submit",command=meter,activebackground='orangered2',activeforeground='white',font='Arial 15 ',bg='firebrick1',fg='white')
clrbt=Button(text="Clear",command=clear,activebackground='green3',activeforeground='white',font='Arial 15 ',bg='lime green',fg='white')


#-----------------------------griding and padding--------------------------
albl.grid(row=3,column=1,padx=6,pady=6)
amenu.grid(row=3,column=2,padx=6,pady=6)

cityLbl.grid(row=4,column=1,padx=6,pady=6)
cityEnt.grid(row=4,column=2,padx=6,pady=6)



citlbl.grid(row=7,column=1,padx=6,pady=6)
plbl.grid(row=7,column=2,padx=6,pady=6)
pEnt.grid(row=7,column=3,padx=6,pady=6)
pmenu.grid(row=8,column=2,padx=6,pady=6)

clbl.grid(row=9,column=1,padx=6,pady=6)
cmenu.grid(row=9,column=2,padx=6,pady=6)
vmenu.grid(row=9,column=3,padx=6,pady=6)
hlbl.grid(row=11,column=1,padx=6,pady=6)
homplabl.grid(row=11,column=2,padx=6,pady=6)
hEnt.grid(row=11,column=3,padx=6,pady=6)

tlbl.grid(row=12,column=1,padx=6,pady=6)
tEnt.grid(row=12,column=2,padx=6,pady=6)

metbt.grid(row=13,column=1,padx=6,pady=6)
clrbt.grid(row=13,column=2,padx=6,pady=6)

pdaylbl.grid(row=15,column=2,padx=6,pady=6)
avglbl.grid(row=15,column=3,padx=6,pady=6)

met1lbl.grid(row=16,column=1,padx=6,pady=6)
met2lbl.grid(row=17,column=1,padx=6,pady=6)
met3lbl.grid(row=18,column=1,padx=6,pady=6)
met4lbl.grid(row=19,column=1,padx=6,pady=6)

met1Ent.grid(row=16,column=2,padx=6,pady=6)
met2Ent.grid(row=17,column=2,padx=6,pady=6)
met3Ent.grid(row=18,column=2,padx=6,pady=6)
met4Ent.grid(row=19,column=2,padx=6,pady=6)

met5Ent.grid(row=16,column=3,padx=6,pady=6)
met6Ent.grid(row=17,column=3,padx=6,pady=6)
met7Ent.grid(row=18,column=3,padx=6,pady=6)
met8Ent.grid(row=19,column=3,padx=6,pady=6)

thrlbl.grid(row=20,column=1,padx=6,pady=6)

root.mainloop()

