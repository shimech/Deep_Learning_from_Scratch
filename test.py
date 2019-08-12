import unittest
import perceptron
import function


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

    def test_XOR(self):
        """
        XORゲートのテストメソッド
        """
        x1s = [0, 0, 1, 1]
        x2s = [0, 1, 0, 1]
        expected_outs = [0, 1, 1, 0]
        for x1, x2, expected_out in zip(x1s, x2s, expected_outs):
            actual_out = perceptron.XOR(x1, x2)
            self.assertEqual(expected_out, actual_out)


class TestFunction(unittest.TestCase):
    """
    function.pyのテストクラス
    """

    def test_step(self):
        """
        ステップ関数のテストメソッド
        """
        xs = [-3.0, 0.0, 2.0, 9.0]
        expected_ys = [0.0, 0.5, 1.0, 1.0]
        expected_ydiffs = [0.0, 1.0, 0.0, 0.0]
        for x, expected_y, expected_ydiff in zip(xs, expected_ys, expected_ydiffs):
            step = function.Step()
            actual_y = step(x)
            actual_ydiff = step.backward()
            self.assertEqual(expected_y, actual_y)
            self.assertEqual(expected_ydiff, actual_ydiff)

    def test_ReLU(self):
        """
        ReLU関数のテストメソッド
        """
        xs = [-3.0, 0.0, 2.0, 9.0]
        expected_ys = [0.0, 0.0, 2.0, 9.0]
        expected_ydiffs = [0.0, 0.0, 1.0, 1.0]
        for x, expected_y, expected_ydiff in zip(xs, expected_ys, expected_ydiffs):
            relu = function.ReLU()
            actual_y = relu(x)
            actual_ydiff = relu.backward()
            self.assertEqual(expected_y, actual_y)
            self.assertEqual(expected_ydiff, actual_ydiff)

    def test_linear(self):
        """
        恒等関数のテストメソッド
        """
        xs = [-3.0, 0.0, 2.0, 9.0]
        expected_ys = [-3.0, 0.0, 2.0, 9.0]
        expected_ydiffs = [1.0, 1.0, 1.0, 1.0]
        for x, expected_y, expected_ydiff in zip(xs, expected_ys, expected_ydiffs):
            linear = function.Linear()
            actual_y = linear(x)
            actual_ydiff = linear.backward()
            self.assertEqual(expected_y, actual_y)
            self.assertEqual(expected_ydiff, actual_ydiff)


if __name__ == "__main__":
    unittest.main()
