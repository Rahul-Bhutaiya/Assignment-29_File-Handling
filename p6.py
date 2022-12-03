#Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

def search_word(filename,word):
    try:
        with open(filename) as file_obj:
            for line in file_obj.readlines():
                for wd in line.split(' '):
                    if word==wd or word+'\n'==wd:
                        return True
            else:
                return False
    except FileNotFoundError:
        print('This File Does Not Exists')
    except:
        print('Some Other Issue')


#print(search_word('F:\Full_Stack\cities.txt','rabarika'))