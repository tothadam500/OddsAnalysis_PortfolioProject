"""
This script checks whether the data from the given URL is already present in the PostgreSQL database.

It does this by comparing the URL to the path_dict["url_txt_path"] file.

If the URL is found in the file, it indicates that the data is already present in the database.
                                                                                                                     """


import os


from data import path_dict


# The location of the txt file
url_path = path_dict["url_txt_path"]


urls_to_send_to_db = []
already_existing_url = []


class urlCheck:
    def __init__(self, url):
        self.url = url

        self.create_txt_file()

        is_file_in_txt = self.is_url_in_file()

        if is_file_in_txt:
            already_existing_url.append(self.url)

        else:
            urls_to_send_to_db.append(url)

    # Creates txt file if it doesn't exist
    @staticmethod
    def create_txt_file():
        if not os.path.isfile(url_path):
            with open(url_path, 'w') as file:
                file.write('URLs: ')
                print(f"Made new file at {url_path}")

    # Checks if the given URL is present in the txt file
    def is_url_in_file(self):
        with open(url_path, 'r') as file:
            for line in file:
                if self.url in line:
                    return True
        return False
