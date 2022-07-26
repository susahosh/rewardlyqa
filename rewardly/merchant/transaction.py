import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from merchant.master import MerchantMasterSuite
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class MerchantPortalTransactionSuite(MerchantMasterSuite):

    def __init__(self, chromeDriverPath):
        super().__init__(chromeDriverPath)

    def setupMethod(self, method):
        super().setupMethod("")

    def teardownMethod(self, method):
        super().teardownMethod("")

    def login(self):
        super().login()

    @tryExcept
    def generateQrCode(self, shop):
        self.driver.find_element(By.ID, "shopDropdownSelector").click()
        dropdown = Select(self.driver.find_element(By.ID, "shopDropdownSelector"))
        dropdown.select_by_visible_text(shop)
        self.driver.find_element(By.ID, "chargeAmountInput").send_keys("20")
        self.driver.find_element(By.ID, "submitButtonToGenerateQRCode").click()
        print('Attempted to generate QR code: ')
        if WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'qrCode'))).is_displayed():
            print("QR code generated for " + shop + ". Test PASSED.")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Generate QR code for ' + shop,
                                   'PASSED', '')
            self.driver.find_element(By.ID, "transactionPopupBackButton").click()
            self.driver.find_element(By.ID, "chargeAmountInput").clear()
        else:
            print("PROBLEM. QR code wasn't created. Test FAILED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Generate QR code for ' + shop,
                                   'FAILED',
                                   'QR code wasn\'t created')

    @tryExcept
    def addItemToList(self):
        self.driver.find_element(By.ID, "productItemInputBox").click()
        self.driver.find_element(By.ID, "productItemInputBox").send_keys("Banana")
        self.driver.find_element(By.ID, "addTillItem").click()
        print('Attempted to add item to list: ')
        if self.driver.find_element(By.CLASS_NAME, "productRow").is_displayed():
            print("Item added successfully. Test PASSED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Add item to list',
                                   'PASSED', '')
        else:
            print("PROBLEM. Item was not added to the list. Test FAILED")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Add item to list',
                                   'FAILED', 'Item was not added to the list')

    @tryExcept
    def incrementItemQuantity(self):
        count = int(self.driver.find_element(By.ID, "productItemQuantity1").text)
        if count == 1:
            self.driver.find_element(By.CSS_SELECTOR, ".productIncrementer").click()
        else:
            print("Cannot perform item increment test. Initial quantity is wrong.")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Increment item quantity',
                                   'FAILED', 'Cannot perform item increment test. Initial quantity is wrong.')
        count = int(self.driver.find_element(By.ID, "productItemQuantity1").text)
        print('Attempted to increment item quantity: ')
        if count == 2:
            print('Increment works. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Increment item quantity',
                                   'PASSED', '')
        else:
            print('Problem with increment function. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Increment item quantity',
                                   'FAILED', 'Problem with increment function')

    @tryExcept
    def decrementItemQuantity(self):
        self.driver.find_element(By.CSS_SELECTOR, ".productDecrementer").click()
        count = int(self.driver.find_element(By.ID, "productItemQuantity1").text)
        print('Attempted to decrement item quantity: ')
        if count == 1:
            print('Decrement works. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Decrement item quantity',
                                   'PASSED', '')
        else:
            print('Problem with decrement function. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Decrement item quantity',
                                   'FAILED', 'Problem with decrement function')

    @tryExcept
    def deleteItem(self):
        if self.driver.find_element(By.CLASS_NAME, "productRow").is_displayed():
            self.driver.find_element(By.CSS_SELECTOR, ".removeItem").click()
        else:
            print('Cannot perform delete item test. List may already be empty.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Delete item',
                                   'FAILED', 'Cannot perform delete item test. List may already be empty.')
        print('Attempted to delete item: ')
        if self.driver.find_element(By.ID, "emptyProductMessage").is_displayed():
            print('Item deleted from list. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Delete item',
                                   'PASSED', '')
        else:
            print('Item was not deleted. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Transaction Suite', 'Delete item',
                                   'FAILED', 'Item was not deleted')

    @tryExcept
    def runSuite(self):
        self.setupMethod("")
        self.login()
        self.generateQrCode("Test Store")
        self.addItemToList()
        self.incrementItemQuantity()
        self.decrementItemQuantity()
        self.deleteItem()
        time.sleep(5)
        self.teardownMethod("")
