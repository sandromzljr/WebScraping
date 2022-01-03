#pip install selenium
#importando apenas webdriver
from os import name
from selenium import webdriver

#importando "teclado"
from selenium.webdriver.common.keys import Keys

#importando "tempo" para espera entre comandos
import time

#pip install xlrd
#Lib xlrd para trabalhar com excel (arquivos em xls)
import xlrd

print("Iniciando o WebScrap")

#Criando um arquivo de texto (bloco de notas)
arquivo = open("resultadoWebScraping.txt", "w")

#Abrindo o arquivo excel para leitura de dominios
workbook = xlrd.open_workbook(r'caminho arquivo excel')

#Utilizando Plan1 dentro do excel
sheet = workbook.sheet_by_name('Plan1')

#Contando linhas e colunas
rows = sheet.nrows
columns = sheet.ncols

#Removendo log no terminal
options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

#Acessando o chrome através do webdriver para Chrome <Caminho>
caminho = r"caminho ChromeDriver"
driver = webdriver.Chrome(caminho, options=options)

#Acessando um site qualquer
driver.get("https://registro.br/")

#Percorrendo de 0 até limite de linhas do arquivo
for currentRow in range(0, rows): 
  #Lendo o conteúdo de currentRow e coluna 0
  value = sheet.cell_value(currentRow, 0)
  #Procurando dentro do site um id igual ao parametro
  pesquisa = driver.find_element_by_id("is-avail-field")
  #Limpando o campo antes de enviar um novo valor para pesquisa
  pesquisa.clear()
  #Enviando o valor de currentRow para pesquisa
  pesquisa.send_keys(value)
  pesquisa.send_keys(Keys.RETURN)
  time.sleep(2)

  #Escrevendo o retorno da busca
  driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong')
  retorno = "Domínio %s %s \n" % (value, driver.find_element_by_xpath('//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
  arquivo.write(retorno)

#Fechando o arquivo de texto
arquivo.close()

#Finalizando o webdriver
driver.close()