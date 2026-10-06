class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = point()
point1.x = 11
print(point1.x)
print(point1.y)
point1.draw()

point2 = point()
point2.x = 30
point2.y = 40
print(point2.x)
print(point2.y)
point2.move()