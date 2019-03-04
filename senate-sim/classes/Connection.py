import logging


class Connection:
    # bond - Friendship / trust on a scale of 1 - 100
    def __init__(self, politicanA, politicanB, bond):
        self.p1 = politicanA
        self.p2 = politicanB
        self.bond = bond

    def interact(self):
        self.p1.interact(self.p2, self.bond)
        self.p2.interact(self.p1, self.bond)
        # knowledge + charisma + bond in a mix
        # more knowledge -> more influence?

    def __str__(self):
        return "{} \n{} \nBond: {}".format(self.p1, self.p2, self.bond)
