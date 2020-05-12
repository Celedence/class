def eat(food, is_healthy):
    ending = "YOLO"
    if is_healthy:
        ending = "because they are good"
    return f"I'm eating {food}, {ending}"

def nap(hours):
    if hours >= 2:
        return f"Im feeling more tired"
    return f"im feeling refreshed after {hours} hour nap"