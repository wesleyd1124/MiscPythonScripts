from selenium import webdriver
from googletrans import Translator
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import shutil
import urllib.request
try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/tesseract.exe'

options = webdriver.ChromeOptions() 
driver = webdriver.Chrome("/chromedriver.exe", chrome_options=options)
driver.get("https://www.thisislanguage.com/")
actions = ActionChains(driver)

input("Press Any Key To Start...")
#Id = word_canvas, class = guess

def readCanvas():
	downloadPath = driver.execute_script(" return document.getElementById('word_canvas').toDataURL();")
	file_name, headers = urllib.request.urlretrieve(downloadPath)
	time.sleep(.5)
	recognizedText = pytesseract.image_to_string(Image.open(file_name))
	os.remove(file_name)
	return recognizedText
	
while True:
	try:
		word = readCanvas()
		print("Word : " + word)
		translator = Translator()
		answer = translator.translate(text=word, src='en', dest='fr')
		print("Answer is:" + answer.text)
		guess = driver.find_element_by_xpath("//input[@class='guess']")
		guess.clear()
		actions.move_to_element(guess).send_keys(answer.text).perform()
	except Exception as e:
		print("Couldn't fill in blank : " + str(e))
	time.sleep(.5)

