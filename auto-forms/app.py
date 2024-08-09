from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Chrome para rodar no Colab
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080")

# Find the correct Chrome binary path
!which google-chrome

# Update the Chrome binary location if necessary
chrome_options.binary_location = "/usr/bin/google-chrome"  # Replace with the actual path if different

# Criação do WebDriver
driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=chrome_options)

# Teste para acessar o formulário do Google
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfMCZE_xTa-IPhN5_gOjk5UOwt8WaMQeM6XbwrVq4VDqHkl-g/viewform")

# Preenche o campo "Digite seu nome completo"
nome_input = driver.find_element(By.XPATH, "//input[@aria-label='Digite seu nome completo']")
nome_input.send_keys("Jonh Alex")

# Preenche o campo "Digite seu CPF"
cpf_input = driver.find_element(By.XPATH, "//input[@aria-label='Digite seu CPF']")
cpf_input.send_keys("123.456.789-00")

# Seleciona a cidade "Vitoria"
cidade_option = driver.find_element(By.XPATH, "//div[@data-value='Vitoria']")
cidade_option.click()

# Seleciona o horário "Tarde"
horario_option = driver.find_element(By.XPATH, "//div[@data-value='Tarde']")
horario_option.click()

# Envia o formulário
submit_button = driver.find_element(By.XPATH, "//span[text()='Enviar']")
submit_button.click()

# Aguarda alguns segundos antes de fechar
time.sleep(3)

# Fecha o navegador
driver.quit()