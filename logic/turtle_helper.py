import turtle
from logic.chem import Bond, table_inv
import subprocess
import os
import numpy as np
from PIL import Image


def draw_single(position, direction):
    '''Draw a single line between atoms.
    
    Return the endposition.'''

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
    '''Draw multiple lines between two atoms.

    Return the endposition.'''

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
    t.write(table_inv[molecule.get_proton()])
    molecule.visited = True

    for bond in molecule.no_repeats():
        if isinstance(bond, Bond) and not bond.visited:
            multiplicity = molecule.orbitals.count(bond)
            draw_body(bond, direction + 1, draw_mult(t.pos(), direction, multiplicity))

        direction += 1
        if direction == 4:
            direction = 0


def crop(png_image_name):
    '''Crop a png-image.'''
    pil_image = Image.open(png_image_name)
    np_array = np.array(pil_image)
    blank_px = [255, 255, 255, 0]
    mask = np_array != blank_px
    coords = np.argwhere(mask)
    x0, y0, z0 = coords.min(axis=0)
    x1, y1, z1 = coords.max(axis=0) + 1
    cropped_box = np_array[x0:x1, y0:y1, z0:z1]
    pil_image = Image.fromarray(cropped_box, 'RGBA')

    pil_image.save(png_image_name)


def draw_postscript(molecule, path):
    '''draw a molecule and save it in path.'''
    t = turtle.Turtle()
    t.hideturtle()
    draw_body(molecule, 0, t.pos())
    canvas = t.getscreen().getcanvas()
    canvas.postscript(file=path + '.ps')
    subprocess.run('C:\\Program Files\\gs\\gs9.52\\bin\\gswin64c.exe -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r300 -sOutputFile=' + \
                   path + ' ' + path + '.ps')
    os.remove(path + '.ps')
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path, "PNG")
    crop(path)