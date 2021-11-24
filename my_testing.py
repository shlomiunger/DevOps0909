from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome(executable_path="C:/Users/ungershx/Downloads/chromedriver_win32/chromedriver.exe")
# my_driver.get("https://github.com")
# sleep(5)
my_driver.get("C:/Users/ungershx/Downloads/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("musicquality").send_keys("5")
my_driver.find_element_by_id("calculate").click()
expected = "9.00"
actual = my_driver.find_element_by_id("tip").text
if expected == actual:
    print("all good")
else:
    print("not good")

# my_driver.refresh()
# my_driver.back()
