from wappdriver import WhatsApp
import csv
from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")


# Enter your list of contacts to send messages to here
contact_list = ["Dane"] 

# Enter your message to be sent here
msg = "Test test test!\nNew line here!" 
# FORMAT STRINGS WITH \N IN ORDER FOR MULTI-LINE MESSAGES TO SEND PROPERLY AS IMAGE CAPTIONS


# Enter the absolute path of your image to be sent here
image_path = r"C:\Users\WeeKe\Desktop\Images\this_is_fine.jpg"

time.sleep(10) # Waits 10 seconds for you to scan the QR code

################# PYTHONIC IMPLEMENTATION ################################
try:
    for person in contact_list:
        if bool(image_path) == True:
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(person))
            user.click()
            attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
            attachment_box.click()
            image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(image_path)
            time.sleep(3)
            caption_bar = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
            caption_bar.click()
            caption_bar.clear()
            for part in msg.split("\n"):
                caption_bar.send_keys(part) # This does not work for multi-line strings. It creates a new line by hitting "Enter", which sends the message prematurely
                caption_bar.send_keys(Keys.SHIFT, "\n")
        caption_bar.send_keys(Keys.RETURN) 
        time.sleep(randint(5,30))
    driver.quit()

except:
    with WhatsApp() as bot:
        bot.send(person, msg)
        time.sleep(randint(5,30))



################### CSV IMPLEMENTATION ###################################

# with open(r"C:\Users\WeeKe\Desktop\Python Playground\Whatsapp Automation\whatsapp_messages.csv") as f:
#     reader = csv.reader(f)
#     next(reader)
#     for name, message in reader:
#         user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
#         user.click()
#         text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#         try:
#             for part in message.split("\n"):
#                 text_box.send_keys(part)
#                 text_box.send_keys(Keys.SHIFT, "\n")
#         except:
#                 text_box.send_keys(message)
#         text_box.send_keys(Keys.RETURN)






# Things to explain 
    # How to install ChromeDriver
    # How to specify message outside of csv
    # How to use the CSV implementation
    # How to paste emojis
    # How to specify files to send