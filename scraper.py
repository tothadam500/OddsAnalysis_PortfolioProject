"""
The script uses a list of URLs to open webpages and scrape data from them.

Once the data has been collected, the script creates a dataframe with the following columns:
    "home_team", "result", "away_team", "home_odd", "draw_odd", "away_odd" + "iso", "league", "season", "country"

After the dataframe is created with the collected data, the script sends it to the createColumns.py script.
                                                                                                                     """


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd


from createColumns import createColumns as cC
from data import path_dict, user_input_dict


# The location of the txt file
url_path = path_dict["url_txt_path"]
# The location of the chrome driver
driver_path = user_input_dict["chrome_driver_path"]


raw_df = pd.DataFrame(columns=["home_team", "result", "away_team", "home_odd", "draw_odd", "away_odd",
                               "iso", "league", "season", "country"])


# noinspection SpellCheckingInspection
class scraper:
    def __init__(self, url_list, where):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1200)
        pd.set_option('display.max_rows', None)

        self.url_list = url_list
        self.where = where

        # Driver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        ser = Service()
        self.driver = webdriver.Chrome(service=ser, options=chrome_options)

        self.create_raw_df()
        self.driver.close()
        self.driver.quit()
        print("Finished")

    # Creats a dataframe
    # noinspection PyBroadException
    def create_raw_df(self):
        for url in self.url_list:
            # Checks the link is present in the txt file
            def is_url_in_file(url_link):
                with open(url_path, 'r') as f:
                    for line in f:
                        if url_link in line:
                            return True
                return False
            self.driver.get(url=url)

            sleep(2)

            # If there's an advertisement close it
            try:
                self.driver.find_element('xpath', '//*[@id="cboxClose"]').click()
            except:
                pass

            # Sets the webpage to full length
            self.driver.find_element('xpath', '//*[@id="events-tab-future"]').click()

            self.start_scraper(url=url)

            # Set data types
            dtypes = {
                'season': 'category',
                'country': 'category',
                'league': 'category',
                'home_team': 'category',
                'away_team': 'category',
                'result': 'category',
                'home_odd': 'float32',
                'draw_odd': 'float32',
                'away_odd': 'float32',
                'iso': 'category'
            }
            raw_df.astype(dtypes)

            # Sets index
            raw_df.reset_index(inplace=True)
            raw_df.drop('index', axis=1, inplace=True)

            print(raw_df)

            # Sent the dataframe to the createColumns.py script
            cC(raw_df=raw_df, is_url_in_file=is_url_in_file(url), where=self.where)

            # After the Dataframe went through each of the scripts, the URL is added to the txt file
            if not is_url_in_file(url_link=url) and self.where != "csv":
                with open(url_path, 'a') as file:
                    file.write(f"{url}\n")

            # Clean the raw_df dataframe
            raw_df.drop(raw_df.index, inplace=True)

    # Datas from the URL link
    # noinspection PyBroadException
    def start_scraper(self, url):

        url_end = url.split("/")[-1]

        iso = url_end[0:3]
        league = url_end.split("-")[-1]
        if league == "primera_division":
            league = "laliga"

        season = str(url_end.split("-")[-3]) + "-" + str(url_end.split("-")[-2])
        country = url_end.split("-")[1].split("_")[0]

        # Get data
        valid_rows = 0
        invalid_rows = 0
        for i in range(1, 421):
            try:
                home_team = self.driver.find_element('xpath',
                                                     f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]'
                                                     f'/table/tbody/tr[{i}]/td[4]/a/span').text

                result = self.driver.find_element('xpath',
                                                  f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]'
                                                  f'/table/tbody/tr[{i}]/td[5]/a').text

                away_team = self.driver.find_element('xpath',
                                                     f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]'
                                                     f'/table/tbody/tr[{i}]/td[6]/a').text

                home_odds = self.driver.find_element('xpath',
                                                     f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]'
                                                     f'/table/tbody/tr[{i}]/td[8]').text

                draw_odds = self.driver.find_element('xpath',
                                                     f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]/'
                                                     f'table/tbody/tr[{i}]/td[9]').text

                away_odds = self.driver.find_element('xpath',
                                                     f'/html/body/div[3]/div[2]/div/div[4]/div[2]/div[1]/div[3]/'
                                                     f'table/tbody/tr[{i}]/td[10]').text

                odds = [home_odds, draw_odds, away_odds]
                vaild_data_all_above_3 = [odd for odd in odds if float(odd) >= 3 or float(odd) == 0 or float(odd) == 1]

                # Checks if the data valid
                valid = True
                if \
                   len(vaild_data_all_above_3) == 3 or\
                   home_team == "" or\
                   away_team == "" or\
                   result == "-" or\
                   float(home_odds) > 20 or\
                   float(draw_odds) > 20 or\
                   float(away_odds) > 20:
                    valid = False

            except:
                pass

            # Sends the data to the raw_df dataframe
            else:
                if valid:
                    raw_df.loc[i-2] = [home_team, result, away_team, home_odds, draw_odds, away_odds,
                                       iso, league, season, country]
                    valid_rows += 1
                    print(f"Current rows in data: {len(raw_df.index)}")
                else:
                    invalid_rows += 1
                    print("Row is invalid!")

        print(f"\nValid rows:{valid_rows}")
        print(f"Invalid rows: {invalid_rows}\n")
