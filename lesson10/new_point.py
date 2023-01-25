import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x},{self.y})"

    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    # def __neg__(self):
    #     return Point2D(-self.x, -self.y)

    def __add__(self, other):
        if type(other) in (int, float):
            return Point2D(self.x + other,
                           self.y + other)
        elif type(other) == tuple and len(other) == 2:
            return Point2D(self.x + other[0],
                           self.y + other[1])
        elif isinstance(other, Point2D):
            return Point2D(self.x + other.x,
                           self.y + other.y)
        else:
            # should be exception in the future
            return None

if __name__ == '__main__':
    p1 = Point2D(1, 2)
    # print(p1)
    p1.translate(0.5, 2)
    # print(p1)
    p2 = Point2D(3, 3)
    distance = p1.distance_from(p2)
    # print(distance)
    print(f"Point2: {p2}")
    p3 = Point2D(3, 3)
    print(f"Point3: {p3}")
    print(f"p2 is p3: {p2 is p3}")
    print(f"p2 == p3 {p2 == p3}")
    print(f"p3 == 5: {p3 == 5}")
    print(f"p3 == 5: {p3 != 5}")
    p4 = Point2D(1, 1)

    print(p3 + p4)
    print(p3 + 5)
    print(p3 + (3,4))
    # print(not p3)

    # l1 = [1,2,3]
    # l2 = [1,2,3]
    # print(f"l1 is l2: {l1 is l2}")
    # print(f"l1 == l2 {l1 == l2}")

    s1 = set([2,3,4])
    s2 = set([3,5,6])
    print(s1 - s2)
