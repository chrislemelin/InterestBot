from boardgamegeek import BGGClient, BGGItemNotFoundError

def main():
    print(fetch("Terraforming Mars"))


def fetch(name):
    bgg = BGGClient()
    try:
        return bgg.game(name)
    except BGGItemNotFoundError:
        return null

if __name__ == "__main__":
    main()