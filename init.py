# -*- coding: utf-8 -*-
import csv
import os
import datetime
#writer = csv.writer(open("some.csv", "wb"), delimiter=',', quoting=csv.QUOTE_MINIMAL,
#                    quotechar='#', lineterminator='\n')
def getfilelist():
    mesyaz = raw_input('Введите нужный месяц:')
    den = raw_input('Введите нужный день:')
    god = raw_input('Введите нужный год:')
    usluga = raw_input('Введите услугу(А, М, Д):')
    dpap = god + '_' + mesyaz + '_' + den
    if usluga == 'А':
        files = 'D:\work\_Chelinvestbank\_Из банка\Архив' + '\\' + dpap + '\\' + 'альт'
    elif usluga == 'M':
        files = 'D:\work\_Chelinvestbank\_Из банка\Архив' + '\\' + dpap + '\\' + 'мастер'
    elif usluga == 'Д':
        files = 'D:\work\_Chelinvestbank\_Из банка\Архив' + '\\' + dpap + '\\' + 'дез'
    else:
        files = 'D:\work\_Chelinvestbank\_Из банка\Архив' + '\\' + dpap
    files = os.listdir(files.decode('utf-8'))
    files = filter(lambda x: x.endswith('.txt'), files)
    return files


def read_csv(files):
    for fil in files:
        reader = csv.reader(open(fil, "rb"))

        for row in reader:
            row = "".join(row).decode('cp866')
            row = row.decode('cp866')
            print row,

read_csv(getfilelist())