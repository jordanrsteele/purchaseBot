from selenium 						   import webdriver
from selenium.webdriver.support.ui 	   import WebDriverWait
from selenium.webdriver.support.select import Select
from random_words import RandomWords
import unittest
import time
import credentials



class LoginTest(unittest.TestCase):

	def setUp(self):
			self.driver = webdriver.Chrome()
			self.driver.get("https://www.amazon.ca/")

	def test_Login(self):

		#generate random word
		rw = RandomWords()
		word = rw.random_word()
		word2 = rw.random_word()


		word = word + " " + word2

		print word 

		driver = self.driver
		amazonUsername = credentials.login['amazonUsername']
		amazonPassword = credentials.login['password']
		goToSignInButtonXpath      = "(//a[contains(@href, 'signin?')])"

		#second page
		emailFieldID     = "ap_email"
		passFieldID      = "ap_password"
		loginButtonXpath = "//input[@id = 'signInSubmit']"

		###third page
		searchFieldXpath 	   = "//input[@id = 'twotabsearchtextbox']"
		searchButtonXpath = "//input[@value = 'Go']"

		#first page (main page)
		goToSignInButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(goToSignInButtonXpath))
		goToSignInButtonElement.click()

		#second page (sign in)
		emailFieldElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))
		passFieldElement    = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldID))
		logInButtonElement  = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

		emailFieldElement.clear()
		emailFieldElement.send_keys(amazonUsername)
		passFieldElement.clear()
		passFieldElement.send_keys(amazonPassword)
		logInButtonElement.click()
		
		#third page (search)
		searchFieldElement 		= WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(searchFieldXpath))
		searchButtonFielElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(searchButtonXpath))

		searchFieldElement.clear()
		searchFieldElement.send_keys(word)
		searchButtonFielElement.click()



		html_list = self.driver.find_element_by_id("s-results-list-atf")
		items = html_list.find_elements_by_class_name("s-result-item")

		for item in items:
			text = item.text
    		print text

		
		elems = self.driver.find_elements_by_class_name('a-link-normal')
		for elem in elems:
			print elem.get_attribute("href")

		

    	time.sleep(15)


def tearDown(self):
	self.driver.quit()



if __name__ == "__main__":
	unittest.main()


