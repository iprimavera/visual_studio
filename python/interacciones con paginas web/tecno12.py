from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput import mouse
import threading
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import keyboard

def hacer_click_en(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def elemento_no_existe(driver, class_name):
    try:
        driver.find_element(By.CLASS_NAME, class_name)
        return False
    except NoSuchElementException:
        return True

# Variable global para detectar el clic del ratón
clicked = False

def on_click(x, y, button, pressed):
    global clicked
    if pressed:
        clicked = True
        # Detener el listener de mouse
        return False

def wait_for_click():
    # Escuchar el clic del ratón en un hilo separado
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def extraer_seguidos():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get('https://mapasinteractivos.didactalia.net/comunidad/mapasflashinteractivos/recurso/rios-de-espaa/6b90cb5d-8084-4d44-9cc6-990fe7068e38')
    
    element = driver.find_element(By.CLASS_NAME, 'css-1sfunq3')
    element.click()
    
    # Crear un hilo para esperar el clic del ratón
    while keyboard.is_pressed('*') == False:
        time.sleep(0.1)
    
    wait_thread = threading.Thread(target=wait_for_click)
    wait_thread.start()

    print("Por favor, haz clic en cualquier parte de la pantalla para continuar...")

    # Esperar a que el clic sea detectado
    wait_thread.join()
    
    time.sleep(0.5)
    
    element = driver.find_element(By.CLASS_NAME, 'jugar')
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    
    while elemento_no_existe(driver, "volverAJugar"):
        
        element = driver.find_element(By.CLASS_NAME, 'objetivo')
        nombre = element.text
        print(nombre)
        match nombre:
            case "TER":
                hacer_click_en(944, 655)
            case "EBRO":
                hacer_click_en(776, 675)
            case "MIÑO":
                hacer_click_en(439, 646)
            case "DUERO":
                hacer_click_en(520, 703)
            case "NALÓN":
                hacer_click_en(544, 573)
            case "NAVIA":
                hacer_click_en(496, 600)
            case "TAJO":
                hacer_click_en(595, 777)
            case "SEGURA":
                hacer_click_en(753, 892)
            case "JÚCAR":
                hacer_click_en(763, 823)
            case "NERVIÓN":
                hacer_click_en(679, 599)
            case "EO":
                hacer_click_en(486, 568)
            case "LLOBREGAT":
                hacer_click_en(903, 690)
            case "GUADALQUIVIR":
                hacer_click_en(603, 899)
            case "TURIA":
                hacer_click_en(761, 764)
            case "GUADALHORCE":
                hacer_click_en(603, 964)
            case "BIDASOA":
                hacer_click_en(738, 576)
            case "BESAYA":
                hacer_click_en(630, 579)
            case "GUADIANA":
                hacer_click_en(525, 843)

    input("Presiona Enter para cerrar el navegador...")
    driver.quit()

extraer_seguidos()
