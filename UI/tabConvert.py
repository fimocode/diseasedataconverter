from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT,BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from tkinter.filedialog import askopenfilename
from controler import models2
from controler import inout
class Content(Frame):
    list_columns = None
    def __init__(self,pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.initUI()
    def selectfile(self):
        Tk().withdraw()
        self.filepath = askopenfilename()
        self.filenameet.insert(0,self.filepath)
    def click_import_file(self):
        self.list_frame=[]
        self.list_columns_label=[]
        self.list_columns_entry=[]
        self.delimiter = self.delimiteret.get()
        inout.load_file(filepath=self.filepath, delimiter=self.delimiter)
        self.frame2 = Frame(self.pr, width=800)
        self.frame2.pack(fill=X,pady=30)
        self.result_label = Label(self.pr,text="")
        self.result_label.pack()
        self.list_columns = inout.get_list_column()
        self.show_list_frame()
    def click_convert(self):
        self.result_label.config(text='Đang...')
        self.list_columns_edit=[]
        for i in range(0,len(self.list_columns_entry)):
            self.list_columns_edit.append(self.list_columns_entry[i].get())
        result=inout.convert(self.list_columns_edit)
        if result==True:
            self.result_label.config(text='Thành công!')
        else:
            self.result_label.config(text='Lỗi ghi file!')
    def initUI(self):
        title1 = Label(self.pr,text = "Convert dữ liệu",font=('Arial',20,'bold'))
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Chọn File", command=self.selectfile)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiteret = Entry(frame1,width = 5)
        self.delimiteret.pack(side=LEFT)
        import_file_button = Button(frame1,text='Nạp file',command=self.click_import_file)
        import_file_button.pack(side=LEFT)
        reset_button = Button(frame1, text='Refresh', command=self.click_reset)
        reset_button.pack(side=RIGHT)
        """
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Chọn File")
        select_tablelb.pack(side=LEFT, fill=X, padx=5, pady=5)
        comboExample = Combobox(frame2, values=models2.getListTables())
        comboExample.current(1)
        comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)
        """

        convert_button = Button(self.pr,text="Convert",command=self.click_convert)
        convert_button.pack(side=BOTTOM)
    def show_list_frame(self):
        for i in range(0, len(self.list_columns)):
            self.list_columns_label.append(Label(self.frame2, text=self.list_columns[i]))
            self.list_columns_entry.append(Entry(self.frame2))
            self.list_columns_entry[i].insert(0,self.list_columns[i])
            self.list_columns_label[i].grid(row=i,column=0, padx = 5, pady = 5)
            self.list_columns_entry[i].grid(row=i,column=1, padx = 5, pady = 5)
    def click_reset(self):
        self.frame2.destroy()
