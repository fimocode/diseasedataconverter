from tkinter import Tk,ttk, Text, TOP, BOTH, X, N, LEFT,StringVar,OptionMenu,RIGHT
from tkinter.ttk import Frame, Label, Entry, Button, Combobox
from UI import tab_import_data,tab_update_data,tab_convert_data
class Index(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.init_ui()
    def init_ui(self):
        #Tao thanh Tabbar
        tabControl=ttk.Notebook(self,width=900)
        tab1 = Frame(tabControl)
        tab2 = Frame(tabControl)
        tab3 = Frame(tabControl)
        tabControl.add(tab1,text='Convert')
        tabControl.add(tab2,text='Import data')
        tabControl.add(tab3, text='Update data')
        tabControl.pack(expand=1,fill='both')
        #Frame noi dung
        tab_convert = tab_convert_data.Content(pr=tab1)
        tab_convert.pack(side=TOP)
        tab_load = tab_import_data.Content(pr=tab2)
        tab_load.pack()
        tab_update = tab_update_data.Content(pr=tab3)
        tab_update.pack()