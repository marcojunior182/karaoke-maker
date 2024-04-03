from karaoke_creator import KaraokeCreator

def main():
    youtube_url = "https://www.youtube.com/watch?v=DHEOF_rcND8"
    karaoke_creator = KaraokeCreator(youtube_url)
    karaoke_creator.criar_karaoke()

if __name__ == "__main__":
    main()
