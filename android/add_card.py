from appium.webdriver.common.appiumby import AppiumBy
import time
from android.master import AndroidMaster
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class AndroidAddCardSuite(AndroidMaster):
    def __init__(self):
        super().__init__()

    def login(self, login, password):
        super().login(login, password)

    def passPopup(self):
        super().passPopup()

    @tryExcept
    def addCard(self):
        time.sleep(2)
        addCardButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView")
        addCardButton.click()
        time.sleep(2)
        cardNNumberField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        cardNNumberField.send_keys("3566664444444445")
        cardHolderNameField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
        cardHolderNameField.send_keys("Mac Vibert")
        expiryField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        expiryField.send_keys("0823")
        cvvField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.EditText")
        cvvField.send_keys("345")
        postalCodeField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        postalCodeField.send_keys("l3v7h2")
        time.sleep(1)
        addCardSubmitButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]")
        addCardSubmitButton.click()

    @tryExcept
    def checkCard(self):
        time.sleep(5)
        try:
            cardNumberElement = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]")
            cardNumber = cardNumberElement.text.replace("Card number: XXXX ", "")
            if cardNumber == '4445':
                print('Proper card number displayed. Test PASSED')
                writeResultsCsv(super().resultsPath, 'Android Portal Add Card Suite', 'Added new card: Is card number properly displayed?', 'PASSED', '')

            else:
                print('Problem. Last 4 card digits not properly displayed. Test FAILED')
                writeResultsCsv(super().resultsPath, 'Android Portal Add Card Suite', 'Added new card: Is card number properly displayed?', 'FAILED', 'Last 4 card digits not properly displayed')

            cardHolderNameElement = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
            cardHolderName = cardHolderNameElement.text.replace("Name: ", "")
            if  cardHolderName == 'Mac Vibert':
                print('Card holder name properly displayed. Test PASSED')
                writeResultsCsv(super().resultsPath, 'Android Portal Add Card Suite', 'Added new card: Is card holder name properly displayed?', 'PASSED', '')
            else:
                print('Problem. Card holder name not displayed properly. Test FAILED')
                writeResultsCsv(super().resultsPath, 'Android Portal Add Card Suite', 'Added new card: Is card holder name properly displayed?', 'FAILED', 'Card holder name not displayed properly')

            # defaultElement = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]")
            # if defaultElement.is_displayed() and defaultElement.text == 'Default':
            #    print('First/only card was made default automatically. Test PASSED')
            # else:
            #    print('Problem. Card was not made default or default not displayed. Test FAILED')
        except Exception as e:
            print('Exception thrown. Card may not have been added. Check if you tried to add the same card. Test FAILED')

            writeResultsCsv(super().resultsPath, 'Android Portal Add Card Suite', 'Added new card: Is card holder name properly displayed?',
                         'FAILED', 'Exception thrown, check if you\'ve already added that card')

    @tryExcept
    def runSuite(self, email, password):
        self.login(email, password)
        self.passPopup()
        self.addCard()
        self.checkCard()
