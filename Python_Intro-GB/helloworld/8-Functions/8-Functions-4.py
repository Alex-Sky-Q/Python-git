# 4: Давайте усложним задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Прим. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа

import random
import time

player_name = input('Your enemy is Ghost. Enter player name: ')

while True:
    if player_name == "Ghost":
        player_name = input('Your name is the same as enemy name. Enter another player name: ')
    else:
        break

player = {"name": player_name, "health": random.randint(50, 100),
          "damage": random.randint(5, 30), "armor": round(random.uniform(1, 3), 1)}
enemy = {"name": "Ghost", "health": random.randint(50, 100),
         "damage": random.randint(5, 30), "armor": round(random.uniform(1, 3), 1)}

print(f'Player {player["name"]}: health is {player["health"]}, '
      f'damage is {player["damage"]}, armor is {player["armor"]}')
print(f'Enemy {enemy["name"]}: health is {enemy["health"]}, '
      f'damage is {enemy["damage"]}, armor is {enemy["armor"]}')

while True:
    gm = int(input('Choose game mode (1 - auto, 2 - manual): '))
    if gm == 1 or gm == 2:
        break
    else:
        print('Invalid entry!')


def attack(attacker, villain):
    print(f'{attacker["name"]} attacks')

    def get_ap():
        x = round(attacker["damage"] / villain["armor"])
        return x
    ap = get_ap()
    villain["health"] -= ap
    print(f'{villain["name"]} was hit by {ap}')
    if villain["health"] <= 0:
        print(f"{villain['name']}'s health is now 0")
        print(f'{attacker["name"]} wins!')
    else:
        print(f"{villain['name']}'s health is now {villain['health']}")


while player["health"] > 0 and enemy["health"] > 0:
    if gm == 1:
        choice = random.randint(1, 2)
        print('---- Action ----')
        time.sleep(2)
    else:
        choice = int(input('Who attacks? (1 - player, 2 - enemy) '))
    if choice == 1:
        attack(player, enemy)
    elif choice == 2:
        attack(enemy, player)
    else:
        print('Invalid entry!')
else:
    print('The End')
