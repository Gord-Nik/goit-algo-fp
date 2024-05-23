import numpy as np
import matplotlib.pyplot as plt


def roll_dice(num_rolls):
    # Генерація випадкових значень для двох кубиків
    die1 = np.random.randint(1, 7, num_rolls)
    die2 = np.random.randint(1, 7, num_rolls)

    # Обчислення суми чисел, що випали на кубиках
    sums = die1 + die2

    # Підрахунок кожної суми
    counts = {sum_value: np.sum(sums == sum_value) for sum_value in range(2, 13)}

    return counts, num_rolls


def calculate_probabilities(counts, num_rolls):
    probabilities = {sum_value: count / num_rolls for sum_value, count in counts.items()}
    return probabilities


# Кількість кидків
num_rolls = 100000

# Проведення симуляції
counts, total_rolls = roll_dice(num_rolls)

# Обчислення ймовірностей
probabilities = calculate_probabilities(counts, total_rolls)

# Вивід результатів
print("Ймовірності сум при киданні двох кубиків:")
for sum_value, prob in sorted(probabilities.items()):
    print(f"Сума {sum_value}: {prob:.4f} ({prob * 100:.2f}%)")

# Створення графіка
labels = list(probabilities.keys())
values = [prob * 100 for prob in probabilities.values()]

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='blue')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xticks(labels)
plt.grid(True)
plt.show()
