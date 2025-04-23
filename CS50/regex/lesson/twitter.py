import re

url = ('https://twitter.com/davidmelon')

username = re.sub(r'^(https?://)?(www.)?twitter.com/','',url)
print(f"Username: {username}")