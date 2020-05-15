def lets_go(i):
    '''
    Функция обработки пользовательского ввода.
    '''
    if i == 'l':
        com_list()
    elif i == 's':
        j = com_shelf()
        if j is not None:
            print('Полка номер', j)
        else:
            print('Такого документа не существует!')
    elif i == 'p':
        com_people()
    elif i == 'a':
        com_add()
    elif i == 'u':
        com_users()
def com_list():
    '''
    l (List) - функция, которая выведет список всех документов.
    '''
    for i in documents:
        print(', '.join(i.values()))
def com_shelf():
    '''
    s (Self) - функция, которая спросит номер документа
    и выведет номер полки, на которой он находится.
    '''
    doc_num = input('Введите номер документа: ')
    for key, value in directories.items():
        if doc_num in value:
            return key
def com_people():
    '''
    p (People) - функция, которая спросит номер документа и
    выведет имя человека, которому он принадлежит.
    '''
    flag = 0
    doc_num = input('Введите номер документа: ')
    for i in documents:
        if doc_num in i.values():
            flag = 1
            print(i.get('name'))
    if flag != 1:
        print('Такого документа не существует!')
def com_add():
    '''
    a (Add) - функция,которая добавит новый документ в каталог и
    в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    '''
    doc_type = input('Введите тип документа: ')
    doc_num = input('Введите номер документа: ')
    doc_shelf = input('Введите номер полки для хранения: ')
    name = input('Введите имя: ')
    if str(doc_shelf) in directories.keys():
        documents.append({'type': doc_type, 'number': doc_num, "name": name})
        directories[str(doc_shelf)].append(doc_num)
        print(documents)
        print(directories)
    else:
        print("Такой полки не существует!")
def com_users():
    for i in documents:
        key_list = list(i.keys())
        assert 'name' in key_list, 'У документа не указан владелец!'
        val_list = list(i.values())
        print(val_list[2])
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "none", "number": "none"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
command = input('Введите команду (l, s, p, a, u): ')
lets_go(command)