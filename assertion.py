def eat_junk(food):
    assert food in [
    'pizza',
    'ice cream',
    'chips'], 'food must be a junk food'
    return f"im eating {food}"

food = input("Enter some food please: ")
print(eat_junk(food))