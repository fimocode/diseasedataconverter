import tkinter
from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT,BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from tkinter.filedialog import askopenfilename
from controler import models2
from controler import inoutFile
class Content(Frame):
    list_columns = None
    def __init__(self,pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.frame2=None
        self.initUI()
    def selectfile(self):
        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0,self.filepath)
        self.import_file_button['state'] = tkinter.NORMAL
    def click_import_file(self):
        self.convert_button['state'] = tkinter.DISABLED
        if self.frame2!=None:
            self.frame2.destroy()
        self.frame2 = Frame(self.pr, width=800)
        self.list_frame=[]
        self.list_columns_label=[]
        self.list_columns_entry=[]
        self.list_columns =[]
        self.delimiter = self.delimiteret.get()
        result=inoutFile.load_file(filepath=self.filepath, delimiter=self.delimiter)
        if result==True:
            self.list_columns = inoutFile.get_list_column()
            self.show_list_frame()
            self.convert_button['state'] = tkinter.NORMAL
            self.convert_button.pack(side=BOTTOM)
            self.result_convert.pack(side=BOTTOM)
            self.frame15.pack(fill=X, pady=10)
            self.frame2.pack(fill=X, pady=15)
        else:
            self.result_filein.config(text='Lỗi nạp file!')
    def click_convert(self):

        self.list_columns_edit=[]
        for i in range(0,len(self.list_columns_entry)):
            self.list_columns_edit.append(self.list_columns_entry[i].get())
        result=inoutFile.convert(self.list_columns_edit)
        if result==True:
            self.result_convert.config(text='Thành công!')
        else:
            self.result_convert.config(text='Lỗi ghi file!')
    def initUI(self):
        title1 = Label(self.pr,text = "Convert dữ liệu",font=('Arial',20,'bold'))
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Chọn File", command=self.selectfile)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiterlb = Label(frame1,text = "Dấu phân cách")
        self.delimiterlb.pack(side = LEFT, padx=5)
        self.delimiteret = Entry(frame1,width = 5)
        self.delimiteret.pack(side=LEFT)
        self.import_file_button = Button(frame1,text='Nạp file',command=self.click_import_file)
        self.import_file_button['state'] = tkinter.DISABLED
        self.import_file_button.pack(side=LEFT,padx = 10)
        self.result_filein = Label(frame1, text="")
        self.result_filein.pack(side=LEFT, padx=5)
        reset_button = Button(frame1, text='Refresh', command=self.click_reset)
        reset_button.pack(side=RIGHT,padx=5)
        #
        self.frame15 = Frame(self.pr, width=800)

        self.conver_title = Label(self.frame15, text="Đổi tên các cột trong file", font=('Arial', 12, 'bold'))
        self.conver_title.pack(fill=X, padx=50)
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
        self.frame15.pack_forget()
        self.frame2.pack_forget()
        self.result_convert.pack_forget()
        self.result_convert.config(text='')
        self.convert_button.pack_forget()
        self.conver_title.pack_forget()
        self.filenameet.delete(0, "end")
        self.import_file_button['state'] = tkinter.DISABLED
        if self.frame2!=None:
            self.frame2.destroy()
