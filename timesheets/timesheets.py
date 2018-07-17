#!/uar/bin/env python

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# import getpass
import keyring


user = 'jaimeruizno@gmail.com'

def load_all_items(driver):
	'''
	Scroll down all the way in order to load all the items in the category.
	'''

	time.sleep(1)

	SCROLL_PAUSE_TIME = 1

	# Get scroll height
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height


def signIn(driver):

	loginURL = 'https://www.3ss.hays.com.au'
	user = 'jaimeruizno@gmail.com'

	driver.get(loginURL)

	print('Attempting login')
	driver.find_element_by_id('username').send_keys(user)
	# passwd = getpass.getpass('Password: ')
	driver.find_element_by_id('password').send_keys(keyring.get_password(loginURL,user), Keys.ENTER) #
	# del passwd

	time.sleep(1)

	# while driver.current_url == 'https://www.3ss.hays.com.au/default.aspx?m=LOGIN_INVALID':
	# 		print('Wrong password')
	# 		print('Try again')
	# 		driver.find_element_by_id('username').send_keys(user)
	# 		passwd = getpass.getpass('Password: ')
	# 		driver.find_element_by_id('password').send_keys(passwd, Keys.ENTER)
	# 		del passwd
	#
	# 		time.sleep(1)





def newTimesheet(driver):

	driver.find_element_by_xpath('//*[@id="newnav"]/div/span/span').click()

	driver.find_element_by_xpath('//*[@id="newnav"]/ul/li[1]/a').click()
	time.sleep(1)

	driver.find_element_by_xpath('//*[@id="id_c08c4620-7fe7-43a4-a4df-f2613932d144"]/tbody/tr[3]/td/div/div/table/tbody/tr/td[1]/a/span').click()
	time.sleep(1)

	try:
		driver.find_element_by_xpath('//*[@id="id_78bfe04a-2650-47fb-a470-29bfe697a052"]/tbody/tr[3]/td/div/div/table/tbody/tr/td[3]/button').click()

	except:
		driver.find_element_by_xpath('//*[@id="cc83677a-78ec-431c-97db-593bb585037e"]/span').click()

	time.sleep(2)

	print('Populating timesheet with default values')
	testTime = driver.find_element_by_xpath('//*[@id="h_start_time"]')
	testTime.send_keys(# Monday
						'8 am', Keys.TAB, ':30', Keys.TAB, # Start time
						'5 pm', Keys.TAB, 	     Keys.TAB, # End time
								Keys.TAB, ':30', Keys.TAB, # Break
								Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, # (Go to next day)
						# Tuesday
						'8 am', Keys.TAB, ':30', Keys.TAB, # Start time
						'5 pm', Keys.TAB, 	     Keys.TAB, # End time
								Keys.TAB, ':30', Keys.TAB, # Break
								Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, # (Go to next day)
						# Wednesday
						'8 am', Keys.TAB, ':30', Keys.TAB, # Start time
						'5 pm', Keys.TAB, 	     Keys.TAB, # End time
								Keys.TAB, ':30', Keys.TAB, # Break
								Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, # (Go to next day)
						# Thursday
						'8 am', Keys.TAB, ':30', Keys.TAB, # Start time
						'5 pm', Keys.TAB, 	     Keys.TAB, # End time
								Keys.TAB, ':30', Keys.TAB, # Break
								Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, # (Go to next day)
						# Friday
						'8 am', Keys.TAB, ':30', Keys.TAB, # Start time
						'5 pm', Keys.TAB, 	     Keys.TAB, # End time
								Keys.TAB, ':30', Keys.TAB, # Break
								Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, # (Go to next day)
								)
	time.sleep(1)

#	driver.find_element_by_xpath('//*[@id="id_80b008f0-992d-45b0-aafb-1e53b858b7d2"]/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td/a').click()

#	time.sleep(1)

	# TODO: add option to write a comment (passed as a CLI argument)
#	driver.find_element_by_xpath('//*[@id="5ccad77c-d3f2-4b08-91d4-2cb2f2467ac6"]').click()

	time.sleep(1)

#	print(driver.find_element_by_xpath('//*[@id="id_7042a4be-7570-4277-a2cb-7cdf6b2e2fbd"]/tbody/tr[4]/td/div/div/table/tbody/tr[2]/td[7]').getText())

if __name__ == '__main__':


	with open('hours.log', 'r') as f:
		hours = f.read()
		if hours:
			print('ATTENTION: Weird hours this week:')
			print(hours)
	time0 = time.time()
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)

	# books = [elem.text for elem in driver.find_elements_by_css_selector('.title .value')]

	signIn(driver)
	newTimesheet(driver)

	# driver.quit()
	print('Total time: {} s'.format(time.time() - time0))
