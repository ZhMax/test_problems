"""
Поставленная задача о нахождении друзей для пикника может быть разбита на две подзадачи.
Первая подзадача заключается в поиске компонент связности неориентированного графа.
Вторая подзадача состоит в раскрашивании вершин связного неориентированного графа таким образом,
чтобы любые две смежные вершины графа не имели одинаковый цвет.

После реешния поставленных подзадач в каждой компоненте связности исходного графа возьмем
группу из наибольшего количества вершин, раскрашенных в один цвет, и объединим их.
Полученное множество вершин исходного графа будет решением всей задачи. 

Для решения первой поставленной подзадачи будем использовать алгоритма поиска в глубину,
для рашения второй подзадачи - "жадный" алгоритм.
"""

import sys
sys.path.append('./usermodules')

import usermodule_graph as um
import random

def dfs(graph, component, v, visited_vertices):
    """
    Рекуррентная функция, которая возвращает список вершин,
    принадлежащих одной компоненте связности графа.

    Parameters
    ----------
    graph : GraphClass
        Граф, являющийся объектом класса GraphClass, в котором
        он задается словарем смежности
    component : list
        Список вершин, принадлежащих одной компоненте 
        связности графа
    v : int
        Индекс вершины графа, которая еще не была посещена
    visited_vertices : dict
        Словарь, который содержит информацию о том,
        были ли посещена вершина, которая задается своим 
        индексом.

    Returns
    -------
    component : list
    """
    
    visited_vertices[v] = True #отмечаем, что вершина v мы посетили
    component.append(v) 

    #рассматриваем вершины, которые смежные с вершиной v
    #если какую то из них еще не посетили вновь вызываем 
    #функцию dfs
    for adj_v in graph.adjacency_dict[v]:
        
        if visited_vertices[adj_v] == False:

            component = dfs(graph, component, adj_v, visited_vertices)
    
    return component

def find_connected_components(graph):
    """
    Функция, возвращающася список компонент связности графа

    Идея алгоритма следюущая. Изначально все вершины помечены
    как непосещенные. Берем вершину графа, которую еще не посетили
    и осуществляем от нее обход графа в глубину по смежным вершинам,
    помечая их как посещенные. Если все вершины посетили, то получаем
    компоненту связности графа, и рассматриваем другие вершины, которые
    еще не посетили. Если таких вершин нет, то найдены все компоненты
    связности.

    Parameters
    ----------
    graph : GraphClass
        Граф, являющийся объектом класса GraphClass, в котором
        он задается словарем смежности

    Returns
    -------
    connected_components : list
        Список, содержащий в себе связные подграфы исходного графа
    """

    #словарь 
    visited_vertices = {v: False for v in graph.vertices}
    connected_components = []

    #Осуществляем цикл по вершинам и проверяем условие
    #были ли они посещены.
    for v in graph.vertices:
        if visited_vertices[v] == False:
            component = []
            #Вызов рекурсивной функции
            component = dfs(graph, component, v, visited_vertices)
            #Создаем связный подграф
            subgraph = um.GraphClass({v: graph.adjacency_dict[v] for v in component})
            connected_components.append(subgraph)
    
    return connected_components

def graph_coloring(graph, color_label='c'):
    """
    Функция, возвращающая словарь из индексов вершин и меток цветов,
    построенный таким образом, что любые две смежные вершины раскрашены
    в разные цвета.  

    Идея алгоритма следующая:
    1) Сначала все вершины графа упорядочиваются по невозрастанию степеней,
    2) Берется вершина с максимальной степенью и ей назначается первый цвет,
    а у вершин смежных с ней, данный цвет исключается из списка возможных.
    3) Повторяем шаг 2 для оставшихся вершин.

    Замечания.
    1) Известно, что "жадный алгоритм" находит раскраску связного графа 
    не более чем в max_degree + 1 цветов, где max_degree - максимальная степень вершин графа.
    Поэтому максимальное количество цветов всегда можно задать.
    2) Для того чтобы сократить число шагов уже раскрашенная вершина, исключается из списков
    смежности вершин, смежных с ней.

    Parameters
    ----------
    graph : GraphClass
        Граф, являющийся объектом класса GraphClass, в котором
        он задается словарем смежности
    color_label : str
        символ (строка) стоящий перед порядковыми номерами цветов, 
        в которые раскрашиваются вершины графа.

    Returns
    -------
    vertices_color : dict
        Словарь ключами, в котором являются индексы вершин графа,
        а значениями метка цвета, в который она может быть раскрашена
    """

    #Копируем словарь смежности графа.
    #копирование выполняется для того, чтобы в дальнейшем можно было удалять
    #уже раскрашенные вершины из словаря смежности
    adjacency_dict_copy = {v: graph.adjacency_dict[v].copy() \
                           for v in graph.adjacency_dict}
    
    #вычисляем степени вершин и упорядочиваем их, по невозрастанию их степеней
    vertices_degree = {v: len(adjacency_dict_copy[v]) for v in adjacency_dict_copy}
    vertices_degree = sorted(vertices_degree.items(), key=lambda x: x[1], reverse=True)
    vertices_degree = dict(vertices_degree)

    #создаем список допустимых цветов, учитывая, что "жадный алгоритм" находит раскраску графа 
    #не более чем в max_degree + 1 цветов, где max_degree - максимальная степень вершин графа
    max_degree = max(list(vertices_degree.values()))
    color_list = [color_label + str(i) for i in range(max_degree + 1)]
    vertices_available_colors = {v: color_list.copy() for v in adjacency_dict_copy}

    #Словарь, хранящий цвет каждой вершины
    vertices_color = {}

    #Цикл по вершинам графа
    for v in vertices_degree:
        #Присваиваем первый из доступных цветов вершине v
        v_color = vertices_available_colors[v][0] 
        vertices_color[v] = v_color

        #Цикл по вершинам смежным вершине v
        for adj_v in adjacency_dict_copy[v]:
            
            #Если цвет v_color входит в список цветов vertices_available_colors,
            #доступных для смежной вершины adj_v,
            #то исключаем его из списка, а саму вершину v исключаем из списка смежности 
            #вершины adj_v
            if v_color in vertices_available_colors[adj_v]:
                vertices_available_colors[adj_v].remove(v_color)
                adjacency_dict_copy[adj_v].remove(v)

    vertices_color = sorted(vertices_color.items(), key=lambda x: x[0])
    vertices_color = dict(vertices_color)

    return vertices_color


def invert_dict(dict_in, sort=True):
    #Функция, которая меняет местами ключи и значения в словаре dict_in
    
    dict_out = {}
    for key, value in dict_in.items():
        dict_out.setdefault(value, list()).append(key)

    #Сортировка по количеству элементов в списках значений
    if sort:
        dict_out = sorted(dict_out.items(), key=lambda x: len(x[1]), reverse=True)
        dict_out = dict(dict_out)
    
    return dict_out

def get_friends_names(graph, saving_path=None):
    """
    Функция, которая возвращает список имен максимального количества
    друзей, не связанных друг с другом ребрами на графе

    Parameters
    ----------
    graph : GraphClass
        Граф, являющийся объектом класса GraphClass, в котором
        он задается словарем смежности
    saving_path : str
        Путь к директории для сохранения результатов

    Returns
    -------
    friends_names : list
        Список имен максимального количества друзей,
        не связанных друг с другом ребрами на графе
    """

    #Поиск компонент связности
    connected_graphs = find_connected_components(graph)
    
    #словарь для хранения индексов вершин исходного графа
    #и меток цветов, в которые они могут быть раскрашены
    vertices_colors = {} 

    #Список для хранения групп, с наибольшим количеством вершин,
    #которые можно раскрасить в один цвет, для каждой компоненты
    #связности графа
    chosen_vertices = []

    #цикл по связным подграфам исходного графа
    for i, subgraph in enumerate(connected_graphs):
        #поиск раскраски для связного подграфа
        subgraph_colors = graph_coloring(subgraph, color_label=f'c_{i}_')
        vertices_colors.update(subgraph_colors)

        #поиск группы с наибольшим количеством вершин,
        #которые можно раскрасить в один цвет
        largest_group_vertices = list(invert_dict(subgraph_colors).values())[0]

        chosen_vertices.extend(largest_group_vertices)

    friends_names = [graph.vertices_weight_dict[v] for v in chosen_vertices]
    print(f'Друзья, которых можно пригласить {friends_names}')

    if saving_path is not None:
        with open(saving_path+'.txt', 'a+', encoding='utf-8') as f:
            f.write(str(friends_names) + '\n')
    graph.get_image(vertices_colors, saving_path=saving_path+'_colors.png')
    
    return friends_names

def main():
    #Загрузка файла с именами друзей
    with open('names.txt', 'r', encoding='utf-8') as f:
        names_list = f.read().splitlines()

    #Директория для хранения результатов
    saving_path = './results/'

    #Проверка алгоритма решения задачи на заданном графе
    adjacency_dict = {0: [4], 1: [4, 3], 4:[0, 1, 2, 3], 5: [3], 2: [4], 3: [1, 5, 4]}
    graph = um.GraphClass(adjacency_dict)
    for v in graph.vertices:
        random.choice(names_list)
        graph.assign_weight_to_vertex(v, random.choice(names_list))

    with open(saving_path + 'prescribed_graph.txt', 'w', encoding='utf-8') as f:
            f.write(str(graph) + '\n')

    get_friends_names(graph, saving_path=saving_path+'prescribed_graph')

    #Проверка алгоритма решения задачи на заданном графе c несколькими компонентами связности
    adjacency_dict = {0: [1, 3], 1: [0], 3: [0, 2], 2: [3], 4: [5], 5: [4], 6: []}
    graph = um.GraphClass(adjacency_dict)
    for v in graph.vertices:
        random.choice(names_list)
        graph.assign_weight_to_vertex(v, random.choice(names_list))
    
    with open(saving_path + 'prescribed_graph_several_components.txt', 'w', encoding='utf-8') as f:
            f.write(str(graph) + '\n')

    get_friends_names(graph, saving_path=saving_path+'prescribed_graph_several_components')

    #Проверка алгоритма на случайных графах
    for num_example in range(0, 8):
        print(f'Пример {num_example}')
        graph = um.GraphClass.create_random_graph()
        for v in graph.vertices:
            random.choice(names_list)
            graph.assign_weight_to_vertex(v, random.choice(names_list))

        with open(saving_path + f'random_graph_{num_example}.txt', 'w', encoding='utf-8') as f:
            f.write(str(graph) + '\n')
        get_friends_names(graph, saving_path=saving_path+f'random_graph_{num_example}')
    
    

if __name__ == '__main__':
    main()
