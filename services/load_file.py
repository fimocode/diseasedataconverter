import pandas as pd
data=None
to_filepath=None
filepath_info  = None
def load_file(filepath,delimiter):
    try:
        global data
        global to_filepath
        global filepath_info
        filepath_info = filepath.split(".")
        to_filepath = filepath_info[0]+'_cv.csv'
        data = pd.read_csv(filepath,delimiter= delimiter,engine='python')
        return True
    except:
        return False
def get_list_column():
    return list(data.columns.values)
def convert(list):
    global data
    try:
        data.columns= list
        data.to_csv(to_filepath,index=False,na_rep='NULL')
        return True
    except SystemExit:
        exit(0)
    except:
        return False