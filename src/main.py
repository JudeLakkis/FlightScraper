from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = '../drivers/geckodriver'
# TODO: find a way to run headless

class TripChecker():
    def __init__(self):
        # Driver Setup
        DRIVER_PATH = '../drivers/geckodriver'
        self.driver = webdriver.Firefox(executable_path=DRIVER_PATH)
        self.pause = 0.3

    def search(self, depLoc, arrLoc, depDate, arrDate=None, oneway=False):
        self.driver.get("https://matrix.itasoftware.com/")
        # Enter Departure Location Data
        depLocElement = self.driver.find_element_by_id("cityPair-orig-0")
        depLocElement.send_keys(str(depLoc)); sleep(self.pause)
        depLocElement.send_keys(Keys.ENTER)
        # Enter Arrival Location Data
        arrLocElement = self.driver.find_element_by_id("cityPair-dest-0")
        arrLocElement.send_keys(str(arrLoc)); sleep(self.pause)
        arrLocElement.send_keys(Keys.ENTER)
        # TODO: doesn't like interacting with calander values…
        # Enter Departure Date
        depDateElement = self.driver.find_element_by_id("calDate-0")
        depDateElement.send_keys(str(depDate)); sleep(self.pause)

        if not oneway:
            # Selects Oneway Tab
            oneway = self.driver.find_element_by_css_selector("td.gwt-TabBarItem-wrapper:nth-child(3)")
            oneway.click()
            arrDateElement = self.driver.find_element_by_id("cityPair-retDate-0")
            arrDateElement.send_keys(str(arrDate)); sleep(self.pause)
        submit = self.driver.find_element_by_id("searchButton-0")
        submit.click()



trip = TripChecker()
trip.search("FRA", "SYD", "02/01/2021", None, True)




# Control
# sleep(0.3)
# oneway.click()
# sleep(0.3)
# fromElement.send_keys("FRA")
# sleep(0.3)
# fromElement.send_keys(Keys.ENTER)
# toElement.send_keys("SYD")
# sleep(0.3)
# toElement.send_keys(Keys.ENTER)


# driver.quit()
