from uniimport import Uniimport

#Класс для Сценария 3
class Product:
    def __init__(self, Артикул, Наименование, Цена, Количество):
        self.article = Артикул
        self.name = Наименование
        self.price = float(Цена)
        self.qty = int(Количество)

    def __repr__(self):
        return f"Product({self.article}, {self.name}, {self.price}, {self.qty})"


def main():
    #Модуль 1
    file_path = "catalog.xlsx"
    sheet_name = "Каталог"
    cell_range = "A1:D10"  # заголовки + 9 строк данных

    data = Uniimport.read_range(file_path, sheet_name, cell_range)

    print("Данные из диапазона A1:D10")
    Uniimport.print_structure(data)

    Uniimport.create_report(
        source_file="catalog.xlsx",
        source_sheet="Каталог",
        cell_range="A1:D10",
        report_file="report_module1.xlsx"
    )

    #Модуль 2
    Uniimport.create_document()
    #результат в document.docx


    #Модуль 3 Сценарий 1
    result = Uniimport.build_report("sales.csv", group_key="category", value_key="amount")

    for row in result:
        print(row)
    #результат в report.xlsx & report.docx

    #Модуль 3 Сценарий 2
    records = Uniimport.read_word_table("source.docx")  # список словарей
    products = Uniimport.records_to_objects(records, Product)  # список объектов

    for p in products:
        print(p)
    #результат в консоли

    #Модуль 3 Сценарий 3
    Uniimport.benchmark_export()
    #результат в big_dataset.xlsx

if __name__ == '__main__':
    main()
