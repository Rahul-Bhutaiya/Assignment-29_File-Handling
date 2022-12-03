"""
Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)
"""
import pickle

def dump_dict(filename,dict_obj):
    with open(filename,'wb') as file_obj:
        pickle.dump(dict_obj,file_obj)
        print('Process Completed')
dump_dict('bookfile.txt',{'satya ke prayog':500,'Wings of Fire':400,'Saurashtra ni Rasdhara':550})