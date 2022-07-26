from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time
from android.master import AndroidMaster
from library.decorate import tryExcept
from library.write_results import writeResultsCsv


class AndroidPasswordChangeSuite(AndroidMaster):
    def __init__(self):
        super().__init__()

    def login(self, login, password):
        super().login(login, password)

    def passPopup(self):
        super().passPopup()

    @tryExcept
    def navigate(self):
        time.sleep(1)
        accountButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[5]/android.widget.TextView")
        accountButton.click()
        time.sleep(2)
        pwChangeButton = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]")
        pwChangeButton.click()

    @tryExcept
    def emptyPasswordFields(self):
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(1)
        errorMessage1 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]")
        errorMessage2 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        errorMessage3 = self.driver.find_element(by=AppiumBy.XPATH,
                                             value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]")
        if errorMessage1.is_displayed() and errorMessage1.text == 'This field is required' and errorMessage2.is_displayed() and errorMessage2.text == 'This field is required' and errorMessage3.is_displayed() and errorMessage3.text == 'This field is required':
            print('Password was not updated. Correct error messages displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change password with empty fields', 'PASSED', '')
        else:
            print('Problem with error messages or updated with empty fields. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change password with empty fields', 'FAILED', 'Problem with error messages or updated with empty fields')

    @tryExcept
    def passwordTooShort(self):
        time.sleep(1)
        oldPasswordField = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        oldPasswordField.send_keys("!Bella123")
        newPasswordField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        newPasswordField1.send_keys("mac")
        newPasswordField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        newPasswordField2.send_keys("mac")
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(1)
        pwLengthMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                 value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if pwLengthMessage.is_displayed() and pwLengthMessage.text == 'Password length must be 8 characters or more':
            print('Password length error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change to password too short', 'PASSED', '')
        else:
            print('Problem with error message or password reset without meeting requirements. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change password with empty fields', 'FAILED', 'Problem with error message or password reset without meeting requirements')

    @tryExcept
    def weakPassword(self):
        time.sleep(1)
        oldPasswordField = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        oldPasswordField.send_keys("!Bella123")
        newPasswordField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        newPasswordField1.send_keys("maciscool")
        newPasswordField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        newPasswordField2.send_keys("maciscool")
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(1)
        pwCharMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]")
        if pwCharMessage.is_displayed() and pwCharMessage.text == 'Password must contain a lowercase, an uppercase,\na number and a special character':
            print('Password required characters error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change to password too weak (missing # and special chars)', 'PASSED', '')
        else:
            print('Problem with error message or password reset without meeting requirements. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change to password too weak (missing # and special chars)', 'FAILED', 'Problem with error message or password reset without meeting requirements')

    @tryExcept
    def nonMatchingPasswords(self):
        time.sleep(1)
        oldPasswordField = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        oldPasswordField.send_keys("!Bella123")
        newPasswordField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        newPasswordField1.send_keys("#Maciscool123")
        newPasswordField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        newPasswordField2.send_keys("#Maciscool12345")
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(1)
        pwMatchMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]")
        if pwMatchMessage.is_displayed() and pwMatchMessage.text == 'Password does not match':
            print('Password does not match error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change passwords when they don\'t match', 'PASSED', '')
        else:
            print('Problem with error message or password reset without matching. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change passwords when they don\'t match', 'FAILED', 'Problem with error message or password reset without matching')

    @tryExcept
    def invalidOldPassword(self):
        time.sleep(1)
        oldPasswordField = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        oldPasswordField.send_keys("!Bella5555")
        newPasswordField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        newPasswordField1.send_keys("#Maciscool123")
        newPasswordField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        newPasswordField2.send_keys("#Maciscool123")
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(2)
        currentPwMessage = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
        if currentPwMessage.is_displayed() and currentPwMessage.text == 'Invalid current password':
            print('Invalid current password error message displayed. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change passwords with invalid old password', 'PASSED', '')
        else:
            print('Problem with error message or password reset with invalid old password. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Try to change passwords with invalid old password', 'FAILED', 'Problem with error message or password reset with invalid old password')

    @tryExcept
    def validPasswordReset(self, oldPassword, newPassword):
        time.sleep(1)
        oldPasswordField = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        oldPasswordField.send_keys(oldPassword)
        newPasswordField1 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        newPasswordField1.send_keys(newPassword)
        newPasswordField2 = self.driver.find_element(by=AppiumBy.XPATH,
                                                     value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.EditText")
        newPasswordField2.send_keys(newPassword)
        time.sleep(1)
        updateButton = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView")
        updateButton.click()
        time.sleep(1)
        profileHeader = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]")
        if profileHeader.is_displayed():
            print('Returned to profile information page. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Valid password change', 'PASSED', '')
        else:
            print('Did not return to profile information page. Test FAILED.')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Valid password change', 'FAILED', 'Did not return to profile information page')

    @tryExcept
    def logout(self):
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(828, 1743)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(798, 1212)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        try:
            logoutButton = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView")
            logoutButton.click()
            time.sleep(2)
            loginHeader = self.driver.find_element(by=AppiumBy.XPATH,
                                    value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]")
            if loginHeader.is_displayed():
                print("successfully logged out. Test PASSED")
                writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Test logout', 'PASSED', '')
            else:
                print('Not redirected to login page. Test FAILED')
                writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Test logout', 'FAILED', 'Not redirected to login page')
        except Exception as e:
            print('Exception thrown. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Test logout', 'FAILED', 'Exception thrown')

    @tryExcept
    def testNewLogin(self, email, newPassword):
        time.sleep(5)
        super().login(email, newPassword)
        time.sleep(2)
        popUp = self.driver.find_element(by=AppiumBy.XPATH,
                                         value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")
        print("Attempted login with valid information: ")
        if popUp.is_displayed():
            print('Successfully logged in with new password. Test PASSED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Test login with updated password', 'PASSED', '')
        else:
            print('Login unsuccessful. Test FAILED')
            writeResultsCsv(super().resultsPath, 'Android Portal Password Change Suite', 'Test login with updated password', 'FAILED',
                                 'Was not redirected/can\'t see welcome pop-up')
        print('CHANGE PASSWORD IN TEST FILE TO: ', newPassword)

    @tryExcept
    def runSuite(self, email, oldPassword, newPassword):
        self.login(email, oldPassword)
        self.passPopup()
        self.navigate()
        self.emptyPasswordFields()
        self.passwordTooShort()
        self.weakPassword()
        self.nonMatchingPasswords()
        self.invalidOldPassword()
        self.validPasswordReset(oldPassword, newPassword)
        self.logout()
        self.testNewLogin(email, newPassword)

