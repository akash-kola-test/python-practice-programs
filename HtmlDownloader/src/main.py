from bs4 import BeautifulSoup
import requests

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


url = "https://google.com"
response = requests.get(url)
if response.status_code == 200 and response.headers["content-type"].find("text/html") != -1:
    html_string = response.text
    clean_string = strip_html_tags(html_string)
    print(clean_string)
