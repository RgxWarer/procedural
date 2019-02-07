shapes_list = []
# parr_keys = ['height', 'width', 'length', 'density']
sphere_keys = ['radius', 'density']


def input_parr(h, w, l, d):
    parr = {
        'height': h,
        'width': w,
        'length': l,
        'density': d
    }
    shapes_list.append(parr)


def input_sphere(r, d):
    sphere = {
        'radius': r,
        'density': d
    }
    shapes_list.append(sphere)


def input_shapes(file_name):
    try:
        file = open(file_name)

    except OSError:
        return print("Файл с данными не найден.")

    for line in file:
        if int(line) == 1:
            h, w, l, d = file.readline().split(" ")
            input_parr(h, w, l, d.strip())
        elif int(line) == 2:
            r, d = file.readline().split(" ")
            input_sphere(r, d.strip())
        else:
            print("Ошибка в формате записи данных в файле.")


def output_shapes(file_name):
    count = 0
    output_file = open(file_name, 'w')
    output_file.write("Container's length = " + str(len(shapes_list)) + "\n")

    while len(shapes_list) != 0:
        shape = shapes_list.pop()
        if list(shape.keys()) == sphere_keys:
            output_file.write(str(count) + ": It's sphere: "
                                           "r = " + shape['radius'] + ", "
                                            "d = " + shape['density']  + "\n")
            count += 1
        else:
            output_file.write(str(count) + ": It's parallelepiped: "
                                           "h = " + shape['height'] + ", "
                                            "w = " + shape['width'] + ", "
                                            "l = " + shape['length'] + ", "
                                              "d = " + shape['density'] + "\n")
            count += 1

    output_file.write("\nEmpty container\n"
                      "Container contains " + str(len(shapes_list)))
