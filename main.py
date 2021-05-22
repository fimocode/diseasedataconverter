import tkinter as tk
import tkinter.font as tkFont
from UI import page_connectsql as cn
from UI import page_index
from models import database_connector as dbc
from controllers import var
try:
    root = tk.Tk()
    root.geometry("900x680")
    def_font = tk.font.nametofont("TkDefaultFont")
    def_font.config(size=10)
    root.minsize(900,680)
    root.title("IDB")
    frame_i1 = page_index.Index(master=root)
    framedn = cn.connect_sql(master=root, next=frame_i1)
    framedn.pack()
    def on_closing():
        var.G.active = False
        dbc.DbConnector.close()
        root.destroy()
        exit(0)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
except SystemExit:
    print('exit')
    exit(0)
except:
    print('end')
    exit(0)
