from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("must be boolean")
    ending = "YOLO"
    if is_healthy:
        ending = "because they are good"
    return f"I'm eating {food}, {ending}"

def nap(hours):
    if hours >= 2:
        return f"Im feeling more tired"
    return f"im feeling refreshed after {hours} hour nap"

def is_funny(person):
    if person is "tim":
        return False
    return True

def laugh():
    return choice(('lol', 'ha', 'tehe'))

