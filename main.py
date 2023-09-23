from AuctionScraper import Scraper

def main():
    AuctionScraper = Scraper("#eu-tarren-mill")
    flower = AuctionScraper.finditem("191462")
    ragePhial = AuctionScraper.finditem("191329")
    power = AuctionScraper.finditem("191381")

    print("Rage Phial : " + ragePhial.getString())
    print("Flower : " + flower.getString())
    print("Power : " + power.getString())


if __name__ == "__main__":
    main()
