from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC







class SortingTesting(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_from_cheapest(self):
		driver = self.driver
		driver.get("https://rockdrive.com.ua/")
		menu = driver.find_element(By.ID, "menewb")
		menu.click()
		driver.find_element(By.ID, "opop368").click()
		electric_g = driver.find_element(By.LINK_TEXT, "Электрогитары")
		electric_g.click()
		element = WebDriverWait(driver, 10).until(
			EC.invisibility_of_element_located((By.XPATH, "//div[@id='after']")))
		sort_bt = driver.find_element(By.XPATH, "//div[@id='sort']//button[@class='btn btn-sm']")
		sort_bt.click()
		try:
			driver.find_element(By.LINK_TEXT, " от дешевых").click()
		except NoSuchElementException:
			sort_bt.click()
		items = driver.find_elements(By.CLASS_NAME, "price")
		first = items[0].text
		for item in items[1:]:
			self.assertGreaterEqual(item.text, first)
		pg = driver.find_elements(By.XPATH, "//div[@id='pag1']//div[@class='pagination']//div//a")
		last_pg = pg[-1].click()
		time.sleep(5)
		items = driver.find_elements(By.CLASS_NAME, "price")
		last = items[-1].text
		for item in items[:-1]:
			self.assertLessEqual(item.text, last)

	def test_alphabet(self):
		driver = self.driver
		driver.get("https://rockdrive.com.ua/")
		menu = driver.find_element(By.ID, "menewb")
		menu.click()
		driver.find_element(By.ID, "opop368").click()
		electric_g = driver.find_element(By.LINK_TEXT, "Электрогитары")
		electric_g.click()
		element = WebDriverWait(driver, 10).until(
			EC.invisibility_of_element_located((By.XPATH, "//div[@id='after']")))
		sort_bt = driver.find_element(By.XPATH, "//div[@id='sort']//button[@class='btn btn-sm']")
		sort_bt.click()
		driver.find_element(By.XPATH, '//*[@id="sort"]/div/a[3]').click()
		time.sleep(5)
		items = driver.find_elements(By.XPATH, '//*[@id="prodsall"]//h2/a/span/b')
		list_current = []
		for i in items:
			list_current.append(i.text)
		list_sorted = sorted(list_current)
		self.assertEqual(list_current, list_sorted)
	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()

