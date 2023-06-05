"""
This scripts connects to the PgSQL database and imports data to it.
If it's necessary it sets the data types.
                                                                                                                     """


from sqlalchemy import create_engine
import psycopg2 as pg2


from data import user_input_dict


# User inputs
sql_database = user_input_dict["pgsql_database_name"]
user = user_input_dict["pgsql_username"]
password = user_input_dict["pgsql_password"]


class dfToSQL:
    def __init__(self, clean_df_dict):
        self.df_dict = clean_df_dict

        # Connect to PgSQL
        self.conn = pg2.connect(database=sql_database, user=user, password=password)
        self.cur = self.conn.cursor()
        self.engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/{sql_database}')

        # Creates PgSQL tables
        for table in self.df_dict:
            self.table_to_sql(table)

        # If it's first time creating it set data types
        if self.execute_set_pg_sql_columns_data_types():
            self.set_pg_sql_columns_data_types()
            print("Data types set")

    # Imports the table into the database
    def table_to_sql(self, table):
        data = self.df_dict[table]
        try:
            data.to_sql(name=table, con=self.engine, if_exists="append", index=False)
        except ValueError:
            print("Already Exists")

    # Checks if the set_pg_sql_columns_data_types should execute
    # noinspection PyMethodMayBeStatic
    def execute_set_pg_sql_columns_data_types(self):
        with open('./urls.txt') as f:
            for line in f:
                pass
            last_line = line
        if last_line == "URLs: ":
            return True
        else:
            return False

    # Set data types to the PgSQL database columns
    # noinspection PyMethodMayBeStatic
    def set_pg_sql_columns_data_types(self):
        # matches
        self.cur.execute('ALTER TABLE matches '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN league SET DATA TYPE varchar(20),'
                         'ALTER COLUMN season SET DATA TYPE varchar(9),'
                         'ALTER COLUMN quarter SET DATA TYPE varchar(2),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # countries
        self.cur.execute('ALTER TABLE countries '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN country SET DATA TYPE varchar(20),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # teams
        self.cur.execute('ALTER TABLE teams '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN home_team SET DATA TYPE varchar(30),'
                         'ALTER COLUMN away_team SET DATA TYPE varchar(30),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # w_l_teams
        self.cur.execute('ALTER TABLE w_l_teams '
                         'ALTER COLUMN match_id TYPE varchar(13),'
                         'ALTER COLUMN winner_team SET DATA TYPE varchar(30),'
                         'ALTER COLUMN loser_team SET DATA TYPE varchar(30),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # results_in_text
        self.cur.execute('ALTER TABLE results_in_text '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN result_h_d_a SET DATA TYPE varchar(4),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # results_in_num
        self.cur.execute('ALTER TABLE results_in_num '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN result_in_num SET DATA TYPE varchar(4),'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # goals
        self.cur.execute('ALTER TABLE goals '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN home_goals SET DATA TYPE smallint USING home_goals::smallint,'
                         'ALTER COLUMN away_goals SET DATA TYPE smallint USING away_goals::smallint,'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()

        # odds
        self.cur.execute('ALTER TABLE odds '
                         'ALTER COLUMN match_id SET DATA TYPE varchar(13),'
                         'ALTER COLUMN home_odds SET DATA TYPE float4 USING home_odds::float4,'
                         'ALTER COLUMN draw_odds SET DATA TYPE float4 USING draw_odds::float4,'
                         'ALTER COLUMN away_odds SET DATA TYPE float4 USING away_odds::float4,'
                         'ALTER COLUMN winner_odds SET DATA TYPE float4 USING winner_odds::float4,'
                         'ALTER COLUMN biggest_odds SET DATA TYPE float4 USING biggest_odds::float4,'
                         'ALTER COLUMN biggest_is_winner_bool SET DATA TYPE bool,'
                         'ADD PRIMARY KEY (match_id);')
        self.conn.commit()
