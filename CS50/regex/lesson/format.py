
import re

name = input("What's your name? ").strip()    #Kaplia,Stani
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")        #hello, Stani Kaplia