import time
from selenium.webdriver.common.by import By
from scrapy import Selector
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from merchant.master import MerchantMasterSuite
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class MerchantPortalCashbackSuite(MerchantMasterSuite):

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

    @tryExcept
    def changeCashBackRate(self, rate):
        self.driver.find_element(By.ID, "cashbackAmountmountEditIcon").click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'updateCashbackInput'))).click()
        self.driver.find_element(By.ID, "updateCashbackInput").send_keys(str(rate))
        self.driver.find_element(By.ID, "updateCashback").click()
        time.sleep(2)
        assert self.driver.switch_to.alert.text == "Cashback amount updated."
        self.driver.switch_to.alert.accept()
        self.checkTable(rate)

    @tryExcept
    def checkTable(self, rate):
        resp = Selector(text=self.driver.page_source)
        rate = str(rate) + "%"
        time.sleep(2)
        merchantCashback = resp.xpath('//*[@id="merchantCashbackTable"]/tbody/tr[2]/td[2]/text()').get()
        # RC = resp.xpath('//*[@id="merchantCashbackTable"]/tbody/tr[2]/td[3]/text()').get()
        print('Attempted to change cashback rate:')
        if rate == merchantCashback:
            print("Rate changed and added to table. Test PASSED.")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Cashback Suite', 'Change Cashback Rate', 'PASSED', '')
        else:
            print("Problem. New rate not visible on table. Test FAILED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Cashback Suite', 'Change Cashback Rate', 'FAILED', 'New rate not visible on table')

    @tryExcept
    def runSuite(self, cashBackRate):
        self.setupMethod("")
        self.login()
        self.navigate()
        self.changeCashBackRate(cashBackRate)
        self.teardownMethod("")
