import json
import requests
import sys

#достаем по api информацию о ссписке песен исполнителя weezor(вводим все в терминале)
#
# if len(sys.argv)!=2:
#     sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#
#
# o = response.json()
# for result in o['results']:
#     print(result['trackName'])


print("===========================================================")

def main():
    print("Search the Art Institute of Chicago")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {'q':artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("couldn;t complete request")
        return

    content = response.json()
    #print(content)
    for artwork in content['data']:
        print(f"*{artwork['title']}")


main()