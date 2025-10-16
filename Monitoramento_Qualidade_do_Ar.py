# Importação das Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# ===========================
# CONFIGURAÇÃO DO SELENIUM
# ===========================

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o Chrome em segundo plano
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializando o driver
driver = webdriver.Chrome(options=chrome_options)

# ===========================
# ACESSANDO O SITE
# ===========================

URL_SITE = "https://weather.com/pt-BR/forecast/air-quality/l/e1af5159ff6ece8ea4699268b22e8c4b390cb745b0549fde9f796b5ffbbfadda?par=samsung_widget_ZTO&cm_ven=L1_condition_aqi&theme=samsungLight"
driver.get(URL_SITE)

# Espera alguns segundos para garantir que a página carregue completamente
time.sleep(5)

# ===========================
# CAPTURANDO O VALOR DA QUALIDADE DO AR
# ===========================

try:
    # Localizando o elemento pelo seletor de classe
    elemento_qualidade = driver.find_element(By.CLASS_NAME, "AirQuality--displayValue--2Usp0")
    
    # Pegando o texto do elemento e convertendo para inteiro
    valor_qualidade = int(elemento_qualidade.text)
    
    print(f"Valor de qualidade do ar obtido: {valor_qualidade}")
    
except Exception as e:
    print("Erro ao capturar a qualidade do ar:", e)
    driver.quit()
    exit()

# ===========================
# INTERPRETAÇÃO DA QUALIDADE DO AR
# ===========================

# Tabela de classificação da qualidade do ar (AQI - Air Quality Index):
# 0-50: Boa
# 51-100: Moderada
# 101-150: Ruim para grupos sensíveis
# 151-200: Ruim
# 201-300: Muito ruim
# 301-500: Perigosa

if 0 <= valor_qualidade <= 50:
    print("Qualidade do ar: Boa")
elif 51 <= valor_qualidade <= 100:
    print("Qualidade do ar: Moderada")
elif 101 <= valor_qualidade <= 150:
    print("Qualidade do ar: Ruim para grupos sensíveis")
elif 151 <= valor_qualidade <= 200:
    print("Qualidade do ar: Ruim")
elif 201 <= valor_qualidade <= 300:
    print("Qualidade do ar: Muito ruim")
elif 301 <= valor_qualidade <= 500:
    print("Qualidade do ar: Perigosa")
else:
    print("Valor de qualidade do ar inválido")

# ===========================
# ENCERRANDO O DRIVER
# ===========================
driver.quit()
