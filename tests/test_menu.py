from src.menu import Dish, Menu

def test_add_and_list_dish():
    menu = Menu()
    dish = Dish("Pizza", 15.0)
    menu.add_dish(dish)
    assert dish in menu.list_dishes()

def test_remove_dish():
    menu = Menu()
    dish = Dish("Pasta", 12.0)
    menu.add_dish(dish)
    menu.remove_dish(dish)
    assert dish not in menu.list_dishes()

def test_duplicate_dish_addition():
    menu = Menu()
    dish = Dish("Burger", 10.0)
    menu.add_dish(dish)
    menu.add_dish(dish)
    dishes = menu.list_dishes()
    assert dishes.count(dish) == 1
