from openpyxl import load_workbook
from sqlite import select_data
from datetime import datetime

coordinate_x = {'KK': {'KI': 66, 'AT': 68, 'DI': 70, },
                'UZB': {'KI': 72, 'AT': 74, 'DI': 76, },
                'RUS': {'KI': 78, 'AT': 80, 'DI': 82, }}

start_and_end = {'I': {'start': '13:30', 'end': '14:50'},
                 'II': {'start': '15:00', 'end': '16:20'},
                 'III': {'start': '16:30', 'end': '17:50'},
                 'IV': {'start': '18:00', 'end': '19:20'}}

book = load_workbook(filename='Book1.xlsx')


def search_coordinate(data):
    sheet = book.worksheets[0]
    language = data[0]
    faculty = data[1]
    time = datetime.now().strftime('%H:%M')
    result = ''
    for i in range(27, 34, 2):
        if sheet[chr(coordinate_x[language][faculty]) + str(i)].value is not None:
            result += f'{sheet["A"+str(i)].value} - Пара\n' \
                      f'<b>Начало:</b> {start_and_end[sheet["A"+str(i)].value]["start"]}\n' \
                      f'<b>Предмет:</b> {sheet[chr(coordinate_x[language][faculty])+str(i)].value}\n' \
                      f'<b>Преподаватель:</b> {sheet[chr(coordinate_x[language][faculty])+str(i+1)].value}\n' \
                      f'<b>Кабинет:</b> {sheet[chr(coordinate_x[language][faculty]+1)+str(i)].value}\n' \
                      f'<b>Конец:</b> {start_and_end[sheet["A"+str(i)].value]["end"]}\n' \
                      f'------------------------------\n'
    return result
