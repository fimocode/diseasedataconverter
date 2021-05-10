import tkinter as tk
import os
from UI import pageConnectsql as cn
from UI import pageIndex
from controller import database_connector as dbc
root = tk.Tk()
root.geometry("900x600")
root.minsize(900,650)
root.title("AppName")
frame_i1 = pageIndex.Index(master=root)
framedn = cn.ConnectSQL(master=root,next=frame_i1)
framedn.pack()
def on_closing():
    root.destroy()
    dbc.DbConnector.close()
    exit(0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
