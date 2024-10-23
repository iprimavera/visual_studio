from pynput import mouse
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def on_move(x, y):
    clear_console()
    print(f'El ratón se movió a ({x}, {y})')

def monitor_mouse():
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        monitor_mouse()
    except KeyboardInterrupt:
        print("Monitoreo terminado.")
