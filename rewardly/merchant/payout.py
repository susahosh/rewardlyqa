from scrapy import Selector
import time
from selenium.webdriver.common.by import By
from merchant.master import MerchantMasterSuite


# UNFINISHED
class payoutCalculation(MerchantMasterSuite):
    def __init__(self, chromeDriverPath):
        super().__init__(chromeDriverPath)

    def setupMethod(self, method):
        super().setupMethod("")

    def teardownMethod(self, method):
        super().teardownMethod("")

    def login(self):
        super().login()

    def navigate(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "adCreditText").click()
        self.driver.find_element(By.LINK_TEXT, "Ad Credit").click()

    def parse(self):
        time.sleep(2)
        resp = Selector(text=self.driver.page_source)
        table = resp.xpath('//*[@id="weeklyAdCreditTableContainer"]/div/table/tbody/tr/td/text()').getall()
        numRows = len(table)/8
        rows = []
        for x in range(0, int(numRows)-1):
            rows.append({
                'date': table[0+(x*8)][8:36],
                'adBudget': float(table[1+(x*8)].replace('$', '')),
                'adCreit': float(table[2+(x*8)].replace('$', '')),
                'totalSale': float(table[3+(x*8)].replace('$', '')),
                'refund': float(table[4+(x*8)].replace('$', '')),
                'finalSale': float(table[5+(x*8)].replace('$', '')),
                'adCreditBalance': float(table[6+(x*8)].replace('$', '')),
                'merchantPayout': float(table[7+(x*8)].replace('$', ''))
            })
        print(rows)
        print(rows[1]['finalSale'])

    # def calculateExpectedPayout(self, numRows, rows):
        # need tips on ad credit page to calculate.

    def runSuite(self):
        self.setupMethod("")
        self.login()
        self.navigate()
        self.parse()
        time.sleep(60)
        self.teardownMethod("")




