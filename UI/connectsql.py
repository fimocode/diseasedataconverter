from controler import database_connector as dc
import tkinter as tk
from tkinter import X, LEFT, RIGHT
from tkinter.ttk import Frame, Button
class ConnectSQL(tk.Frame):
    def __init__(self,next, **kw):
        super().__init__(**kw)
        self.next = next
        self.initUI()
    def initUI(self):
        #hang 0
        frame0 = Frame(self)
        frame0.pack(fill=X)
        header_title1 = tk.Label(frame0,text = "ỨNG DỤNG CHUẨN HÓA DỮ LIỆU",font=('Arial',25,'bold'),)
        header_title1.pack()
        header_title11 = tk.Label(frame0,text = "cho việc giám sát dữ liệu dịch bệnh",font=('Arial',14,'bold'))
        header_title11.pack()
        header_title2 = tk.Label(frame0,text = "Kết mối MYSQL",font=('Arial',20,'bold'),pady=10)
        header_title2.pack()
        #hang1
        frame1 = Frame(self)
        frame1.pack(fill=X)
        hostlb = tk.Label(frame1, text="Host")
        hostlb.pack(side=LEFT,padx=5,pady=5)
        self.hostet = tk.Entry(frame1)
        self.hostet.pack(side=RIGHT,padx=5)
        #hang2
        frame2 = Frame(self)
        frame2.pack(fill=X)
        portlb = tk.Label(frame2, text="Port")
        portlb.pack(side=LEFT, padx=5, pady=5)
        self.portet = tk.Entry(frame2)
        self.portet.pack(side=RIGHT,padx=5)
        #hang3
        frame3 = Frame(self)
        frame3.pack(fill=X)
        usernamelb = tk.Label(frame3, text="Username")
        usernamelb.pack(side=LEFT, padx=5, pady=5)
        self.usernameet = tk.Entry(frame3)
        self.usernameet.pack(side=RIGHT,padx=5)
        #hang4
        frame4 = Frame(self)
        frame4.pack(fill=X)
        passwordlb = tk.Label(frame4, text="Password")
        passwordlb.pack(side=LEFT, padx=5, pady=5)
        self.passwordet = tk.Entry(frame4)
        self.passwordet.pack(side=RIGHT,padx=5)
        #hang5
        frame5 = Frame(self)
        frame5.pack(fill=X)
        dblb = tk.Label(frame5, text="Database")
        dblb.pack(side=LEFT, padx=5, pady=5)
        self.dbet = tk.Entry(frame5)
        self.dbet.pack(side=RIGHT,padx=5)
        # hang6
        frame6 = Frame(self)
        frame6.pack(fill=X)
        self.rel = tk.Label(frame6, text="")
        self.rel.pack(side=LEFT, padx=5, pady=5)
        # hang7
        frame7 = Frame(self)
        frame7.pack(fill=X)
        self.submit = Button(frame7,text="Submit",command=self.connect)
        self.submit.pack(side=LEFT)
    def connect(self):
        rel = dc.DbConnector.connectsql(host=self.hostet.get(),port=self.portet.get(),username=self.usernameet.get(),password=self.passwordet.get(),database=self.dbet.get())
        print(rel)
        if rel == True:
            self.pack_forget()
            self.next.pack()
        else:
            self.rel.config(text="False")
