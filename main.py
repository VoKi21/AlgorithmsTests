import numpy as np
import time


def bisection(a: float, b: float, func, epsilon: float):
    step_count = 0

    while abs(b - a) > epsilon:
        x = (a + b) / 2
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
        step_count += 1

    return (a + b) / 2, step_count


# Test function for any root-finding algorithm
def test_algorithm(algorithm, intervals, epsilon):
    total_steps = 0
    total_time = 0
    num_tests = len(intervals)

    for func, a, b in intervals:
        if a > b:
            a, b = b, a

        start_time = time.time()
        root, steps = algorithm(a, b, func, epsilon)
        time_taken = time.time() - start_time
        total_steps += steps
        total_time += time_taken

    avg_steps = total_steps / num_tests
    avg_time = total_time / num_tests

    return avg_steps, avg_time


# Generate random functions
def generate_random_function():
    a = np.random.uniform(-100, 100)
    b = np.random.uniform(-100, 100)
    c = np.random.uniform(-100, 100)
    d = np.random.uniform(-100, 100)
    e = np.random.uniform(-100, 100)

    return lambda x: a * x**4 + b * x**3 + c * x**2 + d * x + e


# Generate random intervals
def generate_random_intervals(num_intervals):
    intervals = []
    for _ in range(num_intervals):
        func = generate_random_function()
        a = np.random.uniform(-10, 10)
        b = np.random.uniform(-10, 10)
        if a > b:
            a, b = b, a
        intervals.append((func, a, b))
    return intervals


if __name__ == '__main__':
    random_intervals = generate_random_intervals(10000)
    eps = 1e-6
    bisection_steps, bisection_time = test_algorithm(bisection, random_intervals, eps)
    print(f"Bisection: average step count: {bisection_steps}, average time in seconds: {bisection_time}")
