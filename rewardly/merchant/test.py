from merchant.adbudget import MerchantPortalAdBudgetSuite
from merchant.cashback import MerchantPortalCashbackSuite
from merchant.login import MerchantPortalLoginSuite
from merchant.payout import payoutCalculation
from merchant.refund import MerchantPortalRefundSuite
from merchant.shop import MerchantPortalShopSuite
from merchant.transaction import MerchantPortalTransactionSuite

chrome_driver_path = r"C:\Users\macvi\.wdm\drivers\chromedriver\win32\103.0.5060.53\chromedriver.exe"
# Login test suite
login_test = MerchantPortalLoginSuite(chrome_driver_path)
login_test.runSuite()
print()
# ad budget test suite. Pass add budget price to run_suite function.
adBudgetTest = MerchantPortalAdBudgetSuite(chrome_driver_path)
adBudgetTest.runSuite(16.50)
print()

# cashback test suite. Pass cashback % rate to run_suite function.
cashbackTest = MerchantPortalCashbackSuite(chrome_driver_path)
cashbackTest.runSuite(3)
print()

# shop test suite.
shopTest = MerchantPortalShopSuite(chrome_driver_path)
shopTest.runSuite()
print()

# transaction test suite.
transactionTest = MerchantPortalTransactionSuite(chrome_driver_path)
transactionTest.runSuite()
print()

# refund test suite. Pass refund amount of 1 to runSuite method
# ***MANAGER CODE CHANGED, suite currently broken 07/26/22***
# refundTest = MerchantPortalRefundSuite(chrome_driver_path)
# refundTest.runSuite(1)
# print()

# payout calculations test.
# process = payoutCalculation(chrome_driver_path)
# process.runSuite()
