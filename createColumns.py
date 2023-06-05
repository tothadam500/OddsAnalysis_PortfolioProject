"""
From the raw dataframe, additional columns are generated through calculations.
The columns are imported to completedDataframe.
                                                                                                                     """

from completedDataframe import completedDataframe as cD


class createColumns:
    def __init__(self, raw_df, is_url_in_file, where):
        self.where = where
        self.is_url_in_file = is_url_in_file

        self.raw_df = raw_df

        cD(
            match_id_list=self.create_match_id_col(),

            season_list=self.create_season_col(),
            quarter_list=self.create_quarter_col(),

            country_list=self.create_country_col(),

            league_list=self.create_league_col(),
            home_team_list=self.create_home_team_col(),
            away_team_list=self.create_away_team_col(),
            winner_team_list=self.create_winner_team_col(),
            loser_team_list=self.create_loser_team_col(),

            home_goals_list=self.create_home_goals_col(),
            away_goals_list=self.create_away_goals_col(),
            result_h_d_a_list=self.create_result_h_d_a_col(),
            result_in_numbers_list=self.create_result_in_num_col(),

            home_odds_list=self.create_home_odds_col(),
            draw_odds_list=self.create_draw_odds_col(),
            away_odds_list=self.create_away_odds_col(),
            winner_odds_list=self.create_winner_odds_col(),
            biggest_odds_list=self.create_biggest_odds_col(),
            biggest_is_winner_bool_list=self.create_biggest_is_winner_bool_col(),

            is_url_in_file=self.is_url_in_file,
            where=self.where,
           )

# ID list
    # match_id: eng_21-22_45
    def create_match_id_col(self):
        match_id_list = []
        for index in self.raw_df.index:
            first_year = str(self.raw_df.loc[index, "season"].split("-")[0][2:4])
            second_year = str(self.raw_df.loc[index, "season"].split("-")[1][2:4])

            item = self.raw_df.loc[index, "iso"] + "_" + first_year + "-" + second_year + "_" + str(index)
            match_id_list.append(item)

        return match_id_list

# Time lists
    # season: 2021-2022
    def create_season_col(self):
        return self.raw_df["season"].to_list()

    # quarter: q1
    def create_quarter_col(self):

        total_matches = len(self.raw_df.index)
        first_quarter = total_matches / 4
        second_quarter = total_matches / 4 * 2
        third_quarter = total_matches / 4 * 3

        quarter_list = []
        for index in self.raw_df.index:
            index = int(index)
            if index <= first_quarter:
                quarter_list.append("q1")
            elif first_quarter < index <= second_quarter:
                quarter_list.append("q2")
            elif second_quarter < index <= third_quarter:
                quarter_list.append("q3")
            else:
                quarter_list.append("q4")

        return quarter_list

# Country list
    # country: England
    def create_country_col(self):
        country_list = [country.title() for country in self.raw_df["country"].to_list()]
        return country_list

# League & Teams lists
    # league: premier_league
    def create_league_col(self):
        return self.raw_df["league"].to_list()

    # home_team: man_united
    def create_home_team_col(self):
        home_team_list = [team.lower().replace(" ", "_").replace(".", "") for team in
                          self.raw_df["home_team"].to_list()]

        return home_team_list

    # away_team: leicester
    def create_away_team_col(self):
        home_away_list = [team.lower().replace(" ", "_").replace(".", "") for team in
                          self.raw_df["away_team"].to_list()]
        return home_away_list

    # winner_team: man_united
    def create_winner_team_col(self):
        home_goals_list = self.create_home_goals_col()
        away_goals_list = self.create_away_goals_col()

        n = 0
        winner_team_list = []
        for home_goals in home_goals_list:

            home_goals = int(home_goals)
            away_goals = int(away_goals_list[n])

            if home_goals > away_goals:
                winner_team_list.append(self.raw_df.loc[n, "home_team"])
            elif home_goals == away_goals:
                winner_team_list.append("draw")
            elif home_goals < away_goals:
                winner_team_list.append(self.raw_df.loc[n, "away_team"])

            n += 1
        winner_team_list = [team.lower().replace(".", "").replace(" ", "_") for team in winner_team_list]
        return winner_team_list

    # loser_team: leicester
    def create_loser_team_col(self):
        home_goals_list = self.create_home_goals_col()
        away_goals_list = self.create_away_goals_col()

        i = 0
        loser_team_list = []
        for home_goals in home_goals_list:

            home_goals = int(home_goals)
            away_goals = int(away_goals_list[i])

            if home_goals < away_goals:
                loser_team_list.append(self.raw_df.loc[i, "home_team"])
            elif home_goals == away_goals:
                loser_team_list.append("draw")
            elif home_goals > away_goals:
                loser_team_list.append(self.raw_df.loc[i, "away_team"])

            i += 1
        loser_team_list = [team.lower().replace(".", "").replace(" ", "_") for team in loser_team_list]
        return loser_team_list

# Result lists
    # home_goals: 2
    def create_home_goals_col(self):
        home_goals_list = [result.replace(" ", "").split("-")[0] for result in self.raw_df["result"].to_list()]
        return home_goals_list

    # away_goals: 1
    def create_away_goals_col(self):
        away_goals_list = [result.replace(" ", "").split("-")[1] for result in self.raw_df["result"].to_list()]
        return away_goals_list

    # result_h_d_a: home
    def create_result_h_d_a_col(self):

        n = 0
        result_h_d_a_list = []
        for home_goals in self.create_home_goals_col():
            away_goals = self.create_away_goals_col()[n]

            if home_goals > away_goals:
                result_h_d_a_list.append("home")

            elif home_goals == away_goals:
                result_h_d_a_list.append("draw")

            elif home_goals < away_goals:
                result_h_d_a_list.append("away")

            n += 1

        return result_h_d_a_list

    # result_in_num: 2-1
    def create_result_in_num_col(self):
        result_in_num_list = [result.replace(" ", "") for result in self.raw_df["result"].to_list()]
        return result_in_num_list

# Odds lists
    # home_odds: 1.6
    def create_home_odds_col(self):
        home_odds_list = [round(float(odd), 1) for odd in self.raw_df["home_odd"].to_list()]
        return home_odds_list

    # draw_odds: 4.3
    def create_draw_odds_col(self):
        draw_odds_list = [round(float(odd), 1) for odd in self.raw_df["draw_odd"].to_list()]
        return draw_odds_list

    # away_odds: 8.3
    def create_away_odds_col(self):
        away_odds_list = [round(float(odd), 1) for odd in self.raw_df["away_odd"].to_list()]
        return away_odds_list

    # winner_odds: 1.6
    def create_winner_odds_col(self):

        result_list = self.create_result_h_d_a_col()
        home_odds_list = self.create_home_odds_col()
        draw_odds_list = self.create_draw_odds_col()
        away_odds_list = self.create_away_odds_col()

        n = 0
        winner_odds_list = []
        for result in result_list:
            if result == "home":
                winner_odds_list.append(home_odds_list[n])
            elif result == "draw":
                winner_odds_list.append(draw_odds_list[n])
            elif result == "away":
                winner_odds_list.append(away_odds_list[n])
            n += 1

        return winner_odds_list

    # biggest_odds: 8.3
    def create_biggest_odds_col(self):

        home_odds_list = self.create_home_odds_col()
        draw_odds_list = self.create_draw_odds_col()
        away_odds_list = self.create_away_odds_col()

        biggest_odds_list = []
        for n in range(len(home_odds_list)):
            biggest_odd = max([home_odds_list[n], draw_odds_list[n], away_odds_list[n]])
            biggest_odds_list.append(biggest_odd)

        return biggest_odds_list

    # biggest_odd_is_winner: False
    def create_biggest_is_winner_bool_col(self):

        biggest_odds_list = self.create_biggest_odds_col()
        winner_odds_list = self.create_winner_odds_col()

        biggest_is_winner_bool_list = [big_odd == winner_odd for big_odd, winner_odd in
                                       zip(biggest_odds_list, winner_odds_list)]

        return biggest_is_winner_bool_list
