import sys
import logic


def main():
    if len(sys.argv) != 3:
        return print("Вы не ввели нужные аргументы.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    logic.input_shapes(input_name)

    logic.output_shapes(output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")
