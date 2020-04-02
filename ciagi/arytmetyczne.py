def wyraz(a1=1,r=1,ktory=1):
    if ktory==1:
        return a1
    return wyraz(a1+r,r,ktory-1)

def suma(a1=1,r=1,ile=10):
    if ile==1:
        return a1
    return a1+suma(a1+r,r,ile-1)

def iloczyn(a1=1,r=1,ile=10):
    if ile==1:
        return a1
    return a1*iloczyn(a1+r,r,ile-1)