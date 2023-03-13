'''def mysum(x,y):
    return x+y


g=mysum(10,24,30)
print(g)'''

#to send number of parameters to a function without identify it by variable length

'''def mysum(arg,*vartuple):
    result = arg
    for x in vartuple:
        result += x
    print( result)   


mysum(10,24,30,80,60)'''

'''def mysum(x,y):
    return x+y

k=mysum(10,20)
print(k)




mysum2 =lambda x,y:x+y
k=mysum2(10,12)
print(k)'''


'''f=0
print(f)


def do():
    global f
    f=5
    print(f)


do()'''




















'''
str
list
tuple
dict

h ='''  '''' #to document my code its save spaces
'''

class Calc:
    def mysum(x , y):
        return x+y
    
    def mymul(x,y):
        return x*y

C = Calc()
print(C.mysum(9,9))
print(C.mymul(7,7))

    






