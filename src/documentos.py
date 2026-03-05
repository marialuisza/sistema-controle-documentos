import os
from auxiliar import (exibir_subtitulo, voltar_ao_menu, sinalizar_sem_documento)

documentos = []

def cadastrar_documento():
    try:
        exibir_subtitulo('Cᴀᴅᴀsᴛʀᴏ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        id_doc = int(input('Digite o ID do documento: '))
        for documento in documentos:
            if id_doc == documento['id']:
                print('ID já existe no sistema')
                voltar_ao_menu()
                break
        else:
            nome_doc = input('Digite o nome do documento: ')
            tipo_doc = input('Digite o tipo do documento: ')
            data_doc = input('Digite a data do documento (DD/MM/AAAA): ')
            dados_documento = {'id' : id_doc, 'nome' : nome_doc, 'tipo' : tipo_doc, 'data' : data_doc}
            documentos.append(dados_documento)
            print(f'O documento "{nome_doc}" foi cadastrado!\n')
            voltar_ao_menu()
    except ValueError:
            os.system('cls')
            print("ID inválido!")
            voltar_ao_menu()

def listar_documentos():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Lɪsᴛᴀ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        for documento in documentos:
            nome_doc = documento['nome']
            id_doc = documento['id']
            tipo_doc = documento['tipo']
            data_doc = documento['data']
            print(f'- ID: {id_doc} | Documento: {nome_doc} | Tipo: {tipo_doc} | Data: {data_doc}')
        voltar_ao_menu()
    
def buscar_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Bᴜsᴄᴀ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_busca = int(input('Digite o ID do documento que busca: '))
            encontrado = False
            for documento in documentos:
                if id_busca == documento['id']:
                    print(f'O ID {id_busca}, refere-se ao documento: {documento["nome"]}')
                    encontrado = True
                    voltar_ao_menu()
                    break
            if not encontrado:
                    print('ID inválido!')
                    voltar_ao_menu()
        except ValueError:
            os.system('cls')
            print("ID inválido!")
            voltar_ao_menu()

def remover_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Rᴇᴍᴏᴠᴇʀ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_remover = int(input('Digite o ID do documento que deseja remover: '))
            encontrado= False
            for documento in documentos:
                if id_remover == documento['id']:
                    documentos.remove(documento)
                    print('Documento removido com sucesso!')
                    encontrado = True
                    voltar_ao_menu()
                    break
            if not encontrado:
                    print('ID inválido!')
                    voltar_ao_menu()
        except ValueError:
            os.system('cls')
            print('ID inválido!')
            voltar_ao_menu() 

def atualizar_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Aᴛᴜᴀʟɪᴢᴀʀ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_atualizar = int(input('Digite o ID do documento que deseja atualizar: '))
            encontrado = False
            for documento in documentos:
                if id_atualizar == int(documento["id"]):
                    encontrado = True
                    print('Que campo deseja atualizar?')
                    print('1. Nome')
                    print('2. Tipo')
                    print('3. Data\n')
                    atualizar_doc = int(input('Escolha uma opção: '))
                    if atualizar_doc == 1:
                        nome_novo = input('Digite o novo nome: ')
                        documento['nome'] = nome_novo
                        print(f'Campo Nome alterado para "{documento["nome"]}" com sucesso!\n')
                        voltar_ao_menu()
                    elif atualizar_doc == 2:
                        tipo_novo = input('Digite o novo tipo: ')
                        documento['tipo'] = tipo_novo
                        print(f'Campo Tipo alterado para "{documento["tipo"]}" com sucesso!\n')
                        voltar_ao_menu()
                    elif atualizar_doc == 3:
                        data_nova = input('Digite a nova data: ')
                        documento['data'] = data_nova
                        print(f'Campo Data alterado para "{documento["data"]}" com sucesso!\n')
                        voltar_ao_menu()
                    else:     
                        os.system('cls')
                        print('Opção inválida!')
                        voltar_ao_menu()
                    break
            if not encontrado:
                    os.system('cls')
                    print('ID inválido!')  
                    voltar_ao_menu()      
        except ValueError:
            os.system('cls')
            print('ID inválido!')  
            voltar_ao_menu()