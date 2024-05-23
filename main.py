import praw
import datetime
import holidays
import wikipedia
import pycountry
import logging.handlers
import os
import logging

# Setup Reddit client
reddit = praw.Reddit(
    client_id="nY4WstIZvogjrDxmIWyKPw",
    client_secret="jKZGZhgITUi8rd_xgMtlkscMx62JoA",
    user_agent="test-script",
)

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "Status.log",
    maxBytes=1024*1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# Return date in 'YYYY-MM-DD' format.
def get_formatted_date(date):
    return date.strftime('%Y-%m-%d')

# Post holiday details to Reddit based on the holiday's name.
def post_holiday_to_reddit(country, name):
    try:
        summary = wikipedia.summary(name)
        subreddit = reddit.subreddit('randomscreenshot')
        title = f"Happy {name}! (Country: {country})"
        submission = subreddit.submit(title, selftext=summary)
        print(f"Post made with title: {title}")
    except wikipedia.exceptions.PageError:
        print("No Wikipedia page found for this holiday.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def list_countries():
    countriesList = []
    for country in pycountry.countries:
        countriesList.append([f"{country.name}",f"{country.alpha_2}"])
    return countriesList

# Find today's holidays in the US and post them on Reddit.
def find_and_post_holidays():
    current_date = datetime.date.today()
    countryList = list_countries()
    for country in countryList:
        try:
            all_holidays = holidays.CountryHoliday(country[1], years=current_date.year)
            for date, name in all_holidays.items():
                if date == get_formatted_date(current_date):
                    post_holiday_to_reddit(country[0], name)
        except:
            pass

try: 
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
     
if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    find_and_post_holidays()