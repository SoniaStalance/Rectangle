from Point import Point
from Rectangle import GUIRectangle
from random import randint
import turtle


def main():
    rectangle = GUIRectangle(Point(randint(0, 10), randint(0, 10)), Point(randint(11, 20), randint(11, 20)))
    rectangle.print_coordinates()

    print('Guess a point that lies inside the rectangle')
    user_point = Point(float(input('Enter x:')), float(input('Enter y:')))

    user_area = float(input('Calculate and enter the area of the given rectangle:'))

    print(f'Point lies within rectangle: {user_point.lies_inside_rectangle(rectangle)}')
    print(f"Area calculated correctly: {rectangle.check_area(user_area)}")
    if not rectangle.check_area(user_area):
        print(f"Actual area: {rectangle.area()}")

    # GUI
    canvas = turtle.Turtle()
    rectangle.draw(canvas)
    turtle.done()


if __name__ == "__main__":
    main()
