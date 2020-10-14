from send_photo import Send
from login import Login
from web_scraping import BaixarConteudo
from time import sleep as tm
import emoji

def conver_unicode(text):
    palavra_final = ''
    if text == None:

        return None

    for char in text:

            

        if char in emoji.UNICODE_EMOJI:
                
            car = char.encode('unicode-escape').decode('ASCII')

            uni_c = f"u'{car}'"

            
        else:

            palavra_final = palavra_final+char

    print(palavra_final)
    return palavra_final


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
        legenda = conver_unicode(robot.coletar_informacoes())
        

        
        if legenda == None:

            print('')
        else:
            robo = Send()
            robo.send_photo(legenda)
        tm(30)
        


main()

