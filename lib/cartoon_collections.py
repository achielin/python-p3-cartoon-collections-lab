def roll_call_dwarves():
    pass
def roll_call_dwarves(list):
    for dwarf in list:
        print(f"{list.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet():
    pass
def summon_captain_planet(planeteer_calls):
    planeteer_calls = [item.capitalize() + "!" for item in planeteer_calls]
    return planeteer_calls 

def long_planeteer_calls():
    pass
def long_planeteer_calls(planeteer_calls):
    value_list = list()
    for i in planeteer_calls:
        if len(i) > 4:
            value_list.append(i)
            break    
        else:
            pass
    return bool(value_list)

def find_the_cheese(food_list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for item in food_list:
        if item in cheese_list:
            return item

    return None

def find_the_cheese():
    pass
