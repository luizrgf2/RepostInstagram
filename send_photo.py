from selenium import webdriver
import pickle
import os
from time import sleep as tm
from webdriver_manager.chrome import ChromeDriverManager
import emoji

class Send():

    def __init__(self):
        try:
            self.cookies = pickle.load(open('cookies.pkl','rb'))
        except:
            print('Login não ainda não foi feito')
            return

        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=ChromeDriverManager().install())
     
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

        tm(4)

        

        self.driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea').send_keys(legenda)
        
        tm(3)
        
        self.driver.find_element_by_class_name('UP43G').click()
        
        tm(10)
        
        self.driver.close()

    def conver_unicode(self,text):

        for char in text:

            

            if char in emoji.UNICODE_EMOJI:
                
                car = char.encode('unicode-escape').decode('ASCII')

                uni_c = f"u'{car}'"

                palavra_final = palavra_final+uni_c
            else:

                palavra_final = palavra_final+char

        print(palavra_final)
        return palavra_final