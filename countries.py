import json
from pathlib import Path
from dataclasses import dataclass

DATA_FILE = Path(__file__).parent / "countries.json" #create file object

@dataclass
class Country: #defining dataclass that padronizes country-objects properties
    name: str
    code: str

all_countries = [] #list to store countries, used below

def load_countries(): #opens the file, build country list and return it
    with open(DATA_FILE, encoding="utf-8") as f: #open file object and load its data
        data = json.load(f)
    for item in data: #creates and stores country objects into countries list
        all_countries.append(Country(name=item["name"], code=item["code".lower()]))
    return all_countries #finally, return the list

if __name__ == "__main__":
    countries = load_countries()
    print(len(countries))
    print(countries[:3])


