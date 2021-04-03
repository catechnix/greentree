"""
Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.

Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the Circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the Circle.
"""
from Point1 import *
from Point1_soln import *


class Circle:
    """Represents a circle. 
    attributes: radius, center.
    center is the point object.
    """

def point_in_circle(point, circle):

    dis=distance_between_points(point,circle.corner)
    if dis <= 75:
        return point
    else:
        return False
 

def rect_in_circle(rectangle, circle):
    """
    check 4 corners of rect are in circle
    """

    if point_in_circle(rectangle.corner, circle) is False:
        return False
    
    rectangle.corner.x +=rectangle.width
    if point_in_circle(rectangle.corner, circle) is False:
        return False
    
    rectangle.corner.y -=rectangle.height
    if point_in_circle(rectangle.corner, circle) is False:
        return False
    
    rectangle.corner.x -=rectangle.width
    if point_in_circle(rectangle.corner, circle) is False:
        return False
       
    return True

def rect_circle_overlap(rect, circle):
    """
    check if any corner/point of the rectangle falls inside of the circle
    """
    if point_in_circle(rectangle.corner, circle) is True:
        return True
    
    rectangle.corner.x +=rectangle.width
    if point_in_circle(rectangle.corner, circle) is True:
        return True
    
    rectangle.corner.y -=rectangle.height
    if point_in_circle(rectangle.corner, circle) is True:
        return True
    
    rectangle.corner.x -=rectangle.width
    if point_in_circle(rectangle.corner, circle) is True:
        return True
       
    return False


    
def main():
    new_circle=Circle()
    new_circle.corner=Point()
    new_circle.corner.x=150
    new_circle.corner.y=100
    new_circle.radius=75

    new_point=Point()
    new_point.x=160
    new_point.y=180

    new_rect=Rectangle()
    new_rect.corner=Point()
    new_rect.corner.x=100
    new_rect.corner.y=90
    new_rect.width=40
    new_rect.height=90

    print(point_in_circle(new_point, new_circle))

    print(rect_in_circle(new_rect, new_circle))
    
    print(rect_in_circle(new_rect, new_circle))
    
if __name__ == '__main__':
    main()


