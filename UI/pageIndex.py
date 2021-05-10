from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from UI import tabConvert,tabImportData,tabUpdateData
class Index(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.initUI()
    def initUI(self):
        #Tao thanh Tabbar
        tabControl=ttk.Notebook(self,width=900)
        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tab3 = Frame(tabControl)
        tabControl.add(tab1,text='Convert')
        tabControl.add(tab2,text='Load data')
        tabControl.add(tab3, text='Update data')
        tabControl.pack(expand=1,fill='both')
        #Frame noi dung
        tab_convert = tabConvert.Content(pr=tab1)
        tab_convert.pack(side=TOP)
        tab_load = tabImportData.Content(pr=tab2)
        tab_load.pack()
        tab_update = tabUpdateData.Content(pr=tab3)
        tab_update.pack()