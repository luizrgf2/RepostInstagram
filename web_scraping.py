from selenium import webdriver
import pickle
from time import sleep as tm
from selenium.webdriver.common.keys import Keys
import os
from webdriver_manager.chrome import ChromeDriverManager
import requests
from send_photo import Send

class BaixarConteudo():

    def __init__(self,link_perfil):

        self.link_atual = ''

        try:
            self.cookies = pickle.load(open('cookies.pkl','rb'))
        except:
            print('Login não ainda não foi feito')
            return

        self.link = link_perfil

        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=ChromeDriverManager().install())
     
    
    def coletar_informacoes(self):

        self.driver.get('https://www.instagram.com/')
        for cookies in self.cookies:

            self.driver.add_cookie(cookies)
        
        self.driver.get('https://www.instagram.com/')

        tm(3)
        robo = Send()
        
        self.driver.get(self.link)

        tm(3)
        pai = self.driver.execute_script('return document.getElementsByClassName("v1Nh3 kIKUG  _bz0w")[0]')
        self.link_atual = pai.find_element_by_xpath('.//*').get_attribute('href')
        print(self.link_atual)

        confirm = open('link_atual.pkl','r').read()

        if confirm.find(self.link_atual) != -1:

            print('Já existe este post')

        else:

            open('link_atual.pkl','w').write(self.link_atual)

            self.driver.get(self.link_atual)
            tm(2)
            try:
                link_image = self.driver.find_element_by_class_name('FFVAD').get_attribute('src')


                print('===============================================================================================================================================================================')
                print('Iniciando o Download')
                print('===============================================================================================================================================================================')

                open('link_atual.pkl','w').write(self.link_atual+',png')
                self.DownloadImage(link_image)
                    
                print('===============================================================================================================================================================================')
                print('Finalizado o Download')
                print('===============================================================================================================================================================================')
                legenda = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/div/div[1]/div/span/span[1]').text
                    
                return legenda    
                    
                
            except:

                print('Video Detectado!!')
                return

            
        self.driver.close()
    def DownloadImage(self, link):

        response = requests.get(link)

        open('image.png','wb').write(response.content)

    def DownloadVideo(self, link):

        response = requests.get(link)

        open('video.mp4','wb').write(response.content)




