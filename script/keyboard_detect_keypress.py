from datetime import datetime as dt
from pynput import keyboard


def on_press(key):
    try:
        print(f'alphanum key {key.char} pressed')
    except AttributeError:
        print(f'special key{key} pressed')


def on_release(key):
    print(f'{key} released')
    if key == keyboard.Key.esc:
        print(f'termination key pressed at {dt.now()}')
        return False  # stop Listener


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Collect events until released
