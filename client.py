import sys
from logic import init, inp, sort, out_sphere, clear, out



def main():
    if len(sys.argv) != 3:
        return print("Вы не ввели нужные аргументы.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    c = init()
    inp(c, input_name)
    sort(c)
    out(c, output_name)

    clear(c, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")
