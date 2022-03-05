def rotate(xs, n):
    for i in range(n):
        x = xs.pop(0)
        xs.append(x)
    
