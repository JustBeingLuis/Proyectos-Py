#Importamos libreria
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Creamos opcion la cual hace que el navegador que se abre no se cierre
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#Instanciamos el driver y añadimos la opcion
driver = webdriver.Chrome(options=options)

driver.get("https://santander.gov.co/publicaciones/234/solicitud-de-citas-tramite-de-pasaportes/")

click_Realizar_Pago = driver.find_element(By.XPATH, '//*[@id="tabs4322-1"]/div/div/div[2]/div/div/div/p/button')
driver.execute_script("arguments[0].scrollIntoView();", click_Realizar_Pago)
time.sleep(1)
click_Realizar_Pago.click()
time.sleep(1)
click_Confirmar_Pago = driver.find_element(By.XPATH, '//*[@id="modalPago"]/div/div/div[3]/a').click()
time.sleep(3)
#insertar_Cedula = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)

#seleccionar_identificacion = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)

#insertar_Cedula = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)
#insertar_Cedula = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)

#insertar_Nombre = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)
#insertar_Nombre = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)

#insertar_Apellido = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)
#insertar_Apellido = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)

#insertar_Correo = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)
#insertar_Correo = driver.find_element(By.XPATH, '------------------INSERTAR XPATH--------------').send_keys(INSERTAR)




