import os

def voltar_ao_menu():
    input('\nAperte enter para voltar ao menu principal ')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def finalizar_sistema():
    os.system('cls')
    exibir_subtitulo('Finalizando o sistema')
    exit()
    
def opcao_invalida():
    os.system('cls')
    print('Opção inválida!')
    voltar_ao_menu()

def sinalizar_sem_documento():
        os.system('cls')
        print('Nenhum documento cadastrado')
        voltar_ao_menu()