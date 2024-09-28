#create class
class Employee:
    #initializing
    def __init__(self):
        print('Employee created')
    #calling destructor
    def __del__(self):
        print("destructer called")
def Create_obj():
    print('Making Object...')
    obj= Employee()
    print('function end...')
    return obj
print('calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
