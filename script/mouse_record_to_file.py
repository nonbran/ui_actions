from datetime import datetime as dt
from os import remove
from os import getcwd
from os import walk
from os.path import exists
from pathlib import Path
from pynput.mouse import Button, Controller
from time import sleep
mouse = Controller()
path_to_recordings = Path(Path(getcwd()).parent, 'recordings')
now = dt.now()
recordings_filename = 'mouse_recording_' + str(now.hour) + str(now.minute) + str(now.second) + '.txt'
path_to_file = Path(path_to_recordings, recordings_filename)


def delete_txt_files_in_(path: Path):
    ext_to_delete = '.txt'
    for root, _, files in walk(path):
        for file in files:
            if file.endswith(ext_to_delete):
                print(f'deleting {file}')
                remove(Path(root, file))


clean_up = True
if exists(path_to_recordings):
    if clean_up:
        delete_txt_files_in_(path_to_recordings)
    with open(path_to_file, 'w') as rf:
        for i in range(10):
            event = f'the mouse position at {dt.now()} is {mouse.position}\n'
            print(event)
            rf.write(event)
            sleep(.5)
