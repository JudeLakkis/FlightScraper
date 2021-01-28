from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# DRIVER_PATH = '../drivers/geckodriver'
# TODO: find a way to run headless

class TripChecker():
    def __init__(self):
        # Driver Setup
        driver_path = '../drivers/geckodriver'
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.pause = 0.3

    def search(self, depLoc, arrLoc, depDate, arrDate=None, oneway=False):
        self.driver.get("https://matrix.itasoftware.com/")
        sleep(5)
        # TODO: Issue with date selector
        self.driver.find_element_by_css_selector("input[type='radio'][name='datesChoiceRadio']").click()
        # Enter Departure Location Data
        # TODO: Names aren't typed in properly all the time…
        depLocElement = self.driver.find_element_by_id("cityPair-orig-0")
        depLocElement.send_keys(str(depLoc)); sleep(self.pause)
        depLocElement.send_keys(Keys.ENTER)
        # Enter Arrival Location Data
        arrLocElement = self.driver.find_element_by_id("cityPair-dest-0")
        arrLocElement.send_keys(str(arrLoc)); sleep(self.pause)
        arrLocElement.send_keys(Keys.ENTER)
        # Enter Departure Date
        depDateElement = self.driver.find_element_by_id("cityPair-outDate-0")
        depDateElement.send_keys(str(depDate)); sleep(self.pause)

        if oneway:
            # Selects Oneway Tab
            oneway = self.driver.find_element_by_css_selector("td.gwt-TabBarItem-wrapper:nth-child(3)")
            oneway.click()
        else:
            arrDateElement = self.driver.find_element_by_id("cityPair-retDate-0")
            arrDateElement.send_keys(str(arrDate)); sleep(self.pause)
        submit = self.driver.find_element_by_id("searchButton-0")
        submit.click()



trip = TripChecker()
trip.search("Frankfurt", "Melbourne", "02/01/2021", None, True)

# driver_path = '../drivers/geckodriver'
# driver = webdriver.firefox(executable_path=driver_path)
# pause = 0.3


# driver.get("https://matrix.itasoftware.com/")
# depDateElement = driver.find_element_by_id("calDate-0")
# depDateElement.send_keys(str(depDate))
# sleep(pause)


