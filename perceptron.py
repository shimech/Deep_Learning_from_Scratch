# 「ゼロから作るDeep Learning ~ Pythonで学ぶディープラーニングの理論と実装 ~」
# の「2章 パーセプトロン」の実装


def AND(x1: int, x2: int) -> int:
    """
    ANDゲート
    @param x1, x2: 入力 (0 or 1)
    @return out: 出力 (0 or 1)
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        out = 0
    else:
        out = 1
    return out


def NAND(x1: int, x2: int) -> int:
    """
    NANDゲート
    @param x1, x2: 入力 (0 or 1)
    @return out: 出力 (0 or 1)
    """
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        out = 0
    else:
        out = 1
    return out


def OR(x1: int, x2: int) -> int:
    """
    ORゲート
    @param x1, x2: 入力 (0 or 1)
    @return out: 出力 (0 or 1)
    """
    w1, w2, theta = 0.5, 0.5, 0.3
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        out = 0
    else:
        out = 1
    return out


def XOR(x1: int, x2: int) -> int:
    """
    XORゲート
    @param x1, x2: 入力 (0 or 1)
    @return out: 出力 (0 or 1)
    """
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    out = AND(s1, s2)
    return out
