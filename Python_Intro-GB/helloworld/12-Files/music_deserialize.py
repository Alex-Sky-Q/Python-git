import json
import pickle

with open('group.json', 'r', encoding='utf-8') as f:
    my_fav_group = json.load(f)
    print(type(my_fav_group))
    print(my_fav_group)

with open('group.pickle', 'rb') as f:
    my_fav_group = pickle.load(f)
    print(type(my_fav_group))
    print(my_fav_group)

print('Success')
