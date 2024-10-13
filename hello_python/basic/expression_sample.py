"""
Basic Expression Sample
"""


def number_calc():
    """number calc sample"""
    a = 1
    b = 2
    c = a + b

    print("c result:" + str(c))

    product = 4 * 30

    floor = 4 / 2.0
    # 加
    sum = 5 + 10
    # 减
    difference = 95.5 - 4.3
    # 乘
    product = 4 * 30
    #  除
    quotient = 56.7 / 32.2
    # 求余
    remainder = 43 % 5

    print(
        f"sum: {sum}, diff: {difference}, product: {product}, quotient: {quotient}, remainder:{remainder}"
    )
