parties = {
    "Red": "SPD",
    "Green": "Die Grünen",
    "Black": "CDU",
    "Yellow": "FDP",
    "Purple": "AfD",
    "White": "Parteilos"
}


class Topic:
    persons = []
    # related - related knowledge
    def __init__(self, name, related, options):
        self.name = name
        self.related = related
        self.options = options

    def add_person(self, person):
        self.persons.append(person)

    def get_related(self):
        return self.related


class Option:
    options = ["Pro", "Contra", "None"]


class Person:
    # party - Political party of the person
    # knowledge - Pool of Knowledge of the person
    # charisma - Charisma of the person, 1-100
    def __init__(self, name, party, age, knowledge, charisma):
        self.name = name
        self.party = party
        self.age = age
        self.knowledge = knowledge
        self.charisma = charisma

    # return chosen option to topic
    def form_opinion(self, topic):
        pass

    def interact(self, person, topic_person, bond):
        if self.charisma > person.charisma:
            for k, v in topic_person.get_related().items():
                person.knowledge.influence(k, v, self.charisma - person.charisma, bond)

    def __str__(self):
        return "Person " + str(self.name) + "\nParty " + str(self.party) + "\nKnowledge " + str(self.knowledge)


# Integer values from 0 - 100
class Knowledge:
    def __init__(self, family, education, integration, work, law, dataprotection, environment, economy, science, media):
        self.knowledge = {}
        self.knowledge["family"] = family
        self.knowledge["education"] = education
        self.knowledge["integration"] = integration
        self.knowledge["work"] = work
        self.knowledge["law"] = law
        self.knowledge["dataprotection"] = dataprotection
        self.knowledge["environment"] = environment
        self.knowledge["economy"] = economy
        self.knowledge["science"] = science
        self.knowledge["media"] = media

    def influence(self, key, value, charisma, bond):
        self.knowledge[key] += (value + charisma + bond)
        if self.knowledge[key] > 100:
            self.knowledge[key] = 100

    def __str__(self):
        return str(self.knowledge)


class Connection:
    # bond - Friendship / trust on a scale of 1 - 100
    def __init__(self, politicanA, politicanB, bond):
        self.p1 = politicanA
        self.p2 = politicanB
        self.bond = bond

    def interact(self, topic):
        self.p1.interact(self.p2, topic, self.bond)
        self.p2.interact(self.p1, topic, self.bond)
        # knowledge + charisma + bond in a mix
        # more knowledge -> more influence?


def initialize_data(topic):
    connections = []
    k_a = Knowledge(10, 2, 3, 4, 5, 6, 8, 9, 10, 11)
    a = Pgiterson("A", parties["Red"], 40, k_a, 30)
    k_b = Knowledge(4, 51, 2, 45, 13, 3, 73, 18, 40, 21)
    b = Person("B", parties["Black"], 23, k_b, 70)
    c_ab = Connection(a, b, 10)
    connections.append(c_ab)
    topic.add_person(a)
    topic.add_person(b)
    return connections


# iterations
# run through all connections
def simulate(topic, connections):
    for connection in connections:
        connection.interact(topic)
    return connections



if __name__ == "__main__":
    option = Option()
    related = {
            "environment": 70,
            "economy": 70
        }
    topic = Topic(
        "Elbvertiefung",
        related,
        option
    )
    connections = initialize_data(topic)
    for connection in connections:
        print(connection.p1)
        print(connection.p2)
    i = 0
    while i < 1:
        connections = simulate(topic, connections)
        i += 1
    for connection in connections:
        print(connection.p1)
        print(connection.p2)
