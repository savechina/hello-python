import numpy as np


# Example objective function: f(x) = (x - 3)^2
def objective_function(x):
    return (x - 3) ** 2


# Gradient of the objective function: f'(x) = 2 * (x - 3)
def gradient(x):
    return 2 * (x - 3)


# Gradient Descent Algorithm
def gradient_descent(learning_rate=0.1, tolerance=1e-6, max_iter=1000):
    x = np.random.randn()  # Starting point
    prev_value = objective_function(x)

    for i in range(max_iter):
        grad = gradient(x)
        x -= learning_rate * grad  # Update the variable

        # Check convergence by comparing the change in the objective function value
        curr_value = objective_function(x)

        print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {curr_value:.6f}")

        if abs(curr_value - prev_value) < tolerance:
            print(f"Convergence achieved after {i+1} iterations.")
            break

        prev_value = curr_value
    else:
        print("Max iterations reached without convergence.")

    return x
