from selenium import webdriver 
import pynput

import time  
   
from selenium.webdriver.common.keys import Keys  

browser = webdriver.Chrome()  
browser.get('https://www.instagram.com') 

time.sleep(2)

mouse = pynput.mouse.Controller()

login = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
login[0].click()
time.sleep(2)
user = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
user[0].send_keys('anvesha28') 

passw = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')

with open('test.txt', 'r') as myfile:   
    Password = myfile.read().replace('\n', '')
passw[0].send_keys(Password)

time.sleep(2)

log = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]') 
log[0].click()

time.sleep(3) 

browser.get("https://www.instagram.com/{0}/".format('anvesha28'))

lis1 = []
lis2 = []

following = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
following[0].click()

following_elem = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
following_no = int(following_elem.text)

ids1 = []

while len(ids1) < following_no:
    ids1 =  browser.find_elements_by_class_name("FPmhX")
    mouse.scroll(0,-10)

for j in ids1:
    lis1.append(j.text)      

close = browser.find_element_by_class_name('wpO6b')
close.click()

follower = browser.find_elements_by_class_name('Y8-fY ')
follower[1].click()

follower_elem = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
follower_no = int(follower_elem.text)

ids2 = []
   
while len(ids2) < follower_no:
    ids2 =  browser.find_elements_by_class_name("FPmhX")
    mouse.scroll(0,-10)
    
for k in ids2:
    lis2.append(k.text)
    
not_follow = []

for x in lis1:
    if x not in lis2:
        not_follow.append(x)

browser.close()  
