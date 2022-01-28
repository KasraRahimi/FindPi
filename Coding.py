# I will find pi, by finding the area under a half circle

it = int(input("Please define a number of iterations: "))

def HalfCircle(x):
    return (1-x**2)**(1/2)

def AreaUnderCurve(func, start=0, end=1, it=1):
    dx = (end - start) / it
    area = 0
    for num in range(it):
        area += dx * func(start + dx * num)
        print(f'Process is {num*100/it:.2f}% done', end='\r')
    return area

AreaOfHalf = AreaUnderCurve(HalfCircle, -1, 1, it)

pi = AreaOfHalf * 2

print(f"Pi is almost: {pi}")