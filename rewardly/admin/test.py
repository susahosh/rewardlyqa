from admin.add_merchant import AdminAddMerchantSuite

chrome_driver_path = r"C:\Users\macvi\.wdm\drivers\chromedriver\win32\101.0.4951.41\chromedriver.exe"


# Add new merchant test.
# Update merchant id, email and merchant name in add_merchant method to for next new merchant test.
test = AdminAddMerchantSuite(chrome_driver_path)
test.runSuite()
