from mechanize import Browser
from bs4 import BeautifulSoup
url="www.google.com"
br=Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="id")
res = br.submit()