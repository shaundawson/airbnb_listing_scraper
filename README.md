#Airbnb Scraper with Twilio Text Notifications
This is a Python script that scrapes Airbnb listings for a specific location and date range using the Selenium library. It extracts the name and price of the first listing and sends a text message with the extracted information using the Twilio library. The script is designed to be run periodically to keep the user updated on the latest Airbnb listings for their desired location and date range.

##Dependencies
The script requires the following Python libraries to be installed:

##Selenium
Twilio
You will also need to have a Chrome driver installed on your system to use Selenium.

##Installation
To install the required Python libraries, run the following command:
`pip install selenium twilio`
You can download the Chrome driver from the official website.

##Configuration
Before running the script, you will need to configure the following parameters:

- url: The Airbnb URL to scrape.
- location_input: The input element to enter the location.
- checkin_input: The input element to enter the check-in date.
- checkout_input: The input element to enter the check-out date.
- search_button: The search button element to click.
- twilio_account_sid: Your Twilio account SID.
- twilio_auth_token: Your Twilio authentication token.
- twilio_number: Your Twilio phone number.
- recipient_number: The phone number to receive the text message.
You can modify these parameters in the script itself.

##Usage
To run the script, open a terminal or command prompt and navigate to the directory containing the script. Then run the following command:
`main.py`
The script will launch a Chrome window, navigate to the Airbnb URL, enter the search criteria, and retrieve the first listing's name and price. It will then send a text message containing this information to the specified recipient number using Twilio.


##License
This project is licensed under the MIT License - see the LICENSE file for details.
