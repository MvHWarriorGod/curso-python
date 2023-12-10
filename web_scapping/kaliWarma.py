from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar opciones para ejecutar en modo headless
options = ChromeOptions()
options.add_argument('--headless')  # Modo headless para ejecución sin interfaz gráfica

# Configurar el servicio del controlador
service = ChromeService(executable_path=ChromeDriverManager().install())

# Inicializar el navegador Chrome
driver = webdriver.Chrome(service=service, options=options)

# Navegar a la página
driver.get("https://procesocompras2024.qaliwarma.gob.pe/ConvocatoriasT?tipo=TODAS")

# Esperar hasta que el elemento esté presente en el DOM
element_present = EC.presence_of_element_located((By.ID, 'cboUnidad'))
WebDriverWait(driver, 10).until(element_present)

# Encontrar el elemento select por su ID
departamentos = driver.find_element(By.ID, 'cboUnidad')

# Interactuar con el dropdown usando Select
select = Select(departamentos)

# Seleccionar por texto visible
select.select_by_visible_text("SAN MARTIN")

# Esperar a que cargue el contenido (puedes ajustar el tiempo según sea necesario)
time.sleep(5)

# Obtener HTML de la página actual
html = driver.page_source

# Procesar HTML con BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# Imprimir el contenido procesado (o realizar otras acciones según tus necesidades)
print(soup.select('.sinmargin td a')[0]['href'])
# print(soup.select('.tcontenido2')[6].select('table>tr')[2].select('td')[2])

# Cerrar el navegador
driver.quit()
