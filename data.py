########################   install basic   #############################
# sudo apt-get install python-pyaudio python3-pyaudio python-pip
# sudo pip install SpeechRecognition 
import speech_recognition as sr

########################   install selenium   #############################

#wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
#tar -xvzf geckodriver-v0.19.0-linux64.tar.gz
#chmod +x geckodriver
#sudo pip install -U selenium
#sudo cp geckodriver /usr/local/bin/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os 



r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # here
    print("Say something!")
    audio = r.listen(source)
data = r.recognize_google(audio)



if data=="lock":
    os.system("gnome-screensaver-command -l")


browser = webdriver.Firefox()
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search.send_keys(data)
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(15) # sleep for 5 seconds so you can see the results
browser.quit()
