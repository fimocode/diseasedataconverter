from models import database_connector as dc
import tkinter as tk
from tkinter import X
from tkinter.ttk import Frame, Button
class connect_sql(tk.Frame):
    def __init__(self,next, **kw):
        super().__init__(**kw)
        self.next = next
        self.init_ui()
    def init_ui(self):
        #hang 0
        frame0 = Frame(self)
        frame0.pack(fill=X)
        header_title1 = tk.Label(frame0,text = "Data Normalization Application",font=('Arial',18,'bold'),)
        header_title1.pack(pady=50)
        header_title2 = tk.Label(frame0,text = "Connect MYSQL",font=('Arial',15,'bold'),pady=20)
        header_title2.pack()
        #hang1
        frame_form = Frame(self)
        frame_form.pack()
        frame1 = Frame(frame_form)
        frame1.pack()
        hostlb = tk.Label(frame1, text="Host")
        hostlb.grid(row=0,column=0,padx=5,pady=5)
        self.hostet = tk.Entry(frame1)
        self.hostet.grid(row=0,column=1,padx=5,pady=5)
        #hang2
        portlb = tk.Label(frame1, text="Port")
        portlb.grid(row=1,column=0,padx=5,pady=5)
        self.portet = tk.Entry(frame1)
        self.portet.grid(row=1,column=1,padx=5,pady=5)
        #hang3
        usernamelb = tk.Label(frame1, text="Username")
        usernamelb.grid(row=2,column=0,padx=5,pady=5)
        self.usernameet = tk.Entry(frame1)
        self.usernameet.grid(row=2,column=1,padx=5,pady=5)
        #hang4
        passwordlb = tk.Label(frame1, text="Password")
        passwordlb.grid(row=3,column=0,padx=5,pady=5)
        self.passwordet = tk.Entry(frame1)
        self.passwordet.grid(row=3,column=1,padx=5,pady=5)
        #hang5
        dblb = tk.Label(frame1, text="Database")
        dblb.grid(row=4,column=0,padx=5,pady=5)
        self.dbet = tk.Entry(frame1)
        self.dbet.grid(row=4,column=1,padx=5,pady=5)
        # hang6
        frame6 = Frame(frame_form)
        frame6.pack(fill=X)
        self.rel = tk.Label(frame6, text="")
        self.rel.pack(padx=5, pady=5)
        # hang7
        frame7 = Frame(frame_form)
        frame7.pack(fill=X)
        self.submit = Button(frame7,text="Submit",command=self.connect)
        self.submit.pack()

    def connect(self):
        rel = dc.DbConnector.connectsql(host=self.hostet.get(),port=self.portet.get(),username=self.usernameet.get(),password=self.passwordet.get(),database=self.dbet.get())
        if rel == True:
            self.pack_forget()
            self.next.pack()
        else:
            self.rel.config(text="Conection failed!")
