import sys
import json


def update_values(test_dict: dict, value_dict: dict) -> None:
    """Принимает 2 словаря, обновляет значения в test_dict на основе value_dict, ничего не возвращает."""
    # Генерируем словарь-маппинг id -> value из словаря values для удобного поиска значений по id
    value_map = {item['id']: item['value'] for item in value_dict['values']}

    def recursive_update(d: list[dict | list]) -> None:
        """Рекурсивно обновляет значения в словаре test_dict на основе словаря value_map."""
        if isinstance(d, list):
            # Если элемент является списком, рекурсивно проходим по каждому элементу списка
            for item in d:
                recursive_update(item)
        elif isinstance(d, dict):
            # Если элемент является словарем и содержит ключи 'id' и 'value', обновляем значение 'value'
            if 'id' in d and 'value' in d:
                d['value'] = value_map.get(d['id'], d['value'])  # Заменяем значение, если id присутствует в value_map
            # Рекурсивно проходим по всем ключам словаря
            for key in d:
                recursive_update(d[key])

    # Начинаем рекурсивное обновление с ключа 'tests' в основном словаре test_dict
    recursive_update(test_dict['tests'])


def fill_report_file(path_to_values: str, path_to_tests: str, path_to_report: str) -> None:
    """Принимает пути к файлам со значениями, тестами и отчетом, создает отчетный файл с обновленными данными."""
    with open(
            path_to_values, 'r', encoding='utf-8'
    ) as file_values, open(
        path_to_tests, 'r', encoding='utf-8'
    ) as file_tests, open(
        path_to_report, 'w', encoding='utf-8'
    ) as file_report:
        # Читаем данные из файлов values и tests
        values = json.load(file_values)
        tests = json.load(file_tests)

        # Обновляем значения в tests на основе данных из values
        update_values(tests, values)
        # Записываем обновленный словарь tests в файл report с отступами для удобства чтения
        json.dump(tests, file_report, indent=2)


if __name__ == "__main__":
    # Получаем пути к файлам из аргументов командной строки
    filename_values = sys.argv[1]
    filename_tests = sys.argv[2]
    filename_report = sys.argv[3]

    try:
        # Заполняем файл отчета обновленными данными
        fill_report_file(filename_values, filename_tests, filename_report)
        print('Файл report.json сформирован.')

    except FileNotFoundError as e:
        # Если файл не найден, возбуждаем исключение
        print(f'Файл по пути: {e.filename} не найден.')
