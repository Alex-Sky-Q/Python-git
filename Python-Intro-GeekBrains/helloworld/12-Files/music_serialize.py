import json
import pickle

my_fav_group = {
    'name': 'Кипелов',
    'tracks': ['Улица роз', 'Свобода'],
    'Albums': [{'name': 'Игра с огнем', 'year': 1989},
               {'name': 'Герой асфальта', 'year': 1987}]}

with open('group.json', 'w', encoding='utf-8') as f:
    fav_group_json = json.dumps(my_fav_group)
    print(type(fav_group_json))
    print(fav_group_json)
    f.write(fav_group_json)

with open('group.pickle', 'wb') as f:
    fav_group_b = pickle.dumps(my_fav_group)
    print(type(fav_group_b))
    print(fav_group_b)
    f.write(fav_group_b)

print('Success')
