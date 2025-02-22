"""
Знайди ціну найдешевшого польоту між містами, які подаються
як 2-й та 3-й вхідні аргументи.
У випадку неможливості перельоту поверни 0.

Вхідні дані: 3 аргументи: розклад польотів як список
зі списків, місто відправлення і місто прибуття як рядки.

Вихідні дані: Найкраща ціна як ціле число.
"""
import heapq
def cheapest_flight(costs: list, a: str, b: str) -> int:
    # Создание графа из списка рейсов
    graph = {}
    for src, dest, price in costs:
        if src not in graph:
            graph[src] = {}
        graph[src][dest] = price

        # Инициализация очереди с приоритетом и словаря минимальных стоимостей
    priority_queue = [(0, a)]  # (стоимость, город)
    min_cost = {a: 0}

    while priority_queue:
        current_cost, current_city = heapq.heappop(priority_queue)

        # Если достигли целевого города, возвращаем его стоимость
        if current_city == b:
            return current_cost

            # Пропускаем обработку, если найденный путь не является оптимальным
        if current_cost > min_cost.get(current_city, float('inf')):
            continue

            # Обработка соседних городов
        for neighbor, price in graph.get(current_city, {}).items():
            new_cost = current_cost + price
            if new_cost < min_cost.get(neighbor, float('inf')):
                min_cost[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

        # Если путь не найден, возвращаем 0
    print(current_cost)
    return 0



print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)
