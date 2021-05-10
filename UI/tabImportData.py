import time
from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT,BOTTOM,Checkbutton,W
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
import tkinter as tk
import threading
from tkinter.filedialog import askopenfilename
import logger
from models import model
from services import load_file, load_data
from controllers.var import *
lock = threading.Lock()


class Content(Frame):
    result_filein = None
    result_import = None


    def __init__(self, pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.initUI()
        self.filepath=''
        self.frame_show_list  = None

    def selectfile(self):

        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0, self.filepath)
        self.import_file_button['state'] = tk.NORMAL


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
        self.delimiteret.insert(0,',')
        self.delimiteret.pack(side=LEFT)
        self.reset_button = Button(frame1, text='Refresh',command=self.refresh)
        self.reset_button.pack(side=RIGHT,padx = 5)
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Chọn bảng")
        select_tablelb.pack(side=LEFT, fill=X, padx=8, pady=5)
        self.comboExample = Combobox(frame2, values=model.getListTables())
        self.comboExample.current(1)
        self.comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)
        frame3 = Frame(self.pr, width=800)
        frame3.pack(fill=X)
        self.import_file_button = Button(frame3, text='Nạp dữ liệu',command=self.click_import_data)
        self.import_file_button['state'] = tk.DISABLED
        self.import_file_button.pack(side=LEFT,padx=5)
        self.result_filein = Label(frame3, text="")
        self.result_filein.pack(side=LEFT, padx=5)
        self.result_import = Label(self.pr, text="")
        self.frame15 = Frame(self.pr, width=800)
        self.import_title = Label(self.frame15, text="Danh sách cột nhập vào", font=('Arial', 12, 'bold'))
        self.import_title.pack(fill=X, padx=50)
        self.enter_button = Button(self.pr, text="Thực hiện", command=self.enter)


    def click_import_data(self):
        self.enter_button['state']=tk.DISABLED
        if self.frame_show_list !=None:
            self.frame_show_list.destroy()
        self.frame_show_list = Frame(self.pr, width=800)
        self.list_column_show=[]
        self.delimiter = self.delimiteret.get()
        result=load_data.import_data(filepath=self.filepath, delimiter=self.delimiter,table_input=self.comboExample.get())
        if result==True:
            self.frame15.pack(fill=X, pady=10)
            self.list_column = load_data.get_list_column_import()
            self.frame_show_list.pack(fill=X, pady=30,padx = 50)
            self.checkbox_var=[]
            for i in range(0,len(self.list_column)):
                self.checkbox_var.append(tk.IntVar())
                self.list_column_show.append(Checkbutton(self.frame_show_list,text=self.list_column[i],variable=self.checkbox_var[i], onvalue=1, offvalue=0))
                self.checkbox_var[i].set(1)
                self.list_column_show[i].grid(row = i,column=0,sticky=W)
            #Content.result_label.config(text='')
            self.enter_button['state'] = tk.NORMAL
            self.enter_button.pack(side=BOTTOM)
            self.result_import.pack(side=BOTTOM)
        else:
            self.result_filein.config('Lỗi nạp file')


    def refresh(self):
        self.frame15.pack_forget()
        self.enter_button.pack_forget()
        self.frame_show_list.destroy()
        self.result_filein.config(text='')
        self.result_import.config(text='')
        self.import_file_button['state'] = tk.DISABLED
        self.filenameet.delete(0, "end")
        if self.frame_show_list !=None:
            self.frame_show_list.destroy()


    def enter(self):
        self.enter_button['state']=tk.DISABLED
        self.reset_button['state'] = tk.DISABLED
        self.import_file_button['state'] = tk.DISABLED
        list = []
        for i in range(0, len(self.list_column)):
            if self.checkbox_var[i].get() == 1:
                list.append(self.list_column[i])
        update_ui_thread = threading.Thread(target=self.update_ui)
        update_ui_thread.start()
        import_data_thread = threading.Thread(target=load_data.load_data,args=(list,))
        import_data_thread.start()


    def update_ui(self):
        while(G.i<G.len_data):
            self.result_import.config(text=str(int(G.i * 100 / (G.len_data-1))) + '%')
            time.sleep(5)
            print(int(G.i * 100 / G.len_data))
            if G.i ==(G.len_data-1):
                self.enter_button['state'] = tk.NORMAL
                self.reset_button['state'] = tk.NORMAL
                self.import_file_button['state'] = tk.NORMAL
                self.result_import.config(text="done")
                break
            if(G.result_import_data==False):
                self.result_import.config(text="Lỗi import dữ liệu!")
