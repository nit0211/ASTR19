import math

def get_sine(x):
    return math.sin(x)

def get_cosine(x):
    return math.cos(x)

def main():
    start_x = 0.0
    end_x = 2.0
    num_points = 1000
    step = (end_x - start_x) / (num_points - 1)

    x_values = []
    sin_values = []
    cos_values = []

    for i in range(num_points):
        x = start_x + i * step
        x_values.append(x)
        sin_values.append(get_sine(x))
        cos_values.append(get_cosine(x))

    print(f"{'x':>15} | {'sin(x)':>15} | {'cos(x)':>15}")
    print("-" * 49)

    for i in range(10):
        print(f"{x_values[i]:15.4f} | {sin_values[i]:15.4f} | {cos_values[i]:15.4f}")

if __name__ == "__main__":
    main()

