from manim import Dot, Text, Arrow, Create, Write, VGroup, Scene, WHITE, LEFT, ORIGIN, DOWN, RIGHT, UP, YELLOW, BLUE, MathTex, Circle

class CategoryExample(Scene):
    def construct(self):
        # Create the objects
        obj_a = Dot(LEFT * 2).set_color(WHITE)
        obj_b = Dot(ORIGIN).set_color(WHITE)
        obj_c = Dot(RIGHT * 2).set_color(WHITE)

        # Create the object labels
        label_a = Text("A").next_to(obj_a, DOWN)
        label_b = Text("B").next_to(obj_b, DOWN)
        label_c = Text("C").next_to(obj_c, DOWN)

        # Create the morphisms
        morph_ab1 = Arrow(obj_a.get_center(), obj_b.get_center(), buff=0.2).set_color(YELLOW).shift(UP * 0.1)
        morph_ab2 = Arrow(obj_a.get_center(), obj_b.get_center(), buff=0.2).set_color(YELLOW).shift(DOWN * 0.1)
        morph_bc = Arrow(obj_b.get_center(), obj_c.get_center(), buff=0.2).set_color(YELLOW)

        # Create the morphism labels
        label_ab1 = Text("f").next_to(morph_ab1, UP)
        label_ab2 = Text("g").next_to(morph_ab2, DOWN)
        label_bc = Text("h").next_to(morph_bc, UP)

        # Animate the objects
        self.play(Create(obj_a), Create(obj_b), Create(obj_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))

        # Animate the morphisms
        self.play(Create(morph_ab1), Create(morph_ab2), Create(morph_bc))
        self.play(Write(label_ab1), Write(label_ab2), Write(label_bc))

        # Organize the objects and morphisms
        category = VGroup(obj_a, obj_b, obj_c, label_a, label_b, label_c,
                          morph_ab1, morph_ab2, morph_bc, label_ab1, label_ab2, label_bc)

        circle = Circle(radius=2.0, color=BLUE)
        circle.surround(category)

        # Create the label for the circle
        label_circle = MathTex(r"\mathfrak{C}").next_to(circle, UP)

        # Animate the circle and its label
        self.play(Create(circle), Write(label_circle))

        # Group the category with the circle and its label
        group = VGroup(category, circle, label_circle)

        # Shrink and move the entire group to the left
        self.play(group.animate.scale(0.6).move_to(LEFT * 3))

        # Set example

        obj_n = Dot(LEFT * 2).set_color(WHITE)
        obj_bool = Dot(ORIGIN).set_color(WHITE)
        obj_unit = Dot(RIGHT * 2).set_color(WHITE)

        label_n = MathTex(r"\mathbb{N}").next_to(obj_n, DOWN)
        label_bool = MathTex(r"\mathrm{Bool}").next_to(obj_bool, DOWN)
        label_unit = MathTex(r"\mathrm{Unit}").next_to(obj_unit, DOWN)

        morph_nb1 = Arrow(obj_n.get_center(), obj_bool.get_center(), buff=0.2).set_color(YELLOW).shift(UP * 0.1)
        morph_nb2 = Arrow(obj_n.get_center(), obj_bool.get_center(), buff=0.2).set_color(YELLOW).shift(DOWN * 0.1)
        morph_bu = Arrow(obj_bool.get_center(), obj_unit.get_center(), buff=0.2).set_color(YELLOW)

        label_nb1 = MathTex(r"\mathrm{even}").next_to(morph_nb1, UP)
        label_nb2 = MathTex(r"\geq 3").next_to(morph_nb2, DOWN)
        label_bu = MathTex(r"\mathrm{!}").next_to(morph_bu, UP)

        category2 = VGroup(obj_n, obj_bool, obj_unit, label_n, label_bool, label_unit,
                           morph_nb1, morph_nb2, morph_bu, label_nb1, label_nb2, label_bu)

        # Create a circle around the second category
        circle2 = Circle(radius=2.0, color=BLUE)
        circle2.surround(category2)

        label_circle2 = Text("Set").next_to(circle2, UP)

        # Group the second category with its circle and label
        group2 = VGroup(category2, circle2, label_circle2)

        # Position the second group to the right
        group2.scale(0.6).move_to(RIGHT * 3)

        # Animate the second category
        self.play(Create(obj_n), Create(obj_bool), Create(obj_unit))
        self.play(Write(label_n), Write(label_bool), Write(label_unit))
        self.play(Create(morph_nb1), Create(morph_nb2), Create(morph_bu))
        self.play(Write(label_nb1), Write(label_nb2), Write(label_bu))
        self.play(Create(circle2), Write(label_circle2))

        self.wait()
