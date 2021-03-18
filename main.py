import time
from scrapper import get_text

print(f"Put company name in which you are interested")
name = input(">")
print(f"You're interested in {name}.")

get_text(name)

