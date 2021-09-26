#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import logging
import json

### ELEMENTOS
elements_dados = open("elements.json", "r") # Or /home/Your-User/Public/Your-Folder/wirelessClients.json
elements = json.load(elements_dados)

### ENDEREÇOS MAC
wirelessClients_dados = open("wirelessClients.json", "r") # Or /home/Your-User/Public/Your-Folder/wirelessClients.json
wirelessClients = json.load(wirelessClients_dados)

### FUNÇÃO: ABRIR NAGEVADOR E ACESSAR URL
def open_browser():

    global navegador

    navegador = webdriver.Firefox()

    navegador.set_window_position(16, 48)
    navegador.set_window_size(850, 650)
    
    navegador.get(elements["URL"])

### FUNÇÃO: VALIDAÇÃO
def validate():

    global device
    global xpath
    global i

    device = input("Diga nome do dispositivo: ")
    
    while True:  
        
        if device in wirelessClients["valid-devices"]:
            xpath = '//*[@value="%s"]' % wirelessClients[f"{device}"]["reduced-mac-address"] #XPATH (Ex.: //*[@value="71f34vd707fk"])
            break
        elif device == 'exit':
            print("Seleção de dispositivo foi fechada!")
            return device
            break
        else:
            device = input("Dispositivo não existe! (Digite um dispositivo existente): ")

    logging.info(f"Dispositivo {device} escolhido!")
            
### FUNÇÃO: CONECTAR NO ROTEADOR E ENTRAR EM CONFIG ACL
def login_enter():

    ### FUNÇÃO ENTRAR - BLOCO1
    
    buttonLoginElement = navegador.find_element_by_id(elements["Buttons"]["buttonLogin"])

    buttonLoginElement.click()

    print("Login feito!")
    sleep(2)

    navegador.get(elements["Options"]["optionWireless"])

    print("Wireless acessado!")
    sleep(2)

    navegador.get(elements["Options"]["optionWirelessAdvanced"])

    print("Wireless Avançado acessado!")
    sleep(2)
    
    ### FUNÇÃO ENTRAR BLOCO2
    
    buttonSetupELement = navegador.find_element_by_name(elements["Buttons"]["buttonSetup"])

    buttonSetupELement.click()

    print("Cofiguração ACL acessado!")
    sleep(2)

    logging.info("Entrou na Rede!")

### FUNÇÃO: DELETAR
def delete(): 

    selectMACElement = navegador.find_element_by_xpath(xpath)

    selectMACElement.click()

    print(f"Dispositivo {device} escolhido!")
    sleep(2)

    buttonDeleteElement = navegador.find_element_by_name(elements["Buttons"]["buttonDelete"])

    buttonDeleteElement.click()

    alerta = navegador.switch_to.alert
    alerta.accept()

    print(f"Dispositivo {device} deletado da rede!")

    logging.info(f"Deletou Dispositivo {device}!")

### FUNÇÃO: ADICIONAR
def add():   

    inputMACElement = navegador.find_element_by_name(elements["Inputs"]["inputMAC"])

    inputMACElement.click()

    inputMACElement.send_keys(wirelessClients[f"{device}"]["reduced-mac-address"])

    buttonAddElement = navegador.find_element_by_name(elements["Buttons"]["buttonAdd"])

    buttonAddElement.click()

    print(f"Dispositivo {device} adicionado na rede!")

    logging.info(f"Adicionou Dispositivo {device}!")

### FUNÇÃO: FECHAR NAVEGADOR
def close_browser(secs):

    sleep(secs)

    navegador.quit()
