from selenium import webdriver
from pynput.keyboard import Key, Controller
import time

#----Website Name and sensitive information hidden

#go to website XYZ
web = webdriver.Chrome("C:/Users/Pradnya/chromedriver.exe")
web.get('https://XYZ')

#accept and proceed
accept=web.find_element("xpath",'//*[@id="mat-radio-6"]/label/span[1]')
accept.click()
proceed=web.find_element("xpath",'//*[@id="mat-dialog-0"]/XYZ/div/mat-dialog-content/div[2]/input')
proceed.click()

time.sleep(2)
#regulatory update box
cross=web.find_element("xpath",'//*[@id="mat-dialog-1"]/XYZ/div/div/div/mat-icon')#xpath for cross icon
cross.click()


#email field
Email="XYZ"
email=web.find_element("xpath",'//*[@id="mat-input-0"]')
email.send_keys(Email)

#enter type of mutual fund
list=web.find_element("xpath",'/html/body/app-root/div/XYZ/div[2]/div/div[1]/div[2]/div/app-statements/div/div[2]/div/div[2]/form/div[2]/div/mat-form-field/div/div[1]/div[3]')
list.click()
time.sleep(2)
all=web.find_element("xpath",'//*[@id="mat-select-2-panel"]/mat-option-select-all/div')
all.click()

#to escape dropdown list
keyboard = Controller()
keyboard.press(Key.esc)
keyboard.release(Key.esc)


#enter temporary password
Password="XYZ"
password=web.find_element("xpath",'//*[@id="mat-input-5"]')
password.send_keys(Password)
confirmPassword=web.find_element("xpath",'//*[@id="mat-input-6"]')
confirmPassword.send_keys(Password)


time.sleep(10)
#submit button
submit=web.find_element("xpath",'/html/body/app-root/div/XYZ/div[2]/div/div[1]/div[2]/div/app-statements/div/div[2]/div/div[2]/form/div[6]/button[1]')
submit.click()