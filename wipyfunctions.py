#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import logging

### ELEMENTOS
buttonAdd = 'addFilterMac'
buttonDelete = 'deleteSelFilterMac'
buttonLogin = 'loginBtn'
buttonSetup = 'setupList'
macAddress = {
    1: "deviceMacAddress", #Ex.: af:53:3c:2f:a2:94 -> af533c2fa294
    2: "deviceMacAddress",
    3: "deviceMacAddress",
    4: "deviceMacAddress",
    5: "deviceMacAddress",
    6: "deviceMacAddress",
    7: "deviceMacAddress",
    8: "deviceMacAddress",
    9: "deviceMacAddress",
    10: "deviceMacAddress",
    11: "deviceMacAddress"
}
inputMAC = 'mac'
optionWireless = "http://192.168.0.1/wlan_basic.htm"
optionWirelessAdvanced = "http://192.168.0.1/wladvanced.htm"
url = 'http://192.168.0.1/login.htm'

### FUNÇÃO: ABRIR NAGEVADOR E ACESSAR URL
def open_browser():

    global navegador

    navegador = webdriver.Firefox()

    navegador.set_window_position(16, 48)
    navegador.set_window_size(850, 650)
    
    navegador.get(url)

### FUNÇÃO: VALIDAÇÃO
def validate():

    global device
    global xpath
    global i

    device = input("Diga nome do dispositivo: ")
    
    while True:  
        
        if device == 'a10Joao':
            i = 1
            xpath = f'//*[@value="{macAddress[i]}"]' #XPATH (Ex.: //*[@value="af533c2fa294"])
            return device
            break
        elif device == 'a10Breno':
            i = 2
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'tvQuartoBreno':
            i = 3
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'tvSala':
            i = 4
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'tvQuartoBruna':
            i = 5
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'tvBox':
            i = 6
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'e6Mae':
            i = 7
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'noteBreno':
            i = 8
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'noteBruna':
            i = 9
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'a32Bruna':
            i = 10
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
            break
        elif device == 'hpPrint':
            i = 11
            xpath = f'//*[@value="{macAddress[i]}"]'
            return device
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
    
    buttonLoginElement = navegador.find_element_by_id(buttonLogin)

    buttonLoginElement.click()

    print("Login feito!")
    sleep(2)

    navegador.get(optionWireless)

    print("Wireless acessado!")
    sleep(2)

    navegador.get(optionWirelessAdvanced)

    print("Wireless Avançado acessado!")
    sleep(2)
    
    ### FUNÇÃO ENTRAR BLOCO2
    
    buttonSetupELement = navegador.find_element_by_name(buttonSetup)

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

    buttonDeleteElement = navegador.find_element_by_name(buttonDelete)

    buttonDeleteElement.click()

    alerta = navegador.switch_to.alert
    alerta.accept()

    print(f"Dispositivo {device} deletado da rede!")

    logging.info(f"Deletou Dispositivo {device}!")

### FUNÇÃO: ADICIONAR
def add():   

    inputMACElement = navegador.find_element_by_name(inputMAC)

    inputMACElement.click()

    inputMACElement.send_keys(macAddress[i])

    buttonAddElement = navegador.find_element_by_name(buttonAdd)

    buttonAddElement.click()

    print(f"Dispositivo {device} adicionado na rede!")

    logging.info(f"Adicionou Dispositivo {device}!")

### FUNÇÃO: FECHAR NAVEGADOR
def close_browser(secs):

    sleep(secs)

    navegador.quit()
