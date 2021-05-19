import argparse
import time
from tkinter import Tk, X, LEFT, RIGHT,BOTTOM,Checkbutton,W
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
import tkinter as tk
import threading
from tkinter.filedialog import askopenfilename
from models import models
from services import load_data
from controlers.var import *
lock = threading.Lock()
class Content(Frame):
    reset_button = None
    result_filein = None
    result_import = None
    num_record_lb = None
    num_time_lb = None
    def __init__(self, pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.init_ui()
        self.filepath=''
        self.frame_show_list  = None
    def select_file(self):

        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0, self.filepath)
        self.import_file_button['state'] = tk.NORMAL
    def init_ui(self):
        title1 = Label(self.pr, text="Import data", font=G.font_header1)
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Select file", command=self.select_file)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiteret = Entry(frame1, width=5)
        self.delimiteret.insert(0,',')
        self.delimiteret.pack(side=LEFT)
        Content.reset_button = Button(frame1, text='Refresh',command=self.refresh)
        Content.reset_button.pack(side=RIGHT,padx = 5)
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Select table")
        select_tablelb.pack(side=LEFT, fill=X, padx=8, pady=5)
        self.comboExample = Combobox(frame2, values=models.get_list_tables())
        self.comboExample.current(1)
        self.comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)
        frame3 = Frame(self.pr, width=800)
        frame3.pack(fill=X)
        self.import_file_button = Button(frame3, text='Load file',command=self.click_import_data)
        self.import_file_button['state'] = tk.DISABLED
        self.import_file_button.pack(side=LEFT,padx=5)
        self.result_filein = Label(frame3, text="")
        self.result_filein.pack(side=LEFT, padx=5)
        self.frame14 = Frame(self.pr, width=800)
        id_start_lb =Label(self.frame14,text = "Starting from line",font=G.font_header3)
        self.id_start_et = Entry(self.frame14)
        self.id_start_et.insert(0,'0')
        id_start_lb.pack(side = LEFT,padx=40,pady=5)
        self.id_start_et.pack(side=LEFT)
        self.frame15 = Frame(self.pr, width=800)
        self.import_title = Label(self.frame15, text="Select input columns", font=G.font_header3)
        self.import_title.pack(fill=X, padx=40,pady=5)
    def click_import_data(self):
        try:
            self.refresh()
        except:
            pass
        if self.frame_show_list !=None:
            self.frame_show_list.destroy()
        self.frame_show_list = Frame(self.pr, width=800)
        self.list_column_show=[]
        self.delimiter = self.delimiteret.get()
        result= load_data.import_data(filepath=self.filepath, delimiter=self.delimiter, table_input=self.comboExample.get())
        if result==True:
            self.frame14.pack(fill=X,padx=10)
            self.frame15.pack(fill=X,padx=10)
            self.list_column = load_data.get_list_column_import()
            self.frame_show_list.pack(fill=X, pady=30,padx = 50)
            self.checkbox_var=[]
            for i in range(0,len(self.list_column)):
                self.checkbox_var.append(tk.IntVar())
                self.list_column_show.append(Checkbutton(self.frame_show_list,text=self.list_column[i],variable=self.checkbox_var[i], onvalue=1, offvalue=0))
                self.checkbox_var[i].set(1)
                self.list_column_show[i].grid(row = i,column=0,sticky=W)
            self.frame_action_button = Frame(self.pr)
            self.enter_button = Button(self.frame_action_button, text="Import", command=self.enter)
            self.enter_button['state'] = tk.NORMAL
            self.enter_button.pack(side=LEFT)
            self.cancel_button = Button(self.frame_action_button, text="Cancel", command=self.cancel)
            self.cancel_button.pack(side=LEFT)
            self.cancel_button['state']=tk.NORMAL
            self.frame_action_button.pack(side=BOTTOM)
            Content.result_import = Label(self.pr, text="")
            Content.num_record_lb = Label(self.pr, text='')
            Content.num_time_lb = Label(self.pr, text='')
            Content.result_import.pack(side=BOTTOM)
            Content.num_time_lb.pack(side=BOTTOM)
            Content.num_record_lb.pack(side=BOTTOM)
            Content.reset_button['state'] = tk.NORMAL
        else:
            self.result_filein.config('Error load file')
    def refresh(self):
        self.frame14.pack_forget()
        self.frame15.pack_forget()
        self.frame_action_button.destroy()
        Content.result_import.destroy()
        Content.num_record_lb.destroy()
        Content.num_time_lb.destroy()
        self.frame_show_list.destroy()
        self.result_filein.config(text='')
        self.import_file_button['state'] = tk.DISABLED
        #self.filenameet.delete(0, "end")
        if self.frame_show_list !=None:
            self.frame_show_list.destroy()
    def enter(self):
        G.active=True
        self.enter_button['state']=tk.DISABLED
        Content.reset_button['state'] = tk.DISABLED
        self.import_file_button['state'] = tk.DISABLED
        id_start = int(self.id_start_et.get())
        list = []
        for i in range(0, len(self.list_column)):
            if self.checkbox_var[i].get() == 1:
                list.append(self.list_column[i])
        import_data_thread = threading.Thread(target=load_data.load_data, args=(list, id_start))
        import_data_thread.start()
    def cancel(self):
        G.active = False
        Content.reset_button['state']=tk.NORMAL