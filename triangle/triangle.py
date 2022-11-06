def equilateral(sides):
    if check(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return a==b==c
    else:
        return False

def isosceles(sides):
    if check(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return (a==b or a==c or b==c)
    else:
        return False

def scalene(sides):
    if check(sides):
        a, b, c = sides[0], sides[1], sides[2]
        return a!=b and a!=c and b!=c
    else:
        return False

def check(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return a>0 and b>0 and c>0 and a+b>=c and a+c>=b and b+c>=a