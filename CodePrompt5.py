import math

def generate_sine_table():
    start_x = 0.0
    end_x = 2.0
    num_points = 1000
    
    step = (end_x - start_x) / (num_points - 1)

    print(f"{'x':>15} | {'sin(x)':>15}")
    print("-" * 33)

    for i in range(num_points):
        x = start_x + i * step
        sin_of_x = math.sin(x)
        print(f"{x:15.4f} | {sin_of_x:15.4f}")

def main():
    generate_sine_table()

if __name__ == "__main__":
    main()

