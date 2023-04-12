newList=[]
names=['sarah','iam','salma','aan']
def first(names):
    for i in names:
        if len(i)>3:
            newList.append(i)
    print(newList)
first(names)
print('------------')
def second(names):
    newList=[i for i in names if len(i)>3]
    print(newList)
second(names)    
print('------------')
def third(names):
    if len(names)>3:
       return names
newList=list(map(third,names))
print(newList)    
print('------------')
def fifth(name):
    if len(name)>3:
        return True

newList=list(filter(fifth,names))
print(newList)
