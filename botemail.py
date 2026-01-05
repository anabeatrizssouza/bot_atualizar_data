import pyautogui
import time
import mouseinfo
import pyperclip


primCel = 463,297
total_int = 1265
contador = 0

pyautogui.click(primCel, duration=0.5)
time.sleep(0.3)

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
    pyautogui.click(1247,1058)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','l')
    pyautogui.moveTo(925,684)
    pyautogui.doubleClick()
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.3)
    pyautogui.click(162,304, duration=0.3)
    #localizar
    pyautogui.click(1313,686, duration=0.3)
    time.sleep(8)
    pyautogui.click(1097,1061, duration=0.3)
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.3)
    pyautogui.click(1247,1058, duration=0.3)
    pyautogui.click(443,662, duration=0.3)
    time.sleep(0.3)
    pyautogui.moveTo(114,663, duration=0.3)
    pyautogui.doubleClick()
    time.sleep(0.3)
    pyautogui.press('delete', presses=150)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.click(522,104, duration=0.3)
    pyautogui.click(1095,1061, duration=0.3)
    pyautogui.click(1250,8, duration=0.3)
    pyautogui.press('right')
    pyautogui.write("OK")

    pyautogui.press('down')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')

    contador+=1

    time.sleep(1)










