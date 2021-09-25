#!/usr/bin/env python
# coding: utf-8

import logging
from wipyfunctions import *

logging.basicConfig(
    filename = "wipy.log", # Or /home/Your-User/Public/YourFolder/wipy.log
    level = logging.INFO, 
    format = "%(asctime)s - [Nível: %(levelno)s/INFO] [Função: %(funcName)s] [Ação: %(message)s]"
)

init = input("Quer iniciar? (s/n):")

## CONDICIONAL - INICIAR OU NÃO INICIAR
if init == 's':

    open_browser()
    
    teste = input("Oque deseja realizar? (del/add):")
    
    ## LOOP CONDICIONAL - DELETAR MAC, ADICIONAR MAC OU ENCERRAR
    while True:

        if teste == 'd' or teste == 'deletar' or teste == 'del':

            device = validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE DELETAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                close_browser(2)
                break
                
            else:

                login_enter()
                delete()
                close_browser(2)
                break
                
        elif teste == 'a' or teste == 'adicionar' or teste == 'add':
            
            device = validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE ADICIONAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                close_browser(2)
                break
                
            else:

                login_enter()
                add()
                close_browser(2)
                break
                
        elif teste == 'exit':

            print("Programa encerrado!")
            close_browser(2)
            break
        
        ## CONDIÇÃO CASO NÃO SEJA ADICIONAR, DELETAR OU ENCERRAR
        else:

            teste = input("Opção inválida! (digite deletar/del/d ou adicionar/add/a):")
else:

    print("Não iniciado!")