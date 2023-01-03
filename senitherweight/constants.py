dungeons_level50_experience = 569809640
skills_level50_experience = 55172425
skills_level60_experience = 111672425
dungeon_weights = {
    "catacombs": 0.0002149604615,
    "healer": 0.0000045254834,
    "mage": 0.0000045254834,
    "berserk": 0.0000045254834,
    "archer": 0.0000045254834,
    "tank": 0.0000045254834,
}
slayer_weights = {
    "zombie": {
        "divider": 2208,
        "modifier": 0.15,
    },
    "spider": {
        "divider": 2118,
        "modifier": 0.08,
    },
    "wolf": {
        "divider": 1962,
        "modifier": 0.015,
    },
    "enderman": {
        "divider": 1430,
        "modifier": 0.017,
    }
}
skill_weights = {
    # Maxes out mining at 1,750 points at 60.
    "mining": {
        "exponent": 1.18207448,
        "divider": 259634,
        "maxLevel": 60,
    },
    # Maxes out foraging at 850 points at level 50.
    "foraging": {
        "exponent": 1.232826,
        "divider": 259634,
        "maxLevel": 50,
    },
    # Maxes out enchanting at 450 points at level 60.
    "enchanting": {
        "exponent": 0.96976583,
        "divider": 882758,
        "maxLevel": 60,
    },
    # Maxes out farming at 2,200 points at level 60.
    "farming": {
        "exponent": 1.217848139,
        "divider": 220689,
        "maxLevel": 60,
    },
    # Maxes out combat at 1,500 points at level 60.
    "combat": {
        "exponent": 1.15797687265,
        "divider": 275862,
        "maxLevel": 60,
    },
    # Maxes out fishing at 2,500 points at level 50.
    "fishing": {
        "exponent": 1.406418,
        "divider": 88274,
        "maxLevel": 50,
    },
    # Maxes out alchemy at 200 points at level 50.
    "alchemy": {
        "exponent": 1.0,
        "divider": 1103448,
        "maxLevel": 50,
    },
    # Maxes out taming at 500 points at level 50.
    "taming": {
        "exponent": 1.14744,
        "divider": 441379,
        "maxLevel": 50,
    },
    # Sets up carpentry and runecrafting without any weight components.
    "carpentry": {
        "maxLevel": 50,
    },
    "runecrafting": {
        "maxLevel": 25,
    },
}
skill_weight_groups = [
    'mining', 'foraging', 'enchanting', 'farming', 'combat', 'fishing', 'alchemy', 'taming'
]

skill_max_level = {
    "mining": 60,
    "foraging": 50,
    "enchanting": 60,
    "farming": 60,
    "combat": 60,
    "fishing": 50,
    "alchemy": 50,
    "taming": 50,
    "carpentry": 50,
    "runecrafting": 25,
}
