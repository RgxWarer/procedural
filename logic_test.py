import unittest
import logic


class TestLogic(unittest.TestCase):
    # def test_init(self):
    #     container = {
    #         "shapes_list": [],
    #         "size": 0
    #     }
    #
    #     self.assertEqual(logic.init(), container)
    #
    # def test_inp(self):
    #     t = {
    #         'shapes_list': [
    #             {
    #                 'height': '1',
    #                 'width': '1',
    #                 'length': '1',
    #                 'density': '1',
    #                 'temperature': '1'
    #             },
    #             {
    #                 'radius': '2',
    #                 'density': '2',
    #                 'temperature': '2'
    #             },
    #             {
    #                 'a': '3',
    #                 "density": '3',
    #                 'temperature': '3'
    #             },
    #         ],
    #         'size': 3
    #     }
    #     c = logic.init()
    #
    #     self.assertEqual(logic.inp(c, 'input.txt'), t)
    #
    # # def test_clear(self):
    #     # self.assertEqual(logic.clear(logic.init(),[]))
    #     #self.assertTrue(logic.clear(logic.init(), "output.txt"))
    #
    # def test_out(self):
    #     self.assertTrue(logic.out(logic.init(), "output.txt"))
    #
    # def test_out_sphere(self):
    #     self.assertTrue(logic.out_sphere(logic.init(), "output.txt"))
    #
    # def test_output_shape(self):
    #     cube = {
    #         'a': '',
    #         'weight': ''
    #     }
    #
    #     self.assertFalse(logic.output_shape("input.txt", cube))

    def setUp(self):
        self.c = logic.init()
        if not logic.inp(self.c, "input.txt"):
            return
        self.c = logic.sort(self.c)
        logic.out_sphere(self.c, "output.txt")

    def test_square(self):
        sphere = {
            'radius': 5,
            'density': 10,
            'temperature': 300
        }

        self.assertEqual(logic.square(sphere),523.5833333333334)

        parr = {
            'height': 2,
            'width': 4,
            'length': 6,
            'density': 8,
            'temperature': 10
        }
        self.assertEqual(logic.square(parr), 88)

        tetr = {
        'a': 4,
        'density': 7,
        'temperature': 9
        }

        self.assertEqual(logic.square(tetr), 6.928203230275509)

    def test_sort(self):
        sphere = {
            'radius': 5,
            'density': 10,
            'temperature': 300
        }
        sphere0 = {
            'radius': 50,
            'density': 105,
            'temperature': 900
        }
        sphere1 = {
            'radius': 1,
            'density': 10,
            'temperature': 3
        }
        container = {
            'shapes_list': [sphere, sphere0, sphere1],
            'size': 3
        }
        cont_sort = {
            'shapes_list': [sphere0, sphere, sphere1],
            'size': 3
        }

        self.assertEqual(logic.sort(container), cont_sort)

    def test_output(self):
        with open("output.txt") as output_file:
            with open("output_gold.txt") as output_file_gold:
                output = output_file.read()
                output_gold = output_file_gold.read()

                self.assertEqual(output, output_gold)

    def test_clear(self):
        logic.clear(self.c, "output.txt")
        with open("output.txt") as output_file:
            with open("output_gold_clear.txt") as output_file_gold:
                output = output_file.read()
                output_gold = output_file_gold.read()

                self.assertEqual(output, output_gold)

# Test it
    # test_sort()
    # test_square()
    # test_output()
    # test_clear()

if __name__ == '__main__':
    unittest.main()
