"""
Control Flow Sample.
Demonstrates if/elif/else, ternary operator, and match statements in Python.
"""


def if_elif_else_sample():
    """Demonstrates if, elif, else with grade classification."""
    score = 85

    if score >= 90:
        grade = "A (优秀)"
    elif score >= 80:
        grade = "B (良好)"
    elif score >= 70:
        grade = "C (及格)"
    elif score >= 60:
        grade = "D (待提高)"
    else:
        grade = "F (不及格)"

    print(f"分数 {score} 对应的等级: {grade}")

    # Nested if
    age = 18
    if age >= 18:
        status = "成年人"
        if age >= 65:
            status += " (老年人)"
    else:
        status = "未成年人"
    print(f"年龄 {age}: {status}")


def ternary_operator_sample():
    """Demonstrates Python's ternary conditional expression."""
    temperature = 35
    weather = "炎热" if temperature > 30 else "舒适"
    print(f"温度 {temperature}°C, 感觉: {weather}")

    # Multiple ternary operators
    number = -5
    category = "正数" if number > 0 else ("零" if number == 0 else "负数")
    print(f"数字 {number} 是: {category}")


def match_case_sample():
    """Demonstrates Python 3.10+ match/case statement (structural pattern matching)."""
    status_code = 404
    match status_code:
        case 200:
            message = "OK - 请求成功"
        case 301 | 302:
            message = "重定向 (Redirect)"
        case 404:
            message = "Not Found - 页面未找到"
        case 500:
            message = "Server Error - 服务器错误"
        case _:
            message = f"Unknown status code: {status_code}"
    print(f"HTTP {status_code}: {message}")

    # Pattern matching with types
    value = "hello"
    match value:
        case int():
            print(f"'{value}' 是整数 (int)")
        case float():
            print(f"'{value}' 是浮点数 (float)")
        case str():
            print(f"'{value}' 是字符串 (str)，长度: {len(value)}")
        case _:
            print("未知类型")


if __name__ == "__main__":
    if_elif_else_sample()
    print("---")
    ternary_operator_sample()
    print("---")
    match_case_sample()
