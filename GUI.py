
""" GUI for the program """


import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime as dt
import os


from createURLs import createURLs, urls_list
from checkURL import urlCheck, urls_to_send_to_db, already_existing_url
from data import country_dict, path_dict
from scraper import scraper


FONT = "Terminal"
BG = "lightgrey"
add_finish_button_command = None


# --------------------------------------------------- Scraper GUI ------------------------------------------------------
# noinspection PyMethodMayBeStatic,SpellCheckingInspection,PyAttributeOutsideInit,PyTypeChecker
class GUI:
    def __init__(self):
        self.main_page()

    # ------------------------------------------------ Main Page -------------------------------------------------------
    def main_page(self):

        # Window Config
        main_window = Tk()
        main_window.title("Odds Scraper Interface")
        main_window.config(padx=30, pady=30, background=BG)

        # Welcome Label
        welcome_label = Label(text="Welcome to the scraper\n"
                                   " interface ⛏️",
                              font=(FONT, 24, "bold"),
                              background=BG)
        welcome_label.grid(row=0, column=1, columnspan=2, padx=30)

        # Spacing Label 1
        spacing_between_task_and_button = Label(text="\n\n\n\n", background=BG)
        spacing_between_task_and_button.grid(row=2, column=0, columnspan=2)

        # Add League Button
        add_league_button = Button(text="Add League", font=(FONT, 8), width=16, height=2,
                                   command=lambda: [main_window.destroy(), self.add_league_page()])
        add_league_button.grid(row=3, column=1)

        # Open Dasbhoard Button
        open_dashboard_button = Button(text="Open Dashboard", font=(FONT, 8), width=16, height=2,
                                       command=self.open_dasboard_command)
        open_dashboard_button.grid(row=3, column=2)

        # Spacing Label 2
        spacing_between_button_and_info = Label(text="\n\n\n\n\n\n\n", background=BG)
        spacing_between_button_and_info.grid(row=4, column=2)

        # Info Button
        def main_page_info_button_command():
            # Window Config
            info_window = Tk()
            info_window.title("Odds Scraper Interface Info")
            info_window.config(padx=30, pady=40, background=BG)

            # Info Label
            info_label = Label(text="This program is gathering data on football matches across"
                                    " various leagues and seasons\n"
                                    " through the process of web scraping.\n"
                                    "The primary emphasis is placed on the betting odds.\n"
                                    "I have compiled statistics on betting using various strategies.\n"
                                    " You can access the dashboard by clicking on the 'Open Dashboard' button.\n"

                                    "The 'Add League' button allows you to include"
                                    " the following instructions into the program: \n"
                                    " season start date, season end date, league name,\n"
                                    " and the preferred format for saving the data.\n"
                                    "The program scrapes data from the internet to obtain"
                                    " the following information from the games:\n"
                                    "home team, away team, home odd, draw odd, away odd and result.\n"
                                    "The retrieved data can be formatted and stored"
                                    " in both a SQL database and a CSV file.\n\n"
                                    "The program retrieves data from:\n"
                                    "https://www.hatharom.com/\n\n\n",
                               font=(FONT, 22), background=BG
                               )
            info_label.grid(row=0, column=0, columnspan=2)

            # Back Button
            back_to_the_maininterface_button = Button(text="Back", width=12, height=1, font=(FONT, 4),
                                                      command=lambda: [info_window.destroy(), GUI()])
            back_to_the_maininterface_button.grid(row=1, column=0)

            # Close Button
            close_gui_button = Button(text="Quit", width=12, height=1, font=(FONT, 4),
                                      command=info_window.destroy)
            close_gui_button.grid(row=1, column=1)

            # ml
            info_window.mainloop()

        info_button = Button(text="i", font=(FONT, 12, "italic"),
                             command=lambda: [main_window.destroy(), main_page_info_button_command()])
        info_button.grid(row=5, column=2, sticky=E)

        # Quit Button
        quit_button = Button(main_window, text="Quit", font=(FONT, 12, "italic"), width=10, command=sys.exit)
        quit_button.grid(row=5, column=1, sticky=W)

        # ml
        main_window.mainloop()

    # ------------------------------------------------------------------------------------------------------------------

    # --------------------------------------------- Add League Page ----------------------------------------------------
    def add_league_page(self):

        # Where to Save
        self.to_sql_bool = False
        self.to_csv_bool = False

        # Window Config
        self.add_league_window = Tk()
        self.add_league_window.title("Add League")
        self.add_league_window.config(padx=30, pady=10, background=BG)

        # Texts:
        #  Instruction Label
        add_main_label = Label(text="Please add the following datas", font=(FONT, 14, "bold", "underline"), bg=BG)
        add_main_label.grid(row=0, column=0, columnspan=2, pady=20)

        #  Season Start Label
        add_season_start_label = Label(text="Season start:", font=FONT, bg=BG)
        add_season_start_label.grid(row=1, column=0, sticky=W, pady=10)

        #  Season End Label
        add_season_end_label = Label(text="Season end:", font=FONT, bg=BG)
        add_season_end_label.grid(row=2, column=0, sticky=W, pady=10)

        #  Country Label
        add_country_label = Label(text="Country:", font=FONT, bg=BG)
        add_country_label.grid(row=3, column=0, sticky=W, pady=10)

        #  Split Seasons
        # End of Season
        if dt.datetime.today().month > 6:
            last_year = dt.datetime.today().year
        else:
            last_year = dt.datetime.today().year - 1

        add_season_start_list = list(range(2018, last_year))
        add_season_end_list = list(range(2019, last_year + 1))

        # ------------------------------------------------- Boxes ------------------------------------------------------
        #  Season Start Box
        add_season_start_box = ttk.Combobox(values=add_season_start_list,
                                            width=10,
                                            state="readonly",
                                            font=(FONT, 4),
                                            justify="center")
        add_season_start_box.set(2018)
        add_season_start_box.grid(row=1, column=1, sticky=E)

        #  Season End Box
        add_season_end_box = ttk.Combobox(values=add_season_end_list,
                                          width=10,
                                          state="readonly",
                                          font=(FONT, 4),
                                          justify="center")
        add_season_end_box.set(last_year)
        add_season_end_box.grid(row=2, column=1, sticky=E)

        #  Country Box
        countries_list = country_dict["countries_list"]
        countries_list_titled = [title.title() for title in countries_list]
        countries_list_titled.append(country_dict["all_countries"])
        add_country_entry = ttk.Combobox(values=countries_list_titled,
                                         width=10,
                                         state="readonly",
                                         font=(FONT, 4),
                                         justify="center"
                                         )
        add_country_entry.set("Spain")
        add_country_entry.grid(row=3, column=1, sticky=E)

        # ------------------------------------------------- Submit -----------------------------------------------------
        #  Submit Button Command
        def submit_button_command():

            # Format subbmitted data
            submitted_season_start = add_season_start_box.get()
            submitted_season_end = add_season_end_box.get()
            submitted_country = add_country_entry.get().lower()

            # Checks if the season data is valid
            if submitted_season_start >= submitted_season_end:
                messagebox.showerror("Date Error", "The end date of the season cannot be the same as, or earlier than,"
                                                   " the start date."
                                     )

            # If valid creates URLs from it, through createURLs
            else:
                createURLs(
                    start=submitted_season_start,
                    end=submitted_season_end,
                    country=submitted_country
                )

        #  Submit Button
        add_submit_button = Button(text="Submit Seasons", command=submit_button_command, font=(FONT, 4), width=34)
        add_submit_button.grid(row=4, column=0, columnspan=2, pady=20)

        # --------------------------------------------- Check Buttons --------------------------------------------------
        #  PGSQL:
        #   Check Button
        self.to_sql_var = BooleanVar()
        to_sql_checkbutton = Checkbutton(variable=self.to_sql_var,
                                         justify="center",
                                         bg=BG)
        to_sql_checkbutton.grid(row=5, column=1, sticky=E)
        to_sql_checkbutton.select()

        #   Label
        to_sql_label = Label(font=(FONT, 4), text="Data to PgSQL:", bg=BG)
        to_sql_label.grid(row=5, column=0, pady=10, sticky=W)

        #  CSV:
        #   Check Button
        self.to_csv_var = BooleanVar()
        to_csv_checkbutton = Checkbutton(variable=self.to_csv_var,
                                         justify="center",
                                         bg=BG)
        to_csv_checkbutton.grid(row=6, column=1, sticky=E)

        #   Label
        to_csv_label = Label(font=(FONT, 4), text="Data to CSV:", bg=BG)
        to_csv_label.grid(row=6, column=0, pady=10, sticky=W)

        # Creates Command to Start Scraper Button
        # Checks where to save
        def where_to_save_should_scraper_start():
            self.where_to_save()
            global add_finish_button_command
            if self.to_sql_bool and self.to_csv_bool:
                print("Save to both")
                return self.start_scraper(where="both")
            else:
                if self.to_sql_bool:
                    print("Save to PgSQL")
                    return self.start_scraper(where="pgsql")
                elif self.to_csv_bool:
                    print("Save to CSV")
                    return self.start_scraper(where="csv")
                else:
                    messagebox.showerror("Save Error", "You need to select at least one option"
                                                       " from the 'Data to' section.")
                    return None

        # Start Scraper Button
        add_finish_button = Button(text="Start Scraper", font=(FONT, 4), width=34,
                                   command=where_to_save_should_scraper_start)
        add_finish_button.grid(row=8, column=0, columnspan=2, pady=16)

        # --------------------------------------------- Info and Back --------------------------------------------------
        # Add League Page Info Button Command
        def add_info_button_command():

            # Add League Page Info Window Config
            add_info_window = Tk()
            add_info_window.title("Example")
            add_info_window.config(padx=30, pady=50, background=BG)

            # Add League Page Info Label
            add_info_label = Label(text="Example           \n\n\n"
                                        "Season start: 2019\n"
                                        "Season end:   2022\n"
                                        "Country:    France\n\n"
                                        "If you want all:  \n"
                                        "Country:       ALL\n\n\n"
                                        "* Submit *\n\n\n"
                                        "Data to PgSQL:   ✔\n"
                                        "Data to CSV:     ✔\n\n\n"

                                        f"* Start Scraping *\n",
                                   font=(FONT, 4),
                                   bg=BG,
                                   )
            add_info_label.grid(row=0, column=0, padx=10)

            # Add League Page Back Button
            add_info_back_button = Button(text="Back", font=(FONT, 4),
                                          command=lambda: [add_info_window.destroy(), self.add_league_page()])
            add_info_back_button.grid(row=1, column=0, sticky=W)

            # ml
            add_info_window.mainloop()

        # Add League Page Info Button
        add_info_button = Button(text="i", font=(FONT, 4, "italic"),
                                 command=lambda: [self.add_league_window.destroy(), add_info_button_command()])
        add_info_button.grid(row=9, column=1, sticky=E, pady=16)

        #  Add League Page Back Button
        add_back_button = Button(text="Back", font=(FONT, 4, "italic"),
                                 command=lambda: [self.add_league_window.destroy(), GUI()])
        add_back_button.grid(row=9, column=0, sticky=W, pady=16)

        # ml
        self.add_league_window.mainloop()

    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------- Start Scraper -----------------------------------------------------
    def start_scraper(self, where):
        # Checks if URL already in PgSQL
        for url in urls_list:
            urlCheck(url)

        #  URLs that are not in PgSQL yet
        urls_send_clean = list(dict.fromkeys(urls_to_send_to_db))

        # URLs that are in the PgSQL
        urls_keep_clean = list(dict.fromkeys(already_existing_url))

        # All URLs
        urls_all_clean = urls_send_clean + urls_keep_clean

    # Checks if the user add valid data
        self.where_to_save()
        if len(urls_send_clean) == 0 and self.to_sql_bool and not self.to_csv_bool or len(urls_all_clean) == 0:
            messagebox.showerror("Input Error", "Please add at least one season that has not already been included!")

        else:
            # The end of the URLs
            urls_list_send_end = [url.split('/')[-1] for url in urls_send_clean]
            url_list_keep_end = [url.split('/')[-1] for url in urls_keep_clean]
            urls_list_all_end = [url.split('/')[-1] for url in urls_all_clean]
            sep = "\n"

            # Length of URLs that are already presents in the PgSQL Database
            urls_list_len = len(url_list_keep_end)

            # Yes or No Message Box Text
            def msg_text():
                inserted_to_pgsql_with_csv_text = (f'Would you like to start the scraper using these URLs?\n\n'
                                                   f'(All URLs will be used for the CSV file)\n'
                                                   fr"The CSV file's path: {path_dict['csv_folder']}"
                                                   f'\n\nThe data extracted from the following URLs\n'
                                                   f'will be inserted into the PgSQL database'
                                                   f'\n\n{sep.join(urls_list_send_end)}\n\n')

                inserted_to_pgsql_w_o_csv_text = (f'Would you like to start the scraper using these URLs?\n'
                                                  f'\n\nThe data extracted from the following URLs\n'
                                                  f'will be inserted into the PgSQL database'
                                                  f'\n\n{sep.join(urls_list_send_end)}\n\n')

                these_urls_already_present_text = (f'\nThese URLs are already present in the PgSQL database:'
                                                   f'\n\n{sep.join(url_list_keep_end)}')

                to_csv_text = (f'Would you like to start the scraper using these URLs?\n'
                               fr"The CSV file's path: {path_dict['csv_folder']}"
                               f'\n\n{sep.join(urls_list_all_end)}\n\n')

                # There are at least one URL that is already present in the PgSQL Database:
                if urls_list_len > 0:
                    # to CSV and to SQL
                    if self.to_csv_bool and self.to_sql_bool:
                        return (f'{inserted_to_pgsql_with_csv_text}'
                                f'{these_urls_already_present_text}'
                                )
                    # to CSV
                    elif self.to_csv_bool and not self.to_sql_bool:
                        return to_csv_text
                    # to SQL
                    elif self.to_sql_bool and not self.to_csv_bool:
                        return (f'{inserted_to_pgsql_w_o_csv_text}'
                                f'{these_urls_already_present_text}'
                                )

                # There is no URL that is already present in the PgSQL Database:
                else:
                    # to CSV and to SQL
                    if self.to_csv_bool and self.to_sql_bool:
                        return inserted_to_pgsql_with_csv_text
                    # to CSV
                    elif self.to_csv_bool and not self.to_sql_bool:
                        return to_csv_text
                    # to SQL
                    elif self.to_sql_bool and not self.to_csv_bool:
                        return inserted_to_pgsql_w_o_csv_text

            # Checks if the Data to Check Buttons are valid
            if not self.to_csv_bool and not self.to_sql_bool:
                messagebox.showerror("Save Error",
                                     "Please indicate how you would like to save the data")

            # Yes or No Message Box
            else:
                start_querry_msg_box = messagebox.askyesno("Confirm", msg_text())

                # if Yes
                if start_querry_msg_box:
                    self.add_league_window.destroy()

                    # Send URls to Scraper
                    if where == "pgsql":
                        main_urls = urls_send_clean
                    else:
                        main_urls = urls_send_clean + urls_keep_clean

                    scraper(url_list=main_urls, where=where)

                    # Done Window Config
                    start_scrape_interface = Tk()
                    start_scrape_interface.title("Scraper")
                    start_scrape_interface.config(padx=20, pady=30, background=BG)

                    # Done Label
                    start_scrape_interface_label = Label(text="The scraping process has finished!",
                                                         font=(FONT, 32), bg=BG)
                    start_scrape_interface_label.grid(row=0, column=0, padx=15, pady=36)

                    # Quit Button
                    quit_button = Button(text="Quit", command=sys.exit, font=(FONT, 4), width=18)
                    quit_button.grid(row=1, column=0, pady=20)

    # Checking where to save
    def where_to_save(self):
        self.to_sql_bool = self.to_sql_var.get()
        self.to_csv_bool = self.to_csv_var.get()

    # Open Dashboard command
    def open_dasboard_command(self):
        file_path = r'OddsAnalysis.twbx'
        print("Opening Tableau...")
        os.startfile(file_path)
