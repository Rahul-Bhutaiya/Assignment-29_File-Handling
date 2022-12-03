#Write a Python script to create a copy of a file.

def copy_file(oldfilename,newfilename):
    try:
        with open(oldfilename) as file_obj:
            list_of_lines=file_obj.readlines()
    
        with open(newfilename,'w') as file_obj:
            file_obj.writelines(list_of_lines)
            print('File Copied Successfully')

    except FileNotFoundError:
        print('Root File Does Not Exists')
    except:
        print('Some Error..!')
        
#copy_file('F:\Full_Stack\cities.txt','F:\Full_Stack\cities02.txt')