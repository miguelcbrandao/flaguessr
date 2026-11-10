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

if __name__ == "__main__":
    from countries import load_countries
    game = new_game(load_countries())
    print(next_country(game))
    print(next_country(game))
    print(next_country(game))
    print(len(game.remaining))
 