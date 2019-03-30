import sys
import logic


def main():
  #  if len(sys.argv) != 3:
  #      return print("Вы не ввели нужные аргументы.")

    input_name = "input.txt"# sys.argv[1]
    output_name = "output.txt"# sys.argv[2]

    c = logic.init()
    if not logic.inp(c, input_name):
        return
    r = logic.sort(c)
    logic.out_sphere(r, output_name)
   # logic.clear(r, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")
