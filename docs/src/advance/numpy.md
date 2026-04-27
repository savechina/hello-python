# NumPy 数值计算 (NumPy Numerical Computing)

## 导语

假设你需要处理一百万个温度传感器的读数，计算每个读数的偏移量、找最大值、做统计分析。如果用纯 Python 循环，程序可能需要运行数秒甚至数十秒。但若使用 NumPy，同样的操作只需几毫秒——速度差距可达 100 倍以上。这就是 NumPy（Numerical Python）的威力：它通过 C 语言实现的底层数组和**向量化操作**，让 Python 拥有了接近 C/Fortran 的数值计算性能。无论是机器学习、科学计算、金融分析还是图像处理器，NumPy 都是 Python 数据科学生态系统中不可或缺的基石。

## 学习目标

- 理解 NumPy 数组（ndarray）与 Python 列表的本质区别及性能优势
- 掌握数组的广播（broadcasting）、逐元素运算和索引切片
- 学会使用 NumPy 实现梯度下降等经典数值算法

## 概念介绍

NumPy 的核心数据结构是 **n 维数组（ndarray）**。与 Python 原生列表相比，ndarray 有几个关键差异：

1. **同质性** — ndarray 中所有元素必须是相同类型（如全部 float64），这避免了 Python 列表中每个元素都要存储类型信息的开销。
2. **连续性内存** — 数组数据在内存中是连续存储的，CPU 缓存命中率更高，批量操作速度更快。
3. **向量化** — 对数组的算术运算会自动应用到每个元素，无需写 `for` 循环。这种"批量处理"思维是科学计算的核心范式。
4. **广播（Broadcasting）** — NumPy 允许不同形状的数组进行运算。例如一个二维矩阵可以和一个一维向量直接相加——NumPy 会自动将向量"扩展"以匹配矩阵的形状，无需手动复制数据。

> [!NOTE]
> NumPy 是几乎整个 Python 数据科学生态的"地基"：Pandas 内部使用 ndarray 存储数据，scikit-learn 的机器学习算法依赖 NumPy 数组，Matplotlib 的绘图数据也来自 ndarray。学会 NumPy，就等于打开了 Python 数据科学的大门。

## 代码示例

### 示例 1：NumPy 数组与 Python 列表的对比

```python
import numpy as np

# 从 Python 列表创建 NumPy 数组
py_list = [1, 2, 3, 4, 5]
np_array = np.array(py_list)

print(f"Python 列表: {py_list}")       # [1, 2, 3, 4, 5]
print(f"NumPy 数组:   {np_array}")     # [1 2 3 4 5]
print(f"数组类型:     {np_array.dtype}")  # int64

# 创建特殊数组
zeros = np.zeros((3, 3))               # 3x3 全零矩阵
ones = np.ones((2, 4))                 # 2x4 全一矩阵
random_arr = np.random.randn(5)        # 5 个标准正态分布随机数
linspace = np.linspace(0, 1, 5)        # 0 到 1 均匀取 5 个点

# 数组属性
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(f"形状(shape):  {matrix.shape}")  # (3, 2)
print(f"维度(ndim):   {matrix.ndim}")   # 2
print(f"元素数(size):  {matrix.size}")   # 6
```

`np.array()` 从列表创建数组，`dtype` 属性自动推断元素类型。创建数组时，`np.zeros((rows, cols))` 和 `np.ones((rows, cols))` 比用列表推导式更高效。`shape` 返回元组表示各维度大小，`ndim` 是维度数，`size` 是总元素数。

### 示例 2：向量化运算与广播

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 逐元素运算（向量化，无需 for 循环）
print(a + b)   # [11 22 33 44]
print(a * b)   # [10 40 90 160]
print(a ** 2)  # [1 4 9 16]
print(np.sqrt(a))  # [1.    1.414 1.732 2.    ]

# 广播：不同形状的数组自动对齐
matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
vector = np.array([10, 20, 30])

result = matrix + vector  # vector 沿行方向广播到每一行
print(result)
# [[11 22 33]
#  [14 25 36]
#  [17 38 39]]

# 矩阵乘法和统计
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)  # 矩阵乘法 [[19 22] [43 50]]
print(a.mean(), a.std())  # 均值 2.5, 标准差 1.118...
print(a.sum(axis=0))      # 按列求和 [4 6]
```

向量化运算的精髓在于：**表达式直接对应数学公式**，无需嵌套循环。`a + b` 等价于 `[x + y for x, y in zip(a, b)]`，但 NumPy 在 C 层面批量处理，速度快两个数量级。广播规则看似"魔法"，实则是 NumPy 自动在较小数组的前面补 1 维，然后沿该维重复数据以匹配较大数组的形状。

> [!TIP]
> 当你的代码中出现 `for` 循环逐个处理数组元素时，考虑是否能用向量化操作替代。向量化代码不仅更快，而且更简洁易读。

### 示例 3：梯度下降算法实现

```python
import numpy as np


def objective_function(x):
    """目标函数：f(x) = (x - 3)^2"""
    return (x - 3) ** 2


def gradient(x):
    """目标函数的梯度：f'(x) = 2 * (x - 3)"""
    return 2 * (x - 3)


def gradient_descent(learning_rate=0.1, tolerance=1e-6, max_iter=1000):
    x = np.random.randn()  # 随机起点
    prev_value = objective_function(x)

    for i in range(max_iter):
        grad = gradient(x)
        x -= learning_rate * grad  # 沿负梯度方向更新

        curr_value = objective_function(x)
        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {curr_value:.6f}")

        if abs(curr_value - prev_value) < tolerance:
            print(f"收敛！经过 {i+1} 次迭代。")
            break
        prev_value = curr_value

    return x

# 运行梯度下降
optimal_x = gradient_descent()
print(f"最优解 x = {optimal_x:.6f}")
# 期望输出: x ≈ 3.0, f(x) ≈ 0（因为 f(3) = 0 是最小值点）
```

梯度下降是机器学习中最基础的优化算法。核心思想：从随机起点开始，每步计算当前点的梯度（函数的"坡度"），沿负梯度方向（下坡方向）走一小步（步长 = 学习率），迭代直到值的变化小于阈值。`learning_rate` 控制步长——太大可能震荡不收敛，太小收敛太慢。NumPy 在这里虽未显式展示数组运算，但其 `np.random.randn()` 提供了随机数生成能力。

## 常见错误与解决

> [!WARNING]
> **错误 1：数组形状不匹配导致广播失败**
>
> ```python
> import numpy as np
>
> a = np.array([[1, 2, 3]])     # 形状 (1, 3)
> b = np.array([[1], [2]])      # 形状 (2, 1)
> c = a + b                     # ✅ 广播成功，结果形状 (2, 3)
>
> d = np.array([1, 2, 3])       # 形状 (3,)
> e = np.array([1, 2])          # 形状 (2,)
> # f = d + e                  # 💥 ValueError: operands could not be broadcast together
> ```
>
> **原因**：广播要求两个数组从后往前逐维比较，每维必须相等或其中一个为 1。长度 3 和 2 的数组无法匹配。
>
> **解决**：确保数组形状兼容，或使用 `reshape()` 调整维度。
>
> ```python
> e_reshaped = e.reshape(2, 1)  # 转为 (2, 1)，可与 (1, 3) 广播
> ```

> [!WARNING]
> **错误 2：误用 `*` 做矩阵乘法**
>
> ```python
> import numpy as np
>
> a = np.array([[1, 2], [3, 4]])
> b = np.array([[5, 6], [7, 8]])
>
> print(a * b)  # 💥 逐元素相乘: [[5 12] [21 32]]
> print(a @ b)  # ✅ 矩阵乘法:    [[19 22] [43 50]]
> ```
>
> **原因**：NumPy 中 `*` 是逐元素乘（Hadamard 积），不是线性代数中的矩阵乘法。
>
> **解决**：矩阵乘法用 `@` 运算符或 `np.dot(a, b)`。`@` 在 Python 3.5+ 中可用，语法更直观。

## 最佳实践

1. **优先使用向量化操作替代循环** — NumPy 的内置函数（`+`, `*`, `np.sum()`, `np.mean()` 等）在 C 层实现，速度远超 Python `for` 循环
2. **理解广播规则，善用隐式扩展** — 不要用 `np.tile()` 或 `np.repeat()` 手动复制数组来实现广播，让 NumPy 自动处理，节省内存和计算

## 练习

1. 使用 NumPy 计算一组学生成绩 `scores = [78, 92, 65, 88, 71, 95]` 的平均分、标准差、最高分和最低分。

<details>
<summary>查看答案</summary>

```python
import numpy as np

scores = np.array([78, 92, 65, 88, 71, 95])
print(f"平均分: {scores.mean():.1f}")
print(f"标准差: {scores.std():.1f}")
print(f"最高分: {scores.max()}")
print(f"最低分: {scores.min()}")
```

</details>

2. 使用梯度下降编写一个线性回归拟合器：给定数据点 `x = [1, 2, 3, 4, 5]`, `y = [2, 4, 5, 4, 5]`，用 `y = w*x + b` 拟合，迭代更新 `w` 和 `b`。

<details>
<summary>查看答案</summary>

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 4, 5], dtype=float)

w, b = 0.0, 0.0
lr = 0.01
n = len(x)

for i in range(1000):
    pred = w * x + b
    error = pred - y
    dw = (2 / n) * np.sum(error * x)
    db = (2 / n) * np.sum(error)
    w -= lr * dw
    b -= lr * db

print(f"拟合结果: y = {w:.3f}*x + {b:.3f}")
```

</details>

## 知识检查

1. NumPy 数组中所有元素必须是？
    - A. 相同的值
    - B. 相同的类型
    - C. 相同的维度
    - D. 相同的形状

2. 以下哪个操作用于 NumPy 矩阵乘法？
    - A. `a * b`
    - B. `a @ b`
    - C. `a × b`
    - D. `a.mul(b)`

3. 学习率（learning rate）在梯度下降中的作用是？
    - A. 决定迭代次数
    - B. 控制每次更新的步长
    - C. 决定初始参数的随机种子
    - D. 检测收敛的阈值

<details>
<summary>查看答案</summary>

1. B — NumPy 数组是同质类型的，这与 Python 列表不同
2. B — `@` 是矩阵乘法运算符，`*` 是逐元素乘
3. B — 学习率控制沿负梯度方向每次移动的距离，过大则震荡，过小则收敛慢

</details>

## 本章小结

- NumPy 的 ndarray 是同类型、连续内存的高效数组结构，性能远超 Python 列表
- 向量化运算无需 `for` 循环，`a + b` 直接对每个元素操作，代码简洁且极速
- 广播机制允许不同形状的数组进行运算，避免手动重复数据
- 矩阵乘法用 `@` 而非 `*`（`*` 是逐元素乘）
- 梯度下降是优化算法的基础，通过迭代更新参数逼近最优解

## 术语表

| 英文 | 中文 | 说明 |
|------|------|------|
| NumPy | 数值 Python | Python 科学计算的基础库，提供高效的多维数组和数学函数 |
| ndarray | n 维数组 | NumPy 的核心数据结构，同质类型的连续内存数组 |
| gradient descent | 梯度下降 | 通过沿负梯度方向迭代更新参数以最小化目标函数的优化算法 |
| learning rate | 学习率 | 梯度下降中控制每步更新幅度的超参数 |
| convergence | 收敛 | 迭代过程中目标函数值变化小于阈值，算法停止 |

## 下一步

- [阶段复习：进阶部分](./review-advance.md) → 回顾整个进阶部分的知识，检验学习成果

## 源码链接

- [numpy_sample.py](https://github.com/savechina/hello-python/blob/main/hello_python/advance/numpy_sample.py)
