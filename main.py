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


def chords(a: float, b: float, func, epsilon: float):
    step_count = 0
    x = a - epsilon * 2
    x_prev = x - epsilon * 2
    fa = func(a)
    fb = func(b)

    while abs(x - x_prev) > epsilon:
        x_prev = x
        x = a - fa * (b - a) / (fb - fa)
        fx = func(x)
        if (fx * fa) < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
        step_count += 1

    return x, step_count


def newton(a: float, b: float, func, epsilon: float):
    step_count = 0
    x = (a + b) / 2  # Initial guess (midpoint of the interval)
    while True:
        fx = func(x)
        f_prime_x = (func(x + epsilon) - fx) / epsilon  # Approximation of the derivative
        x_next = x - fx / f_prime_x
        if abs(x_next - x) <= epsilon:
            break
        x = x_next
        step_count += 1
    return x, step_count


# Test function for any root-finding algorithm
def test_algorithm(algorithm, intervals, epsilon):
    total_steps = 0
    total_time = 0
    num_tests = len(intervals)

    for func, a, b in intervals:
        if a > b:
            a, b = b, a

        start_time = time.time() * 1000
        root, steps = algorithm(a, b, func, epsilon)
        time_taken = time.time() * 1000 - start_time
        total_steps += steps
        total_time += time_taken

    avg_steps = total_steps / num_tests
    avg_time = total_time / num_tests

    return avg_steps, avg_time


def generate_random_function(a, b):
    root = np.random.uniform(a, b)
    coefficients = np.random.uniform(-100, 100, size=5)
    return lambda x: np.polyval(coefficients, x) * (x - root)


def generate_random_intervals(num_intervals):
    intervals = []
    for _ in range(num_intervals):
        a = np.random.uniform(-10, 10)
        b = np.random.uniform(-10, 10)
        func = generate_random_function(a, b)
        while func(a) * func(b) >= 0:
            func = generate_random_function(a, b)
        if a > b:
            a, b = b, a
        intervals.append((func, a, b))
    return intervals


if __name__ == '__main__':
    random_intervals = generate_random_intervals(100)
    eps = 1e-6

    bisection_steps, bisection_time = test_algorithm(bisection, random_intervals, eps)
    print(f"Bisection: average step count: {bisection_steps}, average time in ms: {bisection_time}")
    # I'm not sure is Newton's method so fast because its good or because i have a mistake
    newton_steps, newton_time = test_algorithm(newton, random_intervals, eps)
    print(f"Newton's method: average step count: {newton_steps}, average time in ms: {newton_time}")
    # Chords are really slow for some reason
    chords_steps, chords_time = test_algorithm(chords, random_intervals, eps)
    print(f"Chords method: average step count: {chords_steps}, average time in ms: {chords_time}")
