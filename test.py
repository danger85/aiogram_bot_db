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
#print(book)

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


### ЗАДАНИЕ: Уменьшить размер data, типа  numpy.ndarray, имеющего 60 объектов,
###  каждый из которых имеет 10 признаков с помощью библиотеки sklearn. Параметр  PCA svd_solver="full"

import numpy as np
from sklearn.decomposition import PCA
# Замените data на ваш массив данных, содержащий 60 объектов с 10 признаками
data = np.genfromtxt("37_25.csv", delimiter=',', skip_header=0)

""" #Создайте экземпляр класса PCA и укажите параметр svd_solver="full":
pca = PCA(svd_solver="full")

#Произведите анализ PCA на ваших данных:
pca.fit(data)

#Определите, сколько главных компонент вы хотите оставить, установив параметр n_components.
# Например, если вы хотите уменьшить размерность до 4 компонент, установите n_components=4:
n_components = 4

#Примените PCA для уменьшения размерности данных:
reduced_data = pca.transform(data)[:, :n_components]

# Теперь reduced_data содержит ваши данные с уменьшенной размерностью.
# Размерность данных была уменьшена до n_components, в данном случае до 4 компонент.
# Вы можете изменить n_components на любое другое число в соответствии с вашими потребностями.

# Заметьте, что PCA позволяет уменьшить размерность данных, удаляя наименее важные компоненты.
# Важность компонент определяется их объясняемой дисперсией.
# Вы можете получить информацию о доле объясненной дисперсии каждой компоненты с помощью атрибута explained_variance_ratio_:

explained_variance = pca.explained_variance_ratio_
print(type(explained_variance),explained_variance, sum(explained_variance))
sum_of_explained_variance=0
i=0
while sum_of_explained_variance<=0.85:
    sum_of_explained_variance+=explained_variance[i]
    i+=1
print("Какое минимальное количество главных компонент необходимо использовать, чтобы доля объясненной дисперсии превышала 0,85? ->", i)
print(reduced_data) """

"""
В предложенном файле находятся синтетические данные. Данные описывают 60 объектов, каждый из которых обладает 10 признаками.
Ваша задача, используя метод главных компонентов и библиотеку slkearn,  перейти к новым координатам и найти следующие параметры:
        1)координату первого объекта относительно первой главной компоненты.
        2)координату первого объекта относительно второй главной компоненты
        3) найти долю объясненной дисперсии при использовании двух главных компонент.
"""

#Для нахождения координат первого объекта относительно первой и второй главных компонент и
# доли объясненной дисперсии при использовании двух главных компонент с использованием
# библиотеки scikit-learn (sklearn), вы можете выполнить следующие шаги:

#Примените метод главных компонент (PCA) к данным и укажите количество компонент, которые вы хотите оставить (в данном случае 2).
n_components = 2
pca = PCA(n_components, svd_solver="full")
reduced_data = pca.fit_transform(data)
print(reduced_data)
#Теперь вы можете получить координаты первого объекта относительно первой и второй главных компонент:

first_object_coordinates = reduced_data[0]
coordinate_1 = first_object_coordinates[0]  # Координата относительно первой главной компоненты
coordinate_2 = first_object_coordinates[1]  # Координата относительно второй главной компоненты
print("Координата относительно первой главной компоненты->",coordinate_1)
print("Координата относительно второй главной компоненты->",coordinate_2)


#Чтобы узнать долю объясненной дисперсии при использовании двух главных компонент, вы можете воспользоваться атрибутом explained_variance_ratio_ объекта PCA:
explained_variance = pca.explained_variance_ratio_
explained_variance_2_components = np.sum(explained_variance)
print("Доля объясненной дисперсии при использовании двух главных компонент->",explained_variance_2_components)

pca2=PCA()
reduced_data2=pca2.fit_transform(data)
explained_variance_of_all_data = pca2.explained_variance_ratio_
sum=0
i=0
for each_variance in explained_variance_of_all_data:
    sum+=each_variance
    i+=1
    if sum>=0.85:
        break
print("Какое минимальное количество главных компонент необходимо использовать, чтобы доля объясненной дисперсии превышала 0,85?->", i)

#Для определения количества групп объектов на основе первых двух главных компонент,
# вы можете использовать метод "локтя" (Elbow Method) вместе с K-средними.
# Этот метод поможет вам выбрать оптимальное количество кластеров.

#Импортируйте необходимые библиотеки:

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
#Создайте объект KMeans с разным количеством кластеров (например, от 1 до 10)
# и вычислите инерцию (сумму квадратов расстояний от каждой точки до центра ближайшего кластера) для каждого случая:

inertias = []

for n_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(reduced_data)
    inertias.append(kmeans.inertia_)
#Постройте график инерции от количества кластеров:

plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()
# По графику инерции найдите "локоть" (точку, где инерция начинает уменьшаться менее резко).
# Это может помочь вам определить оптимальное количество кластеров.
# В данном случае, количество групп объектов будет определяться количеством кластеров.
# Когда вы определите оптимальное количество кластеров,
# вы сможете использовать K-средних или другие методы кластеризации для разделения объектов
# на соответствующие группы на основе первых двух главных компонент.