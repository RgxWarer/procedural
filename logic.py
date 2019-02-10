container = None
# parr_keys = ['height', 'width', 'length', 'density']
sphere_keys = ['radius', 'density']


def init():
    shapes_list = []
    container = {
        'shapes_list': shapes_list,
        'size': 0
    }

    return container


def inp(c, file_name):
    try:
        file = open(file_name)

    except OSError:
        return print("Файл с данными не найден.")

    for line in file:
        input_shape(c, line, file.readline().split(" "))
        c['size'] += 1


def clear(c, file):
    output_file = open(file, 'a')
    output_file.write("Empty container " + str(c['size']))


def out(c, file_name):
    output_file = open(file_name, 'w')
    output_file.write("Container's length = " + str(c['size']) + "\n")

    s = c['size']
    while c['size'] != 0:
        shape = c['shapes_list'].pop()
        output_file.write(str(s - c['size']) + " ")
        output_shape(output_file, shape)
        output_file.write("perimeter: " + str(perimeter(shape)) + "\n")
        c['size'] -= 1


def output_shape(file, shape):
    if list(shape.keys()) == sphere_keys:
        output_sphere(file, shape)
    else:
        output_parr(file, shape)


def output_sphere(file, shape):
    file.write("It's sphere: r = " + shape['radius'] + ", d = " + shape['density'].strip() + " | ")


def output_parr(file, shape):
    file.write(": It's parallelepiped: h = " + shape['height'] + ", "
                "w = " + shape['width'] + ", l = " + shape['length'] + ", "
                "d = " + shape['density'].strip() + " | ")


def input_shape(c, shape_type, param):
    if int(shape_type) == 1:
        input_parr(c, param)
    elif int(shape_type) == 2:
        input_sphere(c, param)
    else:
        return print("Ошибка в формате записи данных в файле.")


def input_parr(c, param):  # создаем функцию ввода параллелепипеда
    parr = {  # словарь с параметрами параллелепипеда
        'height': param[0],
        'width': param[1],
        'length': param[2],
        'density': param[3]
    }
    c['shapes_list'].append(parr)


def input_sphere(c, param):
    sphere = {
        'radius': param[0],
        'density': param[1]
    }
    c['shapes_list'].append(sphere)


def input_shapes(file_name):
    try:
        file = open(file_name)

    except OSError:
        return print("Файл с данными не найден.")

    for line in file:
        inp(container, line, file.readline().split(" "))


def perimeter(shape):
    if list(shape.keys()) == sphere_keys:
        return perimeter_sphere(shape)
    else:
        return perimeter_parr(shape)


def perimeter_sphere(shape):
    return 3.1415 * 2 * int(shape['radius'])


def perimeter_parr(shape):
    return int(shape['width'])*int(shape['height'])*int(shape['length'])*4


def compare(shape0, shape1):
    return perimeter(shape0) < perimeter(shape1)


def sort(c):
    c['shapes_list'].reverse()
    n = len(c['shapes_list'])
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(c['shapes_list'][j], c['shapes_list'][j+1]):
                c['shapes_list'][j], c['shapes_list'][j+1] = c['shapes_list'][j+1], c['shapes_list'][j]
