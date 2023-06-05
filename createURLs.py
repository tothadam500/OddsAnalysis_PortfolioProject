"""
This script takes the user input from the GUI for the start and end of the season, as well as the name of a country.

It uses this information to generate a URL, with the iso code and league of the given country
from the country_dict dictionary located at data.py.

                                                                                                                     """


from data import country_dict


# Data Made by the Class
dict_of_start_end_league = {
                                 "season_start": [],
                                 "season_end": [],
                                 "league": [],
}

# URLs Made by the Class
urls_list = []


# noinspection PyAttributeOutsideInit
class createURLs:
    def __init__(self, start, end, country):
        self.countries_list = country_dict["countries_list"]

        self.country = country
        self.start = int(start)
        self.end = int(end)

        # All Countries
        if self.country == country_dict["all_countries"].lower():
            for country in self.countries_list:
                self.country = country
                self.get_end_start_league_iso()

        # Single
        else:
            self.get_end_start_league_iso()

        print(urls_list)
        print(f"Number of URLs: {len(urls_list)}")

    # Creates every necessary data for the URL
    def get_end_start_league_iso(self):
        # Seperate the gives season
        dict_of_start_end_league["season_start"].append(self.start)
        dict_of_start_end_league["season_end"].append(self.end)

        # Gets Data from the data.py file
        self.league = self.countries_list[self.country]["league"]
        self.iso = self.countries_list[self.country]["iso"]
        dict_of_start_end_league["league"].append(self.league)

        for _ in dict_of_start_end_league["league"]:
            self.get_urls()

    # Creates the URLs
    def get_urls(self):
        # Creates 1 Year Long Seasons
        season_list = []
        for i in range(1, self.end-self.start+1):
            year = self.start+i
            season = str(year - 1) + '-' + str(year)
            season_list.append(season)

        # All Put Together
        for season in season_list:
            if int(season.split("-")[0]) > 2018 and self.iso == "esp":
                self.league = "laliga"

            url = f"https://www.hatharom.com/livescore/{self.iso}-{self.country}_1-{season}-{self.league}"

            if url not in urls_list and url != "https://www.hatharom.com/livescore/esp-spain_1-2018-2019-laliga":
                urls_list.append(url)
