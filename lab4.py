def knapsack(items, capacity):
    sorted_items = sorted(
        items,
        key=lambda item: item[3] / item[2],
        reverse=True,
    )
    max_value = 0
    best_items = []

    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while (
            j < len(sorted_items)
            and total_weight + sorted_items[j][2] <= capacity
        ):
            node_value += sorted_items[j][3]
            total_weight += sorted_items[j][2]
            j += 1

        if j < len(sorted_items):
            free_space = capacity - total_weight
            node_value += free_space * (
                sorted_items[j][3] / sorted_items[j][2]
            )

        return node_value

    def branch_bound(i, weight, value, current_items):
        nonlocal max_value, best_items
        if weight <= capacity and value > max_value:
            max_value = value
            best_items = list(current_items)

        if i == len(sorted_items):
            return

        next_weight = weight + sorted_items[i][2]
        next_value = value + sorted_items[i][3]

        if next_weight <= capacity:
            bound_with = value + (capacity - weight) * (
                sorted_items[i][3] / sorted_items[i][2]
            )
            if bound_with > max_value:
                current_items.append(sorted_items[i])
                branch_bound(i + 1, next_weight, next_value, current_items)
                current_items.pop()

        if node_bound_count(i + 1, weight, value) > max_value:
            branch_bound(i + 1, weight, value, current_items)

    branch_bound(0, 0, 0, [])
    return max_value, best_items


def solve():
    rows = 3
    cols = 3
    total_capacity = rows * cols
    start_points = 10

    all_items = [
        ("Винтовка", "r", 3, 25),
        ("Пистолет", "p", 2, 15),
        ("Боекомплект", "a", 2, 15),
        ("Аптечка", "m", 2, 20),
        ("Ингалятор", "i", 1, 5),
        ("Нож", "k", 1, 15),
        ("Топор", "x", 3, 20),
        ("Оберег", "t", 1, 25),
        ("Фляжка", "f", 1, 15),
        ("Антидот", "d", 1, 10),
        ("Еда", "s", 2, 20),
        ("Арбалет", "c", 2, 20),
    ]

    total_all_points = sum(item[3] for item in all_items)

    inhaler = next(item for item in all_items if item[1] == "i")
    optional_items = [item for item in all_items if item[1] != "i"]

    remaining_capacity = total_capacity - inhaler[2]
    _, best_optional = knapsack(optional_items, remaining_capacity)

    chosen_items = [inhaler] + best_optional
    taken_points = sum(item[3] for item in chosen_items)
    untaken_points = total_all_points - taken_points
    final_score = start_points + taken_points - untaken_points

    if final_score > 0:
        cells = []
        for item in chosen_items:
            cells.extend([f"[{item[1]}]"] * item[2])

        while len(cells) < total_capacity:
            cells.append("[ ]")
        for r in range(rows):
            row_cells = cells[r * cols:(r + 1) * cols]
            print(",".join(row_cells))

        print(f"\nИтоговые очки выживания: {final_score}")
    else:
        print("Не удалось набрать положительное количество очков выживания.")


if __name__ == "__main__":
    solve()