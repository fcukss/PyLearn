from CS50.museum.artists import get_artists

def main():
    # artwork = input("Artwork: ")
    # artworks = get_artwork(query = artwork,limit=3)
    # for artwork in artworks:
    #     print(f"*{artwork}")

    #search for artists
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"*{artist}")



main()