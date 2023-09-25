from AuctionScraper import Scraper
import csv

def main():
    AuctionScraper = Scraper("#eu-tarren-mill")
    Dictionary = {"RagePhial": 191329,
                  "Flower": 191462}

    flower = AuctionScraper.finditem(str(Dictionary["RagePhial"]))
    ragePhial = AuctionScraper.finditem(str(Dictionary["Flower"]))
    power = AuctionScraper.finditem("191381")

    print("Rage Phial : " + ragePhial.getString())
    print("Flower : " + flower.getString())
    print("Power : " + power.getString())

    phial = [191462, ragePhial.gold, ragePhial.silver, ragePhial.copper]
    file = open('export.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(phial)
    file.close()

if __name__ == "__main__":
    main()
