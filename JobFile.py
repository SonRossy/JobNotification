import requests
from bs4 import BeautifulSoup

class Job:
    def __init__(self):
        self.url = "https://stackoverflow.com/jobs/feed?l=Bridgewater%2c+MA%2c+United+States&u=Miles&d=50"
        try:
            self.responseFromURL = requests.get(self.url)
            self.responseFromURL.raise_for_status()
        except (requests.exceptions.ConnectionError, TimeoutError, requests.exceptions.Timeout,
                    requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
            self.Connection = False
            print("bad url")
        except IOError:
            self.Connection=False
        else:
            self.html_JobPage = BeautifulSoup(self.responseFromURL.content, 'html.parser')  # getting the page
            self.allJobs = self.html_JobPage.find_all('item')  # extracting the jobs with th item tag
            self.Connection = True
