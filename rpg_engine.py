# 1. ЗАВАНТАЖЕННЯ (твоя система захисту)
try:
    with open("save.txt", "r") as file:
        saved_level = int(file.read())
except FileNotFoundError:
    saved_level = 1

# 2. ПЕРСОНАЖ (ось тут ми створюємо 'player'!)
player = {"name": "Egor", "level": saved_level}

# 3. ФУНКЦІЯ (твій "завод" прокачки)
def level_up(p_dict):
    p_dict["level"] += 1
    print(f"Level Up для {p_dict['name']}! Тепер рівень: {p_dict['level']}")

# 4. ІГРОВИЙ ЦИКЛ (твій код із останнього скриншота)
while True:
    print("\n--- МЕНЮ ---")
    print("1 - Твій рівень")
    print("2 - Підвищити рівень")
    print("3 - Зберегтись та вийти")
    
    vybor = input("Вибери дію: ")

    if vybor == "1":
        print(f"Твій поточний рівень: {player['level']}")
    elif vybor == "2":
        level_up(player)
    elif vybor == "3":
        with open("save.txt", "w") as file:
            file.write(str(player["level"]))
        print("Прогрес збережено. Бувай!")
        break
    else:
        print("Невірний вибір!")