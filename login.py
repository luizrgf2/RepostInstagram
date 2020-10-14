from selenium import webdriver
import pickle
from time import sleep as tm
from selenium.webdriver.common.keys import Keys
import os
from webdriver_manager.chrome import ChromeDriverManager

class Login():

    def __init__(self,username,pwd,login_newcount):

        self.login_newcount = login_newcount
        self.username = username
        self.pwd = pwd
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        
        self.driver.get('https://www.instagram.com/')
        tm(2)
        try:
            if self.login_newcount == False:
                cookies = pickle.load(open('cookies.pkl','rb'))

                for cookie in cookies:

                    self.driver.add_cookie(cookie)

                    self.driver.get('https://www.instagram.com/')


                

            else:

                self.driver.find_element_by_name('username').send_keys(self.username)

                self.driver.find_element_by_name('password').send_keys(self.pwd)

                self.driver.find_element_by_name('password').send_keys(Keys.RETURN)

                tm(3)

                self.driver.get('https://www.instagram.com/')

                tm(3)

                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()

                cookies = pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))

                

                



        except:

            tm(2)

            self.driver.find_element_by_name('username').send_keys(self.username)

            self.driver.find_element_by_name('password').send_keys(self.pwd)

            self.driver.find_element_by_name('password').send_keys(Keys.RETURN)

            tm(3)

            cookies=pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))

            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()

           
        self.driver.close()
    
    def etc(self,file_name):
        path = "/"
        dir = os.listdir(path)
        for file in dir:
            if file == file_name:
                os.remove(file)

