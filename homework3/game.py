import random
from itertools import permutations
import os

def generate_pole(size_y, size_x, fill_with):
    return [[fill_with for _ in range(size_x)] for _ in range(size_y)]

def show_pole(pole):
    for i in pole:
        print(*i)

def is_step_available(yy, xx):
    if 0 <= yy <= size_y - 1 and 0 <= xx <= size_x - 1: return True
    return False

def one_step(yy, xx, num_steps):
    for _ in range(num_steps):
        while True:
            goto = input('Введите, куда пойти: ')
            steps_vocab = {
                'u': [yy-1, xx],
                'd': [yy+1, xx],
                'r': [yy, xx+1],
                'l': [yy, xx-1]
            }
            if goto in steps_vocab.keys() and is_step_available(*steps_vocab[goto]):
                yy, xx = steps_vocab[goto]
                break
            else:
                print('Введено неверное значение. Повторите попытку')
    return yy, xx

def sort_invent(bag, reverse=False):
    return sorted(bag, reverse=reverse)

def find_in_invent(bag, to_find, way_to_search=0):
    '''вернет bool, если 0 способ поиска, индекс элемента или сообщение, если другой способ поиска'''
    if way_to_search == 0:
        return to_find in bag
    else:
        try:
            return bag.index(to_find)
        except:
            print('Элемент не найден в инвентаре')

def copy_list(l):
    return l[::]

def clear():
    '''очистка терминала'''
    os.system('cls' if os.name=='nt' else 'clear')

def show_instructions():
    print('''
    Вы попали в лабиринт. Вам нужно выйти из него. Внутри вас встретят:
        1. монстр (s)
        2. ключ (k)
        3. портал (p)
        4. ловушка (l)
        5. меч (s)
        6. выход (e)
          
    Чтобы ходить, используйте команды ниже:
        u - вверх
        d - вниз
        r - вправо
        l - влево
    ''')


if __name__ == "__main__":
    y, x = 0, 0  # точка старта игрока
    size_y, size_x = 5, 5  # размеры игрового поля
    game = True
    invent = []  # инвентарь
    health = 3 # количество жизней у персонажа
    prevp = False

    # требования по функционалу
    bag = []  # сумка, чтобы собирать\выбрасывать предметы
    # sort_invent(bag) - возвращает отсортированный по убыванию/возрастанию инвентарь
    # find_in_invent(bag, 's', 1) - поиск в инвентаре
    # copy_list(bag) - вернет копию инвентаря


    admin, player = generate_pole(size_y, size_x, ' '), generate_pole(size_y, size_x, '.')
    player[0][0] = 'Я'

    # задаем позиции игровых элементов поля
    admin[1][1] = 'm'
    admin[0][2] = 'k'
    admin[0][4] = 'p'
    admin[4][0] = 'l'
    admin[2][1] = 's'
    admin[4][4] = 'e'

    """perm = list(permutations(range(size_y), 2))
    perm.append((size_y-1, size_x-1))
    for p in 'mkpels':
        xx, yy = random.choice(perm)
        perm.remove((xx, yy))
        admin[yy][xx] = p"""

    show_pole(player)
    show_instructions()

    while game:
        steps = random.randint(0, 6)  # количество шагов
        print(f'Количество шагов: {steps}')
        pry, prx = y, x
        y, x = one_step(y, x, steps)
        clear()  # очистка терминала
        if admin[pry][prx] in 'mkpels':
            player[pry][prx] = admin[pry][prx]
        else:
            player[pry][prx] = '*'

        if admin[y][x] == 'm':
            if find_in_invent(bag, 's'):
                print('Ты победил монстра!!!')
            else:
                health -= 1
                print(f'Ты попал к монстру!!!\nТебе нужен мечь, чтобы его победить.\nКоличество твоих жизней уменьшено до: {health}')
        elif admin[y][x] == 'k':
            if not find_in_invent(bag, 'k'):
                print('Ты нашел ключ!!!\nТеперь ты можешь выйти из лабиринта')
                bag.append('k')
            else:
                print('Ты уже был в этой клетке!!! Тут лежит ключ.\nПопав на нее второй раз, ты выбросил его из инвентаря!!!\nУ тебя больше нет ключа')
                bag.remove('k')
        elif admin[y][x] == 'p':
            print('Ты попал в портал!!!\nТвое местоположение изменено случайным образом')
            pry, prx = y, x
            y, x = random.randint(0, size_y-1), random.randint(0, size_x-1)
            prevp = True
        elif admin[y][x] == 'e':
            if find_in_invent(bag, 'k'):
                print('Ты победил!!!')
                game = False
            else:
                print('Ты нашел выход!!!\nТебе нужен ключ, чтобы выйти из лабиринта')
        elif admin[y][x] == 'l':
            health -= 1
            print(f'Ты попал в ловушку!!!\nКоличество твоих жизней уменьшено до: {health}')
        elif admin[y][x] == 's':
            if not find_in_invent(bag, 's'):
                print('Ты нашел мечь!!!\nТеперь ты можешь победить монстра')
                bag.append('s')
            else:
                print('Ты уже был в этой клетке!!! Тут лежит мечь.\nПопав на нее второй раз, ты выбросил мечь из инвентаря.\nУ тебя больше нет меча')
                bag.remove('s')


        player[y][x] = 'Я'  # посетили клетку
        show_pole(player)
        if prevp:
            player[pry][prx] = 'p'
            prevp = False

        if health == 0: 
            print('У тебя не осталось жизней.\nТы остался в лабиринте навсегда')
            game = False
        print()