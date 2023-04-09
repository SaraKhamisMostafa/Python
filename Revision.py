names=['jjjj','aha','sara','sama']
'''name='ahamed'  
def myfun(s,y):
    if y in s:
        print(f'{name} is present in the list')
    else:
        print(f'{name} is not in the list')
            
          
    
myfun(names,name)'''
y=3
new=[]
def myfunc(names,y):
    for c in names:
        if len(c) >y :
            new.append(c)
    print(new)
            
myfunc(names,y)
newlist=[]
def mynum(numbers,num):
    for i in numbers:
        if i % num == 0:
            newlist.append(i)
    print(newlist)
numbers=[1,2,3,4,5,6,6,7,10,15]
num=2
mynum(numbers,num)    
            
