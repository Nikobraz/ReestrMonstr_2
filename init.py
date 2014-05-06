# -*- coding: utf-8 -*-
import csv
import os
import datetime
import time
def timer(f):
    """Таймер функции"""
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f" % (time.time()-t)
        return res

    return tmp
#writer = csv.writer(open("some.csv", "wb"), delimiter=',', quoting=csv.QUOTE_MINIMAL,
#                    quotechar='#', lineterminator='\n')
def getfilelist(mesyaz, den, god):
    if mesyaz == '':
        mesyaz = '05'
    if den == '':
        den = '05'
    if god == '':
        god = '2014'
    usluga = raw_input('Введите услугу(А, М, Д):')
    dpap = god + '_' + mesyaz + '_' + den
    if usluga == 'А':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'альт'
    elif usluga == 'M':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'мастер'
    elif usluga == 'Д':
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap + '\\' 'дез'
    else:
        papka = 'D:\work\_Chelinvestbank\_Из банка\Архив' '\\' + dpap
    files = os.listdir(papka.decode('utf-8'))
    files = filter(lambda x: x.endswith('.txt'), files)
    files = [papka.decode('utf-8') + '\\' + fil for fil in files]
    return files

@timer
def search_csv(files, searchstr):
    for fil in files:
#        print fil
        reader = csv.reader(open(fil, "rb"))
        for row in reader:
            row = "".join(row).decode('cp866')
            if searchstr in row:
                print row



def main():
    mesyaz = raw_input('Введите нужный месяц:')
    den = raw_input('Введите нужный день:')
    god = raw_input('Введите нужный год:')
    searchstr = raw_input('Введите искомую строку:')
    search_csv(getfilelist(mesyaz, den, god), searchstr)

if __name__ == "__main__":
    main()