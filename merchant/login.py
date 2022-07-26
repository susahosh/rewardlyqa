import time
from selenium.webdriver.common.by import By
from library.decorate import tryExcept
from merchant.master import MerchantMasterSuite
from library.write_results import writeResultsCsv


class MerchantPortalLoginSuite(MerchantMasterSuite):
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
        if self.driver.find_element(By.XPATH, '/html/body/div[1]/div/center[1]/div').is_displayed():
            print('Did not login. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Empty Login Form', 'PASSED', '')
        else:
            print('Problem. Either logged in with no info or page changed. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Empty Login Form', 'FAILED', 'Either logged in with no info or page changed')

    @tryExcept
    def invalidLogin(self):
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("notarealemail@email.com")
        self.driver.find_element(By.ID, "merchantPasswordInput").click()
        self.driver.find_element(By.ID, "merchantPasswordInput").send_keys("Randompw5")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(1)
        pwError = self.driver.find_element(By.CLASS_NAME, 'loginError')
        print(pwError.text)
        print("Attempted login with invalid information: ")
        if pwError.is_displayed() and pwError.text == 'Invalid merchantId/email or password':
            print('Did not login. Proper error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Invalid Login Form', 'PASSED', '')

        else:
            print('Problem. Either logged in with wrong info or error message is wrong. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Ivalid Login Form', 'FAILED', 'Either logged in with wrong info or error message is wrong')

    @tryExcept
    def validLogin(self):
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("merchant1@metaii.com")
        self.driver.find_element(By.ID, "merchantPasswordInput").click()
        self.driver.find_element(By.ID, "merchantPasswordInput").send_keys("qasdfghjkl")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        print("Attempted login with valid information: ")
        try:
            self.driver.find_element(By.CLASS_NAME, 'rewardlyMenuLogo').is_displayed()
            print('Successfully logged in. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Valid Login Form', 'PASSED', '')

        except Exception as e:
            print('Login unsuccessful. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Valid Login Form', 'FAILED', 'Login unsuccessful')

    @tryExcept
    def clearForms(self):
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.ID, "merchantPasswordInput").clear()

    @tryExcept
    def runSuite(self):
        self.setupMethod("")
        self.emptyLoginForm()
        self.invalidLogin()
        self.clearForms()
        self.validLogin()
        self.teardownMethod("")
