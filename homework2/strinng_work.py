def lvl1(s: str, method_up = False, method_low = False, method_cap = False) -> None:
    if method_up: print(f'upper: from - {s}, to - {s.upper()}')
    if method_low: print(f'lower: from - {s}, to - {s.lower()}')
    if method_cap: print(f'capitalize: from - {s}, to - {s.capitalize()}')

text_1 = 'прИвЕт МИР'

lvl1(text_1, method_up=True, method_low=True, method_cap=True)


def lvl2(s: str, method_find=False, to_find = '', 
         method_replace=False, replace_from = '', replace_to = '',
         method_count=False, to_count = '') -> None:
    if method_find: print(f'find: from - {s}, to_find - {to_find}, idx - {s.find(to_find)}')
    if method_replace: print(f'replace: from - {s}, to - {s.replace(replace_from, replace_to)}')
    if method_count: print(f'count: from - {s}, to_count - {to_find}, idx - {s.lower().count(to_count)}')

text_2 = 'Ботать - это круто. Очень круто!'

lvl2(text_2, method_find=True, to_find='круто')
lvl2(text_2, method_replace=True, replace_from='круто', replace_to='другое слово')
lvl2(text_2, method_count=True, to_count='о')

def lvl3(s: str, method_split=False, split_with='',
         method_join=False, join_with='', to_join=[]) -> None:
    if method_split: print(f'split: from - {s}, to - {s.split(split_with)}')
    if method_join: print(f'join: from - {to_join}, to -', f'{join_with}'.join(to_join))

text_3 = '1,2,3,4,5'
lvl3(text_3, method_split=True, split_with=',')
lvl3(text_3, method_join=True, join_with=';', to_join=text_3.split(','))

def lvl4(s: str, method_isdigit=False, method_isalpha=False, method_strip=False, to_strip=' ') -> None:
    if method_isdigit: print(f'isdigit: check - {s}, result - {s.isdigit()}')
    if method_isalpha: print(f'isalpha: check - {s}, result - {s.isalpha()}')
    if method_strip: print(f'strip: from - {s}, to - {s.strip(to_strip)}')

texts_4 = ['lop', 'lop**', '1234', '123p']
lvl4(texts_4[0], method_isalpha=True)
lvl4(texts_4[1], method_strip=True, to_strip='*')
lvl4(texts_4[2], method_isdigit=True)
lvl4(texts_4[3], method_isdigit=True)

def lvl5(s: str) -> None:
    print(' '.join(s.strip().split(';')).capitalize())

text_5 = '   pYthon;is;AWesome;   '
lvl5(text_5)