from tkinter import font
import time
import datetime

class G:
    i = 0
    j=0
    len_data=0
    time_start=datetime.datetime.utcnow()
    time_end = datetime.datetime.utcnow()
    record_start=0
    record_end = 0
    is_done=False
    result_import_data = True
    result_update_data = True
    active  = True
    font_header1 = ('Arial', 15, 'bold')
    font_header2 = ('Arial', 12, 'bold')
    font_header3 = ('Arial', 11, 'bold')
    font_text = ('Arial', 12, 'bold')