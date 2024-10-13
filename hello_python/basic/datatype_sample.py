"""
Basic DataType Sample.
String、List etc.
"""


def string_sample():
    """
    Basic DataType String Type Sample
    """

    # String variable
    text = "hello world. sample"

    print(text)

    # 格式化字符串
    word = "World"
    s2 = f"Format string, Hello {word}. 你好，世界。！"

    print(s2)

    # str format
    s3 = "The sum of 1 + 2 is {0}".format(1 + 2)
    print(s3)

    fo = "foo"
    print("foo capitalize:" + fo.capitalize())
