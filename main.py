import math

# Функция для нахождения индекса вершины с минимальным весом в списке T, которая еще не была рассмотрена
def arg_min(T, S):
    amin = -1
    m = math.inf  # Максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin

# Матрица смежности графа, где D[i][j] - вес ребра между вершинами i и j
D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

N = len(D)  # Число вершин в графе
T = [math.inf]*N  # Последняя строка таблицы, изначально все значения устанавливаются в бесконечность

v = 0  # Стартовая вершина (нумерация с нуля)
S = {v}  # Множество просмотренных вершин, начинается с вершины v
T[v] = 0  # Нулевой вес для стартовой вершины
M = [0]*N  # Оптимальные связи между вершинами

while v != -1:  # Цикл выполняется, пока не просмотрены все вершины
    for j, dw in enumerate(D[v]):  # Перебираются связанные вершины с вершиной v
        if j not in S:  # Если вершина еще не просмотрена
            w = T[v] + dw  # Рассчитывается новая длина пути до вершины j
            if w < T[j]:  # Если новая длина пути меньше текущей
                T[j] = w  # Обновляется значение T[j] (кратчайшего пути до вершины j)
                M[j] = v  # Связываем вершину j с вершиной v

    v = arg_min(T, S)  # Выбирается следующая вершина с наименьшим весом
    if v >= 0:  # Если выбрана новая вершина
        S.add(v)  # Добавляем ее в множество просмотренных вершин

# Выводим кратчайшие пути T и предшественников M
print("Кратчайшие пути:", T)
print("Предшественники:", M)

# Формируем оптимальный маршрут от стартовой вершины start до конечной вершины end
start = 0
end = 4
P = [end]  # Начинаем с конечной вершины
while end != start:  # Пока не достигнута стартовая вершина
    end = M[P[-1]]  # Находим предшественника
    P.append(end)  # Добавляем предшественника в маршрут

# Выводим оптимальный маршрут от start до end
print("Оптимальный маршрут от вершины", start, "до вершины", P[0], ":", P)
