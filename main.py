from send_photo import Send
from login import Login
from web_scraping import BaixarConteudo
from time import sleep as tm
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



def webdriver_complete():
    mobile_emulation = { "deviceName": "Nexus 5" }

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=ChromeDriverManager().install())

    return driver


def main():

    a = input('Você já fez login?[s=sim,n=não]')

    driver = webdriver_complete()

    if a == 'S' or a == 's':

        try:
            open('cookies.pkl','r')
        except:
            user = input('Digite seu usuario:\n')
            pwd = input('Digite sua senha:\n')

            login = Login(user,pwd,True)
            login.login()
    else:

        user = input('Digite seu usuario:\n')
        pwd = input('Digite sua senha:\n')

        login = Login(user,pwd,True)
        login.login()
    link = input('Link do perfil para pegar os posts\n')
    
    
    while True:

        robot = BaixarConteudo(link,driver)
        legenda = robot.coletar_informacoes()
        

        
        if legenda == None:

            print('')
        else:
            robo = Send(driver)
            robo.send_photo(legenda)
        tm(30)
        


main()

