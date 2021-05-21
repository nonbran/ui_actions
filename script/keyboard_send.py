from pynput.keyboard import Controller

string = list('i like to play factorio')

keyboard = Controller()
for char in string:
    keyboard.press(char)
