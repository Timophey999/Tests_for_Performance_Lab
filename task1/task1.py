from itertools import cycle
import sys


def circular_array_path(n_arg: int, m_arg: int) -> str:
    """Формирует путь по круговому массиву на основе параметров n и m.

    Args:
        n_arg (int): Количество элементов в массиве.
        m_arg (int): Длина шага для обхода массива.

    Returns:
        str: Строка, представляющая путь по начальным элементам интервалов.
    """
    m_counter = 1  # Счетчик для отслеживания текущего шага
    answer = ''  # Переменная для хранения результата

    # Создаем круговой массив из чисел от 1 до n
    n_range = cycle(range(1, n_arg + 1))

    # Итерируемся по круговому массиву
    for index, elem in enumerate(n_range, 1):
        if index == 1:
            answer = str(elem)  # Добавляем первый элемент в ответ
        if index <= n_arg * m_arg:
            if m_counter == m_arg:
                m_counter = 1  # Сбрасываем счетчик после достижения m шагов
                if str(elem) not in answer:
                    answer += str(elem)  # Добавляем элемент в ответ, если он еще не был добавлен
                else:
                    break  # Прекращаем цикл, если элемент уже был добавлен (замыкание на первый элемент)
            m_counter += 1  # Увеличиваем счетчик шагов
        else:
            break  # Прекращаем цикл, если достигли максимально возможного числа шагов
    return answer  # Возвращаем сформированный путь


if __name__ == "__main__":
    try:
        # Преобразуем аргументы командной строки в целые числа
        n = int(sys.argv[1])
        m = int(sys.argv[2])

        # Проверяем, что n и m положительные целые числа
        if n <= 0 or m <= 0:
            raise ValueError("n и m должны быть положительными целыми числами.")

        # Получение пути по круговому массиву
        path = circular_array_path(n, m)

        # Вывод результата
        print(path)

    except ValueError as e:
        # Обработка ошибок, связанных с преобразованием аргументов
        print(f"Ошибка: {e}")
