from karaoke_creator import KaraokeCreator

def main():
    youtube_link = "https://www.youtube.com/watch?v=DHEOF_rcND8"
    karaoke_creator = KaraokeCreator(youtube_link)
    karaoke_creator.criar_karaoke()

if __name__ == "__main__":
    main()
