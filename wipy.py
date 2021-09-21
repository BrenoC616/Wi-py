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

### FUNÇÃO VALIDAÇÃO
def validate():

    global device
    global xpath
    global i

    device = input("Diga nome do dispositivo: ")
    
    while True:  

        if device == 'deviceName':
            i = 1
            xpath = '//*[@value="%s"]' % macAddress[i] #XPATH (Ex.: //*[@value="70fd46d107f4"])
            break
        elif device == 'deviceName':
            i = 2
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 3
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 4
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 5
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 6
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 7
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 8
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 9
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 10
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'deviceName':
            i = 11
            xpath = '//*[@value="%s"]' % macAddress[i]
            break
        elif device == 'exit':
            print("Seleção de dispositivo foi fechada!")
            break
        else:
            device = input("Dispositivo não existe! (Digite um dispositivo existente): ")

    logging.info("Dispositivo %s escolhido!" % device)
            
### FUNÇÃO CONECTAR E ENTRAR
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

### FUNÇÃO DELETAR
def delete(): 

    selectMACElement = navegador.find_element_by_xpath(xpath)

    selectMACElement.click()

    print("Dispositivo %s escolhido!" % device)
    sleep(2)

    buttonDeleteElement = navegador.find_element_by_name(buttonDelete)

    buttonDeleteElement.click()

    alerta = navegador.switch_to.alert
    alerta.accept()

    print("Dispositivo %s deletado da rede!" % device)

    logging.info("Deletou Dispositivo %s!" % device)

### FUNÇÃO ADICIONAR
def add():   

    inputMACElement = navegador.find_element_by_name(inputMAC)

    inputMACElement.click()

    inputMACElement.send_keys(macAddress[i])

    buttonAddElement = navegador.find_element_by_name(buttonAdd)

    buttonAddElement.click()

    print("Dispositivo %s adicionado na rede!" % device)

    logging.info("Adicionou Dispositivo %s!" % device)

init = input("Quer iniciar? (s/n):")

## CONDICIONAL - INICIAR OU NÃO INICIAR
if init == 's':

    navegador = webdriver.Firefox()
    navegador.set_window_position(16, 48)
    navegador.set_window_size(850, 650)
    
    navegador.get(url)
    
    teste = input("Oque deseja realizar? (del/add):")
    
    ## LOOP CONDICIONAL - DELETAR MAC, ADICIONAR MAC OU ENCERRAR
    while True:

        if teste == 'd' or teste == 'deletar' or teste == 'del':
            
            validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE DELETAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                sleep(2)
                navegador.quit()
                break
                
            else:

                login_enter()
                delete()
                sleep(2)
                navegador.quit()
                break
                
        elif teste == 'a' or teste == 'adicionar' or teste == 'add':
            
            validate()
            
            ## CONDICIONAL - CONTINUAR PROCESSO DE ADICIONAR OU ENCERRAR
            if device == 'exit':

                print("Programa encerrado!")
                sleep(2)
                navegador.quit()
                break
                
            else:

                login_enter()
                add()
                sleep(2)
                navegador.quit()
                break
                
        elif teste == 'exit':

            print("Programa encerrado!")
            sleep(2)
            navegador.quit()
            break
        
        ## CONDIÇÃO CASO NÃO SEJA ADICIONAR, DELETAR OU ENCERRAR
        else:

            teste = input("Opção inválida! (digite deletar/del/d ou adicionar/add/a):")
else:

    print("Não iniciado!")