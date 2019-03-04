import logging


class Person:
    # party - Political party of the person
    # knowledge - Pool of Knowledge of the person
    # charisma - Charisma of the person, 1-100
    def __init__(self, id, first_name, name, party, birthdate, knowledge, charisma):
        self.id = id,
        self.first_name = first_name
        self.name = name
        self.party = party
        self.birthdate = birthdate
        self.knowledge = knowledge
        self.charisma = charisma
        self.topic = None
        self.option = None

    # return chosen option to topic
    def form_opinion(self, topic, option):
        self.topic = topic
        self.option = option

    def convince(self, option, charisma_bonus, knowledge, bond):
        if self.option.value is option.value:
            self.option.conviction += ((charisma_bonus + bond)/10) > 100
            if self.option.conviction > 100:
                self.option.conviction = 100
        else:
            conviction = (charisma_bonus/10)
            for key, value in knowledge.items():
                if value > 0:
                    conviction += (value/10)
            change = self.option.conviction - conviction
            if change < 15:
                self.option.value = option.value
                self.option.conviction = 35

    def interact(self, person, bond):
        log_string = "Interaction: {} {} interacting with {} {}".format(
            str(self.first_name),
            str(self.name),
            str(person.first_name),
            str(person.name),
        )
        logging.info(log_string)

        if (self.charisma - person.charisma) > 0:
            charisma_bonus = self.charisma - person.charisma
        else:
            charisma_bonus = 0

        topic_related = self.topic.get_related()
        known = dict()
        for key, value in topic_related.items():
            if self.knowledge.knowledge[key] > person.knowledge.knowledge[key]:
                known[key] = self.knowledge.knowledge[key] - person.knowledge.knowledge[key]
            else:
                known[key] = 0

        for k, v in known.items():
            person.knowledge.influence(k, v, bond)
        person.convince(self.option, charisma_bonus, known, bond)

    def __str__(self):
        return "Person {} {}\nParty {}\nKnowledge {}".format(str(self.first_name), self.name, str(self.party), str(self.knowledge))