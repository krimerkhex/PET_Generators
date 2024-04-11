import random


def create_values() -> list:
    values = []
    for i in range(1, 5):
        values.append(random.randint(1, (100 - sum(values)) - (5 - i)))
    values.append(100 - sum(values))
    return values


def turrets_generator():
    init = create_values()
    return type("Turret", (), {
        "neuroticism": init[0],
        "openness": init[1],
        "conscientiousness": init[2],
        "extraversion": init[3],
        "agreeableness": init[4],
        "shoot": lambda self: print("Shooting"),
        "search": lambda self: print("Searching"),
        "talk": lambda self: print("Talking")
    })()


if __name__ == "__main__":
    turret = turrets_generator()
    print(turret.neuroticism, turret.openness, turret.conscientiousness, turret.extraversion, turret.agreeableness)
    turret.talk()
    turret.shoot()
    turret.talk()
