"""
This script creates tables from the given columns and transfers it to the dfToSQL script.
                                                                                                                     """


import pandas as pd


from dfToPgSQL import dfToSQL
from dfToCsv import dfToCsv


class completedDataframe:
    def __init__(self, match_id_list, season_list, quarter_list, country_list, league_list, home_team_list,
                 away_team_list, winner_team_list, loser_team_list, home_goals_list, away_goals_list, result_h_d_a_list,
                 result_in_numbers_list, home_odds_list, draw_odds_list, away_odds_list, winner_odds_list,
                 biggest_odds_list, biggest_is_winner_bool_list, is_url_in_file, where):

        # All Columns Data
        self.all_columns_dict = {
                            # ID list
                            "match_id": match_id_list,

                            # Time lists
                            "season": season_list,
                            "quarter": quarter_list,

                            # Country list
                            "country": country_list,

                            # League & Teams lists
                            "league": league_list,
                            "home_team": home_team_list,
                            "away_team": away_team_list,
                            # If draw both team value: draw
                            "winner_team": winner_team_list,
                            # If draw both team value: draw
                            "loser_team": loser_team_list,

                            # Result lists
                            "home_goals": home_goals_list,
                            "away_goals": away_goals_list,
                            "result_h_d_a": result_h_d_a_list,
                            "result_in_numbers": result_in_numbers_list,

                            # Odds lists
                            "home_odds": home_odds_list,
                            "draw_odds": draw_odds_list,
                            "away_odds": away_odds_list,
                            "winner_odds": winner_odds_list,
                            "biggest_odds": biggest_odds_list,
                            "biggest_is_winner_bool": biggest_is_winner_bool_list,

                             }

        # Tables
        self.clean_df_dict = {
                              # Main Table
                              "matches": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["league"],
                                                                   self.all_columns_dict["season"],
                                                                   self.all_columns_dict["quarter"]
                                                                    )),
                                                      columns=[
                                                               "match_id",
                                                               "league",
                                                               "season",
                                                               "quarter",
                                                               ]
                                                      ),

                              # Country Table
                              "countries": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["country"],
                                                                      )),
                                                        columns=[
                                                                 "match_id",
                                                                 "country",
                                                                 ]
                                                        ),

                              # Teams Table
                              "teams": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["home_team"],
                                                                   self.all_columns_dict["away_team"],
                                                                  )),
                                                    columns=[
                                                             "match_id",
                                                             "home_team",
                                                             "away_team",
                                                             ]
                                                    ),

                              # Winner & Loser Teams Table
                              "w_l_teams": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["winner_team"],
                                                                   self.all_columns_dict["loser_team"],
                                                                      )),
                                                        columns=[
                                                                 "match_id",
                                                                 "winner_team",
                                                                 "loser_team",
                                                                 ]
                                                        ),

                              # Result [Home, Draw, Away] Table
                              "results_in_text": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["result_h_d_a"],
                                                                            )),
                                                              columns=[
                                                                       "match_id",
                                                                       "result_h_d_a",
                                                                       ]
                                                              ),
                              # Result in Numbers Table
                              "results_in_num": pd.DataFrame(data=list(zip(
                                                                   self.all_columns_dict["match_id"],
                                                                   self.all_columns_dict["result_in_numbers"],
                                                                           )),
                                                             columns=[
                                                                      "match_id",
                                                                      "result_in_num",
                                                                      ]
                                                             ),

                              # Goals Table
                              "goals": pd.DataFrame(data=list(zip(
                                                                  self.all_columns_dict["match_id"],
                                                                  self.all_columns_dict["home_goals"],
                                                                  self.all_columns_dict["away_goals"],
                                                                   )),
                                                    columns=[
                                                             "match_id",
                                                             "home_goals",
                                                             "away_goals",
                                                             ]
                                                    ),



                              # Odds Table
                              "odds": pd.DataFrame(data=list(zip(
                                                      self.all_columns_dict["match_id"],
                                                      self.all_columns_dict["home_odds"],
                                                      self.all_columns_dict["draw_odds"],
                                                      self.all_columns_dict["away_odds"],
                                                      self.all_columns_dict["winner_odds"],
                                                      self.all_columns_dict["biggest_odds"],
                                                      self.all_columns_dict["biggest_is_winner_bool"]
                                                                 )),
                                                   columns=[
                                                            "match_id",
                                                            "home_odds",
                                                            "draw_odds",
                                                            "away_odds",
                                                            "winner_odds",
                                                            "biggest_odds",
                                                            "biggest_is_winner_bool",
                                                            ]
                                                   )
                              }

        # To PgSQL
        if not is_url_in_file and where == "pgsql":
            dfToSQL(self.clean_df_dict)

        # To CSV
        if where == "csv":
            dfToCsv(self.all_columns_dict)

        # To ALL
        if where == "both":
            dfToCsv(self.all_columns_dict)
            if not is_url_in_file:
                dfToSQL(self.clean_df_dict)
