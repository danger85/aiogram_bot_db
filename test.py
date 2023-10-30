text = 'Раз. Два. Три. Четыре. Пять. Прием!'
text2 = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
text3 = '— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, то всё дело в том, что вы сами не знали, в чём вопрос.'
text4 = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'

import os
def _get_part_text(text,start,lenght):
    sym=[".",",",":","!","?",";"]
    #print("Len of text is ", len(text), " desired lenght is ", lenght)
    txt=text[start:start+lenght]
    rest_len=len(text[start+lenght:])
    offset=0
    for i in range(rest_len):
        if text[start+lenght+i] in sym:
            offset+=1
        if i>=2:
            break

    if txt[-1] in sym:
        if offset==0:
            return txt, len(txt)
        else:
            txt=txt[:-offset-1]
    last_sym_pos=0
    for each_sym in sym:
        cur_last_sym_pos=txt.rfind(each_sym)
        if cur_last_sym_pos>last_sym_pos:
            last_sym_pos= cur_last_sym_pos
    #print(txt[last_sym_pos-1],txt[last_sym_pos])

    txt=txt[0:last_sym_pos+1]

    return txt, len(txt)

# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 100


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    book_text = open(path, 'r',encoding='utf-8').read()
    start=0
    lenght=100
    i=1
    while start<len(book_text) :
        book[i] =_get_part_text(book_text,start,lenght)[0].lstrip()
        start+=_get_part_text(book_text,start,lenght)[1]
        i+=1

prepare_book("book.txt")
print(book)

"""
book = {1: 'Пошлость собственной мечты была так заметна, что Таня понимала:',
        2: 'даже мечтать и горевать ей приходится закачанными в голову штампами, и по-другому не может быть,',
        3: 'потому что через все женские головы на планете давно проложена ржавая узкоколейка,',
        4: 'и эти мысли — вовсе не ее собственные надежды,',
        5: 'а просто грохочущий у нее в мозгу коммерческий товарняк.',
        6: 'Словно бы на самом деле думала и мечтала не она,',
        7: 'а в piпустом осеннем сквере горела на стене дома огромная панель,',
        8: 'показывая равнодушным жирным воронам рекламу бюджетной косметики.'}
"""
l=[10, 20, 30, 40, 50]
print(sum([i for i in l])/len(l))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

list3=[]
list3.append([i for i in list1 if i in list2])
print(*list3)

row_name = ["Валюта", "операция", "до 200", "<10.000", ">10.000"]
for x,i in enumerate(row_name):
    print("x is number = ",x)
    print("i is value = ",i)