shows = [
    "Hello",
    "woRld",
    "tom ",
    "Jerry",
    "  Knight monster",
    "Avater: the Last airbender"
]


def main():
    clean_shows=[]
    for show in shows:
        clean_shows.append(show.strip().title())

    print(', '.join(clean_shows))


main()