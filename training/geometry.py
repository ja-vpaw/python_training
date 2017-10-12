__author__ = 'ja'

from geom2d import *


l1 = [Point(3,1), Point(0,0), Point(1,2)]

l2 = sorted(l1, key=lambda p: p.x)

print(l1)
print(l2)
