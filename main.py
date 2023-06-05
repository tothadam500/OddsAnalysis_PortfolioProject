"""
To save data to a PostgreSQL database, you need to first create the database and obtain the login credentials
such as the database name, PostgreSQL username, and password.

Once you have the login credentials, you need to download the Chrome driver from the official website.
This driver will be used to automate web browsing and scraping.


In your program, you should include the following parameters:

    Database name: This is the name of the database that you created to store your data.
    PostgreSQL username: This is the username that you will use to access your PostgreSQL database.
    PostgreSQL password: This is the password that you will use to authenticate yourself when accessing the database.
    Chrome driver's location: This is the path where you have downloaded and saved the Chrome driver on your computer.

By including these parameters in this program in the data.py script, you will be able to establish a connection
to your PostgreSQL database and automate web browsing using the Chrome driver.
                                                                                                                     """

from GUI import GUI
GUI()
