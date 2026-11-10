import json
from pathlib import Path
from dataclasses import dataclass

DATA_FILE = Path(__file__).parent / "assets" / "countries.json" #create file path relative to parent so it works on mobile

@dataclass #dataclass so it standardizes all object properties
class Country: 
    name: str
    code: str

def load_countries() -> list[Country]:
    all_countries = []
    with open(DATA_FILE, encoding="utf-8") as f: 
        data = json.load(f)
    for item in data: 
        all_countries.append(Country(name=item["name"], code=item["code"]))
    return all_countries

if __name__ == "__main__":
    countries = load_countries()
    print(len(countries))
    print(countries[:3])


