from send_photo import Send
from login import Login
from web_scraping import BaixarConteudo
from time import sleep as tm



def main():

    a = input('Você já fez login?[s=sim,n=não]')

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

        robot = BaixarConteudo(link)
        legenda = robot.coletar_informacoes()
        

        
        if legenda == None:

            print('')
        else:
            robo = Send()
            robo.send_photo(legenda)
        tm(30)
        


main()

