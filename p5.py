#Write a Python script to append list of city names in a file ‘cities.txt’

def append_city_name(filename,list_of_citynames):
    with open(filename,'a') as file_obj:
        file_obj.writelines(list_of_citynames)

#append_city_name('F:\Full_Stack\cities.txt',['surat\n','bhavnagar\n','bhopal\n','banglore\n','chennai\n'])