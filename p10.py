"""
Write a Python script to extract book data from a bookfile using pickle. Also print
extracted book data.
"""

import pickle

def load_dict(filename):
    try:
        with open(filename,'rb') as file_obj:
            dict_obj=pickle.load(file_obj)
            for key in dict_obj:
                print(key,':',dict_obj[key])
    except FileNotFoundError:
        print('This File Does Not Exist')

#load_dict("F:\Full_Stack\\bookfile.txt")