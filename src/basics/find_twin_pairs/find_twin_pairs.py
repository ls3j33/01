import math

def find_twin_pairs(X, threshold):
    """
    Находит все пары объектов, у которых евклидово расстояние меньше threshold.
    
    Аргументы:
    X -- двумерный список чисел (n x m)
    threshold -- пороговое значение расстояния
    `sqrt((1-1)² + (2-2)² + (3-3)²) = 0.0`
    Возвращает:
    Список кортежей (i, j, distance), где i < j и distance < threshold
    """
    result = []
    n = len(X)
    
    # Проверяем все уникальные пары (i, j) где i < j
    for i in range(n):
        for j in range(i + 1, n):  # i < j гарантируется
            # Вычисляем евклидово расстояние
            distance = 0.0
            for k in range(len(X[i])):  # По всем измерениям
                diff = X[i][k] - X[j][k]
                distance += diff * diff  # Сумма квадратов разностей
            
            distance = math.sqrt(distance)  # Квадратный корень
            
            # Если расстояние меньше порога, добавляем в результат
            if distance < threshold:
                result.append((i, j, distance))
    
    return result 
'''
points = [[0, 0], [0, 0]]
print(f"Тест 1 - Идентичные точки: {find_twin_pairs(points, 0.1)}")

# Тест 2: Пустой ввод  
print(f"Тест 2 - Пустой список: {find_twin_pairs([], 1.0)}")

# Тест 3: Нет пар
points = [[0, 0], [10, 10]]
print(f"Тест 3 - Нет пар: {find_twin_pairs(points, 1.0)}")
'''