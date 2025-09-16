import random
from db_cursor import count_levels, take_object
from config_manul import (
    one_levles_manul,
    two_level_manul,
    three_level_manul,
    four_level_manul
    

)

def get_random_obj(): #Функция для рандом выпадения карточек
    levels = [1,2,3,4]
    weights = [0.25, 0.25, 0.25, 0.25]
    result = random.choices(levels, weights=weights, k=1)[0]

    if result == 1:
        db_name = "one_level.db"
        table_name = "one_level"
    elif result == 2:
        db_name = "two_level.db"
        table_name = "two_level"
    elif result == 3:
        db_name = "three_level.db"
        table_name = "three_level"
    elif result == 4:
        db_name = "four_level.db"
        table_name = 'four_level'

    total = count_levels(db_name, table_name) #Сколько символом в определенной рарности
    index_object = random.randint(0, total - 1)  
    obj = str(take_object(db_name, table_name, index_object))

    
    if obj.startswith("1"):
        caption = one_levles_manul.get(obj, "Описание не найдено")
    elif obj.startswith("2"):
        caption = two_level_manul.get(obj, "Описание не найдено")
    elif obj.startswith("3"):
        caption = three_level_manul.get(obj, "Описание не найдено")
    elif obj.startswith("4"):
        caption = four_level_manul.get(obj, "Описание не найдено")

    else:
        caption = "Ошибка: объект не найден!"
   
    return obj, caption