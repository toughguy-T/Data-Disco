import os
import pandas as pd


def load_path(file_path):
    #file_path = 'C:/Users/lenovo/Desktop/1.task1/dr3_3858'
    dirs = os.listdir(file_path)
    length = len(dirs)
    #filenames = pd.DataFrame({'filename': dirs})
    #filename.to_csv(save_path, index=False, sep=',')
    return dirs, length
