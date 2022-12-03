#Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

def read_from_file(filename):
    try:
        with open(filename) as file_obj:
            print(file_obj.read())
    except FileNotFoundError:
        print('This File Does Not Exists')
    except:
        print('Some Other Issue..!')

#read_from_file('F:\Full_Stack\myfile.txt')