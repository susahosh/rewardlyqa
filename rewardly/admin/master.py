from selenium import webdriver
from selenium.webdriver.common.by import By
from library.decorate import tryExcept


class AdminPortalMaster:

    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    @tryExcept
    def setupMethod(self, method):
        self.driver.get("https://stage.rewardly.ca/portal/login")
        self.driver.set_window_size(1356, 824)

    @tryExcept
    def teardownMethod(self, method):
        self.driver.quit()

    @tryExcept
    def login(self):
        self.driver.get("https://stage.rewardly.ca/portal/login")
        self.driver.set_window_size(1356, 824)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("rewardlyadmin@metaii.com")
        self.driver.find_element(By.ID, "adminPasswordInput").click()
        self.driver.find_element(By.ID, "adminPasswordInput").send_keys("qasdfghjkl")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
