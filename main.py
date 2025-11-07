from run_tests import tes
from enviar_email import enviar_email
from enviar_email import verificar_email_e_senha



def login():
    usuario = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    try:
        verificar_email_e_senha(usuario, senha)
        tes()
        enviar_email(usuario, senha)

    except:
        print('Email ou senha errados, tente novamente:')
        login()

if __name__ == '__main__':
    login()
