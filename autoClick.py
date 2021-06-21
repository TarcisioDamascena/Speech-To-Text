import pyautogui as gui


def opensoft(params):
    print(params)
    gui.press('win')
    gui.typewrite(params)
    gui.press('return', interval=0.5)