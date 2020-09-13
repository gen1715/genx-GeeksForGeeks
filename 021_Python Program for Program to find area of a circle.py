# Area of a circle can simply be evaluated using following formula.
# Area = pi * r2
# where r is radius of circle

def area(r):
    return (3.14 * (pow(r,2)))

if __name__ == '__main__':
    radius = float(input("Enter the radius:\t"))
    ar = area(radius)
    print(f"Area for the circle with radius {radius} is {ar} ")