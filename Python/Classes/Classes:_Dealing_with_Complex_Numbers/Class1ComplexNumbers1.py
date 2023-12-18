#!/bin/python3
import math

class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, vector2):
        """
        Create the vectors AB & BC as Points objects
        """
        ax, ay, az = self.x, self.y, self.z            # AB = <ax, ay, az>
        bx, by, bz = vector2.x, vector2.y, vector2.z   # BC = <bx, by, bz>
        return Points(ax - bx, ay - by, az - bz)

    def dot(self, vector2):
        """
        Dot Product of the vectors AB & BC
        """
        ax, ay, az = self.x, self.y, self.z
        bx, by, bz = vector2.x, vector2.y, vector2.z
        return (ax*bx + ay*by + az*bz)
        
    def cross(self, vector2):
        """
        Cross Product of the vectors AB & BC
        """
        ax, ay, az = self.x, self.y, self.z
        bx, by, bz = vector2.x, vector2.y, vector2.z
        return Points(ay*bz - by*az, -(ax*bz - bx*az), ax*by - bx*ay)
        
    def absolute(self):
        """"
        Magnitude of the vector
        """
        ax, ay, az = self.x, self.y, self.z
        return (ax*ax + ay*ay + az*az)**(1/2)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
