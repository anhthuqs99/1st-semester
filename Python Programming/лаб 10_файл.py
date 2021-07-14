menu='''
0. Выход.
1. Выбор файла.
2. Создание нового набора записей.
3. добавление записи.
4. Вывод всех записей.
5. Поиск по одному полю.
6. Поиск по двум полям.
'''
def readfile():
    try:
        filename = str(input('Вводите название файла: '))
        file = open(filename,'a')
        file.close()
        return filename
    except FileNotFoundError:
        print('Файл не существует')
        return readfile()
def format(s):
    if s == '':
        return '#'
    else:
        return s
def add(filename):
    file = open(filename,'w')
    n = int(input('Вводите количество студентов: '))
    for i in range(n):
        print(i+1,'-ый студент: ')
        name = format(input('Имя: '))
        math = format(input('Математика: '))
        it = format(input('Информатика: '))
        gr = format(input('графика: '))
        file.write('{}|{}|{}|{}\n'.format(name,math,it,gr))
    file.close()
def add1(filename):
    file = open(filename,'a+')
    name = format(input('Имя: '))
    math = format(input('Математика: '))
    it = format(input('Информатика: '))
    gr = format(input('графика: '))
    file.write('{}|{}|{}|{}\n'.format(name,math,it,gr))
    file.close()
def prints(filename):
    try:
        file = open(filename,'r')
    except: pass
    print('{:<20}{:^10}{:^10}{:^10}'.format('name','math','it','gr'))
    ok = True
    while ok:
        s = file.readline()
        s = s.strip()
        if s == '':
            ok = False
        else:
            name,math,it,gr = map(str,s.split('|'))
            print('{:<20}{:^10}{:^10}{:^10}'.format(name,math,it,gr))
    file.close()
def printf(fileinp,fileout):
    try:
        filei = open(fileinp,'r')
    except: pass
    fileo = open(fileout,'w')
    ok = True
    while ok:
        s = filei.readline()
        s = s.strip()
        if s == '':
            ok = False
        else:
            name,math,it,gr = map(str,s.split('|'))
            fileo.write('{}|{}|{}|{}\n'.format(name,math,it,gr))
    filei.close()
    fileo.close()
def check(key,t,name,math,it,gr):
    if key == 'name':
        ok = name == t
    elif key == 'math':
        ok = math == t
    elif key == 'it':
        ok = it == t
    elif key == 'gr':
        ok = gr == t
    return ok 
def find1(filename,key,t):
    count = 0
    try:
        file = open(filename,'r')
    except: pass
    ok = True
    print('{:<20}{:^10}{:^10}{:^10}'.format('name','math','it','gr'))
    while ok:
        s = file.readline()
        s = s.strip()
        if s== '':
            ok = False
        else:
            name,math,it,gr = map(str,s.split('|'))
            if check(key,t,name,math,it,gr):
                print('{:<20}{:^10}{:^10}{:^10}'.format(name,math,it,gr))
                count += 1
    file.close()
    if count == 0:
        print('Not found')
def find2(filename,key1,t1,key2,t2):
    count = 0
    file = open(filename,'r')
    ok = True
    print('{:<20}{:^10}{:^10}{:^10}'.format('name','math','it','gr'))
    while ok:
        s = file.readline()
        s = s.strip()
        if s== '':
            ok = False
        else:
            name,math,it,gr = map(str,s.split('|'))
            if check(key1,t1,name,math,it,gr) and check(key2,t2,name,math,it,gr):
                print('{:<20}{:^10}{:^10}{:^10}'.format(name,math,it,gr))
                count += 1
    file.close()
    if count == 0:
        print('Not found')
#
filename = ''
keyw ='''
Name                  : 'name'
Math                  : 'math'
Information technology: 'it'
Graphics              : 'gr'
'''
ok = True
while ok:
    try:
        print('menu:',menu)
        choise = int(input('Вводите ваш выбор: '))
        if choise == 0:
            ok = False
        elif choise == 1:
            filename = readfile()
        elif filename == '':
            filename = 'input.txt'
        elif choise == 2:
            add(filename)
        elif choise == 3:
            add1(filename)
        elif choise == 4:
            key = str(input("печать на экран или файле? :'s' or 'f' "))
            if key == 's':
                prints(filename)
            elif key == 'f':
                fileout = readfile()
                printf(filename,fileout)
        elif choise ==5:
            print(keyw)
            key = str(input('Вводите поле: '))
            t = str(input('Вводите условие: '))
            find1(filename,key,t)
        elif choise == 6:
            print(keyw)
            key1 = str(input('Вводите первое поле: '))
            t1 = str(input('Вводите первое условие: '))
            print(keyw)
            key2 = str(input('Вводите второе поле: '))
            t2 = str(input('Вводите второе условие: '))
            find2(filename,key1,t1,key2,t2)
        else:
            print('Input Error')
        if not ok:
            print('Finish')
    except: print('Input Error')
