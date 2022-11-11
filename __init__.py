from apiTrelloo import trello
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui


APITrelloo = trello()
trello_card = str(APITrelloo.getCards())

values = ''.join(map(str, trello_card))
value = eval(values)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)

contatos= ['INSERT NUMBER']
mensagem = "INSERT YOUR MESSENGE"

# Função responsável para fazer a busca dos contatos
def buscarContato(contato):
    campo_pesquisa=driver.find_element(by=By.XPATH, value='//div[contains(@class,"_13NKt copyable-text selectable-text")]') #Novo formato do SELENIUM 4.3
    time.sleep(3) # O timer irá esperar 3 segundos para fazer a busca do contato
    campo_pesquisa.click() # O comando .click irá executar como um clique do mouse em cima da barra de busca do whatsapp
    campo_pesquisa.send_keys(contato) # Será inserido na barra de busca os contatos que foram selecionados 
    campo_pesquisa.send_keys(Keys.ENTER) # Será executado com a tecla enter a busca do contato

#função responsável para fazer o envio da mensagem
def enviarMensagem(mensagem):
    campo_mensagem=driver.find_element(by=By.XPATH, value='//div[contains(@class, "INSERT XPATH DO WPP")]')
    campo_mensagem.click() # O comando .click irá executar como um clique do mouse em cima da barra de busca de envio da mensagem
    time.sleep(3)  # O timer irá esperar 3 segundos para inserir a mensagem na barra de mensagem
    campo_mensagem.send_keys(mensagem) # Será inserido na barra de mensagem as informações que foram postas
    campo_mensagem.send_keys(Keys.ENTER) # Fará o envio da mensagem
    
for contato in contatos: #laço de repetição que passará pelas funções *buscar_contato* e *enviarmensagem* 
    buscarContato(contato) #Irá percorrer pelo elemento da class selecionada
    enviarMensagem(mensagem) #Irá percorrer pe

time.sleep(20) #fechará o navegador utilizado em 20 segundos
pyautogui.hotkey('ctrl', 'w')
