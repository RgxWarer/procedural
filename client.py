import sys
import logic


def main():
    # if len(sys.argv) != 3:
    #     return print("Вы не ввели нужные аргументы.")

    input_name = "input.txt"#sys.argv[1]
    output_name = "output.txt"#sys.argv[2]

    logic.input_shapes(input_name)

    # logic.output_shapes(output_name)
    logic.multiMethod(output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")
