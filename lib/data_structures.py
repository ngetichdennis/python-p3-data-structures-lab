spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
name=get_names(spicy_foods)
print(name)
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
name=get_spiciest_foods(spicy_foods)
print(name)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emoji = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji}")
print(print_spicy_foods(spicy_foods))
   

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))  
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
print(get_spicy_food_by_cuisine(spicy_foods, "Sichuan"))  
print(get_spicy_food_by_cuisine(spicy_foods, "Indian")) 

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food['heat_level'] > 5:
            spice_level = ''
            for i in range(food['heat_level']):
                spice_level += '🌶'
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spice_level}")
print(print_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return round(average_heat_level)
average_heat_level = get_average_heat_level(spicy_foods)
print(average_heat_level)


def create_spicy_food(spicy_foods, spicy_food):
    # Add the new spicy_food to the original list
    spicy_foods.append(spicy_food)

    # Return the updated list
    return spicy_foods
updated_spicy_foods = create_spicy_food(spicy_foods, {
        
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
            
    })
print(updated_spicy_foods)
