POSITIVE_AFFIRMATION_QUOTES = ["I didn't come here to be AVERAGE.", "GIRL! YOU GONNA MAKE IT.",
"WHEN LIFE GIVES YOU LEMONS MAKE LEMONADES.", "PLAY HARD WORK SMARTER.", "KEEP GRINDING LEETCODE."]

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number
import random, schedule, time



def send_message(quote_list=POSITIVE_AFFIRMATION_QUOTES):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to.cellphone,
                           from_=twilio_number,
                            body=quote)

        
schedule.every().day.at("06:00").do(send_message, POSITIVE_AFFIRMATION_QUOTES[0])

#testing
schedule.every().day.at("17:00").do(send_message, POSITIVE_AFFIRMATION_QUOTES[0])

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)