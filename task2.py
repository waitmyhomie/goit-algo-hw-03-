import matplotlib.pyplot as plt
import math

def koch_snowflake(order, p1, p2):
    if order == 0:
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2

    xA, yA = (2 * x1 + x2) / 3, (2 * y1 + y2) / 3
    xB, yB = (x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3

    dx, dy = xB - xA, yB - yA
    xC = xA + dx * math.cos(math.pi / 3) - dy * math.sin(math.pi / 3)
    yC = yA + dx * math.sin(math.pi / 3) + dy * math.cos(math.pi / 3)

    return (
        koch_snowflake(order - 1, p1, (xA, yA)) +
        koch_snowflake(order - 1, (xA, yA), (xC, yC)) +
        koch_snowflake(order - 1, (xC, yC), (xB, yB)) +
        koch_snowflake(order - 1, (xB, yB), p2)
    )

def plot_snowflake(order):
    p1 = (0, 0)
    p2 = (1, 0)
    p3 = (0.5, math.sqrt(3) / 2)

    snowflake = (
        koch_snowflake(order, p1, p2) +
        koch_snowflake(order, p2, p3) +
        koch_snowflake(order, p3, p1)
    )

    x, y = zip(*snowflake)
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, color="blue")
    plt.axis("equal")
    plt.title(f"Сніжинка Коха (Рівень рекурсії: {order})")
    plt.show()

if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії (наприклад, 2 або 3): "))
        if order < 0:
            print("Рівень рекурсії має бути невід'ємним числом.")
        else:
            plot_snowflake(order)
    except ValueError:
        print("Помилка: введіть ціле число для рівня рекурсії.")