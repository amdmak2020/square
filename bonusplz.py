list = [1,2,3,4,5,6,7,8,9,10]

def square(l, x, y):
    values = []
    for i in l:
        if i*i > y:
            values.append(i*i)
        else:
            pass
    return values

print(square(list,1, 10))