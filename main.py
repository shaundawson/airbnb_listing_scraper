from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH, FB_EMAIL, FB_PW
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from twilio.rest import Client

s=Service(executable_path=CHROME_DRIVER_PATH)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
chrome_options.binary_location=(CHROME_BINARY_LOC)
driver = webdriver.Chrome(service=s, options=chrome_options)


# Set up Twilio client
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
client = Client(account_sid, auth_token)

# Set up Airbnb URL and Chrome driver
url = 'https://www.airbnb.com/s/Bed~Stuy--Brooklyn--NY--USA/homes?refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_lengths%5B%5D=one_month&date_picker_type=flexible_dates&adults=2&search_type=filter_change&tab_id=home_tab&query=Bed-Stuy%2C%20Brooklyn%2C%20NY&price_filter_input_type=1&price_filter_num_nights=28&channel=EXPLORE&place_id=ChIJIbiotnVcwokR3OuRZieHvPM&source=structured_search_input_header&price_min=150&price_max=2700&room_types%5B%5D=Entire%20home%2Fapt&amenities%5B%5D=4&superhost=true'


# Navigate to the URL
driver.get(url)

# Wait for the Facebook button to be clickable
facebook_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="social-auth-button-facebook"]')))

# Click on the Facebook button
facebook_button.click()

# Switch to the new window that opens
driver.switch_to.window(driver.window_handles[-1])

# Enter login information in the new window
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
email_input.send_keys(FB_EMAIL)

password_input =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'pass')))
password_input.send_keys(FB_PW)
password_input.send_keys(Keys.ENTER)

# login_button = driver.name("login")
# login_button.click()

# Switch back to the original window
driver.switch_to.window(driver.window_handles[0])

time.sleep(500)

# Get the first listing's name and price
listing_name = driver.find_element_by_xpath('(//div[@class="_gig1e7"])[1]//div[@class="_twmmpk"]/div')
listing_price = driver.find_element_by_xpath('(//div[@class="_gig1e7"])[1]//div[@class="_doc79r"]/span[@aria-hidden="true"]')

# # Send a text message with the details
# message = f"New York Airbnb Listing - Name: {listing_name.text}, Price: {listing_price.text}"
# twilio_number = 'your_twilio_number'
# recipient_number = 'recipient_phone_number'

# client.messages.create(
#     body=message,
#     from_=twilio_number,
#     to=recipient_number
# )

# Quit the driver
driver.quit()