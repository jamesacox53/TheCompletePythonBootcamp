def myfunc(x, y, z):
    if z:
        return x
    else:
        return y
    
print(myfunc('a', 'b', True))

print(myfunc('a', 'b', False))