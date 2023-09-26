from AuctionScraper import Scraper
import csv

header3 = "gold"
header2 = "Scraper"
header1 = "00GSC"
def main():
    AuctionScraper = Scraper("#eu-tarren-mill")
    Dictionary = {"RagePhial": 191329,
                  "Hochenblume": 191462,
                  "potofPower": 191381,
                  "bubblepoppy": 191469,
                  "saxifrage": 191466,
                  "writhebark": 191472}

    Hochenblume = AuctionScraper.finditem(str(Dictionary["Hochenblume"]))
    ragePhial = AuctionScraper.finditem(str(Dictionary["RagePhial"]))
    potofpower = AuctionScraper.finditem(str(Dictionary["potofPower"]))
    bubble_poppy = AuctionScraper.finditem(str(Dictionary["bubblepoppy"]))
    Saxifrage = AuctionScraper.finditem(str(Dictionary["saxifrage"]))
    Writebark = AuctionScraper.finditem(str(Dictionary["writhebark"]))


    print("Rage Phial : " + ragePhial.getString())
    print("Hochenblume : " + Hochenblume.getString())
    print("potofPower : " + potofpower.getString())
    print("Bubble_poppy : " + bubble_poppy.getString())
    print("Saxifrage : " + Saxifrage.getString())
    print("Writhebark : " + Writebark.getString())

    phial = [191462, "RagePot", ragePhial.gold, ragePhial.silver, ragePhial.copper]
    hochen = [191462, "Hochenblume", Hochenblume.gold, Hochenblume.silver, Hochenblume.copper]
    potofpower = [191381, "potofpower", potofpower.gold, potofpower.silver, potofpower.copper]
    bubble_poppy = [191469, "bubble-poppy", bubble_poppy.gold, bubble_poppy.silver, bubble_poppy.copper]

    file = open('export.csv', 'w')
    writer = csv.writer(file)
    writer.writerow(header1)
    writer.writerow(phial)
    writer.writerow(hochen)
    writer.writerow(potofpower)
    writer.writerow(bubble_poppy)

    file.close()
if __name__ == "__main__":
    main()
print("Scraping completed, check CSV File for more info")