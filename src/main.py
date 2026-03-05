import os
from menu import (exibir_menu_sistema, escolher_opcao)

def main():
    while True:
        os.system('cls')
        exibir_menu_sistema()
        escolher_opcao()
    
if __name__ == '__main__':
    main()