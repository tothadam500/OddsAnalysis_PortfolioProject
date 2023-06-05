# Odds Analysis
_This is Tóth Ádám's portfolio project!_
<br>
<br>
<br>
## About the program
<img align="right" src="https://user-images.githubusercontent.com/129130362/236000881-242e9676-331a-4e50-9f4e-b78b9747a805.JPG">
<br>

<br>&ensp;&ensp;I have created a Python program that displays a **Graphical User Interface** upon execution. The **GUI** includes two primary buttons, **'Add League**' and **'Open Dashboard'**.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
 <img align="left" src="https://user-images.githubusercontent.com/129130362/236001605-7b8f246f-d56d-4ace-8799-90be8cb8d4f8.JPG">
 When the user clicks on the **'Add League'** button,
  <br>&ensp; a new page will be displayed where the user can input the start and end dates for a specified football season and league.
  The user will also be able to select whether to save the data to a **CSV file** and/or a **PgSQL database**.
  <br>&ensp;Once the necessary information has been inputted, the user can initiate the scraping process by clicking on the **'Start Scraper'** button.
  <br>&ensp;At this point, the program will begin to scrape the internet for data on football matches played during the specified season and league.
  Once the data has been collected, the program will proceed to clean and manipulate it in order to make it easier to read and analyze. Finally, the program will insert the data into the specified format(s).
<br>
<br>
<br>
<br>
 <img align="right" src="https://user-images.githubusercontent.com/129130362/236006813-5456e562-d79a-47c2-884f-b2dce1287edf.jpg">
 Clicking on the **'Open Dashboard'** button,
  <br>&ensp; will open the _OddsAnalysis.twbx_ file, which contains the visualization created from the data stored in the database.
  <br>&ensp;The user will be able to view the visualization and analyze the data in an interactive and visual manner.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
## Program's operation
 <img align="right" src="https://user-images.githubusercontent.com/129130362/236011393-3603f742-6042-45cb-81ea-fea4f4b410ba.JPG">
 
 &ensp;When the _main.py_ script is executed, it starts the _GUI.py_ script which opens GUI. 
 After the user has selected the appropriate season(s) and submitted them, the program creates the **URLs** for the selected season(s) on the specified webpage.
<br>
<br>
<br>
<br>
 If the user has chosen to save the data to a **PgSQL database**,
   the program checks the _urls.txt_ file to see if the **URL** is already present in the database.
  If the data for that **URL** has already been stored in the database, the program skips that page and moves on to the next one. Once the correct data has been collected from the webpage,
  it is converted into a pandas dataframe and sent to the _createColumns.py_ script for calculations and manipulation.
 <br>&ensp;Once the data has been processed, the resulting dataframe is passed to the _completedDataframe.py_ script, where it is transformed into 8 tables with their corresponding columns.
 <br>&ensp;Finally, the program imports the data into the specified database.
  If it is the first time data is being inserted into the database, the program sets the **data types** for each column.
<br>
<br>
<img align="center" src="https://user-images.githubusercontent.com/129130362/236014562-f7e16cd1-fc12-4076-8d99-d46c340afe77.JPG">
<br>
<br>
<br>
<br>
 If the user has chosen to save the data to a **CSV file**,
 <br>&ensp;The program scrapes through all of the given **URLs** and creates files under the designated (_\league_) folder.
  It first creates a folder for the _country-league_ name and then creates the csv files for the specific league season within that folder.
 <br>
  <br>
 <img align="center" src="https://user-images.githubusercontent.com/129130362/236017382-3e7a3f01-f185-4e3f-b027-bb2aa29e8b30.JPG">
    <br>
    <br>
    
## Tableau
_In Tableau, I have created three dashboards that display different betting strategies._
<br>
<br>
<br>
  <img align="right" src="https://user-images.githubusercontent.com/129130362/236260489-ff984fb9-615c-4c81-999e-5a8f1ea5bfc9.JPG">
The first dashboard is called **"Draw Odds Dashboard"** and is based on a strategy of betting on every match draw.
 <br>&ensp;This dashboard displays the _profits_ for each odd that appears in the draw odds column, filtered 
 _quarter year_ and _country_.
 <br>&ensp;This allows users to analyze the effectiveness of the strategy in different regions and time periods.
 
 <br>&ensp;By examining the profits for each odd, users can gain insight into the success rates of different betting odds and potentially adjust their strategy accordingly.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<img align="left" src="https://user-images.githubusercontent.com/129130362/236026700-68569ab5-372f-477a-9211-4076d8f30c10.JPG">
The second dashboard is named the **"Biggest Odds Dashboard"** and is based on a different betting strategy than the Draw Odds Dashboard. In this strategy, the user only places bets on the match with the highest odds.
<br>&ensp;Like the Draw Odds Dashboard, the Biggest Odds Dashboard has the same filters for _quarter year_ and _country_, allowing users to compare the profitability of the strategy across different regions and time periods.
<br>&ensp;By focusing on the highest odds, users may be able to achieve higher payouts for successful bets, but the lower frequency of such bets may also result in fewer opportunities for profits.
The Biggest Odds Dashboard provides users with the information they need to evaluate the effectiveness of this strategy.
<br>
<br>
<br>
<br>
<br>
<br>
The **"Best Odds Dashboard"**, displays the profitability of a betting strategy based on betting on numbers that appear in any of the odds. This dashboard is also filtered by _quarter year_ and _country_.

Additionally, users have the option to select a _specific number of **top** and **bottom** results_ to display. By filtering the data in this way, users can better understand the most and least profitable numbers to bet on for a given time period and region.

Overall, the Best Odds Dashboard provides users with a powerful tool for evaluating the profitability of this betting strategy and can help them make more informed decisions when placing their bets.
<br>
<br>
<div style="display: flex; flex-wrap: wrap;">
  <img align="right" src="https://user-images.githubusercontent.com/129130362/236034863-97854fc5-2ead-4fc5-9db0-ae1407edc447.JPG" alt="Image 1" style="flex: 50%; height: auto; width: 45%;">
  <img align="left" src="https://user-images.githubusercontent.com/129130362/236037958-3c881c20-3634-4c10-958e-b9ae20098de4.JPG" alt="Image 2" style="flex: 50%; height: auto; width: 45%;">
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Start

To run the program, you will need several software tools, including a **Python text editor**, **PostgreSQL**, **PgAdmin4**, and **Tableau**.
<br>&ensp;To begin using the program, you will need to create a PgSQL database where you can store the data.
<br>&ensp;Additionally, you must download the **Selenium Chrome driver** from the following URL: https://chromedriver.chromium.org/downloads.
<br>
<br>
<img align="right" src="https://user-images.githubusercontent.com/129130362/236040770-2ba8d0ff-3d7c-41bb-a54c-4799f4a2758e.JPG">
Once you have done this, you will need to provide some information to the program in the _'data.py'_ script in order for it to function properly.
<br>
<br>**Specifically, you must enter:**<br>
&ensp;&ensp;- _name of the PgSQL database<br>
&ensp;&ensp;- PgSQL username<br>
&ensp;&ensp;- PgSQL password<br>_
&ensp;&ensp;- _path to the location of the Chrome driver_
