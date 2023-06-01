import sys
sys.path.append('./usermodules')

import usermodule_graph as um

def main():
    #Определение графа посредством словаря смежности
    adjacency_dict = {0: [4], 1: [4, 3], 4:[0, 1, 3], 5: [3], 2: [], 3: [1, 5, 4]}
    vertices_weight_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

    graph = um.GraphClass(adjacency_dict, vertices_weight_dict)
    print(f'Словарь смежности: {graph.adjacency_dict}')
    print(f'Информация в вершинах {graph.vertices_weight_dict}')
    print(f'Список ребер {graph.edges}')

    print('отрисовка графа')
    graph.get_image()

    print('добавление вершины, смежной с вершинами [0, 5] с информацией "G"')
    graph.add_vertex([0, 5], 'G')
    print(graph.adjacency_dict)
    print(graph.vertices_weight_dict)

    print('добавление вершины, смежной с вершинами [0, 1, 3] с информацией "H"')
    graph.add_vertex([0, 1, 3], 'H')
    print(graph.adjacency_dict)
    print(graph.vertices_weight_dict)

    print('добавление информации "N" в вершину 0')
    graph.assign_weight_to_vertex(0, [graph.vertices_weight_dict[0], 'N'])
    print(graph.vertices_weight_dict)

    print('добавление ребра между вершинами 0, 2')
    graph.add_edge(0, 2)
    print(graph.edges)

    print('добавление уже существующего ребра') 
    graph.add_edge(5, 6)
    print(graph.edges)

    print('добавление ребра между несуществующими вершинами')
    graph.add_edge(5, 7)
    print(graph.edges)

    print('отрисовка графа')
    print(graph.adjacency_dict)
    graph.get_image()

    print('Граф из одной вершины')
    graph = um.GraphClass(adjacency_dict={0 : []})
    print(graph.adjacency_dict)
    graph.get_image()

    print('Пустой граф')
    graph = um.GraphClass(adjacency_dict=None)
    print(f'Словарь смежности: {graph.adjacency_dict}')
    graph.get_image()

    print('Создание случайного графа')
    graph = um.GraphClass.create_random_graph()
    print(f'Словарь смежности: {graph.adjacency_dict}')
    graph.get_image()

    print('Создание случайного графа без ребер')
    graph = um.GraphClass.create_random_graph(vertices_num=5, edges_num=0)
    print(f'Словарь смежности: {graph.adjacency_dict}')
    graph.get_image()

if __name__ == '__main__':
    main()