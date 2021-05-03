from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from tkinter.filedialog import askopenfilename
from controler import models2
class Content(Frame):
    def __init__(self,pr, **kw):
        super().__init__(**kw)
        self.pr = pr
        self.initUI()
    def selectfile(self):
        Tk().withdraw()
        filename = askopenfilename()
        self.filenameet.insert(0,filename)
    def initUI(self):
        title1 = Label(self.pr, text="Thêm cột dữ liệu", font=('Arial', 20, 'bold'))
        title1.pack()
        frame1 = Frame(self.pr, width=800)
        frame1.pack(fill=X)
        select_file = Button(frame1, text="Chọn File", command=self.selectfile)
        select_file.pack(side=LEFT, fill=X, padx=5, pady=5)
        self.filenameet = Entry(frame1)
        self.filenameet.pack(side=LEFT)
        self.delimiteret = Entry(frame1, width=5)
        self.delimiteret.pack(side=LEFT)
        import_file_button = Button(frame1, text='Nạp file')
        import_file_button.pack(side=LEFT)
        reset_button = Button(frame1, text='Refresh')
        reset_button.pack(side=RIGHT)
        frame2 = Frame(self.pr, width=800)
        frame2.pack(fill=X)
        select_tablelb = Label(frame2, text="Chọn bảng")
        select_tablelb.pack(side=LEFT, fill=X, padx=5, pady=5)
        comboExample = Combobox(frame2, values=models2.getListTables())
        comboExample.current(1)
        comboExample.pack(side=LEFT, fill=X, padx=5, pady=5)