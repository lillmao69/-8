import random

def throw_ball():
    return random.random() < 0.7

def computer_response():
    responses = [
        "Компьютер: О да, я на все 100%! Спрашивайте что угодно!",
        "Компьютер: Ай, промахнулся! Ну что ж, задавайте вопрос...",
        "Компьютер: Поймал! Спрашивайте, что хотите узнать!",
        "Компьютер: Я в полете! Ваш вопрос, пожалуйста...",
        "Компьютер: Ага, ловко! Сейчас на любой вопрос ответлю!"
    ]
    return random.choice(responses)

def player_response():
    return input("Вы: ")

def play_game():
    history = []
    
    print("Добро пожаловать в смешную игру!")
    print("Компьютер начинает бросать мяч вам...")
    
    for _ in range(5):
        print("\nКомпьютер бросает мяч вам!")
        if throw_ball():
            print("Вы поймали мяч!")
            response = player_response()
            history.append(("Вы", response))
        else:
            print("Вы промахнулись!")
            response = computer_response()
            history.append(("Компьютер", response))
        
        print("\nТеперь ваш ход, бросайте мяч компьютеру!")
        if throw_ball():
            print("Компьютер поймал мяч!")
            response = computer_response()
            history.append(("Компьютер", response))
        else:
            print("Компьютер промахнулся!")
            response = player_response()
            history.append(("Вы", response))
    
    print("\nИгра закончена! Вот итоговая история:")
    for turn, response in history:
        print(turn + ": " + response)

play_game()
