import pyautogui
import time
import webbrowser

planilhas = [
    "https://docs.google.com/spreadsheets/d/1Gd2tQwKsnYNR_ilG2GoPFb-sXF6HcwabIwn9sjW72dc/edit?usp=drivesdk"]

for url in planilhas:
    webbrowser.open(url)
    time.sleep(5)  # espera abrir
    pyautogui.hotkey("ctrl","j")
    time.sleep(1)
    pyautogui.typewrite("A14")
    time.sleep(1)
    pyautogui.hotkey("enter")
    pyautogui.typewrite("1170350")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("right")
    pyautogui.hotkey("up")
    pyautogui.moveTo(250, 647, duration=0.9)#posicao celula b14
    time.sleep(5)
    pyautogui.click(pyautogui.locateOnScreen("C:/Users/Educação/Documents/PROJETOS-PY/permitiracesso/permitirAcesso.png"))
    time.sleep(5)
    pyautogui.hotkey("ctrl","j")
    time.sleep(1)
    pyautogui.typewrite("A14")
    pyautogui.hotkey("enter")
    time.sleep(1)
    pyautogui.hotkey("backspace")
    time.sleep(3)
    pyautogui.hotkey("ctrl","f4")

    time.sleep(2)