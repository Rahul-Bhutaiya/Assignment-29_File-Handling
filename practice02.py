import pickle

def dump(filename,mode,dump_obj):
    with open(filename,mode) as obj:
        pickle.dump(dump_obj,obj)
        print('Process Complete')

def load(filename):
    try:
        with open(filename,'rb') as obj:
            objects=pickle.load(obj)
            for object in objects:
                print(object)
    except FileNotFoundError:
        print('This File Does Not Exists')
    except:
        print('some other issue...')

# dict_var={1:'rahul',2:'utsav',3:'dax',4:'meet'}
#list_var=[1,2,3,4,5]
#dump('F:\Full_Stack\Practice\practice01.txt','wb',list_var)

#load('F:\Full_Stack\Practice\practice01.txt')