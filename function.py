# 活性化関数のクラス定義スクリプト


import numpy as np


class Step:
    """
    ステップ関数クラス
    """

    def __init__(self) -> None:
        pass

    def __call__(self, x: float) -> float:
        """
        ステップ関数
        @param x: 入力
        @return y: 出力
        """
        if x < 0:
            y = 0.
        elif x == 0:
            y = 0.5
        else:
            y = 1.
        return y

    def backward(self, x: float) -> float:
        """
        ステップ関数の微分
        @param x: 入力
        @return y: 出力
        """
        y = 1. if x == 0 else 0.
        return y


class Sigmoid:
    """
    シグモイド関数クラス
    """

    def __init__(self) -> None:
        self.y = None

    def __call__(self, x: float) -> float:
        """
        シグモイド関数
        @param x: 入力
        @return y: 出力
        """
        y = 1.0 / (1 + np.exp(-x))
        self.y = y
        return y

    def backward(self) -> float:
        """
        シグモイド関数の微分
        @return 微分係数
        """
        return self.y * (1.0 - self.y)

