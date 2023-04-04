import csv

import matplotlib.pyplot as plt
import chardet
import pandas as pd
import networkx as nx


def shortest_path(graph, name1, name2):
    _shortest_path = nx.shortest_path(graph, name1, name2, weight='weight')
    # print(nx.shortest_path(g, "Hadiach", "Burshtyn", weight='weight'))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    path_edges = list(zip(_shortest_path, _shortest_path[1:]))
    nx.draw_networkx_nodes(graph, pos, nodelist=_shortest_path, node_color='r')
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)
    print("Shortest way is: ", _shortest_path)
    print("Shortest distance: ", nx.shortest_path_length(graph, name1, name2, weight='weight'))
    plt.show()
    return _shortest_path, nx.shortest_path_length(graph, name1, name2, weight='weight')


def main():
    with open("cities.csv", "rb") as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    df = pd.read_csv('cities.csv', encoding=encoding, header=None, sep=';',
                     dtype={'city 1': 'str', 'city 2': 'str', 'distance': 'int'})
    # df = pd.read_csv('cities.csv', encoding=encoding, header=None)
    # print(df.T[0])

    g = nx.Graph()

    df_transponded = df.T

    for idx in df_transponded:
        g.add_edge(df_transponded[idx][0], df_transponded[idx][1], weight=df_transponded[idx][2])
        # print(df_transponded[idx][2])

    pos = nx.spring_layout(g)
    nx.draw_networkx(g, pos)
    plt.title("Cities graph")
    plt.show()

    try:
        print(shortest_path(g, "Hadiach", "Burshtyn"))
        print(shortest_path(g, "Hadiach123", "Burshtyn"))  # помилка бо такого міста немає
    except:
        print('if u don''t see graphs, something went wrong, probably u named no existing Edges')


if __name__ == '__main__':
    main()
