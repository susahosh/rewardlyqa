import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from merchant.master import MerchantMasterSuite
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class MerchantPortalRefundSuite(MerchantMasterSuite):

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
        self.driver.find_element(By.CSS_SELECTOR, ".tillMenu:nth-child(2) > div").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .invoiceDetailsButton").click()

    @tryExcept
    def clearForms(self):
        self.driver.find_element(By.ID, "refundAmount").clear()
        self.driver.find_element(By.ID, "verificationCodeInputBox").clear()

    @tryExcept
    def canRefund(self, refund):
        time.sleep(1)
        canRefund = float(
            self.driver.find_element(By.CSS_SELECTOR, ".invoiceDetailsBold:nth-child(2)").text.replace("Can refund $",
                                                                                                       ""))
        if canRefund < refund:
            print("Cannot perform refund tests. Nothing left to refund. ADD A NEW TRANSACTION")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Login Suite', 'Refund cases',
                                   'FAILED',
                                   'Cannot perform refund tests. Nothing left to refund. ADD A NEW TRANSACTION')
            return False
        else:
            print('Able to refund $' + str(canRefund))
            return True

    @tryExcept
    def attemptRefundWitInvalidManagerCode(self, refund):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "refundAmount"))).click()
        # self.driver.find_element(By.ID, "refundAmount").click()
        self.driver.find_element(By.ID, "refundAmount").send_keys(str(refund))
        self.driver.find_element(By.ID, "verificationCodeInputBox").click()
        self.driver.find_element(By.ID, "verificationCodeInputBox").send_keys("123")
        self.driver.find_element(By.NAME, "button").click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "confirmRefundButton"))).click()
        # self.driver.find_element(By.ID, "confirmRefundButton").click()
        print('Attempted to refund with invalid manger code:')
        if WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, 'refundPopupError'))).is_displayed():
            if self.driver.find_element(By.ID, "refundPopupError").text == 'Invalid manager verification code':
                print('Invalid manager code error displayed. Test PASSED.')
                writeResultsCsv(super().resultsPath, 'Merchant Portal Refund Suite', 'Attempted to refund with invalid manger code','PASSED', '')
                result = True
            else:
                print('Error thrown but improper message. Test FAILED')
                writeResultsCsv(super().resultsPath, 'Merchant Portal Refund Suite', 'Attempted to refund with invalid manger code','FAILED', 'Error thrown but improper message')
                result = True
        else:
            print("No error message displayed. Test FAILED.")
            writeResultsCsv(super().resultsPath, 'Merchant Portal Refund Suite', 'Attempted to refund with invalid manger code',
                                   'FAILED', 'No error message displayed')
            result = True
        self.driver.find_element(By.ID, "refundPopupCancelButton").click()
        return result

    @tryExcept
    def completeRefund(self, refund):
        time.sleep(1)
        initialCanRefund = float(
            self.driver.find_element(By.CSS_SELECTOR, ".invoiceDetailsBold:nth-child(2)").text.replace("Can refund $",
                                                                                                       ""))
        initialAlreadyRefunded = float(self.driver.find_element(By.CSS_SELECTOR,
                                                    ".invoiceDetails:nth-child(1) > .invoiceDetailsBold").text.replace(
            "$", ""))

        print(initialCanRefund, initialAlreadyRefunded)
        self.driver.find_element(By.ID, "refundAmount").click()
        self.driver.find_element(By.ID, "refundAmount").send_keys(str(refund))
        self.driver.find_element(By.ID, "verificationCodeInputBox").click()
        self.driver.find_element(By.ID, "verificationCodeInputBox").send_keys("1234") #MANAGER CODE CHANGED, NEED TO UPDATE
        self.driver.find_element(By.NAME, "button").click()
        self.driver.find_element(By.ID, "confirmRefundButton").click()
        time.sleep(5)
        alreadyRefunded = float(self.driver.find_element(By.CSS_SELECTOR,
                                            ".invoiceDetails:nth-child(1) > .invoiceDetailsBold").text.replace("$", ""))
        canRefund = float(
            self.driver.find_element(By.CSS_SELECTOR, ".invoiceDetailsBold:nth-child(2)").text.replace("Can refund $",
                                                                                                       ""))
        print('Attempted valid refund:')
        if initialAlreadyRefunded + refund == alreadyRefunded and initialCanRefund - refund == canRefund:
            print('Refund completed with proper values changed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Refund Suite', 'Attempted valid refund',
                                   'PASSED', '')
        else:
            print('Refund not displayed. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Merchant Portal Refund Suite', 'Attempted to refund with invalid manger code',
                                   'FAILED', 'Refund not displayed (investigate)')

    @tryExcept
    def runSuite(self, refund):
        self.setupMethod("")
        self.login()
        self.navigate()
        canProceed = self.canRefund(refund)
        print(self.canRefund)
        if self.canRefund:
            self.attemptRefundWitInvalidManagerCode(refund)
            self.clearForms()
            self.completeRefund(refund)
        self.teardownMethod("")
