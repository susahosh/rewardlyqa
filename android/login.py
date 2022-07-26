from appium.webdriver.common.appiumby import AppiumBy
import time
from android.master import AndroidMaster
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class AndroidLoginSuite(AndroidMaster):
    def __init__(self):
        super().__init__()

    @tryExcept
    def emptyLoginForm(self):
        time.sleep(5)
        loginButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        loginButton.click()
        requiredFieldMessage = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]").text
        print("Attempted login with empty forms: ")
        if requiredFieldMessage == 'This field is required':
            print('Did not login. Proper error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Empty Login Form', 'PASSED', '')

        else:
            print('Problem. Incorrect error message or something else. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Empty Login Form', 'FAILED', 'Incorrect error message or something else')

    @tryExcept
    def invalidLogin(self):
        time.sleep(2)
        emailField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]")
        emailField.click()
        emailField.send_keys("wrongemail@email.com")
        passwordField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]")
        passwordField.send_keys("123456")
        loginButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        time.sleep(2)
        loginButton.click()
        time.sleep(1)
        invalidInfoMessage = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]").text
        print("Attempted login with invalid information: ")
        if invalidInfoMessage == 'Invalid email or password':
            print('Did not login. Proper error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Invalid Login Form', 'PASSED', '')
        else:
            print('Problem. Either logged in with wrong info or error message is wrong. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Invalid Login Form', 'FAILED', 'Either logged in with wrong info or error message is wrong')

    @tryExcept
    def validLogin(self, email, password):
        emailField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]")
        emailField.click()
        emailField.send_keys(email)
        passwordField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]")
        passwordField.click()
        passwordField.send_keys(password)
        passwordField.click()
        loginButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        loginButton.click()
        time.sleep(2)
        popUp = self.driver.find_element(by=AppiumBy.XPATH, value = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
        print("Attempted login with valid information: ")
        if popUp.is_displayed():
            print('Successfully logged in. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Valid Login Form', 'PASSED', '')
        else:
            print('Login unsuccessful. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Login Suite', 'Valid Login Form', 'FAILED', 'Was not redirected/can\'t see welcome pop-up')

    @tryExcept
    def runSuite(self, email, password):
        self.emptyLoginForm()
        self.invalidLogin()
        self.validLogin(email, password)
