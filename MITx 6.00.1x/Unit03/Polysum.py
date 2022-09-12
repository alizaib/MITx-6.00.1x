import math
def polysum(n, s):
    '''
    int: number of sides of regular polygon
    s: lenth of a side
    
    returns: sum of the area and square of the perimeter of the regular polygon, rounded to four decimal places
    '''
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    perimeter = n*s;

    return round(area + perimeter**2, 4)

print(polysum(5, 2))




