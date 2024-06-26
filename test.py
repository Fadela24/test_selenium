from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.laredoute.fr/") 
time.sleep(5)

cookies = driver.find_element(By.XPATH, '//*[@id="popin_tc_privacy_button_2"]').click()
time.sleep(3)

search_bar = driver.find_element(By.XPATH, '//*[@id="headerSearchField"]')

#saisir sandale dans la barre de recherche
search_bar.send_keys("sandale")
search_bar.send_keys(Keys.ENTER)

time.sleep(10)

#cliquer sur sandales femme
# sandale_femme = driver.find_element (By.XPATH,'//*[@id="productListHeader"]'/div[1]/div[1]/ul/li[2]/a/span/b).click

time.sleep(7)