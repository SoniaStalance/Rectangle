class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def print_coordinates(self):
        print(f'The rectangle has the following coordinates: ({self.point1.x},{self.point1.y}),'
              f'({self.point1.x},{self.point2.y}),'
              f'({self.point2.x},{self.point2.y}),'
              f'({self.point2.x},{self.point1.y})')

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

    def check_area(self, user_area):
        if self.area() == user_area:
            return True
        else:
            return False


class GUIRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.goto(self.point1.x, self.point2.y)
        canvas.goto(self.point2.x, self.point2.y)
        canvas.goto(self.point2.x, self.point1.y)
        canvas.goto(self.point1.x, self.point1.y)
