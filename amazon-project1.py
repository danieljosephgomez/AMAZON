# python programming 
# scrape detail information for one book
# soup --> find ul id = s-results-list-atf
# 			findall li class = s-result-item celweight
# 				findall a and get second a tag
# 						a['href']
# 						a.text

from bs4 import BeautifulSoup
from selenium import webdriver

class Book(object):
	"""docstring for Book"""
	def __init__(self):
		self.title = ""
		self.link = ""

def get_book_list():

	driver = webdriver.PhantomJS(executive_path = r'phantomJS')

	url = 'https://amazon.com/s/ref=nb_sb_'

	driver.get(url)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	ul = soup.find('ul', {'id':'s-results-list-atf'})

	book_list = []

	for li in ul.find_all('li', class_ = 's-result-item celweight'):

		all_a = li.find_all('a')
		# print all_a[1].text
		# print all_a[1]['href']

		new_book = Book()
		new_book.title = all_a[1].text
		new_book.link = all_a[1].['href']
		book_list.append(new_book)

	driver.quit()

	return book_list


bl = get_book_list()

for book in bl:
	print book.title
	print book.link