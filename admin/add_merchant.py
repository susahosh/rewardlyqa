import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from admin.master import AdminPortalMaster
from scrapy import Selector
from library.decorate import tryExcept


class AdminAddMerchantSuite(AdminPortalMaster):

    def __init__(self, chromeDriverPath):
        super().__init__(chromeDriverPath)

    def setupMethod(self, method):
        super().setupMethod("")

    def teardownMethod(self, method):
        super().teardownMethod("")

    def login(self):
        super().login()

    @tryExcept
    def addMerchant(self):
        merchantId = "test4"
        email = "test4@email.com"
        merchantName = "Seller of Things 4"
        phonenumber = '7051234567'
        address = '123 merchant road'
        startDate = "07/06/2023"
        endDate = "07/06/2024"

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "addMerchantButton"))).click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "merchantId").click()
        self.driver.find_element(By.NAME, "merchantId").send_keys(merchantId)
        logoButton = self.driver.find_element(By.XPATH, "//*[@class='form-control-file merchantLogoField']")
        logoButton.send_keys(r"C:\Users\macvi\OneDrive\Pictures\Rewardly UI reference screenshots\rewardlyLogo.png")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.ID, "merchantSignupPasswordInput").click()
        self.driver.find_element(By.ID, "merchantSignupPasswordInput").send_keys("Secret123")
        self.driver.find_element(By.ID, "merchantSignupPasswordShowIcon").click()
        self.driver.find_element(By.NAME, "contactName").click()
        self.driver.find_element(By.NAME, "contactName").send_keys("Test Merchant")
        self.driver.find_element(By.NAME, "contactNumber").click()
        self.driver.find_element(By.NAME, "contactNumber").send_keys(phonenumber)
        self.driver.find_element(By.ID, "countrySelector").click()
        # dropdown = self.driver.find_element(By.ID, "countrySelector")
        # dropdown.find_element(By.XPATH, "//option[. = 'Canada']").click()
        dropdown = Select(self.driver.find_element(By.ID, "countrySelector"))
        dropdown.select_by_visible_text('Canada')
        self.driver.find_element(By.ID, "taxLocationSelector").click()
        # dropdown = self.driver.find_element(By.ID, "taxLocationSelector")
        # dropdown.find_element(By.XPATH, "//option[. = 'Ontario, Canada']").click()
        dropdown = Select(self.driver.find_element(By.ID, "taxLocationSelector"))
        dropdown.select_by_visible_text('Ontario, Canada')
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(merchantName)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "contractStartDate").click()
        self.driver.find_element(By.NAME, "contractStartDate").send_keys(startDate)
        self.driver.find_element(By.ID, "contractLengthSelector").click()
        # dropdown = self.driver.find_element(By.ID, "contractLengthSelector")
        # dropdown.find_element(By.XPATH, "//option[. = '1 year']").click()
        dropdown = Select(self.driver.find_element(By.ID, "contractLengthSelector"))
        dropdown.select_by_visible_text('1 year')
        self.driver.find_element(By.NAME, "bankName").click()
        self.driver.find_element(By.NAME, "bankName").send_keys("bank")
        self.driver.find_element(By.NAME, "bankAccountHolderName").click()
        self.driver.find_element(By.NAME, "bankAccountHolderName").send_keys("Card Holder")
        self.driver.find_element(By.NAME, "bankAccountNumber").click()
        self.driver.find_element(By.NAME, "bankAccountNumber").send_keys("7654321")
        self.driver.find_element(By.NAME, "bankBranchNumber").click()
        self.driver.find_element(By.NAME, "bankBranchNumber").send_keys("00555")
        self.driver.find_element(By.NAME, "bankInstitutionNumber").click()
        self.driver.find_element(By.NAME, "bankInstitutionNumber").send_keys("010")
        time.sleep(2)
        self.driver.find_element(By.ID, "signupButton").click()
        time.sleep(1)
        self.checkTable(merchantName, address, phonenumber, endDate)
        print('Update merchant id, email and merchant name in add_merchant method to for next new merchant test.')

    @tryExcept
    def checkTable(self, merchantName, address, phonenumber, endDate):
        time.sleep(2)
        resp = Selector(text=self.driver.page_source)
        merchantNames = resp.xpath('//*[@id="merchantListWrapper"]/table/tbody/tr/td[1]/text()').getall()
        newShopIndex = merchantNames.index('Seller of Things 2')
        # print(newShopIndex)
        newShopInfo = resp.xpath('//*[@id="merchantListWrapper"]/table/tbody/tr['+str(newShopIndex + 1)+']/td/text()').getall()
        name = newShopInfo[0]
        displayedAddress = newShopInfo[2]
        displayedPhone = newShopInfo[3]
        displayedEndDate = newShopInfo[5]
        # print(name, displayedAddress, displayedPhone, displayedEndDate)
        if name == merchantName and displayedAddress == address and displayedPhone == phonenumber and displayedEndDate == endDate:
            print('New merchant added to list with correct info. Test PASSED')
        else:
            print('Either merchant wasn\'t added to list or info not properly displayed. Test FAILED')

    @tryExcept
    def runSuite(self):
        self.setupMethod("")
        self.login()
        self.addMerchant()
        self.teardownMethod("")
