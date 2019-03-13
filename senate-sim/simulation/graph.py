import networkx as nx
import matplotlib.pyplot as plt
import pathlib

from data.politicans import politicians

__location__ = pathlib.Path(__file__)


def draw_graph(loop_count, topic, connections):
    G = nx.Graph()
    print("################{}###################".format(loop_count))
    log_list = []
    for con in connections:
        if con.p1 not in log_list:
            print("{} is voting {} for the topic with conviction {}"
                  .format(con.p1.first_name, con.p1.opinion.value, con.p1.opinion.conviction))
            log_list.append(con.p1)
        G.add_node(str(con.p1.first_name))
        G.add_node(str(con.p2.first_name))
        G.add_edge(str(con.p1.first_name), str(con.p2.first_name), weight=int(con.bond)/20, color=colorize(con.bond))

        # Topic
        G.add_edge(str(con.p1.first_name), topic.name,
                   weight=(con.p1.opinion.conviction/10), color=colorize_opinion(con.p1.opinion))
        G.add_edge(str(con.p2.first_name), topic.name,
                   weight=(con.p2.opinion.conviction/10), color=colorize_opinion(con.p2.opinion))
    log_list.clear()

    color_map = []
    for idx, item in enumerate(G.nodes()):
        if item is topic.name:
            color_map.insert(idx, "teal")
        else:
            for k, v in politicians.items():
                if v['first_name'] is item:
                    color_map.insert(idx, v['party'])
                    break
    print(G.nodes())
    print(color_map)
    pos = nx.circular_layout(G)

    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    weights = [G[u][v]['weight'] for u, v in edges]
    nodes = G.nodes()
    print(nodes)
    print(color_map)

    nx.draw(G, pos, edges=edges, edge_color=colors, node_color=color_map, width=weights, with_labels=True)
    plt.savefig(
        str(pathlib.Path(
                __location__.parent.parent / "graphs" / "simulation-graph-sim-{}.png".format(str(loop_count)))))
    plt.show()


def colorize(bond):
    comparisons = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    comparison = {
        0: "cyan",
        10: "b",
        20: "y",
        30: "y",
        40: "y",
        50: "lawngreen",
        60: "forestgreen",
        70: "darkorange",
        80: "r",
        90: "r",
    }
    for border in comparisons:
        if bond >= border:
            return comparison[border]


def colorize_opinion(opinion):
    opinions = {
        None: "y",
        True: "g",
        False: "r"
    }
    return opinions[opinion.value]
