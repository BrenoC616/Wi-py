#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import logging
import json

### ELEMENTOS
elementsData = open("source/json/elements.json", "r") # Or /home/Your-User/Public/Your-Folder/Wi-py/source/json/elements.json
elements = json.load(elementsData)

### ENDEREÇOS MAC
wirelessClientsData = open("source/json/wirelessClients.json", "r") # Or /home/Your-User/Public/Your-Folder/Wi-py/source/json/wirelessClients.json
wirelessClients = json.load(wirelessClientsData)

### FUNÇÃO: ABRIR NAGEVADOR E ACESSAR URL
def open_browser():

    global browser

    browser = webdriver.Firefox()

    browser.set_window_position(16, 48)
    browser.set_window_size(850, 650)
    
    browser.get(elements["URL"])

### FUNÇÃO: VALIDAÇÃO
def validate():

    global device
    global xpath

    device = input("Diga nome do dispositivo: ")
    
    while True:  
        
        if device in wirelessClients:
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
    
    buttonLoginElement = browser.find_element_by_id(elements["Buttons"]["buttonLogin"])

    buttonLoginElement.click()

    print("Login feito!")
    sleep(2)

    browser.get(elements["Options"]["optionWireless"])

    print("Wireless acessado!")
    sleep(2)

    browser.get(elements["Options"]["optionWirelessAdvanced"])

    print("Wireless Avançado acessado!")
    sleep(2)
    
    ### FUNÇÃO ENTRAR BLOCO2
    
    buttonSetupELement = browser.find_element_by_name(elements["Buttons"]["buttonSetup"])

    buttonSetupELement.click()

    print("Cofiguração ACL acessado!")
    sleep(2)

    logging.info("Entrou na Rede!")

### FUNÇÃO: DELETAR
def delete(): 

    selectMACElement = browser.find_element_by_xpath(xpath)

    selectMACElement.click()

    print(f"Dispositivo {device} escolhido!")
    sleep(2)

    buttonDeleteElement = browser.find_element_by_name(elements["Buttons"]["buttonDelete"])

    buttonDeleteElement.click()

    alerta = browser.switch_to.alert
    alerta.accept()

    print(f"Dispositivo {device} deletado da rede!")

    logging.info(f"Deletou Dispositivo {device}!")

### FUNÇÃO: ADICIONAR
def add():   

    inputMACElement = browser.find_element_by_name(elements["Inputs"]["inputMAC"])

    inputMACElement.click()

    inputMACElement.send_keys(wirelessClients[f"{device}"]["reduced-mac-address"])

    buttonAddElement = browser.find_element_by_name(elements["Buttons"]["buttonAdd"])

    buttonAddElement.click()

    print(f"Dispositivo {device} adicionado na rede!")

    logging.info(f"Adicionou Dispositivo {device}!")

### FUNÇÃO: FECHAR NAVEGADOR
def close_browser(secs=2):

    sleep(secs)

    browser.quit()
