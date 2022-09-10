import math

def main():
    print()
    print ('We have ax^2 + bx + c = 0, so...')
    print()
    print("enter a ")
    a=ask_value()
    print()
    print ('okay, a is', a)
    print()
    print("enter b ")
    b=ask_value()
    print()
    print ('okay, b is', b)
    print()
    print("enter c ")
    c=ask_value()
    print()
    print ('okay, c is', c)
    print()
    solv_square(a,b,c)

def ask_value():
    x=input("type value: ")
    while not x.lstrip('-').isdigit():
        print()   
        print(x, "is not a number!")
        x=input("Enter value: ")
    else:
        x = int(x)
        return x

def solv_square(a,b,c):
    d=discriminant(a,b,c)
    print ('Discriminant is', d)
    print()
    print('Root(s):', roots(d,a,b,c))
    
def discriminant(a,b,c):
    return (b**2-4*a*c)

def roots(d,a,b,c):
    if d<0:
        return "no roots"
    if d==0:
        return (-b/2*a)
    if d>0:
        x1=int(((-b)+math.sqrt(d))/2*a)
        x2=int(((-b)-math.sqrt(d))/2*a)
        lst=[x1,x2]
        return lst
    
main()