from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Initializing Driver Configurations
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


# Initializing Classes
oopClass = {
    "link": "https://meet.google.com/lookup/bnt77k65q5?authuser=0&hs=179", "name": "OOP"}
dpdClass = {
    "link": "https://meet.google.com/lookup/fg24ncramk?authuser=0&hs=179", "name": "DPD"}
dmClass = {
    "link": "https://meet.google.com/lookup/hi7cyixnw3?authuser=0&hs=179", "name": "DM"}
dsClass = {
    "link": "https://meet.google.com/lookup/hkyjwb3oif?authuser=0&hs=179", "name": "DS"}
coClass = {
    "link": "https://meet.google.com/lookup/b65cg7mq4z?authuser=0&hs=179", "name": "CO"}

timeTable = [
    [dpdClass, oopClass, dmClass, dsClass],  # mon
    [dpdClass, dmClass, coClass, dsClass],  # tue
    [dmClass, coClass, oopClass, dpdClass],  # wed
    [oopClass, dpdClass, dsClass, coClass],  # thu
    [coClass, dsClass, dmClass, oopClass],  # fri
]


def joinClass(link):
    print(link['name']+" class")
    print("Class starts in 3 minutes")
    driver = webdriver.Chrome(options=chrome_options)

    # Joining the class
    driver.get(link['link'])
    print("got in "+link['name']+" class")

    # disabling audio and video
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div').click()  # video not allow
    print("disabled video")
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div').click()  # audio not allow
    print("disabled audio")

    # joining the class
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]').click()
    print('joined the class')

    # calculating the presentees
    time.sleep(5)
    presents = driver.find_element_by_xpath(
        '//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
    presents = int(presents.text)
    # TODO --joining other classes if presenties stay below 10 for 5 min
    print("Number of presentees: ", presents)

    # Waiting for the class to end
    print("going into sleep for 30min...")
    time.sleep(1800)

    checkPresenties()  # checking the presenties every 30s

    # Exiting the class
    try:
        driver.find_element_by_xpath(
            '//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[2]/div[2]/div').click()
    except:
        driver.get("https://www.google.com")
    print("Exited the class")


def checkPresenties(driver):
    for i in range(0, 60):
        try:
            presenties = int(driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]').text)
            print("no of presenties: ", presenties)
            if presenties < 20:
                return
            print("Going into sleep for 30s...")
            time.sleep(30)
        except:
            print("Error happened")


while 1:
    local = time.localtime()
    i = local.tm_wday
    j = str(local.tm_hour)+" "+str(local.tm_min)
    print("Time Now: ", local)

    if(j == "8 57"):
        k = 0
        print("time is up")
        joinClass(timeTable[i][k])
    elif j == "9 57":
        k = 1
        print("time is up")
        joinClass(timeTable[i][k])
    elif j == "11 27":
        k = 2
        print("time is up")
        joinClass(timeTable[i][k])
    elif j == "12 27":
        k = 3
        print("time is up")
        joinClass(timeTable[i][k])

    print("\n\ngoing into sleep for 30s...")
    time.sleep(30)
