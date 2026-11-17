from countries import load_countries
import game

countries = load_countries()
game1 = game.new_game(countries)

while 1:
    game.next_country(game1)
    print(game1.current.code)
    input("press enter to show the answer ")
    print(game1.current.name)
    answer  = input("Y/N ") 
    if answer.lower() == "y": game.answer_right(game1)
    else: game.answer_wrong(game1)
    if not game.is_over(game1): continue
    else: 
        i = input('Continue or leave Y/N ')
        if i.lower() == 'y': game1 = game.new_game(countries)
        else: break



