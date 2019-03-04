import networkx as nx
import matplotlib.pyplot as plt
import pathlib

__location__ = pathlib.Path(__file__)


def draw_graph(loop_count, topic, connections):
    G = nx.Graph()
    for con in connections:
        G.add_node(str(con.p1.first_name), color=con.p1.party)
        G.add_node(str(con.p2.first_name))
        G.add_edge(str(con.p1.first_name), str(con.p2.first_name), weight=int(con.bond)/100, color=colorize(con.bond))

        # Topic
        print("{} is voting {} for the topic with conviction {}".format(con.p1.first_name, con.p1.option.value, con.p1.option.conviction))
        G.add_edge(str(con.p1.first_name), topic.name, weight=(con.p1.option.conviction/10), color=colorize_option(con.p1.option))
        G.add_edge(str(con.p2.first_name), topic.name, weight=(con.p2.option.conviction/10), color=colorize_option(con.p2.option))

    pos = nx.circular_layout(G)
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]
    weights = [G[u][v]['weight'] for u, v in edges]
    nx.draw(G, pos, edges=edges, edge_color=colors, width=weights, with_labels=True)
    plt.savefig(
        str(pathlib.Path(
                __location__.parent.parent / "graphs" / "simulation-graph-sim-{}.png".format(str(loop_count)))))
    plt.show()


def colorize(bond):
    comparison = {
        20: "b",
        30: "b",
        40: "b",
        50: "g",
        60: "g",
        70: "r",
        80: "r",
    }
    for key, value in comparison.items():
        if bond >= key:
            return comparison[key]


def colorize_option(option):
    options = {
        None: "r",
        True: "g",
        False: "r"
    }
    return options[option.value]
