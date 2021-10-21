#!/usr/bin/env python
# coding: utf-8

import logging
from source.functions import wipyfunctions

logging.basicConfig(
    filename = "log/wipy.log", # Or /home/Your-User/Public/YourFolder/Wi-py/log/wipy.log
    level = logging.INFO, 
    format = "%(asctime)s - [Nível: %(levelno)s/INFO] [Função: %(funcName)s] [Ação: %(message)s]"
)   

init = input("Quer iniciar? (s/n):")

## CONDICIONAL - INICIAR OU NÃO INICIAR
if init == 's':

    wipyfunctions.open_browser()
    
    action = input("Oque deseja realizar? (del/add):")
    
    ## LOOP CONDICIONAL - DELETAR MAC, ADICIONAR MAC OU ENCERRAR
    while True:

        if action == 'd' or action == 'deletar' or action == 'del':

            device = wipyfunctions.validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE DELETAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                wipyfunctions.close_browser()
                break
                
            else:

                wipyfunctions.login_enter()
                wipyfunctions.delete()
                wipyfunctions.close_browser()
                break
                
        elif action == 'a' or action == 'adicionar' or action == 'add':
            
            device = wipyfunctions.validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE ADICIONAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                wipyfunctions.close_browser()
                break
                
            else:

                wipyfunctions.login_enter()
                wipyfunctions.add()
                wipyfunctions.close_browser()
                break
                
        elif action == 'exit':

            print("Programa encerrado!")
            wipyfunctions.close_browser()
            break
        
        ## CONDIÇÃO CASO NÃO SEJA ADICIONAR, DELETAR OU ENCERRAR
        else:

            action = input("Opção inválida! (digite deletar/del/d ou adicionar/add/a):")
else:

    print("Não iniciado!")