class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lies_inside_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and \
                rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class GUIPoint(Point):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(10, 'red')
