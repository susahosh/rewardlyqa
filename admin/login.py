from selenium.webdriver.common.by import By
from admin.master import AdminPortalMaster
from library.decorate import tryExcept


class AdminPortalLoginSuite(AdminPortalMaster):

    def __init__(self, chromeDriverPath):
        super().__init__(chromeDriverPath)

    def setupMethod(self, method):
        super().setupMethod("")

    def teardownMethod(self, method):
        super().teardownMethod("")

    @tryExcept
    def emptyLoginForm(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        print("Attempted login with empty forms: ")
        if self.driver.find_element(By.ID, "adminPasswordInput").is_displayed():
            print('Did not login. Test PASSED')
        else:
            print('Problem. Either logged in with no info or page changed. Test FAILED')

    @tryExcept
    def invalidLogin(self):
        self.driver.get("https://stage.rewardly.ca/portal/login")
        self.driver.set_window_size(1356, 824)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("qwertyuiopasdfgh@jklzx")
        self.driver.find_element(By.ID, "adminPasswordInput").click()
        self.driver.find_element(By.ID, "adminPasswordInput").send_keys("qwertyuiopasdfghjkl")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        error = self.driver.find_element(By.CSS_SELECTOR, "#portalLoginFormContainer > div > div:nth-child(2) > form > "
                                                          "center:nth-child(4) > div").text
        print("Attempted login with invalid information: ")
        if error == "Invalid email or password":
            print('Did not login. Proper error message displayed. Test PASSED')
        else:
            print('Problem. Either logged in with wrong info or error message is wrong. Test FAILED')

    @tryExcept
    def successfulLogin(self):
        self.driver.get("https://stage.rewardly.ca/portal/login")
        self.driver.set_window_size(1356, 824)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("rewardlyadmin@metaii.com")
        self.driver.find_element(By.ID, "adminPasswordInput").click()
        self.driver.find_element(By.ID, "adminPasswordInput").send_keys("qasdfghjkl")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        print("Attempted login with valid information: ")
        try:
            self.driver.find_element(By.CLASS_NAME, 'rewardlyMenuLogo').is_displayed()
            print('Successfully logged in. Test PASSED')
        except Exception as e:
            print('Login unsuccessful. Test FAILED')

    @tryExcept
    def clearForms(self):
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.ID, "adminPasswordInput").clear()

    @tryExcept
    def runSuite(self):
        self.setupMethod("")
        self.emptyLoginForm()
        print()
        self.invalidLogin()
        print()
        self.clearForms()
        self.successfulLogin()
        self.teardownMethod("")
