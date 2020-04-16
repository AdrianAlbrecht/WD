def fiboc(max):
    a=0
    b=1
    while b<max:
        yield b
        temp=a+b
        a=b
        b=temp
#można też zrobić wersję nieskończoną generatora: bez atrybutu i w pętli while dać zamiast warunku "True"
        

fib=fiboc(400)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))