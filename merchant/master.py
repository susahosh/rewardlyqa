import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from library.write_results import writeResultsCsv
from library.decorate import tryExcept

class MerchantMasterSuite:

    # Path for csv file where test results will be recorded
    resultsPath = r'C:\Users\macvi\PycharmProjects\rewardly\results\merchant_results.csv'

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    @tryExcept
    def setupMethod(self, method):
        self.driver.get("https://stage.rewardly.ca/merchant/till")
        self.driver.set_window_size(1360, 824)

    @tryExcept
    def teardownMethod(self, method):
        self.driver.quit()

    @tryExcept
    def login(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("merchant1@metaii.com")
        self.driver.find_element(By.ID, "merchantPasswordInput").click()
        self.driver.find_element(By.ID, "merchantPasswordInput").send_keys("qasdfghjkl")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()


