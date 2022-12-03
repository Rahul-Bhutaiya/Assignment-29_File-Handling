#Write a Python script to store a list of city names in a file ‘cities.txt’

def store_city_names(file_name,list_of_cities):
    with open(file_name,'w') as file_obj:
        file_obj.writelines(list_of_cities)

store_city_names('F:\Full_Stack\cities.txt',['surat\n','bhavnagar\n','bhopal\n','banglore\n','chennai\n'])