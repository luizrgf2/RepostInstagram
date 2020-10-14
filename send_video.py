from selenium import webdriver
import pickle
import os
from time import sleep as tm
from webdriver_manager.chrome import ChromeDriverManager
class Send():

    def __init__(self):
        try:
            self.cookies = pickle.load(open('cookies.pkl','rb'))
        except:
            print('Login não ainda não foi feito')
            return

        

        chrome_options = webdriver.ChromeOptions()

        

        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=ChromeDriverManager().install())
     
    def send_photo(self,legenda):

        self.driver.get('https://www.instagram.com/')
        for cookies in self.cookies:

            self.driver.add_cookie(cookies)

        self.driver.get('https://www.instagram.com/')

        tm(3)

        self.driver.get('https://www.instagram.com/felipergfg/channel/')

        tm(3)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[4]/a/button').click()
        
        tm(2)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/form/div/div[1]/label/div/div/div[2]').click()

        tm(2)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/form/div/div[1]/label/input').send_keys(os.getcwd()+'\\video.mp4')

        tm(3)
        
robo = Send()
robo.send_photo('waaw')
