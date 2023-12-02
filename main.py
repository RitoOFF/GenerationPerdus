from time import sleep
import keyboard
from pynput.keyboard import Controller, Key
clavier = Controller()
mot = "Je t'aime à "
keyboard.wait("e")
for i in range(100):
    for k in range(len(mot)):
        clavier.tap(mot[k])
        sleep(0.01)
    for j in range(len(str(i))):
        clavier.tap(str(i)[j])
    sleep(0.1)
    clavier.tap("%")
    sleep(2)
    clavier.press(Key.enter)    