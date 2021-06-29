"""
Created on Thu Jun 17 11:18:43 2021

@author: abhishek.m
"""

import pymongo
from pymongo import MongoClient
from tkinter import *
from tkcalendar import * 
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.messagebox import askyesno
from tkinter import messagebox

import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  
import configparser


import configparser
parser = configparser.ConfigParser()
parser.add_section('Mongodb_compass')
parser.set('Mongodb_compass', 'host', 'localhost 127.0.0.1')
parser.set('Mongodb_compass', 'port', '27017')
parser.set('Mongodb_compass', ' Data base:', 'task')
parser.set('Mongodb_compass', ' collcetion :', 'ins1')
parser.add_section('Required')
parser.set('Required','imp',' download Mongodb compass verson 1.26.1')
parser.set('Required','create',' db has test')
parser.set('Required','create',' database name has task & collcetion name has ins1')
parser.set('Required', 'After completing above steps','Enjoy')
fp=open('test.ini','w')
parser.write(fp)
fp.close()


print("To start this program ,you need check test (configuration file) in dist folder ,otherwise ignore this message ")

myclient= pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=myclient["task"]
mycol=mydb["ins1"]
window=Tk()
window.title("FIDROX")
client = MongoClient('mongodb://localhost:27017/')




with myclient:
    
   
              for mydb in mycol.find().sort("_id", -1).limit(1):
                     
                      x1=('{0}'.format(mydb['_id']))
                      
                      print("previous _id value:-",x1)
                      
                                      
               
def fun():
     
         
       try:
                    
        
        
      
            for i in range((int(entry9.get()))): 
                    
                 
                    x2=int(entry9.get())
                    
                    x3=int(x1)-(int(x2)-1)
                    
                        
                  
                  
                    
                    mydict=[{"_id":int(x3)+(int(x2)+(i)),"person":entry2.get(),"emotion":entry4.get(),"date":cal.get_date(),"age":entry3.get(),"FrameNo":entry5.get(),"Gender":v.get()},
               
                         ]   
                    print(mydict)     
                    p=entry2.get()
        
                    print(p)
       
        
                   
               
            
                 
                  
                 
                    x=mycol.insert_many(mydict)
                   
            messagebox.showinfo("Hello", " Data inserted")  
       except NameError:
                            mydict=[{"_id":1,"person":"person 0","emotion":"happy","date":"3/3/21","age":"21","FrameNo":"212","Gender":"Male"},]
                            x31=mycol.insert_one(mydict)
                            messagebox.showinfo("Hello","You deleted all the data,Now default data will be added,close GUI to add next data")
        
           
       

            
def de():  
    
    
           
                 
                

            with myclient:
    
                
              for mydb in mycol.find().sort("_id",int(entryby.get())).limit(int(entry9.get())): #sort by user values 1 ,-1
                      
                      print(entryby.get())                    
                      x12=('{}'.format(mydb['_id']))
                      print("sorted  _id value:-",x12)
                    
                      for i in range((int(entry9.get()))): 
                          
                           x13=int(entry9.get())
                           x29=(int(x12))
                           
                           print("x29 value",x29)
                                                       
                           
                          
             
                     
                           x18=mycol.delete_many({"_id":int(x29)})
                                
                           x19=mycol.delete_many({"person":entry2.get()})
                           x20=mycol.delete_many({"emotion":entry4.get()})
                           x21=mycol.delete_many({"date":cal.get_date()})
                           x22=mycol.delete_many({"age":entry3.get()})
                           x23=mycol.delete_many({"FrameNo":entry5.get()})
                           x24=mycol.delete_many({"Gender":v.get()})
                           
                         
              messagebox.showinfo("Hello" ,"Deleted ")
             
                      
   
   
   
   


label1=Label(window,text="Insert/Delete ",relief="sunken",width=20,bg ='light slate blue', fg='#000000', bd=0,font=("arial 15 bold"))
label1.place(x=150,y=50)


sortby=Label(window,text="value must be:1or-1" ,width=20,font=("aSrial 10 bold")) 
sortby.place(x=80,y=145)
entryby=Entry(window,textvariable="st")
entryby.place(x=240,y=145)

st=StringVar()




label8=Label(window,text=" Num of Insert/Delete :-",width=20,font=("aSrial 10 bold"))
label8.place(x=80,y=185)
entry9=Entry(window,textvariable="ib")
entry9.place(x=240,y=190)
ib=IntVar()


label2=Label(window,text="person:-",width=20,font=("arial 10 bold"))
label2.place(x=80,y=240)
entry2=tk.Entry(window,textvariable='pvalue')
entry2.place(x=240,y=242)
pvalue=StringVar()

label3=Label(window,text="Age:-",width=20,font=("arial 10 bold"))
label3.place(x=80,y=280)
entry3=Entry(window,textvariable='ag')
entry3.place(x=240,y=282)
ag=StringVar()



label4=Label(window,text="Emotion:-",width=20,font=("arial 10 bold"))
label4.place(x=80,y=320)
entry4=Entry(window,textvariable='em')
entry4.place(x=240,y=322)
em=StringVar()



def get_date():
   label9.config(text=cal.get_date())
   
   
 


cal= Calendar(window, selectmode="day",year= 2021, month=6, day=10)
cal.pack(pady=20)
cal.place(x=400,y=200)
cal.bind("<<DateEntrySelected>>")
label9=Label(window,text="",width=20,font=("arial 10 bold"))
label9.place(x=210,y=360)
ttk.Button(window, text='DateEntry', command=get_date).place(x=120,y=360)


label5=Label(window,text="FrameNo:-",width=20,font=("arial 10 bold"))
label5.place(x=80,y=400) 
entry5=Entry(window,textvariable='fn')
entry5.place(x=240,y=402)
fn=StringVar()

v =StringVar()
v.set(0)

gender_label = Label(window, text="Gender:-",width=20,font=("arial 10 bold"))
gender_label.place(x=80,y=440)
data1=Entry(window,textvariable="ge")
male = Radiobutton(window, text="Male" ,value="Male",font=("arial 10 bold"),variable=v,command ="ShowChoice")
male.place(x=240,y=460)
female = Radiobutton(window, text="Female",value="Female",font=("arial 10 bold"),variable=v,command="ShowChoice")
female.place(x=300,y=460)
def ShowChoice():
    print(v.get())

ge=StringVar()


add=Button(window,height=1,width=10,text="ADD Data",bg="skyblue",command=fun)
add.place(x=360,y=500)


delete=Button(window,height=1,width=10,text="Delete Data",bg="red",command=de)
delete.place(x=360,y=550)



window.geometry('700x700')
window.mainloop()
