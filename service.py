from openpyxl import load_workbook
from sqlite import select_data
from datetime import datetime

coordinate_x = {'KK': {'KI': 66, 'AT': 68, 'DI': 70, },
                'UZB': {'KI': 72, 'AT': 74, 'DI': 76, },
                'RUS': {'KI': 78, 'AT': 80, 'DI': 82, }}

book = load_workbook(filename='Book1.xlsx')


def search_coordinate(data):
    sheet = book.worksheets[0]
    language = data[0]
    faculty = data[1]
    time = datetime.now().strftime('%H:%M:%S')
    nomer = sheet['A'+'3'].value
    predmet = sheet[chr(coordinate_x[language][faculty])+'3'].value
    prepod = sheet[chr(coordinate_x[language][faculty])+'4'].value
    kabinet = sheet[chr(coordinate_x[language][faculty]+1)+'3'].value
    return f'{nomer} - Пара\n<b>Начало:</b>\n<b>Предмет:</b> {predmet}\n<b>Преподаватель:</b> ' \
           f'{prepod}\n<b>Кабинет:</b>{kabinet}\n<b>Конец:</b>\n{time}'
