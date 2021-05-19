import tkinter
from tkinter import Tk, X, LEFT, RIGHT, BOTTOM, TOP, W, NW
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from tkinter.filedialog import askopenfilename
from services import load_file
from models import models
from controlers.var import *
class Content(Frame):
    list_columns = None
    def __init__(self,pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.frame2=None
        self.list_column_frame4=None
        self.initUI()
    def select_file(self):
        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0,self.filepath)
        self.import_file_button['state'] = tkinter.NORMAL
    def click_import_file(self):
        self.convert_button['state'] = tkinter.DISABLED
        if self.frame2!=None:
            self.frame2.destroy()
        self.frame2 = Frame(self.frame_content_3, width=800)
        self.list_frame=[]
        self.list_columns_label=[]
        self.list_columns_entry=[]
        self.list_columns =[]
        self.delimiter = self.delimiteret.get()
        result= load_file.load_file(filepath=self.filepath, delimiter=self.delimiter)
        if result==True:
            self.list_columns = load_file.get_list_column()
            self.show_list_frame()
            self.convert_button['state'] = tkinter.NORMAL
            self.convert_button.pack(side=BOTTOM)
            self.result_convert.pack(side=BOTTOM)
            #Hien thi cac frame
            self.frame2.pack(fill=X, pady=15)
            self.conver_title.grid(row=0, column=0,padx=20)
            self.frame_content_2.grid(column=1, row=0, sticky=W,padx=20)
            self.frame_content_3.grid(column=0, row=1, sticky=W,padx=20)
            self.frame_content_4.grid(column=1, row=1, sticky=W,padx=20)
            self.frame_content.pack(side=LEFT)
        else:
            self.result_filein.config(text='Error import file!')
    def click_convert(self):

        self.list_columns_edit=[]
        for i in range(0,len(self.list_columns_entry)):
            self.list_columns_edit.append(self.list_columns_entry[i].get())
        result= load_file.convert(self.list_columns_edit)
        if result==True:
            self.result_convert.config(text='Successful!')
        else:
            self.result_convert.config(text='Error write file!')
    def initUI(self):
        title1 = Label(self.pr,text = "Convert data",font=G.font_header1)
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Select File", command=self.select_file)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiterlb = Label(frame1,text = "Delimiter")
        self.delimiterlb.pack(side = LEFT, padx=5)
        self.delimiteret = Entry(frame1,width = 5)
        self.delimiteret.pack(side=LEFT)
        self.import_file_button = Button(frame1,text='Load file',command=self.click_import_file)
        self.import_file_button['state'] = tkinter.DISABLED
        self.import_file_button.pack(side=LEFT,padx = 10)
        self.result_filein = Label(frame1, text="")
        self.result_filein.pack(side=LEFT, padx=5)
        reset_button = Button(frame1, text='Refresh', command=self.click_reset)
        reset_button.pack(side=RIGHT,padx=5)
        #frame content
        self.frame_content = Frame(self.pr, width=800,height=600)
        #self.frame_content.pack()
        #self.frame_content_1 = Frame(self.frame_content)
        self.frame_content_2 = Frame(self.frame_content)
        self.frame_content_3 = Frame(self.frame_content)
        self.frame_content_4 = Frame(self.frame_content)
        #self.frame_content_1.grid(column = 0, row =0, sticky=W)

        self.conver_title = Label(self.frame_content, text="Change columns name in file", font=G.font_header2)

        #Init ui frame RIGHT
        self.select_table_lb = Label(self.frame_content_2, text='See table infomation',font=G.font_header2)
        self.select_table_lb.pack(side=TOP)
        self.table_box = Combobox(self.frame_content_2, values=models.get_list_tables())
        self.table_box.current(1)
        self.table_box.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.select_table_button = Button(self.frame_content_2,text='See',command = self.click_select_table)
        self.select_table_button.pack(side=LEFT)
        #button convert
        self.result_convert = Label(self.pr, text="")
        self.convert_button = Button(self.pr,text="Convert",command=self.click_convert)

    def show_list_frame(self):
        for i in range(0, len(self.list_columns)):
            self.list_columns_label.append(Label(self.frame2, text=self.list_columns[i]))
            self.list_columns_entry.append(Entry(self.frame2))
            self.list_columns_entry[i].insert(0,self.list_columns[i])
            self.list_columns_label[i].grid(row=i,column=0, padx = 5, pady = 5)
            self.list_columns_entry[i].grid(row=i,column=1, padx = 5, pady = 5)
    def click_reset(self):
        self.frame_content.forget()
        self.frame2.pack_forget()
        self.conver_title.grid_forget()
        self.frame_content_2.grid_forget()
        self.frame_content_3.grid_forget()
        self.frame_content_4.grid_forget()
        self.result_convert.pack_forget()
        self.result_convert.config(text='')
        self.convert_button.pack_forget()
        self.conver_title.pack_forget()
        self.filenameet.delete(0, "end")
        self.import_file_button['state'] = tkinter.DISABLED
        if self.frame2!=None:
            self.frame2.destroy()
        if self.list_column_frame4!=None:
            self.list_column_frame4.destroy()
    def click_select_table(self):
        if self.list_column_frame4!=None:
            self.list_column_frame4.destroy()
        self.list_column_frame4 = Frame(self.frame_content_4)
        list_column = models.get_list_columns_in_table(self.table_box.get())
        list_column_lb=[]
        title_frame_4 = Label(self.list_column_frame4, text="List of columns", font=G.font_header2)
        title_frame_4.grid(row=0,column=0,pady=10,padx=30,sticky = NW)
        for i in range(0,len(list_column)):
            list_column_lb.append(Label(self.list_column_frame4, text = list_column[i]))
            list_column_lb[i].grid(row=i+1,column=0,padx = 30,sticky = NW)
        self.list_column_frame4.pack()