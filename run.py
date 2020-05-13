from selenium import webdriver
import time

name = "Jannett Lin"
email = "ypan23@uw.edu"
tel = "111-983-4793"
address = "4509 NE 55th st"
zip = "98103"
city = "Seattle"
state = "WA"
country = "USA"

number = "0000 0000 0000 0000"
expiration_month = '06'
expiration_year = "2025"
cvv = "810"

chromedriver_location = "chromedriver.exe"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click()

time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()


name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_path = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_path).send_keys(email)

tel_path = '//*[@id="order_tel"]'
driver.find_element_by_xpath(tel_path).send_keys(tel)

address_path = '//*[@id="bo"]'
driver.find_element_by_xpath(address_path).send_keys(address)

zip_path = '//*[@id="order_billing_zip"]'
driver.find_element_by_xpath(zip_path).send_keys(zip)

city_path = '//*[@id="order_billing_city"]'
driver.find_element_by_xpath(city_path).send_keys(city)

state_path = '//*[@id="order_billing_state"]/option[56]'
driver.find_element_by_xpath(state_path).click()

number_path = '//*[@id="rnsnckrn"]'
driver.find_element_by_xpath(number_path).send_keys(number)

expiration_month_path = '//*[@id="credit_card_month"]/option[6]'
driver.find_element_by_xpath(expiration_month_path).click()

expiration_year_path = '//*[@id="credit_card_year"]/option[6]'
driver.find_element_by_xpath(expiration_year_path).click()

cvv_path = '//*[@id="orcer"]'
driver.find_element_by_xpath(cvv_path).send_keys(cvv)

i_agree_path = '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
driver.find_element_by_xpath(i_agree_path).click()

process_path = '//*[@id="pay"]/input'
driver.find_element_by_xpath(process_path).click()

print("Web Driver Run")
