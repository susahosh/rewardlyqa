from android.add_card import AndroidAddCardSuite
from android.balance import AndroidAddFundsSuite
from android.change_password import AndroidPasswordChangeSuite
from android.login import AndroidLoginSuite
from android.pin import AndroidPinChangeSuite
from android.profile import AndroidProfileSuite
from android.signup import AndroidSignupSuite

password = "!Password555"
email = "mac@rewardly.ca"

# Login Suite
test = AndroidLoginSuite()
test.runSuite(email, password)

# signup test suite. Pass email and password strings to runSuite function
# Update email so test can run again.
test2 = AndroidSignupSuite()
test2.runSuite("thisisatest7@email.ca", "#Passkey123")

# Add Card test suite. Pass login info to runSuite method (email, password).
test3 = AndroidAddCardSuite()
test3.runSuite(email, password)

# Adding funds test suite. Pass login info to runSuite method (email, password).
test4 = AndroidAddFundsSuite()
test4.runSuite(email, password)

# Changing profile information. Pass (email, password, new name, new city) to runSuite function
test5 = AndroidProfileSuite()
test5.runSuite(email, password, 'Mac3', 'Van3')

# Change password test suite. Pass (email, old password, new password) to runSuite function.
# UPDATE THE PASSWORD AT THE TOP OF THIS FILE TO THE NEW PASSWORD AFTER RUNNING THIS TEST
# THEN CHANGE NEW PASSWORD IN runSuite METHOD
test6 = AndroidPasswordChangeSuite()
test6.runSuite(email, password, '!Password88')

# Change pin suite. Pass (new pin, current password) to runSuite function
# UPDATE PIN AFTER EACH TIME THIS SUITE IS RUN
test7 = AndroidPinChangeSuite()
test7.runSuite(email, password)
