def areaofTrapezoid(a, b):
    return (a+b)/2

def areaofparallelogram(a, b):
    return a * b

def volumeofCylinder(a, b, c):
    return a * b * c

def areaofCylinder(r, h):
    return 3.14 * r * 2 * h
    
    
print(f"area of trapeziod {areaofTrapezoid(2,3)}")

print(f"area of parallelogram {areaofparallelogram(2, 3)}")

print(f"volume of cylinder = {volumeofCylinder(2, 3, 4)}")

print(f"area of cylinder = {areaofCylinder(2, 3)}")
    
