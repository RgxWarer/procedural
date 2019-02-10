import sys
import logic


def main():
    if len(sys.argv) != 3:
        return print("Вы не ввели нужные аргументы.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    c = logic.init()
    logic.inp(c, input_name)
    logic.out_sphere(c, output_name)

    logic.clear(c, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")
