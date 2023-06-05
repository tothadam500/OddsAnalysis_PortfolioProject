"""
Creates the CSV file at the file_name folder, if necessary it creates the file.
                                                                                                                     """


from pathlib import Path
import pandas as pd


from data import path_dict


folder_name = path_dict["csv_folder"]


class dfToCsv:
    def __init__(self, data):
        league = data["league"][0]
        year = data["season"][0]
        country = data["country"][0].lower()
        df = pd.DataFrame(data)
        df = self.set_data_types(df)

        leagues_folder = rf'{folder_name}\{country + "-" + league}'
        Path(leagues_folder).mkdir(parents=True, exist_ok=True)
        df.to_csv(rf'{leagues_folder}\{league}_{year}.csv')

    # Set data types
    # noinspection PyMethodMayBeStatic
    def set_data_types(self, df):
        dtypes = {'match_id': 'object',
                  'quarter': 'category',
                  'country': 'category',
                  'league': 'category',
                  'home_team': 'category',
                  'away_team': 'category',
                  'winner_team': 'category',
                  'loser_team': 'category',
                  'home_goals': 'int8',
                  'away_goals': 'int8',
                  'result_h_d_a': 'category',
                  'result_in_numbers': 'category',
                  'home_odds': 'float32',
                  'draw_odds': 'float32',
                  'away_odds': 'float32',
                  'winner_odds': 'float32',
                  'biggest_odds': 'float32',
                  'biggest_is_winner_bool': 'bool'}

        return df.astype(dtypes)
