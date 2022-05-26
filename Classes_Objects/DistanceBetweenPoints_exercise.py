from __future__ import print_function, division

import copy
import math
from xmlrpc.server import DocXMLRPCRequestHandler

from Classes_Objects.Point1 import Point, Rectangle

def distance_between_points(p1, p2):
    """Computes the distance between 2 point objects"""

    p1: Point
    p2: Point

    returns: float
    
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def find_center(rect):
    """Returns a point at the centre of a rectangle. rect: Rectangle. returns: new Point"""

    p= Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    
    """change the size of a rectangle without changing its position"""
    rect.width = rect.width + 50
    rect.height = rect.height + 100


"""functions that modify objects. For example, grow_rectangle takes a 
Rectangle object and two numbers, dwidth and dheight, 
and adds the numbers to the width and height of the rectangle:"""
def grow_rectanlge(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dy, dx):
    """Move the Rectangle by modifying its corner object

    rect: Rectangle object
    dx: change in x coordinate (can be negative)
    dy: change in y coordinate (cna be negative)"""
    rect.corner.x += dx
