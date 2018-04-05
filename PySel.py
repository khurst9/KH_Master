from selenium import webdriver


import time
from selenium import webdriver

driver = webdriver.Chrome('C:/selenium/chromedriver')  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('https://www.spirit.com/');
print('waiting')
time.sleep(2) # Let the user actually see something!

#flight page 1
depart_city = driver.find_element_by_id('departCityCodeSelect')
depart_city.send_keys('PIT')
#depart_city.send_keys(Keys.ENTER)
time.sleep(2)

depart_date = driver.find_element_by_id('departDate')
depart_date.send_keys('07/07/2018')
time.sleep(2)

return_date = driver.find_element_by_id('returnDate')
return_date.send_keys('07/14/2018')
time.sleep(2)

numAdults = driver.find_element_by_id('paxAdults')
numAdults.send_keys('2')
time.sleep(2)

numChildren = driver.find_element_by_id('paxMinors')
numChildren.send_keys('1')
time.sleep(2)

dest_city = driver.find_element_by_id('destCityCodeSelect')
dest_city.send_keys('MYR')

#depart_city.send_keys(Keys.ENTER)

search_flights = driver.find_element_by_xpath('//*[@id="book-travel-form"]/div/p/button')
search_flights.click()

#young traveler page
mob = driver.find_element_by_id('child_0_month')
mob.click()
dob = driver.find_element_by_id('child_0_day')
dob.click()
yob = driver.find_element_by_id('child_0_year')
yob.click()
continue_button = driver.find_element_by_xpath('//*[@id="childBirthDates"]/div/div/div[3]/p/button')
continue_button.click()

