#Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

def write_file(filename,text):
    with open(filename,'w') as file_obj:
        file_obj.write(text)

write_file('myfile.txt','Hello Good Evening 4:47 PM')