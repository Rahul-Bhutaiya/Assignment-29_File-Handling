#Write a Python script to count the number of Python keywords occurring in a python source file.

from keyword import kwlist

def count_keywords(py_resource_file):    
    try:
        with open(py_resource_file) as file_obj:
            count=0
            for line in file_obj.readlines():
                if line[0]=='#':
                    continue
                for word in line.split(' '):
                    if 'else:' in word or 'except:' in word or 'try:' in word or 'True' in word or 'False' in word:
                        count+=1
                        print(word)
                        continue
                    if word in kwlist:
                        count+=1
                        print(word)
            else:
                return count
    except FileNotFoundError:
        print('This File Does Not Exists')
    except:
        print('Some Other Issue..!')

print(count_keywords('F:\Full_Stack\Python\Assignments\Assignment-27_Exception Handling\p4.py'))
