from datetime import date


# Ausschuss für Jugendschutz und Datenschutz
politicians = {
    1: {
        "first_name": "Milan",
        "name": "Pein",
        "party": "red",
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
        "party": "grey",
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
            "party": "red",
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
            "party": "red",
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
            "party": "red",
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
            "party": "red",
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
            "party": "red",
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
            "party": "grey",
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
            "party": "green",
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
            "party": "purple",
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
            "party": "yellow",
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
            "party": "orange",
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
            "topics": {
                0: {
                    "value": None,
                    "conviction": 10
                }
            }
        },
}


connections = [
    # 1
    [1, 2, 35],
    [1, 3, 58],
    [1, 4, 87],
    [1, 5, 45],
    [1, 6, 34],
    [1, 7, 28],
    [1, 8, 58],
    [1, 9, 62],
    [1, 10, 28],
    [1, 11, 36],
    [1, 12, 0],
    # 2
    [2, 3, 24],
    [2, 4, 31],
    [2, 5, 41],
    [2, 6, 17],
    [2, 7, 69],
    [2, 8, 78],
    [2, 9, 23],
    [2, 10, 12],
    [2, 11, 58],
    [2, 12, 0],
    # 3
    [3, 4, 71],
    [3, 5, 64],
    [3, 6, 59],
    [3, 7, 34],
    [3, 8, 23],
    [3, 9, 57],
    [3, 10, 23],
    [3, 11, 42],
    [3, 12, 0],
    # 4
    [4, 5, 78],
    [4, 6, 65],
    [4, 7, 23],
    [4, 8, 45],
    [4, 9, 67],
    [4, 10, 32],
    [4, 11, 46],
    [4, 12, 0],
    # 5
    [5, 6, 73],
    [5, 7, 87],
    [5, 8, 75],
    [5, 9, 35],
    [5, 10, 15],
    [5, 11, 60],
    [5, 12, 0],
    # 6
    [6, 7, 82],
    [6, 8, 64],
    [6, 9, 46],
    [6, 10, 13],
    [6, 11, 56],
    [6, 12, 0],
    # 7
    [7, 8, 74],
    [7, 9, 32],
    [7, 10, 26],
    [7, 11, 68],
    [7, 12, 0],
    # 8
    [8, 9, 23],
    [8, 10, 58],
    [8, 11, 58],
    [8, 12, 0],
    # 9
    [9, 10, 52],
    [9, 11, 23],
    [9, 12, 0],
    # 10
    [10, 11, 9],
    [10, 12, 0],
    # 11
    [11, 12, 0],
]
