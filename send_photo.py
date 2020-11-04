from selenium import webdriver
import pickle
import os
from time import sleep as tm
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key , Controller

class Send():

    def __init__(self,driver:webdriver):
        try:
            self.cookies = pickle.load(open('cookies.pkl','rb'))
        except:
            print('Login não ainda não foi feito')
            return
        self.driver = driver
     
    def send_photo(self,legenda):

        self.driver.get('https://www.instagram.com/')
        for cookies in self.cookies:

            self.driver.add_cookie(cookies)

        self.driver.get('https://www.instagram.com/')

        tm(3)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]').click()
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav[2]/div/div/form/input').send_keys(os.getcwd()+'\\image.png')

        tm(3)
        
        self.driver.find_element_by_class_name('UP43G').click()
        
        tm(3)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').click()
        keyboard = Controller()
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        tm(4)

        

        self.driver.execute_script(f'var a = document.getElementsByClassName("_472V_"); a[0].value="{legenda}" ')
        tm(1)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(Keys.LEFT_CONTROL+'a')
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(Keys.LEFT_CONTROL+'c')
        tm(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(Keys.TAB)

        tm(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').click()

        tm(4)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(Keys.LEFT_CONTROL+'v')
        tm(1)
        
        
        
        
        tm(3)
        
        self.driver.find_element_by_class_name('UP43G').click()
        
        tm(10)
        
        
