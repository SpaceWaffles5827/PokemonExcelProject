import gspread
from oauth2client.service_account import ServiceAccountCredentials
import selenium
from selenium import webdriver





def idGrabber():
    AllIdList = []
    CardIDList = ["start"]

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        AllIdList.append(str(ii.get_attribute('id')))

    for x in AllIdList:
        if len(x) > 0:
            if len(x) == 6 or len(x) == 7:
                if x[0] == "a":
                    CardIDList.append(x)

    CardIDList.append("end")
    return CardIDList






def startselenium():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    return webdriver.Chrome(PATH)



def startGoogleSlides():
    scope = ['https://spreadsheets.google.com/feeds', "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json')
    gc = gspread.authorize(credentials)
    return gc.open('Test').sheet1



def getCardNameFromCardNumber(targetCardNumber): #Takes a card number and returns Name of the Pokemon
    if(targetCardNumber > 2):
        cardCounter = targetCardNumber -1
    else:
        cardCounter = targetCardNumber
    while(int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("number").text) != targetCardNumber):
        if(int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("number").text) > targetCardNumber):
            cardCounter -= 1
        if(int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("number").text) < targetCardNumber):
            cardCounter += 1
    else:
        return (driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("product").text)




def getMarketPriceFromCardNumber(targetCardNumber):
    if (targetCardNumber > 2):
        cardCounter = targetCardNumber - 1
    else:
        cardCounter = targetCardNumber
    while (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
            "number").text) != targetCardNumber):
        if (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
                "number").text) > targetCardNumber):
            cardCounter -= 1
        if (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
                "number").text) < targetCardNumber):
            cardCounter += 1
    else:
        out = str(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("marketPrice").text)
        out = out.replace("$","")
        out = float(out)
        return out



def getRarityFromCardNumber(targetCardNumber):
    if (targetCardNumber > 2):
        cardCounter = targetCardNumber - 1
    else:
        cardCounter = targetCardNumber
    while (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
            "number").text) != targetCardNumber):
        if (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
                "number").text) > targetCardNumber):
            cardCounter -= 1
        if (int(driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name(
                "number").text) < targetCardNumber):
            cardCounter += 1
    else:
        return (driver.find_element_by_id(CardIDList[cardCounter]).find_element_by_class_name("rarity").text)





def CheckCardNumberAndSetName():   #Gets the card number from collum B and sets the name to collum C
    rowChecker = 2
    while (int(wks.acell('B' + str(rowChecker)).value) > 0):
        wks.update(('C' + str(rowChecker)), getCardNameFromCardNumber((int(
            wks.acell('B' + str(rowChecker)).value))))
        rowChecker += 1



def CheckCardNumberAndSetMarketPrice():
    rowChecker = 2
    while (int(wks.acell('B' + str(rowChecker)).value) > 0):
        wks.update(('E' + str(rowChecker)), getMarketPriceFromCardNumber((int(wks.acell('B' + str(rowChecker)).value))))
        rowChecker += 1


def CheckCardNumberAndSetRarity():
    rowChecker = 2
    while (int(wks.acell('B' + str(rowChecker)).value) > 0):
        wks.update(('D' + str(rowChecker)), getRarityFromCardNumber((int(wks.acell('B' + str(rowChecker)).value))))
        rowChecker += 1




def UpdateEverything():
    rowChecker = 2
    while (int(wks.acell('B' + str(rowChecker)).value) > 0):
        wks.update(('C' + str(rowChecker)), getCardNameFromCardNumber((int(wks.acell('B' + str(rowChecker)).value))))
        wks.update(('D' + str(rowChecker)), getRarityFromCardNumber((int(wks.acell('B' + str(rowChecker)).value))))
        wks.update(('E' + str(rowChecker)), getMarketPriceFromCardNumber((int(wks.acell('B' + str(rowChecker)).value))))
        rowChecker += 1


driver = startselenium()

wks = startGoogleSlides()

driver.get("https://shop.tcgplayer.com/price-guide/pokemon/" + wks.acell('A2').value)
test = driver.find_element_by_class_name("NumberHead")
test.click()


CardIDList = idGrabber()



#print(getMarketPriceFromCardNumber(4))

#CheckCardNumberAndSetName()
#CheckCardNumberAndSetMarketPrice()
#CheckCardNumberAndSetRarity()

UpdateEverything()


#cardList = [card() for i in range(102)]










driver.close()






