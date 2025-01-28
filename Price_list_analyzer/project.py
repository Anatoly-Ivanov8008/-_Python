"""
Практическое задание "Анализатор прайс-листов."
"""

# Для работы с файловой системой
import os
# Для работы с табличными данными
import pandas as pd
# Для форматированного вывода в консоли
from prettytable import PrettyTable


class PriceAnalyzer:
    def __init__(self, input_folder="prices", output_folder="output"):
        """
        Инициализация класса PriceAnalyzer.
        :param input_folder: Папка, где хранятся файлы прайс-листов.
        :param output_folder: Папка, куда будут экспортироваться результаты.
        """
        # Папка с файлами
        self.input_folder = input_folder
        # Папка для результатов
        self.output_folder = output_folder
        # Таблица с объединёнными данными
        self.data = pd.DataFrame()
        # Таблица с результатами последнего поиска
        self.filtered_data = pd.DataFrame()

    def load_prices(self):
        """
        Загружает данные из файлов в указанной папке.
        Находит только файлы с "price" в названии, проверяет их и объединяет данные.
        """
        # Находим файлы с "price" в названии
        price_files = [f for f in os.listdir(self.input_folder) if "price" in f.lower()]
        # Список для хранения данных из всех файлов
        all_data = []

        # Обрабатываем каждый файл из списка
        for file in price_files:
            # Полный путь к файлу
            file_path = os.path.join(self.input_folder, file)
            try:
                # Читаем файл как CSV
                df = pd.read_csv(file_path)

                # Нормализация названий колонок
                columns_map = {
                    "название": "name",
                    "продукт": "name",
                    "товар": "name",
                    "наименование": "name",
                    "цена": "price",
                    "розница": "price",
                    "фасовка": "weight",
                    "масса": "weight",
                    "вес": "weight",
                }
                # Приведение к нижнему регистру и переименование
                df = df.rename(columns=str.lower).rename(columns=columns_map)

                # Проверяем, что в файле есть нужные колонки
                if {"name", "price", "weight"}.issubset(df.columns):
                    # Оставляем только нужные столбцы
                    df = df[["name", "price", "weight"]]
                    # Добавляем столбец с названием файла
                    df["file"] = file
                    # Удаляем строки с пустыми значениями
                    df = df.dropna(subset=["name", "price", "weight"])
                    # Вычисляем цену за килограмм
                    df["price_per_kg"] = df["price"] / df["weight"]
                    # Добавляем данные в общий список
                    all_data.append(df)
            except Exception as e:
                # Обрабатываем ошибку при чтении или обработке файла
                print(f"Ошибка при обработке файла {file}: {e}")

        # Объединяем все данные в одну таблицу
        if all_data:
            self.data = pd.concat(all_data, ignore_index=True)

    def export_to_html(self, data=None, filename="output.html"):
        """
        Экспортирует данные в HTML файл в папке output.
        :param data: DataFrame для экспорта (по умолчанию все данные).
        :param filename: Название файла для сохранения.
        """
        # Если не переданы данные, берём все загруженные данные
        if data is None:
            data = self.data

        if data.empty:
            print("Нет данных для экспорта.")
            return

        # Создаём папку output, если она не существует
        os.makedirs(self.output_folder, exist_ok=True)
        # Путь к итоговому файлу
        output_path = os.path.join(self.output_folder, filename)

        # Сортируем данные по цене за кг и сбрасываем индексы после сортировки
        data = data.sort_values(by="price_per_kg").reset_index(drop=True)

        # Добавляем нумерацию
        data.insert(0, "№", data.index + 1)  # Нумерация начинается с 1

        # Округляем числовые значения до двух знаков после запятой
        data["price"] = data["price"].round(2)
        data["weight"] = data["weight"].round(2)
        data["price_per_kg"] = data["price_per_kg"].round(2)

        # Переименовываем столбцы для HTML
        renamed_data = data.rename(
            columns={
                "name": "Наименование",
                "price": "Цена",
                "weight": "Вес",
                "file": "Файл",
                "price_per_kg": "Цена за кг"
            }
        )

        # Экспортируем в HTML
        renamed_data.to_html(output_path, index=False, escape=False)
        print(f"Данные экспортированы в {output_path}")

    def find_text(self, text):
        """
        Ищет текст в названиях продуктов и возвращает отсортированный список найденных позиций.
        :param text: Текст для поиска.
        :return: Отфильтрованный DataFrame с результатами.
        """
        if self.data.empty:
            print("Данные не загружены.")
            return pd.DataFrame()

        # Фильтруем данные по тексту в столбце "name"
        self.filtered_data = self.data[self.data["name"].str.contains(text, case=False, na=False)]
        # Сортируем по цене за кг
        self.filtered_data = self.filtered_data.sort_values(by="price_per_kg")

        # Создаём таблицу для красивого вывода в консоль
        table = PrettyTable()
        table.field_names = ["№", "Наименование", "Цена", "Вес", "Файл", "Цена за кг"]
        for i, row in enumerate(self.filtered_data.itertuples(), start=1):
            table.add_row([i, row.name, f"{row.price:.2f}", f"{row.weight:.2f}", row.file, f"{row.price_per_kg:.2f}"])

        # Выводим таблицу в консоль
        print(table)
        return self.filtered_data


if __name__ == "__main__":
    # Создаём объект класса
    analyzer = PriceAnalyzer()

    # Загружаем данные из файлов
    analyzer.load_prices()

    # Основной цикл для поиска и экспорта
    print(f"Введите текст для поиска \n"
          f"'export' для экспорта последнего результата поиска\n"
          f"'exit' для выхода:")
    while True:
        # Получаем текст от пользователя
        query = input("> ")
        # Проверяем, ввёл ли пользователь "exit"
        if query.lower() == "exit":
            print("Работа завершена.")
            # Экспорт всех данных
            analyzer.export_to_html()
            break
        # Если пользователь ввёл "export"
        elif query.lower() == "export":
            # Проверяем, есть ли результаты последнего поиска
            if analyzer.filtered_data.empty:
                print("Нет данных для экспорта. Сначала выполните поиск.")
            else:
                analyzer.export_to_html(data=analyzer.filtered_data, filename="filtered_output.html")
        else:
            # Ищем текст в данных
            analyzer.find_text(query)
