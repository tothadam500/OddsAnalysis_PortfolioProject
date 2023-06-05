
# Please enter your data:
pgsql_database_name = "odds_analysis"
pgsql_username = "postgres"
pgsql_password = ""
chrome_driver_path = r""


# Data about country: [league, iso]
country_dict = {
                "countries_list": {
                                    "hungary": {
                                            "league": "nb_i",
                                            "iso": "hun"
                                    },

                                    "england": {
                                            "league": "premier_league",
                                            "iso": "eng"
                                    },

                                    "spain": {
                                            "league": "primera_division",
                                            "iso": "esp"
                                    },

                                    "italy": {
                                            "league": "serie_a",
                                            "iso": "ita"
                                    },
                                    "france": {
                                            "league": "ligue_1",
                                            "iso": "fra"
                                    },

                                    "germany": {
                                            "league": "1._bundesliga",
                                            "iso": "ger"
                                    },

                                    "austria": {
                                            "league": "bundesliga",
                                            "iso": "aut"
                                    },

                                    "russia": {
                                            "league": "premier_league",
                                            "iso": "rus"
                                    },

                                    "netherlands": {
                                            "league": "eredivisie",
                                            "iso": "ned"
                                    },
                                    "portugal": {
                                            "league": "primeira_liga",
                                            "iso": "por"
                                    },

                                    "scotland": {
                                            "league": "premiership",
                                            "iso": "sco"
                                    },

                                    "belgium": {
                                            "league": "first_division_a",
                                            "iso": "bel"
                                    },

                                    "greece": {
                                            "league": "super_league",
                                            "iso": "gre"
                                    },

                                    "switzerland": {
                                            "league": "super_league",
                                            "iso": "sui"
                                    },

                                    "romania": {
                                            "league": "liga_i",
                                            "iso": "rou"
                                    },

                                    "turkey": {
                                            "league": "super_lig",
                                            "iso": "tur"
                                    },
                                                                             },

                "all_countries": "* ALL *"
                }


# Path dictionary
path_dict = {
    "url_txt_path": 'urls.txt',
    "csv_folder": "leagues",
}

# User input dictionary
user_input_dict = {
    "chrome_driver_path": chrome_driver_path,
    "pgsql_database_name": pgsql_database_name,
    "pgsql_username": pgsql_username,
    "pgsql_password": pgsql_password
                    }
