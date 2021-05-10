import time
from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT,BOTTOM,Checkbutton,W
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
import tkinter as tk
import threading
from tkinter.filedialog import askopenfilename
from controler import models2
from controler import inoutFile,loadData
from controler.var import *
class Content(Frame):
    def __init__(self, pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.initUI()
        self.filepath=''
    def selectfile(self):
        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0, self.filepath)
        self.import_file_button['state'] = tk.NORMAL
    def initUI(self):
        title1 = Label(self.pr, text="Cập nhật dữ liệu", font=('Arial', 20, 'bold'))
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
        self.reset_button = Button(frame1, text='Refresh', command=self.refresh)
        self.reset_button.pack(side=RIGHT,padx = 5)
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Chọn bảng")
        select_tablelb.pack(side=LEFT, fill=X, padx=8, pady=5)
        self.comboExample = Combobox(frame2, values=models2.getListTables())
        self.comboExample.current(1)
        self.comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)
        frame3 = Frame(self.pr, width=800)
        frame3.pack(fill=X)
        self.import_file_button = Button(frame3, text='Nạp dữ liệu', command=self.click_import_data)
        self.import_file_button['state']=tk.DISABLED
        self.import_file_button.pack(side=LEFT, padx=5)
        self.result_filein = Label(frame3, text="")
        self.result_filein.pack(side=LEFT, padx=5)
        self.enter_button = Button(self.pr, text="Thực hiện", command=self.enter)

        self.result_update = Label(self.pr, text="")
        self.frame15 = Frame(self.pr, width=800)
        self.update_title = Label(self.frame15, text="Danh sách cột update dữ liệu", font=('Arial', 12, 'bold'))
        self.frame_show_content = None

    def click_import_data(self):
        self.enter_button['state']=tk.DISABLED
        #hien thi frame
        # frame chon khoa chinh
        if self.frame_show_content != None:
            self.frame_show_content.destroy()
        self.frame_show_content = Frame(self.pr, width=800)
        self.frame_selectkey = Frame(self.frame_show_content, width=800)
        self.frame_selectkey.grid(row=0, column=0)
        self.select_tablelb = Label(self.frame_selectkey, text="Chọn khóa chính")
        self.select_tablelb.pack(side=LEFT, fill=X, padx=8, pady=5)
        self.list_column = []
        self.combobox_key = Combobox(self.frame_selectkey, values=self.list_column)
        # self.combobox_key.current(1)
        self.combobox_key.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.frame_show_list = Frame(self.frame_show_content, width=800)
        self.frame_show_list.grid(row=1, column=0, pady=10, padx=50)
        self.update_title.pack(fill=X, padx=50)
        self.list_column_show=[]
        self.delimiter = self.delimiteret.get()
        result=loadData.import_data(filepath=self.filepath, delimiter=self.delimiter,table_input=self.comboExample.get())
        if(result==True):
            self.frame15.pack(fill=X, pady=10)
            self.list_column = loadData.get_list_column_import()
            self.combobox_key['values']=self.list_column
            self.frame_show_content.pack(fill=X, pady=15,padx=50)
            # chon khoa chinh

            self.checkbox_var = []
            for i in range(0,len(self.list_column)):
                self.checkbox_var.append(tk.IntVar())
                self.list_column_show.append(Checkbutton(self.frame_show_list,text=self.list_column[i],variable=self.checkbox_var[i], onvalue=1, offvalue=0))
                self.checkbox_var[i].set(0)
                self.list_column_show[i].grid(row = i,column=0,sticky=W)
            self.enter_button['state'] = tk.NORMAL
            self.enter_button.pack(side=BOTTOM)
            self.result_update.pack(side=BOTTOM)
        else:
            self.result_filein.config('Lỗi nạp file')
    def refresh(self):
        self.frame15.pack_forget()
        self.enter_button.pack_forget()
        if self.frame_show_content != None:
            self.frame_show_content.destroy()
        self.result_filein.config(text='')
        self.result_update.config(text='')
        self.import_file_button['state'] = tk.DISABLED
        self.filenameet.delete(0,"end")
    def enter(self):
        self.enter_button['state'] = tk.DISABLED
        self.reset_button['state'] = tk.DISABLED
        self.import_file_button['state'] = tk.DISABLED
        list = []
        for i in range(0, len(self.list_column)):
            if self.checkbox_var[i].get()==1:
                list.append(self.list_column[i])
        if(self.combobox_key.get() in list):
            list.remove(self.combobox_key.get())
        update_ui_thread = threading.Thread(target=self.update_ui)
        update_ui_thread.start()
        update_data_thread = threading.Thread(target=loadData.update_data, args=(self.combobox_key.get(),list,self.comboExample.get()))
        update_data_thread.start()
        #result = loadData.update_data(key = self.combobox_key.get(),list_column=list,table=self.comboExample.get())
    def update_ui(self):
        while(G.j<G.len_data):
            self.result_update.config(text=str(int(G.j * 100 / (G.len_data-1))) + '%')
            time.sleep(5)
            print(f"{G.j}-{G.len_data}")
            if G.j==(G.len_data-1):
                self.result_update.config(text="Done!")
                self.enter_button['state'] = tk.NORMAL
                self.reset_button['state'] = tk.NORMAL
                self.import_file_button['state'] = tk.NORMAL
                break
            if(G.result_update_data==False):
                self.result_update.config(text="Lỗi update dữ liệu!")