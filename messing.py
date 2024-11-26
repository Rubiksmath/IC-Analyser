#element, *emoji = 3,
#print((*emoji,))

def t(a, *b):
    print(b)

c = (0,1,2,3)
d,*e=c
t(d,e)

def f(*x):
    a,*b = *x,
    print(x)
    print(*x)
    print(a)
    print(*b)
print(e)
f(1)
f(1,2)
f((1,2))