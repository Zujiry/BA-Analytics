from data.politicans import politicians, connections as cons
from data.topics import topics
from classes import Connection, Knowledge, Opinion, Topic, Person

import logging


def initialize_topic(topic_id):
    topic = topics[topic_id]
    option = Opinion()
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
        opinion = Opinion(
            value=politician["topics"][topic.id]["value"],
            conviction=politician["topics"][topic.id]["conviction"]
        )
        new_person.form_opinion(topic, opinion)
        persons.append(new_person)

    for con in cons:
        for p1 in persons:
            for p2 in persons:
                if p1.number[0] is con[0] and p2.number[0] is con[1]:
                    new_connection = Connection(p1, p2, con[2])
                    connections.append(new_connection)

    return connections

