def greedy_algorithm(items, budget):
    # Створюємо список страв, сортований за співвідношенням калорій до вартості (за спаданням)
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    chosen_items = {}

    for item, info in sorted_items:
        if budget >= info['cost']:
            chosen_items[item] = info
            total_calories += info['calories']
            budget -= info['cost']

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо таблицю, де індекс - це бюджет, значення - максимальна калорійність
    dp = [0] * (budget + 1)
    item_list = [[[] for _ in range(budget + 1)]]

    for item, info in items.items():
        for current_budget in range(budget, info['cost'] - 1, -1):
            if dp[current_budget - info['cost']] + info['calories'] > dp[current_budget]:
                dp[current_budget] = dp[current_budget - info['cost']] + info['calories']
                item_list[0][current_budget] = item_list[0][current_budget - info['cost']] + [item]

    return item_list[0][budget], dp[budget]


# Вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм вибір:", greedy_result)
print("Жадібний алгоритм калорійність:", greedy_calories)

# Алгоритм динамічного програмування
dp_items, dp_calories = dynamic_programming(items, budget)
print("Динамічне програмування вибір:", dp_items)
print("Динамічне програмування калорійність:", dp_calories)
