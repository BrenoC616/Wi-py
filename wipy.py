#!/usr/bin/env python
# coding: utf-8

import logging
from source.functions import wipyfunctions

logging.basicConfig(
    filename="log/wipy.log",
    level=logging.INFO,
    format="%(asctime)s - [Nível: %(levelno)s/INFO] [Função: %(funcName)s] [Ação: %(message)s]")

init = input("Quer iniciar? (s/n):")
wipyfunctions.set_browser()

if init == 's':
    wipyfunctions.open_browser()
    action = input("Oque deseja realizar? (del/add):")
    
    while True:
        if action == 'd' or action == 'deletar' or action == 'del':
            device = wipyfunctions.validate()
            
            if device != 'exit':
                wipyfunctions.login_enter()
                wipyfunctions.delete()
                wipyfunctions.close_browser()
                break
                
            else:
                print("Programa encerrado!")
                wipyfunctions.close_browser()
                break
                              
        elif action == 'a' or action == 'adicionar' or action == 'add':
            device = wipyfunctions.validate()
            
            if device != 'exit':
                wipyfunctions.login_enter()
                wipyfunctions.add()
                wipyfunctions.close_browser()
                break
                
            else:
                print("Programa encerrado!")
                wipyfunctions.close_browser()
                break
                
        elif action == 'exit':
            print("Programa encerrado!")
            wipyfunctions.close_browser()
            break

        else:
            action = input("Opção inválida! (digite deletar/del/d ou adicionar/add/a):")
            
else:
    print("Não iniciado!")
