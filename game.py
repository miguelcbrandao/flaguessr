from dataclasses import dataclass
from countries import Country 
import random

@dataclass
class Game:
    remaining: list[Country]
    current: Country | None
    score: int
    lives: int

def new_game(countries: list[Country]) -> Game: #creates a new Game object, so we can use it on runs
    """receives list containing countries, copies and shuffles it."""
    remaining = countries.copy()
    random.shuffle(remaining)
    return Game(remaining=remaining, current=None, score=0, lives=3)

def next_country(game: Game) -> Country | None:
    if not game.remaining:
        return None
    game.current = game.remaining.pop()
    return game.current

def answer_right(game: Game) -> None:
    game.score += 10
    

def answer_wrong(game: Game) -> None:
    game.score -= 5
    game.lives -= 1
    if game.score < 0:
        game.score = 0

def is_over(game: Game) -> bool:
    return game.lives == 0 or not game.remaining

if __name__ == "__main__":
    from countries import load_countries
    game = new_game(load_countries())
    #test cases below
    answer_right(game)
    print(game.score, game.lives, is_over(game))
    answer_right(game)
    print(game.score, game.lives, is_over(game))
    answer_wrong(game)
    print(game.score, game.lives, is_over(game))
    answer_wrong(game)
    print(game.score, game.lives, is_over(game))
    answer_wrong(game)
    print(game.score, game.lives, is_over(game))
    