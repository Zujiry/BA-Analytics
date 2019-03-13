from simulation.initialization import initialize_data, initialize_topic
from simulation.graph import draw_graph
import logging


# iterations
# run through all connections
def simulate(loop, connections):
    if loop % 2 is 0:
        for connection in connections:
            connection.interact(loop)
    else:
        for connection in reversed(connections):
            connection.interact(loop)
    return connections


if __name__ == "__main__":
    topic = initialize_topic(0)
    connections = initialize_data(topic)

    i = 0
    while i < 3:
        logging.info("simulation Main Loop - Count " + str(i))
        connections = simulate(i, connections)
        draw_graph(i, topic, connections)
        i += 1
