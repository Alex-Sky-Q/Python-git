# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# # ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# # ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# # ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# # Функция должна сама работать со словарями и изменять их значения.

import random

player_name = input('Your enemy is Ghost. Enter player name: ')

while True:
    if player_name == "Ghost":
        player_name = input('Your name is the same as enemy name. Enter another player name: ')
    else:
        break

player = {"name": player_name, "health": random.randint(50, 100), "damage": random.randint(5, 30)}
enemy = {"name": "Ghost", "health": random.randint(50, 100), "damage": random.randint(5, 30)}

print(f'Player {player["name"]}: health is {player["health"]}, damage is {player["damage"]}')
print(f'Enemy {enemy["name"]}: health is {enemy["health"]}, damage is {enemy["damage"]}')
input('Press Enter to start ')


def attack(attacker, villain):
    print(f'{attacker["name"]} attacks')
    villain["health"] -= attacker["damage"]
    print(f'{villain["name"]} was hit by {attacker["damage"]}')
    if villain["health"] <= 0:
        print(f"{villain['name']}'s health is now 0")
        print(f'{attacker["name"]} wins!')
    else:
        print(f"{villain['name']}'s health is now {villain['health']}")


while player["health"] > 0 and enemy["health"] > 0:
    attacker = int(input('Who attacks? (1 - player, 2 - enemy) '))
    if attacker == 1:
        attack(player, enemy)
    elif attacker == 2:
        attack(enemy, player)
    else:
        print('Invalid entry!')
else:
    print('The End')
