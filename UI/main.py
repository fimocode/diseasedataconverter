import tkinter as tk
from UI import connectsql as cn
from UI import index
from controler import database_connector as dbc
root = tk.Tk()
root.geometry("900x600")
root.minsize(900,600)
root.title("AppName")
frame_i1 = index.Index(master=root)
framedn = cn.ConnectSQL(master=root,next=frame_i1)
framedn.pack()
def on_closing():
    root.destroy()
    dbc.DbConnector.close()
    exit(0)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
