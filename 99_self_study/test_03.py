pi = 3.14

class Point:
    def __init__(self, x_sign, y_sign):
        
        self.x_sign = x_sign
        self.y_sign = y_sign

    def __str__(self):
        return f'Point: ({self.x_sign}), r:{self.y_sign}'

class Circle(Point):
    def __init__(self, center, r_rich):
        # super().__init__
        self.r_rich = r_rich
        self.center = (center.x_sign, center.y_sign)

    def get_area(self):
        return (pi*(self.r_rich**2))

    def get_perimeter(self):
        return (2*pi*self.r_rich)

    def get_center(self):
        return f'({self.center})'

    def __str__(self):
        return f'Circle: ({self.center}), r:{self.r_rich}'

p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
print(c1)
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
print(c2)