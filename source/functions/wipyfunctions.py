#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import logging
import json
import configparser

with open("source/json/elements.json", "r") as elementsData:
    elements = json.load(elementsData)

with open("source/json/wirelessClients.json", "r") as wirelessClientsData:
    wirelessClients = json.load(wirelessClientsData)

config = configparser.ConfigParser()

def set_browser():
    filepath = "source/config/config.ini"

    config.read(filepath)
    configDefault = config["default"]
    configDefaultSet = configDefault["set"]

    if configDefaultSet == "0":
        value = input("Defina seu navegador (Chrome/Firefox): ")
        configDefault["browser"] = value
        configDefault["set"] = "1"

        with open(filepath, "w") as configfile:
            config.write(configfile)


def open_browser():
    global browser

    filepath = "source/config/config.ini"

    config.read(filepath)
    configDefault = config["default"]
    configDefaultBrowser = configDefault["browser"]

    if configDefaultBrowser == "Firefox":
        browser = webdriver.Firefox()

    elif configDefaultBrowser == "Chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--remote-debugging-port=9222")
        browser = webdriver.Chrome(chrome_options=chromeOptions)

    browser.set_window_position(16, 48)
    browser.set_window_size(850, 650)
    browser.get(elements["URL"])


def validate():
    global device
    global xpath

    device = input("Diga nome do dispositivo: ")

    while True:
        if device in wirelessClients:
            xpath = '//*[@value="%s"]' % wirelessClients[f"{device}"]["reduced-mac-address"]
            break

        elif device == 'exit':
            print("Seleção de dispositivo foi fechada!")
            return device
            break
        
        else:
            device = input(
                "Dispositivo não existe! (Digite um dispositivo existente): ")

    logging.info(f"Dispositivo {device} escolhido!")


def login_enter():
    buttonLoginElement = browser.find_element_by_id(
        elements["Buttons"]["buttonLogin"])
    buttonLoginElement.click()
    print("Login feito!")
    sleep(2)

    browser.get(elements["Options"]["optionWireless"])
    print("Wireless acessado!")
    sleep(2)

    browser.get(elements["Options"]["optionWirelessAdvanced"])
    print("Wireless Avançado acessado!")
    sleep(2)

    buttonSetupELement = browser.find_element_by_name(
        elements["Buttons"]["buttonSetup"])
    buttonSetupELement.click()
    print("Cofiguração ACL acessado!")
    sleep(2)

    logging.info("Entrou na Rede!")


def delete():
    selectMACElement = browser.find_element_by_xpath(xpath)
    selectMACElement.click()
    print(f"Dispositivo {device} escolhido!")
    sleep(2)

    buttonDeleteElement = browser.find_element_by_name(
        elements["Buttons"]["buttonDelete"])
    buttonDeleteElement.click()

    alert = browser.switch_to.alert
    alert.accept()
    print(f"Dispositivo {device} deletado da rede!")

    logging.info(f"Deletou Dispositivo {device}!")


def add():
    inputMACElement = browser.find_element_by_name(
        elements["Inputs"]["inputMAC"])
    inputMACElement.click()
    inputMACElement.send_keys(
        wirelessClients[f"{device}"]["reduced-mac-address"])

    buttonAddElement = browser.find_element_by_name(
        elements["Buttons"]["buttonAdd"])
    buttonAddElement.click()
    print(f"Dispositivo {device} adicionado na rede!")

    logging.info(f"Adicionou Dispositivo {device}!")


def close_browser(secs=2):
    sleep(secs)
    browser.quit()
