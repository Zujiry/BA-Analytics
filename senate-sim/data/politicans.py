from datetime import date


# Ausschuss für Jugendschutz und Datenschutz
politicians = {
    1: {
        "first_name": "Milan",
        "name": "Pein",
        "party": "Red",
        "born": date(1974, 1, 31),
        "charisma": 50,
        "knowledge": {
            "family": 40,
            "education": 35,
            "integration": 30,
            "work": 70,
            "law": 95,
            "dataprotection": 70,
            "environment": 30,
            "economy": 40,
            "science": 35,
            "media": 20,
            "culture": 20
        },
        "connections": {
            2: 20
        },
        "topics": {
            0: {
                "value": True,
                "conviction": 70
            }
        }
    },
    2: {
        "first_name": "Richard",
        "name": "Seelmaecker",
        "party": "Black",
        "born": date(1973, 2, 12),
        "charisma": 55,
        "knowledge": {
            "family": 90,
            "education": 80,
            "integration": 40,
            "work": 40,
            "law": 85,
            "dataprotection": 65,
            "environment": 55,
            "economy": 40,
            "science": 45,
            "media": 55,
            "culture": 20
        },
        "connections": {
            3: 20
        },
        "topics": {
            0: {
                "value": True,
                "conviction": 90
            }
        }
    },
    3: {
            "first_name": "Peri",
            "name": "Arndt",
            "party": "Red",
            "born": date(1965, 1, 21),
            "charisma": 60,
            "knowledge": {
                "family": 20,
                "education": 30,
                "integration": 30,
                "work": 40,
                "law": 30,
                "dataprotection": 65,
                "environment": 30,
                "economy": 30,
                "science": 43,
                "media": 35,
                "culture": 85
        },
        "connections": {
            1: 20
        },
        "topics": {
            0: {
                "value": True,
                "conviction": 60
            }
        }
    },
    4: {
            "first_name": "Hendrikje",
            "name": "Blandow-Schlegel",
            "party": "Red",
            "born": date(1961, 10, 11),
            "charisma": 52,
            "knowledge": {
                "family": 90,
                "education": 65,
                "integration": 30,
                "work": 30,
                "law": 85,
                "dataprotection": 70,
                "environment": 20,
                "economy": 40,
                "science": 31,
                "media": 35,
                "culture": 25,
            },
            "connections": {
                1: 20
            },
            "topics": {
                0: {
                    "value": True,
                    "conviction": 50
                }
            }
        },
    5: {
            "first_name": "Olaf",
            "name": "Steinbiss",
            "party": "Red",
            "born": date(1966, 11, 7),
            "charisma": 65,
            "knowledge": {
                "family": 40,
                "education": 35,
                "integration": 40,
                "work": 50,
                "law": 80,
                "dataprotection": 70,
                "environment": 30,
                "economy": 40,
                "science": 28,
                "media": 30,
                "culture": 50,
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": False,
                    "conviction": 60
                }
            }
        },
    6: {
            "first_name": "Urs",
            "name": "Tabbert",
            "party": "Red",
            "born": date(1971, 12, 5),
            "charisma": 25,
            "knowledge": {
                "family": 40,
                "education": 30,
                "integration": 35,
                "work": 30,
                "law": 75,
                "dataprotection": 85,
                "environment": 25,
                "economy": 30,
                "science": 45,
                "media": 30,
                "culture": 30
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": True,
                    "conviction": 60
                }
            },
        },
    7: {
            "first_name": "Henriette",
            "name": "von Enckevort",
            "party": "Red",
            "born": date(1980, 2, 25),
            "charisma": 42,
            "knowledge": {
                "family": 40,
                "education": 40,
                "integration": 60,
                "work": 70,
                "law": 80,
                "dataprotection": 70,
                "environment": 35,
                "economy": 40,
                "science": 51,
                "media": 20,
                "culture": "45"
            },
            "connections": {
                2: 60
            },
            "topics": {
                0: {
                    "value": True,
                    "conviction": 40
                }
            }
        },
    8: {
            "first_name": "Joachim",
            "name": "Lenders",
            "party": "Black",
            "born": date(1961, 12, 6),
            "charisma": 73,
            "knowledge": {
                "family": 40,
                "education": 55,
                "integration": 45,
                "work": 40,
                "law": 65,
                "dataprotection": 72,
                "environment": 25,
                "science": 47,
                "economy": 40,
                "media": 20,
                "culture": 24
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": True,
                    "conviction": 40
                }
            }
        },
    9: {
            "first_name": "Carola",
            "name": "Timm",
            "party": "Green",
            "born": date(1969, 5, 6),
            "charisma": 57,
            "knowledge": {
                "family": 50,
                "education": 57,
                "integration": 40,
                "work": 70,
                "law": 80,
                "dataprotection": 85,
                "environment": 45,
                "economy": 30,
                "science": 67,
                "media": 30,
                "culture": 30
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": False,
                    "conviction": 90
                }
            },
        },
    10: {
            "first_name": "Martin",
            "name": "Dolzer",
            "party": "Purple",
            "born": date(1966, 12, 23),
            "charisma": 30,
            "knowledge": {
                "family": 28,
                "education": 37,
                "integration": 85,
                "work": 40,
                "law": 73,
                "dataprotection": 62,
                "environment": 32,
                "economy": 30,
                "science": 31,
                "media": 40,
                "culture": 27
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": False,
                    "conviction": 70
                }
            }
        },
    11: {
            "first_name": "Anna-Elisabeth",
            "name": "von Treuenfels-Frowein",
            "party": "Yellow",
            "born": date(1962, 5, 13),
            "charisma": 45,
            "knowledge": {
                "family": 75,
                "education": 90,
                "integration": 25,
                "work": 30,
                "law": 80,
                "dataprotection": 64,
                "environment": 25,
                "science": 45,
                "economy": 45,
                "media": 22,
                "culture": 31
            },
            "connections": {
                2: 20
            },
            "topics": {
                0: {
                    "value": True,
                    "conviction": 70
                }
            }
        },
    12: {
            "first_name": "Dirk",
            "name": "Nockemann",
            "party": "Orange",
            "born": date(1958, 5, 5),
            "charisma": 23,
            "knowledge": {
                "family": 35,
                "education": 0,
                "integration": 0,
                "work": 35,
                "law": 85,
                "dataprotection": 70,
                "environment": 0,
                "science": 12,
                "economy": 36,
                "media": 26,
                "culture": 51
            },
            "connections": {
            },
            "topics": {
                0: {
                    "value": None,
                    "conviction": 10
                }
            }
        },
}
