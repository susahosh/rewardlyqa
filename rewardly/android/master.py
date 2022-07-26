from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from library.write_results import writeResultsCsv
from library.decorate import tryExcept


class AndroidMaster:
    desired_caps = {
        "deviceName": "emulator-5554",
        "platformName": "android",
        "app": r"C:\Users\macvi\AppData\Local\Android\Sdk\platform-tools\android-0.0.20.apk"
    }

    # Path for csv file where test results will be recorded
    resultsPath = r'C:\Users\macvi\PycharmProjects\rewardly\results\android_results.csv'

    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)

    @tryExcept
    def login(self, email, password):
        time.sleep(3)
        emailField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[1]")
        emailField.click()
        emailField.send_keys(email)
        passwordField = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText[2]")
        passwordField.click()
        passwordField.send_keys(password)
        passwordField.click()
        loginButton = self.driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        loginButton.click()

    @tryExcept
    def passPopup(self):
        time.sleep(2)
        okayButton = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]")
        okayButton.click()

