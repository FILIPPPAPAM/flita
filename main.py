def input_graph_vertexes():
    graph = {}
    try:
        count_vertexes = int(input('Количество вершин в графе: '))
        vertexes = ''
        for i in range(count_vertexes):
            keys = sorted(graph)
            vertex = input('Имя: ')
            if ((len(vertex) != 1) or (vertex in keys)):
                while ((len(vertex) != 1) or (vertex in keys)):
                    print('Введите уникальное имя, состоящее из одного символа')
                    vertex = input('Имя: ')

            graph[vertex] = []
        for i in sorted(graph):
            vertexes += i
    except:
        print('Ошибка')
    return graph, vertexes


def input_graph_edges(graph, vertexes):
    try:
        print('Введите одно или несколько слов через пробел.')
        print('Формат слова - первая буква - имя вершины')
        print('Все последующие - связи')
        edges = input('Ввод :').split()
        for i in edges:
            vertex = i[0]
            if (vertex in vertexes):
                array1 = []
                edges_split = i[1:]
                for j in edges_split:
                    if j in vertexes and vertex != j:
                        graph[vertex].append(j)
                        graph[j].append(vertex)
        for j in graph:
            graph[j] = sorted(set(graph[j]))
    except:
        print(':(')

    return 0


def output(graph, vertexes):
    count_vertexes = len(vertexes)
    ttt = []
    for i in range(count_vertexes):
        t = []
        q1 = vertexes[i]

        for j in range(count_vertexes):
            q2 = vertexes[j]
            if i == j:
                t.append('0')
            elif q2 in graph[q1]:
                t.append('1')
            else:
                t.append('0')
        ttt.append(t)
    ww = sorted(graph)

    print('   ' + ' '.join(ww))
    print('  ' + ' _' * count_vertexes)

    for i in range(count_vertexes):
        print(ww[i] + '|', end='')
        for j in range(count_vertexes):
            print(' ' + ttt[i][j], end='')
        print()
    print()
    for i in graph:
        print(i, ' :', graph[i])


def main():
    try:
        graph, vertexes = input_graph_vertexes()
        input_graph_edges(graph, vertexes)
        output(graph, vertexes)
    except:
        print('\n:(')


main()
