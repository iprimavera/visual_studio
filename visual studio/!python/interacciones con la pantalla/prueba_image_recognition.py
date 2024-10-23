import win32api
import win32con
import time
import pyautogui

def hacer_clic_si_negro(coordenada_x, coordenada_y):
    if pyautogui.pixelMatchesColor(coordenada_x, coordenada_y, (0, 0, 0), 20):
        # Simular clic izquierdo en las coordenadas especificadas
        win32api.SetCursorPos((coordenada_x, coordenada_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
 # Bucle infinito para repetir el proceso continuamente
    if pyautogui.pixelMatchesColor(coordenada_x, coordenada_y, (120, 54, 222), 20):
        # Simular clic izquierdo en las coordenadas especificadas
        win32api.SetCursorPos((coordenada_x, coordenada_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while True:
    # Verificar si se presiona la tecla "q" para salir del bucle
    if win32api.GetAsyncKeyState(ord('Q')):
        break
    hacer_clic_si_negro(948, 1079)
    hacer_clic_si_negro(1143, 1079)
    hacer_clic_si_negro(1345, 1079)
    hacer_clic_si_negro(1539, 1079)

#1 X:  977 Y: 1200
#2 X: 1211 Y: 1200
#3 X: 1378 Y: 1200
#4 X: 1549 Y: 1200