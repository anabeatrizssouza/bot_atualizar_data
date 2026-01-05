import pyautogui
import time
import mouseinfo
import pyperclip
import pyscreeze

pyautogui.FAILSAFE = True
primCel = 463,297
total_int = 1160
contador = 0

pyautogui.click(primCel, duration=0.5)
time.sleep(0.3)

pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')

time.sleep(0.3)

while True: 
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.3)
    texto = pyperclip.paste()
       
    if texto.strip().lower() != "ok":
        break  

    # Senão, desce para a próxima linha e volta para a célula de matrícula
    pyautogui.press('down')  # Vai pra próxima linha
    pyautogui.press('left')  # Volta para a célula da matrícula
    pyautogui.press('right')  # Vai para a célula com o OK (de novo)

# Volta para a célula da matrícula onde deve começar
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('left')

time.sleep(0.3)

while contador < total_int:

    
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(1097,1060)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','l')
    pyautogui.moveTo(997,667)
    pyautogui.doubleClick()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.3)
    pyautogui.doubleClick(147,324, duration=0.5)
    time.sleep(2)
    #localizar
    pyautogui.click(1331,667, duration=0.3)
    time.sleep(8)
    pyautogui.click(301,350, duration=0.3)
    time.sleep(1)
    pyautogui.click(65,448, duration=0.3)
    time.sleep(0.5)
    pyautogui.click(65,637, duration=0.5)
    time.sleep(2)
    pyautogui.click(375,429, duration=0.3)
    time.sleep(0.5)
    pyautogui.click(180,549, duration=0.3)
    time.sleep(0.5)
    pyautogui.doubleClick(405,426, duration=0.3)
    time.sleep(0.9)
    pyautogui.write('010126')
    time.sleep(0.9)
    pyautogui.doubleClick(482,426, duration=0.3)
    time.sleep(0.9)
    pyautogui.write('311226')
    pyautogui.click(505,116, duration=0.5)
    time.sleep(2)
    pyautogui.click(1006,1056, duration=0.3)
    time.sleep(2)
    
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')

    pyautogui.write("ok")
    
    pyautogui.press('down')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')

    time.sleep(1)

    contador+=1

    time.sleep(1)










