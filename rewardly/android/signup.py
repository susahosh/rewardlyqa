from appium.webdriver.common.appiumby import AppiumBy
import time
from android.master import AndroidMaster
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class AndroidSignupSuite(AndroidMaster):
    def __init__(self):
        super().__init__()

    @tryExcept
    def navigate(self):
        time.sleep(5)
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]")
        signupButton.click()

    @tryExcept
    def emptyEmailForm(self):
        time.sleep(2)
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(1)
        fieldRequiredMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if fieldRequiredMessage.is_displayed() and fieldRequiredMessage.text == 'This field is required':
            print('Error message displayed and is correct. Did not proceed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty Email Form', 'PASSED', '')
        else:
            print('Problem. Either proceeded with no email or error message is broken. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty Email Form', 'FAILED', 'Either proceeded with no email or error message is broken')

    @tryExcept
    def invalidEmail(self):
        emailField = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        emailField.send_keys("notanemail")
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(1)
        enterValidEmailMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if enterValidEmailMessage.is_displayed() and enterValidEmailMessage.text == 'Enter valid email':
            print('Error message displayed and is correct. Did not proceed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Invalid Email', 'PASSED', '')
        else:
            print('Problem. Either proceeded with no email or error message is broken. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Invalid Email', 'FAILED', 'Either proceeded with no email or error message is broken')

    @tryExcept
    def alreadyUsedEmail(self):
        time.sleep(1)
        emailField = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")

        emailField.send_keys("mac@rewardly.ca")
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(1)
        emailAlreadyExistsMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if emailAlreadyExistsMessage.is_displayed() and emailAlreadyExistsMessage.text == 'Email already exists. Try another':
            print('Error message displayed and is correct. Did not proceed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Already Used Email', 'PASSED', '')
        else:
            print('Problem. Either proceeded with previously used email or error message is broken. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Already Used Email', 'FAILED', 'Either proceeded with previously used email or error message is broken')

    @tryExcept
    def validEmail(self, email):
        emailField = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        emailField.send_keys(email)
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(2)
        enterCityName = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")
        if enterCityName.is_displayed() and enterCityName.text == 'Enter your city name':
            print('Proceeded to city form. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Valid Email', 'PASSED', '')
        else:
            print('Problem. City form not visible. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Valid Email', 'FAILED', 'May not have proceeded, city form not visible')

    @tryExcept
    def emptyCityForm(self):
        # Button not visible rn for some reason. Will add unique identifiers when available.
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(2)
        fieldRequiredMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if fieldRequiredMessage.is_displayed() and fieldRequiredMessage.text == 'This field is required':
            print('Error message displayed and is correct. Did not proceed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty City Form', 'PASSED', '')
        else:
            print('Problem. Either proceeded with no city or error message is broken. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty City Form', 'FAILED',
                                 'Either proceeded with no city or error message is broken')

    @tryExcept
    def validCity(self):
        cityForm = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
        cityForm.send_keys("cityville")
        nextButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView")
        nextButton.click()
        time.sleep(2)
        enterPasswordText = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if enterPasswordText.is_displayed() and enterPasswordText.text == 'Please secure your account with password.':
            print('Proceeded to password page. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Valid City Form', 'PASSED', '')
        else:
            print('Problem. Enter password text not visible. May not have proceeded. Test FAILED. ')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Valid City Form', 'FAILED', 'Enter password text not visible. May not have proceeded.')

    @tryExcept
    def emptyPasswordFields(self):
        time.sleep(1)
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        signupButton.click()
        time.sleep(1)
        fieldRequiredMessage1 = self.driver.find_element(by=AppiumBy.XPATH,
                                                        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        fieldRequiredMessage2 = self.driver.find_element(by=AppiumBy.XPATH,
                                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]")
        if fieldRequiredMessage1.is_displayed() and fieldRequiredMessage1.text == 'This field is required' and fieldRequiredMessage2.is_displayed() and fieldRequiredMessage2.text == 'This field is required':
            print('Error message displayed and is correct. Did not signup. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty password forms ', 'PASSED', '')
        else:
            print('Problem. Either proceeded with no email or error message is broken. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Empty password forms', 'FAILED',
                                 'Either signed up with no password or error message is broken')

    @tryExcept
    def passwordTooShort(self):
        time.sleep(1)
        pwField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        pwField1.send_keys("mac")
        pwField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]")
        pwField2.send_keys("mac")
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        signupButton.click()
        time.sleep(1)
        pwLengthMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if pwLengthMessage.is_displayed() and pwLengthMessage.text == 'Password length must be 8 characters or more':
            print('Did not signup. Password length error message displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Password Too Short', 'PASSED', '')
        else:
            print('Problem. Either signed up with short password or error message is broken. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Password Too Short', 'FAILED', 'Either signed up with short password or error message is broken')

    @tryExcept
    def weakPassword(self):
        time.sleep(1)
        pwField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        pwField1.send_keys("maciscool")
        pwField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]")
        pwField2.send_keys("maciscool")
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        signupButton.click()
        time.sleep(1)
        charactersMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                               value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")

        if charactersMessage.is_displayed() and charactersMessage.text == 'Password must contain a lowercase, an uppercase,\na number and a special character':
            print('Did not signup. Password required characters error message displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Password Missing Caps, Number and Special chars', 'PASSED', '')
        else:
            print('Problem. Either signed up with password missing special character, number and a capital letter or error message is broken. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Password Missing Caps adn Special chars', 'FAILED', 'Either signed up with password missing special character, number and capital letter or error message is broken')

    @tryExcept
    def nonMatchingPasswords(self):
        time.sleep(1)
        pwField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        pwField1.send_keys("#Maciscool123")
        pwField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]")
        pwField2.send_keys("#Maciscool12")
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        signupButton.click()
        time.sleep(1)
        pwDoesNotMatchMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]")
        if pwDoesNotMatchMessage.is_displayed() and pwDoesNotMatchMessage.text == 'Password does not match':
            print('Did not signup. Password does not match error message displayed. Test PASSED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Non-Matching Passwords', 'PASSED', '')
        else:
            print('Problem. Either signed up with passwords that don\'t match or error message is broken. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Signup Suite', 'Non-Matching Passwords', 'PASSED', 'Either signed up with passwords that don\'t match or error message is broken')

    @tryExcept
    def validPassword(self, email, password):
        time.sleep(1)
        pwField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
        pwField1.send_keys(password)
        pwField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                            value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]")
        pwField2.send_keys(password)
        signupButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        signupButton.click()
        self.testNewAccountLogin(email, password)

    @tryExcept
    def testNewAccountLogin(self, email, password):
        time.sleep(5)
        super().login(email, password)
        time.sleep(2)
        popUp = self.driver.find_element(by=AppiumBy.XPATH,
                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
        print("Attempted login with valid information: ")
        if popUp.is_displayed():
            print('Successfully logged in with new account. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Valid Login Form', 'PASSED', '')
            print('\nUpdate email in the test file so next new account can be created/tested')
        else:
            print('Login unsuccessful. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Valid Login Form', 'FAILED',
                                 'Was not redirected/can\'t see welcome pop-up')

    @tryExcept
    def runSuite(self, email, password):
        self.navigate()
        # self.emptyEmailForm()
        # self.invalidEmail()
        # self.alreadyUsedEmail()
        time.sleep(2)
        self.validEmail(email)
        time.sleep(5)
        self.emptyCityForm()
        self.validCity()
        self.emptyPasswordFields()
        self.passwordTooShort()
        self.weakPassword()
        self.nonMatchingPasswords()
        self.validPassword(email, password)
