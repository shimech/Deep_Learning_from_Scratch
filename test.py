import unittest
import perceptron


class TestPerceptron(unittest.TestCase):
    """
    perceptron.pyのテストクラス
    """

    def test_AND(self):
        """
        ANDゲートのテストメソッド
        """
        x1s = [0, 0, 1, 1]
        x2s = [0, 1, 0, 1]
        expected_outs = [0, 0, 0, 1]
        for x1, x2, expected_out in zip(x1s, x2s, expected_outs):
            actual_out = perceptron.AND(x1, x2)
            self.assertEqual(expected_out, actual_out)

    def test_NAND(self):
        """
        NANDゲートのテストメソッド
        """
        x1s = [0, 0, 1, 1]
        x2s = [0, 1, 0, 1]
        expected_outs = [1, 1, 1, 0]
        for x1, x2, expected_out in zip(x1s, x2s, expected_outs):
            actual_out = perceptron.NAND(x1, x2)
            self.assertEqual(expected_out, actual_out)

    def test_OR(self):
        """
        ORゲートのテストメソッド
        """
        x1s = [0, 0, 1, 1]
        x2s = [0, 1, 0, 1]
        expected_outs = [0, 1, 1, 1]
        for x1, x2, expected_out in zip(x1s, x2s, expected_outs):
            actual_out = perceptron.OR(x1, x2)
            self.assertEqual(expected_out, actual_out)


if __name__ == "__main__":
    unittest.main()
