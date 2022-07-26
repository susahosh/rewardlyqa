import time
from selenium.webdriver.common.by import By
from library.decorate import tryExcept
from merchant.master import MerchantMasterSuite
from library.write_results import writeResultsCsv


class MerchantPortalAdBudgetSuite(MerchantMasterSuite):
    def __init__(self, chromeDriverPath):
        super().__init__(chromeDriverPath)

    def setupMethod(self, method):
        super().setupMethod("")

    def teardownMethod(self, method):
        super().teardownMethod("")

    def login(self):
        super().login()

    @tryExcept
    def navigate(self):
        self.driver.find_element(By.ID, "adCreditText").click()
        self.driver.find_element(By.LINK_TEXT, "Ad Credit").click()

    @tryExcept
    def changeAdCredit(self, budget):
        self.driver.find_element(By.ID, "weeklyAmountEditIcon").click()
        self.driver.find_element(By.ID, "updateAdBudgetInput").click()
        self.driver.find_element(By.ID, "updateAdBudgetInput").send_keys(str(budget))
        self.driver.find_element(By.ID, "updateAdBudgetButton").click()
        time.sleep(2)
        assert self.driver.switch_to.alert.text == "Ad budget has been added for next week"
        self.driver.switch_to.alert.accept()
        self.verifyChange(budget)

    @tryExcept
    def verifyChange(self, budget):
        time.sleep(2)
        temp = self.driver.find_element(By.ID, "weeklyBudgetAmount").text
        testBudget = float(temp.replace("$", ""))
        print('Attempted to change AdBudget:')
        if testBudget == budget:
            print("Budget changed. Test PASSED.")
            writeResultsCsv(super().resultsPath, 'Merchant Portal adBudget Suite', 'Change Ad Credit', 'PASSED', '')
        else:
            print("PROBLEM. Budget was not updated. Test FAILED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal adBudget Suite', 'Change Ad Credit', 'FAILED', 'Budget was not updated')

    @tryExcept
    def runSuite(self, ad_budget):
        self.setupMethod("")
        self.login()
        self.navigate()
        self.navigate()
        self.changeAdCredit(ad_budget)
        self.teardownMethod("")

