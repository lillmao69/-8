import random

def simulate_game():
    doors = ["пусто", "пусто", "приз"]
    random.shuffle(doors)
    
    player_choice = random.randint(0, 2)
    door_to_open = (player_choice + 1) % 3
    
    player_switch_choice = (door_to_open + 1) % 3
    
    return doors[player_switch_choice] == "приз", doors[player_choice] == "приз"

def calculate_probabilities(num_simulations):
    switch_wins = sum(simulate_game()[0] for _ in range(num_simulations))
    stay_wins = sum(simulate_game()[1] for _ in range(num_simulations))
    
    return switch_wins / num_simulations, stay_wins / num_simulations

# Ввод данных
num_simulations = 10000

# Расчет вероятностей выигрыша
switch_prob, stay_prob = calculate_probabilities(num_simulations)

# Вывод результатов
print("Вероятность выигрыша для игрока, меняющего свой выбор:", switch_prob)
print("Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе:", stay_prob)
