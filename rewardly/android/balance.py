from appium.webdriver.common.appiumby import AppiumBy
import time
from android.master import AndroidMaster
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class AndroidAddFundsSuite(AndroidMaster):
    def __init__(self):
        super().__init__()

    def login(self, login, password):
        super().login(login, password)

    def passPopup(self):
        super().passPopup()

    @tryExcept
    def navigate(self):
        time.sleep(2)
        addWalletBalanceButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]")
        addWalletBalanceButton.click()

    @tryExcept
    def quickAddFunds(self, quickAddAmount, xpath):
        time.sleep(5)
        walletBalanceElement = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]")
        initialWalletBalance = float(walletBalanceElement.text.replace("$",""))
        time.sleep(2)
        quickAddButton = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        quickAddButton.click()
        time.sleep(2)
        try:
            cancelButton = self.driver.find_element(by=AppiumBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")
            cancelButton.click()
            print('Cancel button works. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite','Test quick add confirmation popup cancel buttton functionality.', 'PASSED', '')
        except Exception as e:
            print('Cancel button did not work, exception thrown. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite','Test quick add confirmation popup cancel buttton functionality.', 'FAILED', 'Cancel button did not work, exception thrown')

        time.sleep(2)
        quickAddButton.click()
        quickAddButton.click() # have to click twice after cancel?????? Ask Sush
        time.sleep(2)
        okayAddButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        okayAddButton.click()
        time.sleep(5)
        walletBalanceElement = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]")
        currentWalletBalance = walletBalanceElement.text.replace("$", "")
        if initialWalletBalance + float(quickAddAmount) == float(currentWalletBalance):
            print(quickAddAmount + ' dollars added with quick add. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check quick add balance increase for $' + quickAddAmount, 'PASSED', '')
        else:
            print(quickAddAmount + ' dollars was not added to balance. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite','Check quick add balance increase for $' + quickAddAmount, 'FAILED', quickAddAmount + ' dollars was not added to balance')
        print('fuck this')
        # updatedMessage = self.driver.find_element(by=AppiumBy.XPATH,
        #                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]")
        # if updatedMessage.is_displayed() and updatedMessage.text == 'Wallet balance updated':
        #     print('Wallet balance updated message displayed. Test PASSED')
        #     writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check wallet balance update message.', 'PASSED', '')
        # elif updatedMessage.is_displayed() and updatedMessage.text == 'Failed to process your request. Please try again':
        #     print("'Failed to process your request. Please try again' error shown. Test FAILED")
        #     writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Check wallet balance update message.', 'FAILED', "'Failed to process your request. Please try again' error shown")
        # else:
        #     print('Wallet balance updated message not visible. Test FAILED')
        #     writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check wallet balance update message.', 'FAILED', "Wallet balance updated message not visible")
        # time.sleep(1)
        self.checkTransactionHistory(quickAddAmount)

    @tryExcept
    def customBalance(self, addAmount):
        time.sleep(5)
        walletBalanceElement = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]")
        initialWalletBalance = float(walletBalanceElement.text.replace("$", ""))
        addCustomBalanceButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView")
        addCustomBalanceButton.click()
        time.sleep(2)
        addAmountField = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
        addAmountField.send_keys(str(addAmount))
        time.sleep(1)
        addBalanceButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        addBalanceButton.click()
        time.sleep(2)
        okayAddButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        okayAddButton.click()
        time.sleep(5)
        walletBalanceElement = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]")
        currentWalletBalance = walletBalanceElement.text.replace("$", "")
        if initialWalletBalance + addAmount == float(currentWalletBalance):
            print(str(addAmount) + ' dollars added with custom add. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite','Added ' + addAmount + 'dollars with custom add', 'PASSED', '')
        else:
            print(str(addAmount) + ' dollars was not added to balance. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite','Added ' + str(addAmount) + 'dollars with custom add', 'FAILED', str(addAmount) + ' dollars was not added to balance.')
        time.sleep(2)
        # updatedMessage = self.driver.find_element(by=AppiumBy.XPATH,
        #                                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]")
        # if updatedMessage.is_displayed() and updatedMessage.text == 'Wallet balance updated':
        #     print('Wallet balance updated message displayed. Test PASSED')
        #     writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check wallet balance update message.', 'PASSED', '')
        # elif updatedMessage.is_displayed() and updatedMessage.text == 'Failed to process your request. Please try again':
        #     print("'Failed to process your request. Please try again' error shown. Test FAILED")
        #     writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check wallet balance update message.', 'FAILED', "'Failed to process your request. Please try again' error shown")
        # else:
        #     print('Wallet balance updated message not visible. Test FAILED')
        #     writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check wallet balance update message.', 'FAILED', "Wallet balance updated message not visible")
        # time.sleep(1)
        self.checkTransactionHistory(str(addAmount))

    @tryExcept
    def checkTransactionHistory(self, lastTransactionAmount):
        time.sleep(2)
        transactionHistoryButton = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[4]")
        transactionHistoryButton.click()
        time.sleep(2)
        # /android.widget.TextView[2] is where the amount is for each transaction.
        # The ViewGroup[x] just before that is what transaction you're on. The very top one is x = 1.
        # Each transaction block is ViewGroup[x] where x = 1,2,3,...,n.
        lastShownTransactionAmountElement = self.driver.find_element(by=AppiumBy.XPATH,
                                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]")
        lastShownTransactionAmount = lastShownTransactionAmountElement.text.replace("+$", "")
        if lastShownTransactionAmount == lastTransactionAmount:
            print('Last transaction was displayed in history. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check is last transaction is show in history', 'PASSED', '')
        else:
            print('Either wrong amount displayed or last transaction was not displayed in history. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Wallet Balance Suite', 'Check is last transaction is show in history', 'FAILED', 'Either wrong amount displayed or last transaction was not displayed in history')

        self.navigate()

    # @tryExcept
    def runSuite(self, email, password):
        # dictionary of xpaths for the different quick add amounts
        quickAddPaths = {
            '20': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]',
            '40': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]',
            '80': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]',
            '100': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[4]'
        }
        self.login(email, password)
        self.passPopup()
        self.navigate()
        # for amount in quickAddPaths:
        #    time.sleep(2)
         #   self.quickAddFunds(amount, quickAddPaths[amount])
        self.customBalance(5)
