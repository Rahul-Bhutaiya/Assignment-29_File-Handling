def check_the_word(filename,word):
    try:
        with open(filename,'rt') as obj:
            for line in obj.readlines():
                for wd in line.split(' '):
                    if wd==word or wd==word+'\n':
                        return True
            else:
                return False
    except FileNotFoundError:
        print('This File Doesn\'t Exists')
    except:
        print('Some Other Issue...')


def find_all(filename,word):
    lineno,check=0,True
    try:
        with open(filename,'rt') as obj:
            for line in obj.readlines():
                lineno+=1
                wordno=0
                for wd in line.split(' '):
                    wordno+=1
                    if wd==word or wd==word+'\n':
                        check=False
                        print(lineno,':',wordno)
                
            if check:
                print('This Word Doesn\'t Exists In This File...')        
    except FileNotFoundError:
        print('This File Doesn\'t Exists')
    except:
        print('Some Other Issue...')

find_all('F:\Full_Stack\Python\Assignments\Assignment-29_File Handling\p6.py','is')

def modify_file(filename,oldword,newword):
    if check_the_word(filename,oldword):
        list_var=[]

        with open(filename) as gettext_obj:
            for line in gettext_obj.readlines():
                list_var.append(line.replace(oldword,newword))

        with open(filename,'w') as settext_obj:
            settext_obj.write(''.join(list_var))
            print('File Updated')

    else:
        print('So,This Word Does Not Exist...')    

#modify_file('F:\Full_Stack\practic.txt','Singh','Dhoni')

def delete_single_word(filename,deleting_word):
    if check_the_word(filename,deleting_word):
        list_var=[]

        with open(filename) as obj1:
            for line in obj1.readlines():
                list_var.append(line.replace(deleting_word,'').replace('  ',' ')) if '  ' in line.replace(deleting_word,'') else list_var.append(line.replace(deleting_word,''))
                    
        with open(filename,'w') as obj2:
            obj2.write(''.join(list_var))
            print('All Words Deleted From File')
    else:
        print('So, This Word Does Not Exist...')

#delete_single_word('F:\Full_Stack\practice.txt','bhutaiya Shukla')

def switch_data(old_filename,new_filename):
    try:
        with open(old_filename) as reading:
            list_of_lines=reading.readlines()
    
        with open(new_filename,'w') as writing:
            writing.writelines(list_of_lines)
            print('Data Transfered.')
    except FileNotFoundError:
        print('This File Does Not Exist')
    except:
        print('Some Other Issue..!')

#switch_data('Practice\practice02.txt','Practice\practice03.txt')