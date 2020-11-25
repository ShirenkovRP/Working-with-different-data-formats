# Написать программу, которая будет выводить топ 10 самых часто
# встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Написать программу для файла в формате xml.

import xml.etree.ElementTree as ET

# Извлечение данных из файла
tree = ET.parse("newsafr.xml")
root = tree.getroot()
new_xml = root.findall("channel/item")
data = []
for news in new_xml:
    data.append(news.find("description").text)
    
    
def top_world(arg):
    # Получение списка слов из новостей
    # и списка уникальных слов (множество)
    myset = set()
    world_list = []
    for items_list in arg:
        desc_list = items_list.split(" ")
        for i in desc_list:
            world_list.append(i)
            myset.add(i)

    # Получение списка уникальных слов в которых больше 6 символов
    top_list = []
    for world in myset:
        if len(world) > 6:
            top_list.append(world)

    # Составление словаря ключ уникальное слово,
    # значение количество повторений в новостях
    top_dict = {}
    for top in top_list:    
        top_dict[top] = world_list.count(top)

    # Сортировка словаря
    top_dict = list(top_dict.items())
    top_dict.sort(key=lambda k: k[1])
    top_dict.reverse()
    print("Toп - 10 самых частовстречающихся в новостях слов длиннее 6 символов ")

    # Вывод топ - 10 слов
    for i in range(0, 10):
        print(f"На {i + 1 } месте слово - {top_dict[i][0]}")    


top_world(data)
