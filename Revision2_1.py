newList=[]
names=['sara','mariam','salma','aan']
def first(names):
    for i in names:
        newList.append(len(i))
    print(newList)
first(names)
print('------------')
def second(names):
    newList=[len(i)for i in names]
    print(newList)
second(names)    
print('------------')
def third(n):
    return len(n)
newList=list(map(third,names))
print(newList)
print('------------')
def fourth(names):
    newList =list(len(n) for n in names)
    print(newList)
fourth(names)    
