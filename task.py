'''print("While")
x=1
while x <=20:
    print(x)
    x =x+1
print('-----------------------')

print("for")
c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for x in c:
    print(x)
    x = x+1
print('-----------------------') 

print("range")
for x in range(21):
    print( x)
    x=x+1
print('-----------------------')
'''



'''print("first way")
x=0
for x in range(201):
    if x%2==0:
        print('Even:',x)
        x=+1
    else:
        print('Odd:',x)

print("second")
even=[]
odd=[]
for i in range(201):
    if i%2 !=0:
        odd.append(i)
    else:
        even.append(i)
print("Even nmbers:",even)
print("odd numbers:",odd)

print("third way")
while x<=200:
    if x%2==0:
        print("even",x)
        x=x+1
    else:
        print('odd',x)
        x=x+1'''


names=['sara','mostafa','marwa']
count_names=[]
def my_function(names):
    for x in names:
        for c in x:
            c=names.count(x)
            count_names.append(c)
    return count_names
print(my_function(names))
        
    
        
        

        

        

        
   
   
