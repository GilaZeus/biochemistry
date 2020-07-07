import turtle
from chain_to_import import formate
from logic.chem import Bond, table_inv
formate = formate.molecule


def draw_single(position, direction):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(position)
    t.pendown()
    t.right(direction * 90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(40)
    t.penup()
    t.forward(20)
    return t.position()


def draw_mult(position, direction, multiplicity=1):
    if multiplicity == 1:
        return draw_single(position, direction)
    elif multiplicity == 2:
        if direction == 0 or direction == 2:
            position += turtle.Vec2D(0, 5)
            draw_single(position, direction)
            position -= turtle.Vec2D(0, 10)
            return draw_single(position, direction) + turtle.Vec2D(0, 5)
        elif direction == 1 or direction == 3:
            position += turtle.Vec2D(5, 0)
            draw_single(position, direction)
            position -= turtle.Vec2D(10, 0)
            return draw_single(position, direction) + turtle.Vec2D(5, 0)
    elif multiplicity == 3:
        if direction == 0 or direction == 2:
            draw_single(position, direction)
            position += turtle.Vec2D(0, 5)
            draw_single(position, direction)
            position -= turtle.Vec2D(0, 10)
            return draw_single(position, direction) + turtle.Vec2D(0, 5)
        elif direction == 1 or direction == 3:
            draw_single(position, direction)
            position += turtle.Vec2D(5, 0)
            draw_single(position, direction)
            position -= turtle.Vec2D(10, 0)
            return draw_single(position, direction) + turtle.Vec2D(5, 0)


def draw_body(molecule, direction, position):
    t = turtle.Turtle()
    t.penup()
    t.setposition(position)
    t.pendown()
    t.right((3 - direction) * 90)
    t.hideturtle()
    t.getscreen()
    t.write(table_inv[molecule.get_proton()])
    molecule.visited = True

    for bond in molecule.no_repeats():
        if isinstance(bond, Bond) and not bond.visited:
            multiplicity = molecule.orbitals.count(bond)
            draw_body(bond, direction + 1, draw_mult(t.pos(), direction, multiplicity))

        direction += 1
        if direction == 4:
            direction = 0
        


t = turtle.Turtle()
t.hideturtle()

draw_body(formate, 0, t.pos())


turtle.mainloop()

