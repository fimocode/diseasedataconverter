import pandas as pd
data=None
to_filepath=None
def load_file(filepath,delimiter):
    global data
    global to_filepath
    to_filepath=filepath
    print(delimiter)
    data = pd.read_csv(filepath,delimiter= delimiter,engine='python')
def get_list_column():
    return list(data.columns.values)
def convert(list):
    global data
    try:
        print('load convert')
        data.columns= list
        data.to_csv(to_filepath,index=False)
        print('done')
        return True
    except:
        print('error')
        return False