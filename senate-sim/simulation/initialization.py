from data.politicans import politicians
from data.topics import topics
from classes import Connection, Knowledge, Option, Topic, Person

import logging


def initialize_topic(topic_id):
    topic = topics[topic_id]
    option = Option()
    return Topic(
        topic_id,
        topic["name"],
        topic["related"],
        option
    )


def initialize_data(topic):
    persons = []
    connections = []
    for key, politician in politicians.items():
        new_knowledge = Knowledge(
            politician["knowledge"]["family"],
            politician["knowledge"]["education"],
            politician["knowledge"]["integration"],
            politician["knowledge"]["work"],
            politician["knowledge"]["law"],
            politician["knowledge"]["dataprotection"],
            politician["knowledge"]["environment"],
            politician["knowledge"]["economy"],
            politician["knowledge"]["science"],
            politician["knowledge"]["media"],
            politician["knowledge"]["culture"],
        )
        new_person = Person(
            int(key),
            politician["first_name"],
            politician["name"],
            politician["party"],
            politician["born"],
            new_knowledge,
            politician["charisma"],
        )
        option = Option(
            value=politician["topics"][topic.id]["value"],
            conviction=politician["topics"][topic.id]["conviction"]
        )
        new_person.form_opinion(topic, option)
        persons.append(new_person)

    for key, value in politicians.items():
        for number, bond in value["connections"].items():
            new_connection = Connection(persons[key-1], persons[number-1], bond)
            connections.append(new_connection)

    return connections

