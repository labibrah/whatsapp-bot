from selenium import webdriver
import time
driver = webdriver.Chrome(r"/usr/local/bin/chromedriver") //location of chromedriver


driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
#msg = input('Enter your message : ')
lyrics = ('<Message>') // enter message here



#count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')

for i in range(100):
    msg_box.send_keys(lyrics)
    time.sleep(0.8)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
