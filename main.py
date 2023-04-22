# Import necessary libraries
import time
from selenium import webdriver
from twilio.rest import Client

# Set up Twilio client
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
client = Client(account_sid, auth_token)

# Set up Airbnb URL and Chrome driver
url = 'https://www.airbnb.com'
driver = webdriver.Chrome('path_to_chrome_driver')

# Navigate to the URL
driver.get(url)

# Enter the search criteria
location_input = driver.find_element_by_xpath('//input[@placeholder="Where are you going?"]')
location_input.send_keys('New York')

checkin_input = driver.find_element_by_xpath('//input[@name="checkin"]')
checkin_input.clear()
checkin_input.send_keys('2023-05-01')

checkout_input = driver.find_element_by_xpath('//input[@name="checkout"]')
checkout_input.clear()
checkout_input.send_keys('2023-05-07')

search_button = driver.find_element_by_xpath('//button[@aria-label="Search"]')
search_button.click()

time.sleep(10)

# Get the first listing's name and price
listing_name = driver.find_element_by_xpath('(//div[@class="_gig1e7"])[1]//div[@class="_twmmpk"]/div')
listing_price = driver.find_element_by_xpath('(//div[@class="_gig1e7"])[1]//div[@class="_doc79r"]/span[@aria-hidden="true"]')

# Send a text message with the details
message = f"New York Airbnb Listing - Name: {listing_name.text}, Price: {listing_price.text}"
twilio_number = 'your_twilio_number'
recipient_number = 'recipient_phone_number'

client.messages.create(
    body=message,
    from_=twilio_number,
    to=recipient_number
)

# Quit the driver
driver.quit()