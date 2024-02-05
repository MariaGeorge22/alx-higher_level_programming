#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
r.__width = 0
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, 5)
    r2.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, 5)
    r2.integer_validator("heighst", True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

print(issubclass(Rectangle, BaseGeometry))
