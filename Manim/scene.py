from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))  # show the circle on screen
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.add(circle, square)
        self.wait(2)
        self.remove(circle)
        self.wait(2)

