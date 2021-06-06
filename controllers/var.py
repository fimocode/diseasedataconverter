from tkinter import font
import time
import datetime
import multiprocessing

from settings import number_of_process_import


manager = multiprocessing.Manager()

class G:
    i = 0
    j=0
    len_data=0
    time_start = datetime.datetime.utcnow()
    time_end = datetime.datetime.utcnow()
    record_start = 0
    record_end = 0

    process_index_data = manager.list(range(number_of_process_import))
    process_time_start = manager.list(range(number_of_process_import))
    process_time_end = manager.list(range(number_of_process_import))
    process_record_start = manager.list(range(number_of_process_import))
    process_record_end = manager.list(range(number_of_process_import))

    # is_done=[0] * number_of_process
    result_import_data = True
    result_update_data = True
    active  = True
    font_header1 = ('Arial', 15, 'bold')
    font_header2 = ('Arial', 12, 'bold')
    font_header3 = ('Arial', 11, 'bold')
    font_text = ('Arial', 12, 'bold')
