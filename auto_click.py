import pyautogui as gui
from disc_webhook import postWebhook

def defIdentify(params):
    li = list(params.split(" "))

    if(li[0].lower() == 'abrir'):
        openSoft(li[1])

    if(li[0].lower() == 'digite' or li[0].lower() == 'escreva'):
        li.pop(0)
        newPhrase = " ".join(li)
        typeit(newPhrase)

    if(li[0].lower() == 'alerta'):
        li.pop(0)
        newPhrase = " ".join(li)
        postWebhook(newPhrase)

def minimizeWindow():
    gui.moveTo(1271, 10, 0.3)
    gui.click()

def typeit(params):
    print('digitando: ' + params)
    gui.typewrite(params, interval=0.05)

def openSoft(params):
    print(params)
    gui.press('win')
    gui.typewrite(params)
    gui.press('return', interval=0.5)