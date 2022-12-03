"""
Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file
"""

def get_file_status(file_object):
    print('This File is Read Only File' if file_object.mode=='r' else 'This File is Not Read Only File')
    print('The File is Closed' if file_object.closed else 'This File isn\'t Closed Yet')
    print('File Opening Mode is :',file_object.mode)    
    print('The File Name is :',file_object.name)

