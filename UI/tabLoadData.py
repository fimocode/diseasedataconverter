import time
from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT,BOTTOM,Checkbutton
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
import tkinter as tk
import threading
from tkinter.filedialog import askopenfilename

import logger
from controler import models2
from controler import inout,loadData
from controler.var import *
lock = threading.Lock()
class Content(Frame):
    result_label = None
    result_label2 = None
    def __init__(self, pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.initUI()

    def selectfile(self):
        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0, self.filepath)
    def initUI(self):
        title1 = Label(self.pr, text="Import dữ liệu", font=('Arial', 20, 'bold'))
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Chọn File", command=self.selectfile)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiteret = Entry(frame1, width=5)
        self.delimiteret.pack(side=LEFT)
        reset_button = Button(frame1, text='Refresh',command=self.refresh)
        reset_button.pack(side=RIGHT)
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Chọn bảng")
        select_tablelb.pack(side=LEFT, fill=X, padx=8, pady=5)
        self.comboExample = Combobox(frame2, values=models2.getListTables())
        self.comboExample.current(1)
        self.comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)
        frame3 = Frame(self.pr, width=800)
        frame3.pack(fill=X)
        import_file_button = Button(frame3, text='Nạp dữ liệu',command=self.click_import_data)
        import_file_button.pack(side=LEFT,padx=5)
        Content.result_label = Label(frame3, text="")
        Content.result_label.pack(side=LEFT,padx=5)
        convert_button = Button(self.pr, text="Thực hiện",command=self.enter)
        convert_button.pack(side=BOTTOM)
        Content.result_label2 = Label(self.pr, text="...")
        Content.result_label2.pack(side=BOTTOM)
    def click_import_data(self):
        self.list_column_show=[]
        self.delimiter = self.delimiteret.get()
        loadData.import_data(filepath=self.filepath, delimiter=self.delimiter,table_input=self.comboExample.get(),label=Content.result_label)
        self.list_column = loadData.get_list_column_import()
        self.frame_show_list = Frame(self.pr, width=800)
        self.frame_show_list.pack(fill=X, pady=30)
        self.checkbox_var=[]
        for i in range(0,len(self.list_column)):
            self.checkbox_var.append(tk.IntVar())
            self.list_column_show.append(Checkbutton(self.frame_show_list,text=self.list_column[i],variable=self.checkbox_var[i], onvalue=1, offvalue=0))
            self.checkbox_var[i].set(1)
            self.list_column_show[i].grid(row = i,column=0)
        #Content.result_label.config(text='')
    def refresh(self):
        self.frame_show_list.destroy()
        Content.result_label.config(text='')
        Content.result_label2.config(text='')
    def enter(self):
        result = loadData.load_data(list=self.list_column,label=Content.result_label2)
    def update_ui(self):
        print(f'{G.i}+{G.len_data}')
        while(G.i<G.len_data):
            time.sleep(5)
            print(int(G.i * 100 / G.len_data))
            Content.result_label2.config(text=str(int(G.i * 100 / G.len_data)) + '%')
        if(G.i==G.len_data and G.is_done==True):
            Content.result_label2.config(text="Done!")
        print('done')
