import random
import math

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class GraphClass(object):
    """
    Класс для создания и модификации неориентированного графа.
    Граф определяется списком смежности, в котором каждой вершине графа
    ставится в соответстствие список смежных с ней вершин. 
    В списке каждая вершина графа, кодируется положительным целочисленным индексом. 
    Также вершинам графа может быть присвоена некоторая дополнительная информация.


    Attributes
    ----------
    adjacency_dict : dict
        Список смежности неориентированного графа, для которого в коде python
        используется тип данных dictionary. Каждый ключ (key) словаря соответствует
        вершине графа. Значения словаря (value) представляют собой списки (list),
        хранящие смежные вершины.
        Для того чтобы избежать двусмысленности далее "cписок смежности графа" будем называть
        "cловарь смежности графа", а список, хранящий вершины смежные с данной вершиной 
        будем называть "список смежности вершины".
    vertices : list
        Список вершин графа
    vertices_weight_dict : dict
        Словарь для хранения информации, присвоенной каждой вершине графа
    edges : list 
        Список ребер графа. Каждое ребро задается кортежом (tuple) вершин графа
    
    Methods
    -------
    create_random_methods(vertices_num=None, edges_num=None)
        Классовый метод для создания случайного графа

    is_vertex_in_graph(vertex_idx)
        Метод для проверки принадлежит ли вершина графу
    are_vertices_in_graph(vertices_idx)
        Метод для проверки принадлежит ли список вершин графу
    is_edge_in_graph(edge)
        Метод для проверки принадлежит ли ребро графу

    assign_weight_to_vertex(vertex_idx, vertex_weight)
        Метод для присвоения вершине дополнительной информации
    add_vertex(adjacent_vertices, vertex_weight=None)
        Метод для добавление к графу новой вершины
    add_edge(vertex_idx1, vertex_idx2)
        Метод для добавления ребра между двумя вершинами
    get_image(vertex_colors=None, color_palette=mcolors.TABLEAU_COLORS, 
              figsize=(5, 5), saving_path=None)
        Метод для отрисовки графа с использованием библиотеки matplotlib
    """

    def  __init__(self, adjacency_dict, vertices_weight_dict=None):

        if adjacency_dict is not None:
            #Формирование списка вершин
            self.vertices = sorted(list(set(adjacency_dict.keys())))
            #Формирование словаря смежности
            self.adjacency_dict = {v: sorted(list(set(adjacency_dict[v]))) \
                                   for v in self.vertices}
        else:
            self.adjacency_dict = {None : []}
            self.vertices = []


        #Формирование словаря для информации, которая содержится в вершинах
        if vertices_weight_dict is None:
            self.vertices_weight_dict = {v: None \
                                         for v in self.vertices}
        else:
            self.vertices_weight_dict = {v: vertices_weight_dict[v] \
                                         for v in self.vertices}

        #Формирование списка ребер графа
        self.edges = []
        for vertex in self.adjacency_dict:
            for adj_vertex in self.adjacency_dict[vertex]:
                edge = tuple(sorted((vertex, adj_vertex)))
                if edge not in self.edges:
                    self.edges.append((vertex, adj_vertex))
    
    def __str__(self):
        adjacency_dict_ext = {(v, self.vertices_weight_dict[v]): self.adjacency_dict[v] \
                              for v in self.adjacency_dict}
        adjacency_dict_str = str(adjacency_dict_ext)
        adjacency_dict_str = adjacency_dict_str.replace('{', '')
        adjacency_dict_str = adjacency_dict_str.replace('}', ';')
        return adjacency_dict_str

    @classmethod 
    def create_random_graph(cls, vertices_num=None, edges_num=None):
        """
        Классовый метод для создания случайного графа.
        Граф задается путем списка смежности. Количество вершин и ребер графа
        определяется случайно либо может быть задано.

        Parameters
        ----------
        vertices_num : int
            Количество вершин графа. 
            Предполагается число большее либо равное 2
        edges_num : int
            Количество ребер графа
        
        Returns
        -------
        cls(adjacency_dict, vertices_weight_dict)
            Возвращается объект класса

        """
        #Если количество вершин не задано, то оно определяется случайным значением
        if vertices_num is None:
            vertices_num = random.randint(2, 10)

        vertices_list = [i for i in range(vertices_num)]

        #Если количество ребер не задано, то оно определяется случайным значением.
        #Максимальное случайное значение определяется количеством ребер в полном графе,
        #состоящем из vertices_num вершин
        if edges_num is None:
            max_edge_num = vertices_num * (vertices_num - 1) / 2
            edges_num = random.randint(1, max_edge_num)

        #Создание словаря смежности для неориентированного графа
        #со случайными связями между вершинами
        adjacency_dict = {v: [] for v in sorted(vertices_list)}
        for _ in range(edges_num):
            v1 = random.choice(vertices_list)
            v2 = random.choice(vertices_list)

            #Условие для исключения петель в случайном графе
            if v1 != v2:
                adjacency_dict[v1].append(v2)
                adjacency_dict[v2].append(v1)

        adjacency_dict = {v: sorted(list(set(adjacent_v))) \
                          for v, adjacent_v in adjacency_dict.items()}
        
        #Информация в вершины добавляется в виде случайного числа 
        #из равномерного распределения U(0, 1)
        vertices_weight_dict = {v: round(random.uniform(0, 1), 2) \
                                for v in adjacency_dict.keys()}

        return cls(adjacency_dict, vertices_weight_dict)

    def is_vertex_in_graph(self, vertex_idx):
        """
        Метод для проверки принадлежит ли графу вершина с индексом vertex_idx
        """

        if vertex_idx in self.vertices:
            return True
        else:
            #print('Вершина не принадлежит графу!')
            return False
    
    def are_vertices_in_graph(self, vertices_idx):
        """
        Метод для проверки все ли вершины из списка vertices_idx
        принадлежат графу
        """

        if (set(vertices_idx) <= set(self.vertices)):
            return True
        else:
            #print('Одна или несколько вершин не принадлежит графу!')
            return False
        
    def is_edge_in_graph(self, edge):
        """
        Метод для проверки принадлежит ли графу ребро edge,
        заданное кортежом (tuple) из индексов двух вершин
        """

        if tuple(sorted(edge)) in self.edges:
            return True
        else:
            #print('Вершина не принадлежит графу!')
            return False


    def assign_weight_to_vertex(self, vertex_idx, vertex_weight):
        """
        Метод для присвоения вершине графа с индексом vertex_idx 
        информации vertex_weight
        """

        if self.is_vertex_in_graph(vertex_idx):
            self.vertices_weight_dict[vertex_idx] = vertex_weight
        else:
            print('Вершина не принадлежит графу!')


    def add_vertex(self, adjacent_vertices, vertex_weight=None):
        """
        Метод для добавление к графу вершины, смежной с вершинами из списка adjacent_vertices
        и содержащей информацию vertex_weight.
        Индекс новой вершины определяется автоматически, как максимальный индекс вершин 
        графа плюс 1.
        """

        if self.are_vertices_in_graph(adjacent_vertices):
            #Вычисление индекса новой вершины
            last_vertex_idx = max(list(self.adjacency_dict.keys())) + 1

            #Добавление вершины в словарь смежности вместе со списком
            #смежных с ней вершин
            self.adjacency_dict[last_vertex_idx] = adjacent_vertices
            self.adjacency_dict[last_vertex_idx].sort()
            self.vertices.append(last_vertex_idx)

            #Добавление новой вершины в списки смежности вершин из adjacent_vertices
            for adj_v_idx in adjacent_vertices:
                self.adjacency_dict[adj_v_idx].append(last_vertex_idx)
                edge = (adj_v_idx, last_vertex_idx)
                self.edges.append(edge)
            
            #Присвоение вершине информации
            self.assign_weight_to_vertex(last_vertex_idx, vertex_weight)

        else:
            print('Указанные смежные вершины не принадлежат графу!')

    def add_edge(self, vertex_idx1, vertex_idx2):
        """
        Метод для соединения вершин с индексами vertex_idx1 
        и vertex_idx2 ребром.
        """
       
        if not self.are_vertices_in_graph([vertex_idx1, vertex_idx2]):
            print('Указанные вершины не принадлежит графу!')
            return None
        
        if not self.is_edge_in_graph((vertex_idx1, vertex_idx2)):
            edge = tuple(sorted((vertex_idx1, vertex_idx2)))
            
            #добавление нового ребра в список всех ребер графа
            self.edges.append(edge) 

            #изменение словаря смежности, путем
            #добавление вершин в списки смежности друг друга
            self.adjacency_dict[vertex_idx1].append(vertex_idx2)
            self.adjacency_dict[vertex_idx1].sort()

            self.adjacency_dict[vertex_idx2].append(vertex_idx1)
            self.adjacency_dict[vertex_idx2].sort()

        else:
            print('Ребро уже существует!')

    def get_image(self, vertices_colors=None, 
                  color_palette=mcolors.TABLEAU_COLORS, figsize=(5, 5),
                  saving_path=None):
        """
        Метод для отрисовки графа с использованием библиотеки matplotlib.
        Вершины графа располагаются по окружности так, что индекс вершин
        увеличивается по часовой стрелке.

        Parameters
        ----------
        vertices_colors : dict
            Словарь, ключами в котором явлются индексы вершин графа,
            а значениями метка цвета (произвольная строка). 
            Вершины с одинаковой меткой раскрашиваются в один цвет.
        color_palette : matplotlib.colors
            Цветовая палитра из библиотеки matplotlib
        figsize : tuple
            Кортеж для указания размеров изображения в дюймах
        saving_path : str
            Путь, содержащий имя файла, для сохранения изображения
        """

        if len(self.vertices) == 0:
            print('В графе нет вершин!')
            return
        
        vertices_num = len(self.vertices) #Количество вершин

        PI = math.pi #константа pi
        R = 1 #радиус окружности

        phi0 = PI / 2 #угол, с которого начинается отрисовка вершин с 0 индексом

        #углы отклонений от начального угла для отрисовки последующих вершин
        dphi_list = [2*PI * i / vertices_num for i in range(0, vertices_num)] 

        #Построение словаря с декартовыми координатами вершин для их отрисовки 
        #на графике
        x_coords = [R * math.cos(phi0 - dphi_i) for dphi_i in dphi_list]
        y_coords = [R * math.sin(phi0 - dphi_i) for dphi_i in dphi_list]
        vertices_coords= {self.vertices[idx]: (x_coords[idx], y_coords[idx]) \
                                 for idx in range(vertices_num)}

        #Построение изображения
        plt.figure(figsize=figsize)
        #Если цвета вершин не указаны, то они раскрашиваются в один цвет,
        #иначе они будут раскрашены в цвета из палитры color_palette
        if vertices_colors is None:
            
            #изображаем вершины
            plt.scatter(x_coords, y_coords, s=3, alpha=0.7, c=color_palette['tab:cyan'])            
            for idx in vertices_coords:
                plt.text(vertices_coords[idx][0], 
                        vertices_coords[idx][1],
                        str(self.vertices[idx]) + ' | ' + str(self.vertices_weight_dict[idx]),
                        fontdict={'color': 'black', 'fontsize': 10},
                        bbox = {'facecolor': color_palette['tab:cyan'], 
                                'alpha': 0.7, 
                                'boxstyle': 'circle, pad=0.3', 'ec': 'black'},
                        va='center',
                        ha='center')
        else:
            color_palette_val = list(color_palette) 
            
            #словарь для связи меток цвета из vertices_colors с
            #цветами из палитры color_palette
            marker_colors = {} 
            for i, vertex_c in enumerate(vertices_colors.values()):
                marker_colors[vertex_c] = color_palette_val[i]

            #цикл по индексам вершин
            for idx in vertices_colors:
                #назначаем цвет, исходя из метки вершины
                vertex_c = vertices_colors[idx]
                c = marker_colors[vertex_c]

                #изображаем вершины
                plt.scatter(x_coords[idx], y_coords[idx], s=3, alpha=0.7, c=c)            
                plt.text(vertices_coords[idx][0], 
                        vertices_coords[idx][1],
                        str(self.vertices[idx]) + ' | ' + str(self.vertices_weight_dict[idx]),
                        fontdict={'color': 'black', 'fontsize': 10},
                        bbox = {'facecolor': c, 
                                'alpha': 0.7, 
                                'boxstyle': 'circle, pad=0.3', 'ec': 'black'},
                        va='center',
                        ha='center')
        
        #изображаем ребра
        if len(self.edges) > 0:
            for edge in self.edges:
                idx1, idx2 = edge
                x_axis = [vertices_coords[idx1][0], 
                          vertices_coords[idx2][0]]
                y_axis = [vertices_coords[idx1][1], 
                          vertices_coords[idx2][1]] 
                plt.plot(x_axis, y_axis, zorder=0)
        


        #plt.gca().set_aspect('equal')
        plt.axis('off')
        if saving_path is not None:
            plt.savefig(saving_path)
        plt.show()
