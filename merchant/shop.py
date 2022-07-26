import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from merchant.master import MerchantMasterSuite
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class MerchantPortalShopSuite(MerchantMasterSuite):

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
        self.driver.find_element(By.CSS_SELECTOR, ".storeText").click()

    @tryExcept
    def addNewShop(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "addStoreButton"))).click()
        # self.driver.find_element(By.ID, "addStoreButton").click()
        self.driver.find_element(By.ID, "storeName").click()
        self.driver.find_element(By.ID, "storeName").send_keys("Test Store")
        self.driver.find_element(By.ID, "storeAddress").click()
        self.driver.find_element(By.ID, "storeAddress").send_keys("123 shop road")
        self.driver.find_element(By.NAME, "city").click()
        dropdown = Select(self.driver.find_element(By.NAME, "city"))
        dropdown.select_by_visible_text('Toranto, Canada')
        self.driver.find_element(By.ID, "storeInstagram").click()
        self.driver.find_element(By.ID, "storeInstagram").send_keys("teststoregram")
        self.driver.find_element(By.NAME, "shopCategory").click()
        dropdown = Select(self.driver.find_element(By.NAME, "shopCategory"))
        dropdown.select_by_visible_text('Book')
        self.driver.find_element(By.ID, "addShop").click()
        print('New shop added.')

    @tryExcept
    def editShop(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@class="editCardOperationLogo"]'))).click()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopName").click()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopName").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopName").send_keys(
            "Test Store 2")
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopAddress").click()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopAddress").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopAddress").send_keys(
            "1234 shop road")
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .addStoreInputField > .form-control").click()
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR,
                                            ".grid-item:nth-child(1) .addStoreInputField > .form-control"))
        dropdown.select_by_visible_text('Test, Canada')
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopInstagram").click()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopInstagram").clear()
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .updatableShopInstagram").send_keys(
            "teststoregram1")
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR,
                                            ".grid-item:nth-child(1) .editStoreInputField > .addShopInputBox"))
        dropdown.select_by_visible_text('Grocery')
        self.driver.find_element(By.CSS_SELECTOR, ".grid-item:nth-child(1) .editShop").click()
        print('Shop info updated.')

    @tryExcept
    def checkShopInfo(self):
        time.sleep(2)
        name = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[1]"))).text
        type = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[2]"))).text
        address = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[3]"))).text
        instagram = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/div[3]"))).text
        print("Is shop info properly displayed?")
        if name == 'Test Store':
            print('Store name properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is name properly displayed?', 'PASSED', '')
        else:
            print('Problem with store name. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is name properly displayed?', 'FAILED', 'Problem with store name')
        if type == 'Book':
            print('Store type properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is type properly displayed?', 'PASSED', '')
        else:
            print('Problem with store type. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is type properly displayed?', 'FAILED', 'Problem with store type')
        if address == '123 shop road, Toranto':
            print('Store address properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is address properly displayed?', 'PASSED', '')
        else:
            print('Problem with store address. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is address properly displayed?', 'FAILED', 'Problem with store address')
        if instagram == 'teststoregram':
            print('Store instagram handle properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is instagram handle properly displayed?', 'PASSED', '')
        else:
            print('Problem with store instagram handle. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Added new shop: is instagram handle properly displayed?', 'FAILED', 'Problem with store instagram handle')

    @tryExcept
    def checkShopInfoAfterUpdated(self):
        time.sleep(2)
        name = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[1]"))).text
        type = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[2]"))).text
        address = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/p[3]"))).text
        instagram = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class='grid-item']/div[3]"))).text
        print("\nAre updated values correct?")
        if name == 'Test Store 2':
            print('Store name properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is name properly displayed?', 'PASSED', '')
        else:
            print('Problem with store name. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is name properly displayed?', 'FAILED', 'Problem with store name')
        if type == 'Grocery':
            print('Store type properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is type properly displayed?', 'PASSED', '')
        else:
            print('Problem with store type. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is type properly displayed?', 'FAILED', 'Problem with store type')
        if address == '1234 shop road, Test':
            print('Store address properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is address properly displayed?', 'PASSED', '')
        else:
            print('Problem with store address. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is address properly displayed?', 'FAILED', 'Problem with store address')
        if instagram == 'teststoregram1':
            print('Store instagram handle properly displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is instagram handle properly displayed?', 'PASSED', '')
        else:
            print('Problem with store instagram handle. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Updated shop: is instagram handle properly displayed?', 'FAILED', 'Problem with store instagram handle')

    @tryExcept
    def deleteShop(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="cardOperationLogo"]'))).click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".grid-item:nth-child(1) > #deleteStorePopupContainer > #deleteStorePopupWrapper .deleteShop").click()
        print("\nAttempted to delete shop")
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@class="grid-item"]').is_displayed()
            print("Shop not deleted. Test FAILED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Delete shop', 'FAILED', 'Shop not deleted')

        except Exception as e:
            print("Shop deleted. Test PASSED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Delete shop', 'PASSED', '')
            self.addShopNoReport()
        except 'NoSuchElementException' as a:
            print("Shop deleted. Test PASSED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Shop Suite', 'Delete shop', 'PASSED', '')
            self.addShopNoReport()

    #The 'No Report' methods are to create and delete shops pre and post test execution so the next test can start properly.
    # There must be a shop in order for the transaction tests to work.
    # There must be no shop at the start of this shop test suite.

    @tryExcept
    def addShopNoReport(self):
        self.driver.find_element(By.ID, "addStoreButton").click()
        self.driver.find_element(By.ID, "storeName").click()
        self.driver.find_element(By.ID, "storeName").send_keys("Test Store")
        self.driver.find_element(By.ID, "storeAddress").click()
        self.driver.find_element(By.ID, "storeAddress").send_keys("123 shop road")
        self.driver.find_element(By.NAME, "city").click()
        dropdown = Select(self.driver.find_element(By.NAME, "city"))
        dropdown.select_by_visible_text('Toranto, Canada')
        self.driver.find_element(By.ID, "storeInstagram").click()
        self.driver.find_element(By.ID, "storeInstagram").send_keys("teststoregram")
        self.driver.find_element(By.NAME, "shopCategory").click()
        dropdown = Select(self.driver.find_element(By.NAME, "shopCategory"))
        dropdown.select_by_visible_text('Book')
        self.driver.find_element(By.ID, "addShop").click()

    @tryExcept
    def deleteShopNoReport(self):
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="cardOperationLogo"]'))).click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".grid-item:nth-child(1) > #deleteStorePopupContainer > #deleteStorePopupWrapper .deleteShop").click()

    @tryExcept
    def runSuite(self):
        self.setupMethod("")
        self.login()
        self.navigate()
        try:
            self.deleteShopNoReport()
        except Exception as e:
            print("Already no shop\n", e)
        self.addNewShop()
        self.checkShopInfo()
        self.editShop()
        self.checkShopInfoAfterUpdated()
        self.deleteShop()
        self.teardownMethod("")



