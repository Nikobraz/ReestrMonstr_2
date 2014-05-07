# -*- coding: utf-8 -*-
import csv
import os
import time
import sys


def timer(f):
    """Таймер функции"""
    coding = sys.stdin.encoding

    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f".decode('UTF-8').encode(coding) % (time.time()-t)
        return res
    return tmp


def get_filelist(mesyaz, den, god):
    coding = sys.stdin.encoding
    if mesyaz == '':
        mesyaz = '05'
    if den == '':
        den = '05'
    if god == '':
        god = '2014'
    usluga = raw_input('Введите услугу(1 Альт, 2 Мастер, 3 Дез):'.decode('UTF-8').encode(coding))
    dpap = god + '_' + mesyaz + '_' + den
    if usluga == '1':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'альт'
    elif usluga == '2':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'мастер'
    elif usluga == '3':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'дез'
    else:
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap
    files = os.listdir(papka.decode('utf-8'))
    files = filter(lambda x: x.endswith('.txt'), files)
    files = [papka.decode('utf-8') + '\\' + fil for fil in files]
    return files


@timer
def search_csv(files, search_str):
    for fil in files:
#        print fil
        reader = csv.reader(open(fil, "rb"), delimiter=';')

        for row in reader:
            row = "".join(row).decode('cp866')
            if search_str.decode('UTF-8').upper() in row:
                print fil
                print row


def main():
    coding = sys.stdin.encoding
    den = raw_input('Введите нужный день:'.decode('UTF-8').encode(coding))
    mesyaz = raw_input('Введите нужный месяц:'.decode('UTF-8').encode(coding))
    god = raw_input('Введите нужный год:'.decode('UTF-8').encode(coding))
    search_str = raw_input('Введите искомую строку:'.decode('UTF-8').encode(coding))
    search_csv(get_filelist(mesyaz, den, god), search_str)
    a = raw_input('')
    print a

if __name__ == "__main__":
    while True:
        main()