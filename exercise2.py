import matplotlib.pyplot as plt
import numpy as np


def draw_square(ax, origin, size, angle):
    """ Функція для малювання квадрата. """
    cos_theta, sin_theta = np.cos(angle), np.sin(angle)
    square = [
        origin,
        (origin[0] + size * cos_theta, origin[1] + size * sin_theta),
        (origin[0] + size * cos_theta - size * sin_theta, origin[1] + size * cos_theta + size * sin_theta),
        (origin[0] - size * sin_theta, origin[1] + size * cos_theta),
        origin
    ]
    square = np.array(square)
    ax.plot(square[:, 0], square[:, 1], 'b-')


def pythagoras_tree(ax, origin, size, angle, depth):
    """ Рекурсивна функція для створення фракталу 'Дерево Піфагора'. """
    if depth == 0:
        return

    draw_square(ax, origin, size, angle)

    new_size = size / np.sqrt(2)
    right_origin = (
        origin[0] + size * np.cos(angle) - new_size * np.sin(angle),
        origin[1] + size * np.sin(angle) + new_size * np.cos(angle)
    )
    left_origin = (
        origin[0] - new_size * np.sin(angle),
        origin[1] + new_size * np.cos(angle)
    )

    pythagoras_tree(ax, right_origin, new_size, angle + np.pi / 4, depth - 1)
    pythagoras_tree(ax, left_origin, new_size, angle - np.pi / 4, depth - 1)


def main():
    fig, ax = plt.subplots()
    recursion_depth = int(input("Введіть рівень рекурсії: "))
    pythagoras_tree(ax, (0, 0), 100, 0, recursion_depth)
    ax.set_aspect('equal')
    plt.show()


if __name__ == "__main__":
    main()
