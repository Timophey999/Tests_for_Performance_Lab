import sys


def min_move(way_to_file: str) -> int:
    """Читает список чисел из файла и вычисляет минимальное количество движений
    для приведения всех чисел к среднему значению.

    Args:
        way_to_file (str): Путь к файлу, содержащему список чисел.

    Returns:
        int: Минимальное количество движений, необходимых для приведения всех чисел к числу,
        ближайшему к среднему значению.
    """
    # Открываем файл для чтения с указанием кодировки 'utf-8'
    with open(way_to_file, 'r', encoding='utf-8') as file:
        # Читаем все строки из файла, удаляем пробелы и преобразуем в целые числа
        array_of_num = [int(i.strip()) for i in file.readlines()]

        # Вычисляем среднее значение чисел в списке
        middle_num = sum(array_of_num) / len(array_of_num)

        # Находим число, наиболее близкое к среднему значению
        close_number = min(map(lambda x: (abs(middle_num - x), x), array_of_num))[1]

        min_move_counter = 0  # Счетчик для количества ходов

        # Проходим по каждому элементу списка и приводим его к ближайшему числу
        for elem in array_of_num:
            # Изменяем значение элемента до тех пор, пока оно не станет равно ближайшему числу
            while elem != close_number:
                if elem > close_number:
                    elem -= 1  # Уменьшаем элемент
                    min_move_counter += 1  # Увеличиваем счетчик ходов
                else:
                    elem += 1  # Увеличиваем элемент
                    min_move_counter += 1  # Увеличиваем счетчик ходов

        return min_move_counter  # Возвращаем общее количество ходов


if __name__ == "__main__":
    # Получаем путь к файлу из аргументов командной строки
    filename = sys.argv[1]

    try:
        # Вызываем функцию min_move и передаем путь к файлу
        m_move = min_move(filename)

        # Выводим результат на экран
        print(m_move)

    except FileNotFoundError as e:
        # Если файл не найден, возбуждаем исключение
        print(f'Файл по пути: {e.filename} не найден.')
