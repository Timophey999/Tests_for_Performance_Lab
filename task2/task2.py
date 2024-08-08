import sys


def position_of_point(path_to_file1: str, path_to_file2: str) -> list:
    """Определяет положение точек относительно окружности на основе данных из двух файлов.

    Args:
        path_to_file1 (str): Путь к файлу с данными окружности.
        path_to_file2 (str): Путь к файлу с координатами точек.

    Returns:
        list: Список значений, указывающих положение каждой точки:
              0 - точка лежит на окружности,
              1 - точка внутри окружности,
              2 - точка вне окружности.
    """
    # Открываем файлы с данными окружности и точек
    with open(path_to_file1, 'r', encoding='utf-8') as data_circle, \
            open(path_to_file2, 'r', encoding='utf-8') as data_point:

        # Читаем и обрабатываем данные точек
        data_point_list = [i.strip().split() for i in data_point.readlines()]

        # Читаем и обрабатываем данные окружности
        data_circle_list = data_circle.readlines()
        centr_x, centr_y = [int(i) for i in data_circle_list[0].strip().split()]
        radius = int(data_circle_list[1].strip())

        # Определяем диапазоны значений x и y для окружности
        x_interval_circle = range(centr_x - radius + 1, centr_x + radius)
        y_interval_circle = range(centr_y - radius + 1, centr_y + radius)

        answer_list = []  # Список для хранения результатов

        # Проходим по каждому набору координат точек
        for x, y in data_point_list:
            x, y = int(x), int(y)
            # Проверяем, находится ли точка внутри окружности
            if x in x_interval_circle and y in y_interval_circle:
                answer_list.append(1)  # Точка внутри окружности
            # Проверяем, лежит ли точка на границе окружности
            elif (x in (centr_x + radius, centr_x - radius) and y == centr_y) or \
                    (y in (centr_y + radius, centr_y - radius) and x == centr_x):
                answer_list.append(0)  # Точка на окружности
            else:
                answer_list.append(2)  # Точка вне окружности

        return answer_list  # Возвращаем список результатов


if __name__ == "__main__":
    # Получаем пути к файлам из аргументов командной строки
    filename_1 = sys.argv[1]
    filename_2 = sys.argv[2]

    try:
        # Вызываем функцию для определения положения точек и получаем результат
        pos_points = position_of_point(filename_1, filename_2)
        # Выводим результат для каждой точки
        [print(i) for i in pos_points]

    except FileNotFoundError as e:
        # Если файл не найден, возбуждаем исключение
        print(f'Файл по пути: {e.filename} не найден.')
