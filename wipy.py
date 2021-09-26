#!/usr/bin/env python
# coding: utf-8

import logging
import wipyfunctions

logging.basicConfig(
    filename = "wipy.log", # Or /home/Your-User/Public/YourFolder/wipy.log
    level = logging.INFO, 
    format = "%(asctime)s - [Nível: %(levelno)s/INFO] [Função: %(funcName)s] [Ação: %(message)s]"
)   

init = input("Quer iniciar? (s/n):")

## CONDICIONAL - INICIAR OU NÃO INICIAR
if init == 's':

    wipyfunctions.open_browser()
    
    teste = input("Oque deseja realizar? (del/add):")
    
    ## LOOP CONDICIONAL - DELETAR MAC, ADICIONAR MAC OU ENCERRAR
    while True:

        if teste == 'd' or teste == 'deletar' or teste == 'del':

            device = wipyfunctions.validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE DELETAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                wipyfunctions.close_browser(2)
                break
                
            else:

                wipyfunctions.login_enter()
                wipyfunctions.delete()
                wipyfunctions.close_browser(2)
                break
                
        elif teste == 'a' or teste == 'adicionar' or teste == 'add':
            
            device = wipyfunctions.validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE ADICIONAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                wipyfunctions.close_browser(2)
                break
                
            else:

                wipyfunctions.login_enter()
                wipyfunctions.add()
                wipyfunctions.close_browser(2)
                break
                
        elif teste == 'exit':

            print("Programa encerrado!")
            wipyfunctions.close_browser(2)
            break
        
        ## CONDIÇÃO CASO NÃO SEJA ADICIONAR, DELETAR OU ENCERRAR
        else:

            teste = input("Opção inválida! (digite deletar/del/d ou adicionar/add/a):")
else:

    print("Não iniciado!")